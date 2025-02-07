from typing import Dict, Tuple

from manim import *
import numpy as np
import networkx as nx

from ..manim_chemistry_molecule import MCMolecule


class SimpleLine(Line):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sheen_direction = self._get_unit_vector()

    def _get_unit_vector(self) -> np.array:
        vector = self.end - self.start

        return vector / np.linalg.norm(vector)


class DoubleLine(ArcBetweenPoints):
    def __init__(
        self,
        start=[-1, 0, 0],
        end=[1, 0, 0],
        angle: float = PI / 4,
        radius: float | None = None,
        **kwargs,
    ):
        self.start = start
        self.end = end
        super().__init__(start=start, end=end, angle=angle, radius=radius, **kwargs)
        self.sheen_direction = self._get_unit_vector()
        other_arc = ArcBetweenPoints(
                    start=start, end=end, angle=-angle, radius=radius, **kwargs
                )
        other_arc.sheen_direction = self.sheen_direction
        self.add(other_arc)

    def _get_unit_vector(self) -> np.array:
        vector = self.end - self.start

        return vector / np.linalg.norm(vector)

    def get_vector(self):
        return self._get_unit_vector()

    def set_points_by_ends(self, start, end, *args, **kwargs) -> None:
        self.put_start_and_end_on(start=start, end=end)


class TripleLine(DoubleLine):
    def __init__(
        self, start=[-1, 0, 0], end=[1, 0, 0], angle: float = PI / 4, *args, **kwargs
    ):
        super().__init__(start=start, end=end, *args, **kwargs)
        middle_line = Line(start=start, end=end, *args, **kwargs)
        middle_line.sheen_direction = self.sheen_direction
        self.add(middle_line)


class GraphMolecule(Graph):
    SUPPORTED_BOND_TYPES = {
        1: SimpleLine,
        2: DoubleLine,
        3: TripleLine,
    }

    def __init__(
        self,
        vertices_dict: dict,
        edges_dict: dict,
        label: bool = False,
        numeric_label: bool = False,
        label_color: str = BLACK,
        *args,
        **kwargs,
    ):
        self.edges_dict = edges_dict
        labels = False
        if label or numeric_label:
            labels = self.make_labels(vertices_dict, numeric_label, label_color)

        super().__init__(
            vertices=vertices_dict.keys(),
            edges=edges_dict.keys(),
            vertex_config=self.make_vertex_config(vertices_dict),
            edge_config=self.make_edge_config(edges_dict),
            layout=self.make_layout(vertices_dict),
            labels=labels,
            *args,
            **kwargs,
        )

        self.move_to(ORIGIN)
        self.atoms = self.vertices
        self.bonds = self.edges

    def _populate_edge_dict(self, edges, _):
        self.edges = {}

        for u, v in edges:
            bond_type = self.select_bond_from_edge((u, v))
            bond = bond_type(
                start=self[u].get_center(),
                end=self[v].get_center(),
                z_index=-1,
                **self._edge_config[(u, v)],
            )
            self.edges[(u, v)] = bond

    def select_bond_from_edge(self, edge):
        bond_type = self.edges_dict[edge].bond_type
        return self.select_bond_type(bond_type)

    def select_bond_type(self, bond_type: int):
        bond = self.SUPPORTED_BOND_TYPES.get(int(bond_type))

        if not bond:
            raise Exception(
                f"{bond_type} is an unknown type of bond. Options are 1, 2 or 3"
            )

        return bond

    def make_layout(self, vertices_dict: dict):
        return {index: vertex.coords for index, vertex in vertices_dict.items()}

    def make_vertex_config(self, vertices_dict: dict):
        v_dict = {}
        for vertex_index, mc_atom in vertices_dict.items():
            v_dict[vertex_index] = {
                "color": mc_atom.element.color,
                "radius": 0.2,
            }

        return v_dict

    def make_edge_config(self, edges: dict):
        edge_config = {}
        for edge_key, edge in edges.items():
            edge_config[edge_key] = {
                "stroke_color": color_gradient(
                    [
                        edge.from_atom.element.color,
                        edge.to_atom.element.color,
                    ],
                    length_of_output=2,
                )
            }

        return edge_config

    def make_labels(self, vertices_dict: dict, numeric_label: bool, label_color: str):
        if numeric_label:
            return {
                index: Text(str(index), color=label_color).scale(0.5)
                for index in vertices_dict.keys()
            }
        return {
            index: Text(vertex.element.symbol, color=BLACK).scale(0.5)
            for index, vertex in vertices_dict.items()
        }

    @classmethod
    def molecule_from_file(self, filepath, label=False, *args, **kwargs):
        """
        Reads a file and returns a single molecule from that file.

        By default retrieves the first molecule generated by the file.

        Args:
            filepath (_type_): Pathlike or str
            label (bool, optional): Add a label such as element symbol or number. Defaults to False.

        Returns:
            GraphMolecule: GraphMolecule from the file
        """
        mc_molecule = MCMolecule.construct_from_file(filepath=filepath)
        if isinstance(mc_molecule, list):
            mc_molecule = mc_molecule[0]

        vertices, edges = self.mc_molecule_to_graph(mc_molecule=mc_molecule)
        return GraphMolecule(vertices, edges, label, *args, **kwargs)

    @classmethod
    def multiple_molecules_from_file(filepath, label=False, *args, **kwargs) -> VGroup:
        """
        Reads a file and returns a collection of molecules from that file as a VGroup.

        Args:
            filepath (str | Pathlike): Path to the molecule
            label (bool, optional): Wether or not add a label.. Defaults to False.

        Raises:
            Exception: In case the mc_molecules parsed is not a list.

        Returns:
            VGroup: VGroup with the molecules inside.
        """

        mc_molecules = MCMolecule.construct_from_file(filepath=filepath)

        if not isinstance(mc_molecules, list):
            raise Exception(f"Expected a list of molecules. Received {mc_molecules}")

        graph_molecules = VGroup()
        for mc_molecule in mc_molecules:
            vertices, edges = GraphMolecule.mc_molecule_to_graph(
                mc_molecule=mc_molecule
            )
            graph_molecules.add(GraphMolecule(vertices, edges, label, *args, **kwargs))

        return graph_molecules

    def depth_first_search(
        self, graph: nx.Graph, atom: int, visited_atoms: set, connected_atoms: list
    ) -> list:
        """
        Recursive depht-first search to find connected atoms.
        Warning: Only works properly for non cyclic structures. If you use
        an atom from a cycle as the starting point, it will take the whole cycle.
        """
        for neighbor in graph.neighbors(atom):
            if neighbor not in visited_atoms:
                visited_atoms.add(neighbor)
                connected_atoms.append(neighbor)
                self.depth_first_search(
                    graph=graph,
                    atom=neighbor,
                    visited_atoms=visited_atoms,
                    connected_atoms=connected_atoms,
                )

        return connected_atoms

    def get_connected_atoms(self, from_atom_index: int, to_atom_index: int) -> list:
        """
        Given two atoms index, returns the connected atoms to the second atom
        after the bond between the first atom and the second one.

        Example:
        Index: 0 1 2 3 4 5
        Atoms: C-O-C-N-C-H
        This function applied to atoms 2 (C) and 3 (N), would return
        [3, 4, 5], the indices of atoms N, C and H.
        """
        if not self._graph.has_edge(from_atom_index, to_atom_index):
            raise Exception(
                f"There is no bond between atoms {from_atom_index} and {to_atom_index}"
            )

        visited_atoms = set([from_atom_index])
        connected_atoms = [to_atom_index]

        return self.depth_first_search(
            self._graph,
            atom=to_atom_index,
            visited_atoms=visited_atoms,
            connected_atoms=connected_atoms,
        )

    def get_atoms_vgroup_from_index(self, atoms_indices):
        return VGroup(*[self.vertices[atom_index] for atom_index in atoms_indices])

    def get_connected_atoms_v_group(
        self, from_atom_index: int, to_atom_index: int
    ) -> list:
        connected_atoms = self.get_connected_atoms(
            from_atom_index=from_atom_index, to_atom_index=to_atom_index
        )
        return self.get_atoms_vgroup_from_index(connected_atoms)

    def get_bonds_from_atoms_indices(
        self, connected_atoms: list, excluded_atom: int = 0
    ) -> list:
        """
        Given a list of atoms, returns the bonds related to those atoms.
        """
        edges = []
        for atom in connected_atoms:
            for bond in self.edges.keys():
                if atom in bond and excluded_atom not in bond:
                    edges.append(bond)

        return edges

    def get_bonds_vgroup_from_index(self, connected_atoms: list, excluded_atom: int):
        bonds = self.get_bonds_from_atoms_indices(connected_atoms, excluded_atom)
        return VGroup(*[self.edges[bond_atoms] for bond_atoms in bonds])

    def get_connected_atoms_and_bonds_group_from_index(
        self, connected_atoms: list, excluded_atom: int = 0
    ):
        return VGroup(
            self.get_atoms_vgroup_from_index(atoms_indices=connected_atoms),
            self.get_bonds_vgroup_from_index(
                connected_atoms=connected_atoms, excluded_atom=excluded_atom
            ),
        )

    def get_connected_atoms_and_bonds(self, from_atom: int, to_atom: int) -> VGroup:
        connected_atoms = self.get_connected_atoms(
            from_atom_index=from_atom, to_atom_index=to_atom
        )
        return self.get_connected_atoms_and_bonds_group_from_index(
            connected_atoms=connected_atoms, excluded_atom=from_atom
        )

    def find_atom_position_by_index(self, atom_index: int) -> np.array:
        """_summary_
        Returns the position of a single atom given its index.

        Example:
        ```
        molecule = GraphMolecule.molecule_from_file("examples/element_files/dimethylpropane.mol")
        print(molecule.find_atom_position_by_index(1))
        >>> array([ 0.9397, -0.7497,  0.    ])
        ```


        Args:
            atom_index (int): Index of the atom inside the VDict.

        Returns:
            np.array: Array with the [x, y, z] coordinates of the atom.
        """
        try:
            atom = self.atoms[atom_index]
            return atom.get_center()

        except KeyError as key_error:
            # TODO: Change from print to proper logging system.
            print(f"Atom index {atom_index} is not valid for molecule {self}")
            print(f"Valid indices are: {self.atoms.submob_dict.keys()}")
            raise key_error

        except Exception as exception:
            raise exception

    def find_atoms_position_by_index(self, atoms_index_list: list) -> list:
        """_summary_

        Returns the position of multiple atoms given their indices.

        Example:
        ```
        molecule = GraphMolecule.molecule_from_file("examples/element_files/dimethylpropane.mol")
        print(molecule.find_atoms_position_by_index([1,2,3]))
        >>> [array([ 0.0713, -0.0263,  0.    ]), array([-1.2754,  0.3464,  0.    ]), array([0.9674, 1.2186, 0.    ])]
        ```
        Args:
            atoms_index_list (list): List of atoms indices to be gotten.

        Returns:
            list: List of the atoms positions.
        """
        atoms_positions = []
        for atom_index in atoms_index_list:
            atoms_positions.append(
                self.find_atom_position_by_index(atom_index=atom_index)
            )

        return atoms_positions

    def find_bond_center_by_tuple(self, bond_tuple: tuple) -> np.array:
        """_summary_

        Returns the [x, y, z] coordinates of a bond given a bond tuple.
        The bund tuple corresponds to the indices of the atoms in the bond.

        Example:
        ```
        molecule = GraphMolecule.molecule_from_file("examples/element_files/dimethylpropane.mol")
        print(molecule.find_bond_center_by_tuple((1, 2))
        >>> array([0.51935, 0.59615, 0.     ])
        ```

        Args:
            bond_index (tuple): index of the bond

        Returns:
            np.array: [x, y, z] coordinates of bond center.
        """
        try:
            bond = self.bonds[bond_tuple]
            return bond.get_center()

        except KeyError as key_error:
            # TODO: Change from print to proper logging system.
            print(f"Bond tuple {bond_tuple} is not valid for molecule {self}")
            raise key_error

        except Exception as exception:
            raise exception

    def find_position_along_bond_axis(
        self, bond_tuple: int, position_buff: float
    ) -> np.array:
        """_summary_
        Returns a position along the bond axis given a bond index and depending on a position_buff.
        A value of 1 will return one end of the bond. A value of -1 will return the other end.
        All values in between return positions at some point of the middle of the bond, being 0 the center.
        Values bigger or lower that 1 and -1 will return positions outside the bond.

        Args:
            bond_tuple (int): Tuple of the bond
            position_buff (float): Position buff

        Returns:
            np.array: [x, y, z] coordinates of the final position selected.
        """

        try:
            bond = self.bonds[bond_tuple]

        except KeyError as key_error:
            # TODO: Change from print to proper logging system.
            print(f"Bond index {bond_tuple} is not valid for molecule {self}")
            print(f"Valid indices are: {self.bonds.submob_dict.keys()}")
            raise key_error

        bond_vector = bond.get_vector()
        bond_center = bond.get_center()

        return bond_center + bond_vector * position_buff * 0.5

    def find_bonds_center_by_tuple(self, bonds_tuples_list: list) -> list:
        """_summary_

        Returns the position of multiple bonds given their indices.

        Example:
        ```
        molecule = GraphMolecule.molecule_from_file("examples/element_files/dimethylpropane.mol")
        print(molecule.find_bonds_center_by_tuple([1,2,3]))
        >>> [array([ 0.0713, -0.0263,  0.    ]), array([-1.2754,  0.3464,  0.    ]), array([0.9674, 1.2186, 0.    ])]
        ```
        Args:
            bondss_index_list (list): List of bonds indices to be gotten.

        Returns:
            list: List of the bonds positions.
        """
        bonds_positions = []
        for bond_index in bonds_tuples_list:
            bonds_positions.append(
                self.find_bond_center_by_tuple(bond_index=bond_index)
            )

        return bonds_positions

    def find_all_atoms_positions(self) -> dict:
        atoms_positions = {}
        for atom_index in self.atoms.keys():
            atoms_positions[atom_index] = self.find_atom_position_by_index(
                atom_index=atom_index
            )

        return atoms_positions

    def find_all_bonds_centers(self) -> dict:
        bonds_positions = {}
        for bond_tuple in self.bonds:
            bonds_positions[bond_tuple] = self.find_bond_center_by_tuple(
                bond_tuple=bond_tuple
            )

        return bonds_positions

    @staticmethod
    def mc_molecule_to_graph(mc_molecule: MCMolecule) -> Tuple[Dict, Dict]:
        """
        Transforms the structure of a mc_molecule to a (vertices, edges) tuple
        with the following structure:
        - Vertices: {<atom_index>: MCAtom}
        - Edges: {(<from_atom_index>, <to_atom_index>): MCBond}

        Args:
            mc_molecule (MCMolecule): The origin MCMolecule

        Returns:
            Tuple[Dict, Dict]: See above.
        """

        vertices = mc_molecule.atoms_by_index

        edges = {
            (bond.from_atom.molecule_index, bond.to_atom.molecule_index): bond
            for bond in mc_molecule.bonds
        }

        return vertices, edges

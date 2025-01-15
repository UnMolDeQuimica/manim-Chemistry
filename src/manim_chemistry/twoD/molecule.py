from manim import (DOWN, GREEN, ORIGIN, RED, MarkupText, MathTex, SVGMobject,
                   VDict, VGroup)

from ..utils import (mol_parser, mol_parser_string, sdf_parser,
                     sdf_parser_string)
from .atom import MAtomObject
from .bond import *


class MMoleculeObject(VGroup):
    def __init__(
        self,
        atoms_dict: dict,
        bonds_dict: dict,
        representation_type: str or None = None,
        explicit_carbons: bool = False,
        explicit_hydrogens: bool = False,
        planar: bool = True,
        add_atoms_numbering: bool = False,
        add_bonds_numbering: bool = False,
        rotate_bonds: list = [],
        **kwargs,
    ):
        VGroup.__init__(self, **kwargs)
        self.atoms_dict = atoms_dict
        self.bonds_dict = bonds_dict
        self.representation_type = representation_type
        self.explicit_carbons = explicit_carbons
        self.explicit_hydrogens = explicit_hydrogens
        self.planar = planar
        self.atoms, self.atoms_by_index = self.get_atoms()
        self.bonds = self.get_bonds()
        self.add(self.atoms, self.bonds)
        if add_atoms_numbering:
            self.add_atom_numbering()
        if add_bonds_numbering:
            self.add_bond_numbering()
        self.rotate_bond(rotate_bonds)
        self.complete_missing_hydrogens()
        self.move_to(ORIGIN)

    def get_atoms(self):
        atoms = VDict()
        atoms_by_index = {}
        for index, atom in self.atoms_dict.items():
            matom = MAtomObject(
                coords=atom["coords"],
                element=atom["element"],
                explicit_carbons=self.explicit_carbons,
                explicit_hydrogens=self.explicit_hydrogens,
                representation_type=self.representation_type,
                planar=self.planar,
                bond_to=atom.get("bond_to"),
                index=index,
            )
            atoms.add([(index, matom)])
            atoms_by_index[index] = matom

        return atoms, atoms_by_index

    def get_bonds(self):
        bonds = VGroup()
        bond_index = 0
        for index, bond_list in self.bonds_dict.items():
            for bond in bond_list:
                # TODO: Add logic to check type of bond
                from_atom = self.atoms_by_index.get(index)
                to_atom = self.atoms_by_index.get(bond.get("to"))
                if from_atom.element == "H" or to_atom.element == "H":
                    stereo = bond.get("stereo")

                    if stereo:
                        if int(stereo) == 1 or int(stereo) == 4:
                            self.atoms[from_atom.index] = (
                                from_atom.copy_with_explicit_hydrogens()
                            )
                            self.atoms[to_atom.index] = (
                                to_atom.copy_with_explicit_hydrogens()
                            )
                            from_atom = self.atoms[from_atom.index]
                            to_atom = self.atoms[to_atom.index]
                            new_bond = PlainCramBond(
                                from_atom=from_atom,
                                to_atom=to_atom,
                                index=bond_index,
                                type=bond_type,
                            )

                            bond_index += 1
                            bonds.add(new_bond)

                        elif int(stereo) == 6:
                            self.atoms[from_atom.index] = (
                                from_atom.copy_with_explicit_hydrogens()
                            )
                            self.atoms[to_atom.index] = (
                                to_atom.copy_with_explicit_hydrogens()
                            )
                            from_atom = self.atoms[from_atom.index]
                            to_atom = self.atoms[to_atom.index]
                            new_bond = DashedCramBond(
                                from_atom=from_atom,
                                to_atom=to_atom,
                                index=bond_index,
                                type=bond_type,
                            )

                            bond_index += 1
                            bonds.add(new_bond)

                        else:
                            continue
                    # you don't need not x and not y
                    # just use De Morgan's law ! (syntactic detail, doesn't change code)
                    elif (from_atom.explicit_hydrogens) or (to_atom.explicit_hydrogens):
                        # make bonds to explicit hydrogens
                        # TODO: clean repetitive code
                        self.atoms[from_atom.index] = (
                            from_atom.copy_with_explicit_hydrogens()
                        )
                        self.atoms[to_atom.index] = (
                            to_atom.copy_with_explicit_hydrogens()
                        )
                        from_atom = self.atoms[from_atom.index]
                        to_atom = self.atoms[to_atom.index]
                        new_bond = SimpleBond(
                            from_atom=from_atom,
                            to_atom=to_atom,
                            index=bond_index,
                            type=bond_type,
                        )

                        bond_index += 1
                        bonds.add(new_bond)
                        continue

                else:
                    bond_type = int(bond.get("type"))
                    if bond_type == 2 or bond_type == 5 or bond_type == 7:
                        new_bond = DoubleBond(  # TODO: Add function inside bond to create it from data
                            from_atom=from_atom,
                            to_atom=to_atom,
                            index=bond_index,
                            type=bond_type,
                        )
                    elif bond_type == 3:
                        new_bond = TripleBond(
                            from_atom=from_atom,
                            to_atom=to_atom,
                            index=bond_index,
                            type=bond_type,
                        )
                    else:
                        if bond.get("stereo"):
                            if int(bond.get("stereo")) == 1:
                                new_bond = PlainCramBond(
                                    from_atom=from_atom,
                                    to_atom=to_atom,
                                    index=bond_index,
                                    type=bond_type,
                                )

                            else:
                                new_bond = DashedCramBond(
                                    from_atom=from_atom,
                                    to_atom=to_atom,
                                    index=bond_index,
                                    type=bond_type,
                                )
                        else:
                            new_bond = SimpleBond(
                                from_atom=from_atom,
                                to_atom=to_atom,
                                index=bond_index,
                                type=bond_type,
                            )
                    bond_index += 1
                    bonds.add(new_bond)

        return bonds

    def add_atom_numbering(self):
        numbering = VGroup()
        for atom in self.atoms:
            if not self.explicit_hydrogens:
                if atom.element != "H":
                    numbering.add(
                        MarkupText(str(atom.index))
                        .scale(0.5)
                        .move_to(atom.coords)
                        .set_color(RED)
                    )
            else:
                numbering.add(
                    MarkupText(str(atom.index))
                    .scale(0.5)
                    .move_to(atom.coords)
                    .set_color(RED)
                )

        self.add(numbering)

        return self

    def add_bond_numbering(self):
        numbering = VGroup()
        for bond in self.bonds:
            if (
                not bond.from_atom.explicit_hydrogens
                and not bond.to_atom.explicit_hydrogens
            ):
                if bond.from_atom.element != "H" and bond.to_atom.element != "H":
                    numbering.add(
                        MarkupText(str(bond.index))
                        .set_color(GREEN)
                        .move_to(bond.get_center())
                        .scale(0.5)
                    )

        self.add(numbering)

        return self

    def rotate_bond(self, rotate_bonds):
        if isinstance(rotate_bonds, int):
            rotate_bonds = [rotate_bonds]

        for bond in rotate_bonds:
            direction = self.bonds[bond][0][0].end - self.bonds[bond][0][0].start
            self.bonds[bond].rotate(
                PI, about_point=self.bonds[bond][0][0].get_center(), axis=direction
            )

        return self

    def complete_missing_hydrogens(self):
        supported_atoms = ["O", "S", "N", "P"]

        for atom in self.atoms:
            if atom.element not in supported_atoms:
                continue

            total_bonds = len(atom.bond_to)
            bonds_direction = 0
            if not atom.bonds_fulfilled():
                minimum_bonds = {"O": 2, "S": 2, "N": 3, "P": 3}
                for bond in self.bonds:
                    if bond.atom_is_in_bond(atom) and 0 < bond.type <= 4:
                        total_bonds += bond.type - 1
                        bonds_direction += (
                            bond.to_atom.coords[0] - bond.from_atom.coords[0]
                        )

                if total_bonds < minimum_bonds.get(atom.element):
                    needed_hydrogens = minimum_bonds.get(atom.element) - total_bonds
                    if bonds_direction < 0:
                        if needed_hydrogens > 1:
                            self.atoms[atom.index] = atom.rename_atom(
                                f"H<sub>{needed_hydrogens}</sub>" + atom.element,
                                bonds_direction,
                            )
                        else:
                            self.atoms[atom.index] = atom.rename_atom(
                                "H" + atom.element, bonds_direction
                            )
                    else:
                        if needed_hydrogens > 1:
                            self.atoms[atom.index] = atom.rename_atom(
                                atom.element + f"H<sub>{needed_hydrogens}</sub>",
                                bonds_direction,
                            )
                        else:
                            self.atoms[atom.index] = atom.rename_atom(
                                atom.element + "H", bonds_direction
                            )

    def from_mol_file(filename, *args, **kwargs):
        atoms, bonds = mol_parser(filename)
        return MMoleculeObject(atoms, bonds, *args, **kwargs)

    def from_mol_string(mol_string, *args, **kwargs):
        atoms, bonds = mol_parser_string(mol_string)
        return MMoleculeObject(atoms, bonds, *args, **kwargs)
    
    def from_sdf_file(filename, *args, **kwargs):
        molecules = sdf_parser(filename)
        moleculeObjects = []
        for molecule in molecules:
            atoms, bonds = molecule
            moleculeObjects.append(MMoleculeObject(atoms, bonds, *args, **kwargs))
        return moleculeObjects
    
    def from_sdf_string(sdf_string, *args, **kwargs):
        molecules = sdf_parser_string(sdf_string)
        moleculeObjects = []
        for molecule in molecules:
            atoms, bonds = molecule
            moleculeObjects.append(MMoleculeObject(atoms, bonds, *args, **kwargs))
        return moleculeObjects
        
    def find_atom_position_by_index(self, atom_index: int) -> np.array:
        """_summary_
        Returns the position of a single atom given its index.
        
        Example:
        ```
        molecule = MMoleculeObject.from_mol_file("examples/element_files/dimethylpropane.mol")
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
        molecule = MMoleculeObject.from_mol_file("examples/element_files/dimethylpropane.mol")
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
            atoms_positions.append(self.find_atom_position_by_index(atom_index=atom_index))
            
        return atoms_positions
    
    def find_bond_center_by_index(self, bond_index: int) -> np.array:
        """_summary_

        Returns the [x, y, z] coordinates of a bond given a bond index.
        
        Example:
        ```
        molecule = MMoleculeObject.from_mol_file("examples/element_files/dimethylpropane.mol")
        print(molecule.find_bond_center_by_index(1))
        >>> array([0.51935, 0.59615, 0.     ])
        ```
        
        Args:
            bond_index (int): index of the bond

        Returns:
            np.array: [x, y, z] coordinates of bond center.
        """
        try:
            bond = self.bonds[bond_index]
            return bond.get_center()
            
        except KeyError as key_error:
            # TODO: Change from print to proper logging system.
            print(f"Bond index {bond_index} is not valid for molecule {self}")
            raise key_error
        
        except Exception as exception:
            raise exception
        
    def find_position_along_bond_axis(self, bond_index: int, position_buff: float) -> np.array:
        """_summary_
        Returns a position along the bond axis given a bond index and depending on a position_buff. 
        A value of 1 will return one end of the bond. A value of -1 will return the other end. 
        All values in between return positions at some point of the middle of the bond, being 0 the center.
        Values bigger or lower that 1 and -1 will return positions outside the bond.
        
        Args:
            bond_index (int): Index of the bond
            position_buff (float): Position buff

        Returns:
            np.array: [x, y, z] coordinates of the final position selected.
        """
        
        try:
            bond = self.bonds[bond_index]
        
        except KeyError as key_error:
            # TODO: Change from print to proper logging system.
            print(f"Bond index {bond_index} is not valid for molecule {self}")
            print(f"Valid indices are: {self.bonds.submob_dict.keys()}")
            raise key_error
    
        bond_vector = bond.get_vector()
        bond_center = bond.get_center()
        
        return bond_center + bond_vector * position_buff * 0.5
        
        
    def find_bonds_center_by_index(self, bonds_index_list: list) -> list:
        """_summary_

        Returns the position of multiple bonds given their indices.
        
        Example:
        ```
        molecule = MMoleculeObject.from_mol_file("examples/element_files/dimethylpropane.mol")
        print(molecule.find_bonds_center_by_index([1,2,3]))
        >>> [array([ 0.0713, -0.0263,  0.    ]), array([-1.2754,  0.3464,  0.    ]), array([0.9674, 1.2186, 0.    ])]
        ```
        Args:
            bondss_index_list (list): List of bonds indices to be gotten.

        Returns:
            list: List of the bonds positions.
        """
        bonds_positions = []
        for bond_index in bonds_index_list:
            bonds_positions.append(self.find_bond_center_by_index(bond_index=bond_index))
            
        return bonds_positions
    
    def find_all_atoms_positions(self) -> dict:
        
        atoms_positions = {}
        for atom_index in self.atoms.submob_dict.keys():
            atoms_positions[atom_index] = self.find_atom_position_by_index(atom_index=atom_index)
        
        return atoms_positions
    
    
    def find_all_bonds_centers(self) -> dict:
        
        bonds_positions = {}
        for bond_index, _ in enumerate(self.bonds):
            bonds_positions[bond_index] = self.find_bond_center_by_index(bond_index=bond_index)
        
        return bonds_positions
        
class NamedMolecule(VGroup):
    def __init__(
        self,
        name,
        molecule_data,
        direction=DOWN,
        buff=1,
        tex=False,
        font="",
        *args,
        **kwargs,
    ):
        if isinstance(molecule_data, MMoleculeObject):
            self.molecule = molecule_data

        else:
            self.molecule = MMoleculeObject(molecule_data, *args, **kwargs)

        if isinstance(name, SVGMobject):
            name_text = name

        elif tex:
            name_text = MathTex(name, *args, **kwargs)
        else:
            name_text = MarkupText(name, font=font, *args, **kwargs)

        name_text.next_to(self.molecule, direction, buff)

        super().__init__(*[self.molecule, name_text], **kwargs)
        self.atoms = self.molecule.atoms
        self.bonds = self.molecule.bonds

    def from_mol_file(
        name, filename, direction=DOWN, buff=1, tex=False, font="", *args, **kwargs
    ):
        molecule = MMoleculeObject.from_mol_file(filename, *args, **kwargs)

        return NamedMolecule(
            name,
            molecule,
            direction=direction,
            buff=buff,
            tex=tex,
            font=font,
            *args,
            **kwargs,
        )
    
    def from_mol_string(
        name, mol_str, direction=DOWN, buff=1, tex=False, font="", *args, **kwargs
    ):
        molecule = MMoleculeObject.from_mol_string(mol_str, *args, **kwargs)

        return NamedMolecule(
            name,
            molecule,
            direction=direction,
            buff=buff,
            tex=tex,
            font=font,
            *args,
            **kwargs,
        )
    
    def from_sdf_file(
        name, filename, direction=DOWN, buff=1, tex=False, font="", *args, **kwargs
    ):
        molecules = MMoleculeObject.from_sdf_file(filename, *args, **kwargs)
        named_molecules = []
        for index, molecule in enumerate(molecules):
            named_molecules.append(
                NamedMolecule(
                    name + f"_{index}",
                    molecule,
                    direction=direction,
                    buff=buff,
                    tex=tex,
                    font=font,
                    *args,
                    **kwargs,
                )
            )
        return named_molecules
    
    def from_sdf_string(
        name, sdf_str, direction=DOWN, buff=1, tex=False, font="", *args, **kwargs
    ):
        molecules = MMoleculeObject.from_sdf_string(sdf_str, *args, **kwargs)
        named_molecules = []
        for index, molecule in enumerate(molecules):
            named_molecules.append(
                NamedMolecule(
                    name + f"_{index}",
                    molecule,
                    direction=direction,
                    buff=buff,
                    tex=tex,
                    font=font,
                    *args,
                    **kwargs,
                )
            )
        return named_molecules

    def rotate_bond(self, bonds: int | list):
        self.molecule = self.molecule.rotate_bond(bonds)

        return self

    def add_bond_numbering(self):
        self.molecule = self.molecule.add_bond_numbering()
        self.molecule[-1].move_to(self.molecule[1].get_center())

        return self

    def add_atom_numbering(self):
        # Atom numbering is not working correctly.
        self.molecule = self.molecule.add_atom_numbering()
        self.molecule[-1].move_to(self.molecule[0].get_center())

        return self

    def find_atom_position_by_index(self, atom_index: int) -> np.array:
        """_summary_
        Returns the position of a single atom given its index.
        
        Example:
        ```
        molecule = MMoleculeObject.from_mol_file("examples/element_files/dimethylpropane.mol")
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
        molecule = MMoleculeObject.from_mol_file("examples/element_files/dimethylpropane.mol")
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
            atoms_positions.append(self.find_atom_position_by_index(atom_index=atom_index))
            
        return atoms_positions
    
    def find_bond_center_by_index(self, bond_index: int) -> np.array:
        """_summary_

        Returns the [x, y, z] coordinates of a bond given a bond index.
        
        Example:
        ```
        molecule = MMoleculeObject.from_mol_file("examples/element_files/dimethylpropane.mol")
        print(molecule.find_bond_center_by_index(1))
        >>> array([0.51935, 0.59615, 0.     ])
        ```
        
        Args:
            bond_index (int): index of the bond

        Returns:
            np.array: [x, y, z] coordinates of bond center.
        """
        try:
            bond = self.bonds[bond_index]
            return bond.get_center()
            
        except KeyError as key_error:
            # TODO: Change from print to proper logging system.
            print(f"Bond index {bond_index} is not valid for molecule {self}")
            print(f"Valid indices are: {self.bonds.submob_dict.keys()}")
            raise key_error
        
        except Exception as exception:
            raise exception
        
    def find_position_along_bond_axis(self, bond_index: int, position_buff: float) -> np.array:
        """_summary_
        Returns a position along the bond axis given a bond index and depending on a position_buff. 
        A value of 1 will return one end of the bond. A value of -1 will return the other end. 
        All values in between return positions at some point of the middle of the bond, being 0 the center.
        Values bigger or lower that 1 and -1 will return positions outside the bond.
        
        Args:
            bond_index (int): Index of the bond
            position_buff (float): Position buff

        Returns:
            np.array: [x, y, z] coordinates of the final position selected.
        """
        
        try:
            bond = self.bonds[bond_index]
        
        except KeyError as key_error:
            # TODO: Change from print to proper logging system.
            print(f"Bond index {bond_index} is not valid for molecule {self}")
            print(f"Valid indices are: {self.bonds.submob_dict.keys()}")
            raise key_error
    
        bond_vector = bond.get_vector()
        bond_center = bond.get_center()
        
        return bond_center + bond_vector * position_buff * 0.5
        
        
    def find_bonds_center_by_index(self, bonds_index_list: list) -> list:
        """_summary_

        Returns the position of multiple bonds given their indices.
        
        Example:
        ```
        molecule = MMoleculeObject.from_mol_file("examples/element_files/dimethylpropane.mol")
        print(molecule.find_bonds_position_by_index([1,2,3]))
        >>> [array([ 0.0713, -0.0263,  0.    ]), array([-1.2754,  0.3464,  0.    ]), array([0.9674, 1.2186, 0.    ])]
        ```
        Args:
            bondss_index_list (list): List of bonds indices to be gotten.

        Returns:
            list: List of the bonds positions.
        """
        bonds_positions = []
        for bond_index in bonds_index_list:
            bonds_positions.append(self.find_bond_center_by_index(bond_index=bond_index))
            
        return bonds_positions
    
    def find_all_atoms_positions(self) -> dict:
        
        atoms_positions = {}
        for atom_index in self.atoms.submob_dict.keys():
            atoms_positions[atom_index] = self.find_atom_position_by_index(atom_index=atom_index)
        
        return atoms_positions
    
    
    def find_all_bonds_centers(self) -> dict:
        
        bonds_positions = {}
        for bond_index, _ in enumerate(self.bonds):
            bonds_positions[bond_index] = self.find_bond_center_by_index(bond_index=bond_index)
        
        return bonds_positions
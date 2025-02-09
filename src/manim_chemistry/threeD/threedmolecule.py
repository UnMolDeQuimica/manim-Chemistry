from typing import Optional

from manim import ORIGIN, config
from manim.constants import RendererType
from manim.mobject.opengl.opengl_mobject import OpenGLGroup

from ..element import Element
from ..utils import mol_parser, mol_parser_string
from .threedatom import ThreeDAtom
from .threedbond import ThreeDBond
from ..manim_chemistry_molecule import MCMolecule, MC_ELEMENT_DICT
from ..molecule import AbstractMolecule


class ThreeDMolecule(OpenGLGroup, AbstractMolecule):
    """Draws a 3D Molecule

    Requires using opengl renderer.

    Examples:
    ---------
    .. code-block:: python

        from manim_chemistry import *

        class ThreeDMoleculeFromFile(Scene):
            def construct(self):
                config.renderer = "opengl"
                molecule = GraphMolecule.molecule_from_file(
                    "../examples/molecule_files/mol_files/acetone_3d.mol"
                )
                self.wait()
                self.play(Write(molecule))
                self.wait()


    .. code-block:: python

        from manim_chemistry import *

        class ThreeDMoleculeFromFileWithHydrogens(Scene):
            def construct(self):
                config.renderer = "opengl"
                molecule = ThreeDMolecule.molecule_from_file(
                    "../examples/molecule_files/mol_files/acetone_3d.mol",
                    ignore_hydrogens=False
                )
                self.wait()
                self.play(Write(molecule))
                self.wait()


    .. code-block:: python

        from manim_chemistry import *

        class ThreeDMoleculeFromPubChem(Scene):
            def construct(self):
                config.renderer = "opengl"
                molecule = ThreeDMolecule.molecule_from_pubchem(name="acetone")
                self.wait()
                self.play(Write(molecule))
                self.wait()

    .. code-block:: python

        from manim_chemistry import *

        class ThreeDMoleculeFromPubChemThreeD(Scene):
            def construct(self):
                config.renderer = "opengl"
                molecule = ThreeDMolecule.molecule_from_pubchem(
                    name="acetone",
                    three_d=True,
                    ignore_hydrogens=False
                )
                self.wait()
                self.play(Write(molecule))
                self.wait()
    """

    group_class = OpenGLGroup

    def __init__(
        self,
        atoms_dict,
        bonds_dict,
        source_csv: Optional[str] = None,
        add_bonds=True,
        add_atoms=True,
        *mobjects,
        **kwargs,
    ):
        if config.renderer != RendererType.OPENGL:
            raise Exception(
                "ThreeDMolecule requires using a OpenGL renderer. You can use it adding the `--renderer=opengl` flag or adding `config.renderer = opengl` to your python file."
            )
        self.atoms_dict = atoms_dict
        self.bonds_dict = bonds_dict
        self.source_csv = source_csv
        self.atoms = self.get_atoms_from_csv()
        self.bonds = self.get_bonds()
        super().__init__(**kwargs)
        self.add(*mobjects)
        if add_bonds:
            self.add(self.bonds)
        if add_atoms:
            self.add(self.atoms)
        self.move_to(ORIGIN)

    def get_atoms_from_csv(self):
        atoms = OpenGLGroup()
        for _, atom in self.atoms_dict.items():
            if self.source_csv:
                element = Element.from_csv_file(self.source_csv, atom.get("element"))
            else:
                element = MC_ELEMENT_DICT.get(atom.get("element"))
            atoms.add(ThreeDAtom(element, atom.get("coords")))

        return atoms

    def get_bonds(self):
        bonds = OpenGLGroup()
        for index, bonds_list in self.bonds_dict.items():
            from_atom = self.atoms[index - 1]
            for bond in bonds_list:
                to_atom = self.atoms[bond.get("to") - 1]
                bond_type = bond.get("type")
                bonds.add(
                    ThreeDBond(
                        from_atom=from_atom, to_atom=to_atom, bond_type=int(bond_type)
                    )
                )

        return bonds

    @staticmethod
    def mc_molecule_to_atoms_and_bonds(mc_molecule: MCMolecule):
        """
        Transforms the structure of a mc_molecule to a (atoms, bonds) tuple
        with the following structure:
        - Vertices: {<atom_index>: MCAtom}
        - Edges: {(<from_atom_index>, <to_atom_index>): MCBond}

        Args:
            mc_molecule (MCMolecule): The origin MCMolecule

        Returns:
            Tuple[Dict, Dict]: See above.
        """

        atoms = {}
        for index, atom in mc_molecule.atoms_by_index.items():
            bond_to = {}
            for bond in atom.bonds:
                # TODO: This patches an issue with from_atom and to_atom but does not solve it completely.
                # Fix later the root cause
                if bond.from_atom.molecule_index == index:
                    bond_to[bond.to_atom.molecule_index] = bond.to_atom.element.symbol

                else:
                    bond_to[bond.from_atom.molecule_index] = (
                        bond.from_atom.element.symbol
                    )

            atom_data = {
                "coords": atom.coords,
                "element": atom.element.symbol,
                "bond_to": bond_to,
            }

            atoms[index] = atom_data

        bonds = {}
        for atom_index in atoms.keys():
            atom_bonds = []
            for bond in mc_molecule.bonds:
                if atom_index == bond.to_atom.molecule_index:
                    atom_bonds.append(
                        {
                            "to": bond.from_atom.molecule_index,
                            "type": bond.bond_type,
                            "stereo": bond.stereo,
                            "topology": bond.topology,
                            "reacting_center_status": bond.reacting_center_status,
                        }
                    )
            if atom_bonds:
                bonds[atom_index] = atom_bonds

        return atoms, bonds

    def from_mol_file(filename, source_csv):
        atoms, bonds = mol_parser(file=filename)
        return ThreeDMolecule(atoms_dict=atoms, bonds_dict=bonds, source_csv=source_csv)

    def from_mol_string(mol_string, source_csv):
        atoms, bonds = mol_parser_string(mol_string)
        return ThreeDMolecule(atoms_dict=atoms, bonds_dict=bonds, source_csv=source_csv)

from manim import ORIGIN
from manim.mobject.opengl.opengl_mobject import OpenGLGroup

from ..element import Element
from ..utils import (mol_parser, mol_parser_string, sdf_parser,
                     sdf_parser_string)
from .threedatom import ThreeDAtom
from .threedbond import ThreeDBond


class ThreeDMolecule(OpenGLGroup):
    """
    Uses a .mol file, a data source csv, ThreeDAtoms
    and ThreeDBonds to create a ThreeDMolecule.
    """

    def __init__(
        self,
        atoms_dict,
        bonds_dict,
        source_csv,
        add_bonds=True,
        add_atoms=True,
        *mobjects,
        **kwargs,
    ):
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
            element = Element.from_csv_file(
                self.source_csv, atom.get("element")
            )  # TODO: Make the file an option
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

    def from_mol_file(filename, source_csv):
        atoms, bonds = mol_parser(file=filename)
        return ThreeDMolecule(atoms_dict=atoms, bonds_dict=bonds, source_csv=source_csv)

    def from_mol_string(mol_string, source_csv):
        atoms, bonds = mol_parser_string(mol_string)
        return ThreeDMolecule(atoms_dict=atoms, bonds_dict=bonds, source_csv=source_csv)
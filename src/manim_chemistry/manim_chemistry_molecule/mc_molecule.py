from typing import Dict, List, Optional

from .mc_atom import MCAtom
from .mc_bond import MCBond
from ..utils import FileHandler


class MCMolecule:
    """
    Abstraction of a molecule:
    - MCAtoms.
    - MCBonds.
    - Molecule name.
    - Extra properties (To be defined)
    """

    def __init__(
        self,
        atoms: Optional[List[MCAtom]] = None,
        bonds: Optional[List[MCBond]] = None,
        name: Optional[str] = None,
    ):
        self.atoms = atoms or []
        self.bonds = bonds or []
        self.atoms_by_index = {}
        self.name = name

    def add_atoms_from_atoms_dict(self, atoms_dict: Dict):
        """
        Uses the atoms dict returned by a parser to add the atoms to the molecule.

        Args:
            atoms_dict (Dict): Atoms dict from a parser. See BaseParser.
        """

        if self.atoms and not isinstance(self.atoms, list):
            raise Exception(f"Atoms list {self.atoms} is not an atoms list.")

        else:
            self.atoms = []

        for atom_index, atom_data_dict in atoms_dict.items():
            mc_atom = MCAtom.construct_from_atom_dict(
                atom_index=atom_index, atom_data_dict=atom_data_dict
            )
            mc_atom.assign_molecule(self)
            self.atoms.append(mc_atom)
            self.atoms_by_index[atom_index] = mc_atom

    def add_bonds_from_bonds_dict(self, bonds_dict: Dict):
        """
        Uses the bonds dict returned by a parser to add the bonds to the molecule.

        Args:
            bonds_dict (Dict): Bonds dict from a parser. See Base Parser.
        """

        if self.bonds and not isinstance(self.bonds, list):
            raise Exception("Bonds list is not a bonds list.")

        else:
            self.bonds = []

        for bond_index, bond_data_dict in bonds_dict.items():
            self.bonds.append(
                MCBond.construct_from_bond_dict(
                    bond_index=bond_index, bond_data_dict=bond_data_dict, molecule=self
                )
            )

    def add_connections_between_atoms(self):
        """
        Uses the MCBonds to add connections between MCAtoms.
        """

        if self.bonds and not isinstance(self.bonds, list):
            raise Exception("Bonds list is not a bonds list.")

        for mc_bond in self.bonds:
            mc_bond.from_atom.add_atoms(mc_bond.to_atom)
            mc_bond.from_atom.add_bonds(mc_bond)
            mc_bond.to_atom.add_atoms(mc_bond.from_atom)
            mc_bond.to_atom.add_bonds(mc_bond)

    @staticmethod
    def construct_from_data_dict(atoms_data_dict: dict, bonds_data_dict: dict):
        """
        Given data with the format provided by a parser, constructs a MCMolecule,
        the corresponding MCAtoms and MCBonds and stablishes the connections between
        MCAtoms and bonds.

        Args:
            atoms_data_dict (dict): Atoms data
            bonds_data_dict (dict): Bonds data
        """

        mc_molecule = MCMolecule()
        mc_molecule.add_atoms_from_atoms_dict(atoms_dict=atoms_data_dict)
        mc_molecule.add_bonds_from_bonds_dict(bonds_dict=bonds_data_dict)
        mc_molecule.add_connections_between_atoms()

        return mc_molecule

    @staticmethod
    def construct_from_file(filepath):
        """
        Returns an MCMolecule given a file path.

        Args:
            filepath: File path
        """
        parsed_data = FileHandler(
            file_path=filepath
        ).parsed_atoms_bonds_data()

        if isinstance(parsed_data, list):
            parsed_data = parsed_data[0]

        atoms_dict, bonds_dict = parsed_data
        return MCMolecule.construct_from_data_dict(atoms_dict, bonds_dict)

    @staticmethod
    def construct_multiples_from_file(filepath):
        """
        Similar to `construct_from_file` but returning a list of MCMolecules.
        """

        list_of_data_dicts = FileHandler(file_path=filepath).parsed_atoms_bonds_data()
        mc_molecules = []
        for atoms_dict, bonds_dict in list_of_data_dicts:
            mc_molecules.add(
                MCMolecule.construct_from_data_dict(
                    atoms_data_dict=atoms_dict,
                    bonds_data_dict=bonds_dict
                )
            )

        return mc_molecules

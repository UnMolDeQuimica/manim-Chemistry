from typing import Dict, List, Optional

from .mc_atom import MCAtom
from .mc_bond import MCBond
from .mc_element import MCElement
from ..utils import FileHandler


class MCMolecule:
    """
    Abstraction of a molecule made of:
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
        elements: Optional[MCElement] = None,
    ):
        self.atoms = atoms or []
        self.bonds = bonds or []
        self.elements = elements or {}
        self.atoms_by_index = {}
        self.name = name

    def add_atoms_from_atoms_dict(self, atoms_dict: Dict, elements_data_dict: Dict):
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
                atom_index=atom_index,
                atom_data_dict=atom_data_dict,
                elements_data_dict=elements_data_dict,
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
    def construct_from_data_dict(
        atoms_data_dict: dict,
        bonds_data_dict: dict,
        ignore_hydrogens: bool = True,
        ignore_all_hydrogens: bool = False,
        elements_data_dict: Optional[dict] = None,
    ):
        """
        Given data with the format provided by a parser, constructs a MCMolecule,
        the corresponding MCAtoms and MCBonds and stablishes the connections between
        MCAtoms and bonds.

        Args:
            atoms_data_dict (dict): Atoms data
            bonds_data_dict (dict): Bonds data
        """

        mc_molecule = MCMolecule()
        mc_molecule.add_atoms_from_atoms_dict(
            atoms_dict=atoms_data_dict, elements_data_dict=elements_data_dict
        )
        mc_molecule.add_bonds_from_bonds_dict(bonds_dict=bonds_data_dict)
        mc_molecule.add_connections_between_atoms()

        if ignore_all_hydrogens:
            mc_molecule.remove_all_hydrogens()

        elif ignore_hydrogens:
            mc_molecule.remove_carbon_hydrogens()

        return mc_molecule

    @staticmethod
    def construct_from_file(
        filepath,
        ignore_hydrogens: bool = True,
        ignore_all_hydrogens: bool = False,
        elements_data_dict: Optional[dict] = None,
    ):
        """
        Returns an MCMolecule given a file path.

        Args:
            filepath: File path
        """
        parsed_data = FileHandler(file_path=filepath).parsed_atoms_bonds_data()

        if isinstance(parsed_data, list):
            parsed_data = parsed_data[0]

        atoms_dict, bonds_dict = parsed_data
        return MCMolecule.construct_from_data_dict(
            atoms_dict,
            bonds_dict,
            ignore_hydrogens=ignore_hydrogens,
            ignore_all_hydrogens=ignore_all_hydrogens,
            elements_data_dict=elements_data_dict,
        )

    @staticmethod
    def construct_multiples_from_file(
        filepath,
        ignore_hydrogens: bool = True,
        ignore_all_hydrogens: bool = False,
        elements_data_dict: Optional[dict] = None,
    ):
        """
        Similar to `construct_from_file` but returning a list of MCMolecules.
        """

        list_of_data_dicts = FileHandler(file_path=filepath).parsed_atoms_bonds_data()
        mc_molecules = []
        for atoms_dict, bonds_dict in list_of_data_dicts:
            mc_molecules.append(
                MCMolecule.construct_from_data_dict(
                    atoms_data_dict=atoms_dict,
                    bonds_data_dict=bonds_dict,
                    ignore_hydrogens=ignore_hydrogens,
                    ignore_all_hydrogens=ignore_all_hydrogens,
                    elements_data_dict=elements_data_dict,
                )
            )

        return mc_molecules

    @staticmethod
    def construct_from_string(
        string: str,
        format: str = "json",
        ignore_hydrogens: bool = True,
        ignore_all_hydrogens: bool = False,
        elements_data_dict: Optional[dict] = None,
    ):
        """
        Reads a string and returns a molecule. Supported formats are:
        - mol
        - sdf
        - asnt
        - json
        - xml

        Uses json format by default.
        """
        parsed_data = FileHandler.parse_from_string(string=string, format=format)

        if isinstance(parsed_data, list):
            parsed_data = parsed_data[0]

        atoms_dict, bonds_dict = parsed_data
        return MCMolecule.construct_from_data_dict(
            atoms_dict,
            bonds_dict,
            ignore_hydrogens=ignore_hydrogens,
            ignore_all_hydrogens=ignore_all_hydrogens,
            elements_data_dict=elements_data_dict,
        )

    @staticmethod
    def construct_multiples_from_string(
        string: str,
        format: str = "json",
        ignore_hydrogens: bool = True,
        ignore_all_hydrogens: bool = False,
        elements_data_dict: Optional[dict] = None,
    ):
        """
        Similar to `construct_from_string` but returning a list of MCMolecules.
        """
        parsed_data = FileHandler.parse_from_string(string=string, format=format)
        mc_molecules = []
        for atoms_dict, bonds_dict in parsed_data:
            mc_molecules.append(
                MCMolecule.construct_from_data_dict(
                    atoms_data_dict=atoms_dict,
                    bonds_data_dict=bonds_dict,
                    ignore_hydrogens=ignore_hydrogens,
                    ignore_all_hydrogens=ignore_all_hydrogens,
                    elements_data_dict=elements_data_dict,
                )
            )

        return mc_molecules

    def remove_carbon_hydrogens(self):
        atoms_to_be_removed = []
        for index, atom in self.atoms_by_index.items():
            if atom.element.atomic_number != 1 or atom.element.symbol != "H":
                continue

            if (
                atom.bonds[0].to_atom.element.atomic_number == 6
                or atom.bonds[0].from_atom.element.atomic_number == 6
                or atom.bonds[0].to_atom.element.symbol == "C"
                or atom.bonds[0].from_atom.element.symbol == "C"
            ):
                atoms_to_be_removed.append(index)

        return self.remove_hydrogens(atoms_to_be_removed)

    def remove_all_hydrogens(self):
        atoms_to_be_removed = []
        for index, atom in self.atoms_by_index.items():
            if atom.element.atomic_number != 1:
                continue

            atoms_to_be_removed.append(index)

        return self.remove_hydrogens(atoms_to_be_removed)

    def remove_hydrogens(self, atoms_to_be_removed: list):
        if not atoms_to_be_removed:
            return
        for atom in atoms_to_be_removed:
            self.atoms_by_index.pop(atom)

        self.atoms = list(self.atoms_by_index.values())

        bonds_to_be_removed = []
        for index, bond in enumerate(self.bonds):
            if bond.from_atom.molecule_index in atoms_to_be_removed:
                bonds_to_be_removed.append(index)

            if bond.to_atom.molecule_index in atoms_to_be_removed:
                bonds_to_be_removed.append(index)

        if not bonds_to_be_removed:
            return

        bonds_to_be_removed.reverse()

        for bond in bonds_to_be_removed:
            self.bonds.pop(bond)

        self.reindex_molecule_atoms()

    def reindex_molecule_atoms(self):
        self.atoms_by_index = {}
        atoms_old_index_mapping = {}
        for index, atom in enumerate(self.atoms, start=1):
            atoms_old_index_mapping[atom.molecule_index] = index
            atom.molecule_index = index
            self.atoms_by_index[index] = atom

        for bond in self.bonds:
            if bond.from_atom.molecule_index in atoms_old_index_mapping.keys():
                bond.from_atom.molecule_index = atoms_old_index_mapping[
                    bond.from_atom.molecule_index
                ]

            if bond.to_atom.molecule_index in atoms_old_index_mapping.keys():
                bond.to_atom.molecule_index = atoms_old_index_mapping[
                    bond.to_atom.molecule_index
                ]

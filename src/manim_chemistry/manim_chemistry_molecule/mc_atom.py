from typing import Dict, Optional

import numpy as np

from .mc_element import *


class MCAtom:
    """
    Abstraction of an atom in a molecule:
    - It's MCElement.
    - It's 3D coordinates.
    - The atoms bonded to it.
    - The bonds associated with it.
    - It's molecule.
    - It's index in the molecule.
    """

    def __init__(
        self,
        element: MCElement,
        coords: np.array = np.array([0, 0, 0]),
        atoms: Optional[list] = None,
        bonds: Optional[list] = None,
        molecule: None = None,
        molecule_index: Optional[int] = None,
    ):
        self.element = element
        self.coords = coords
        self.atoms = atoms or []
        self.bonds = bonds or []
        self.molecule = molecule
        self.molecule_index = molecule_index

    def add_atoms(self, atoms):
        """
        Assigns bonded atoms to MCAtom.

        Args:
            atoms (MCAtom or List[MCAtom])

        Raises:
            Exception: In case the atoms are not MCAtoms or a list.
        """
        if not atoms:
            pass

        if not isinstance(atoms, MCAtom) and not isinstance(atoms, list):
            raise Exception(
                f"Expected {MCAtom} or list of {MCAtom} when assigning atoms but received {atoms}"
            )

        if isinstance(self.atoms, list) and isinstance(atoms, MCAtom):
            self.atoms.append(atoms)

        if isinstance(self.atoms, list) and isinstance(atoms, list):
            if not all([isinstance(atom, MCAtom) for atom in atoms]):
                raise Exception(
                    f"Expected {MCAtom} or list of {MCAtom} when assigning atoms but received {atoms}"
                )

            self.atoms.extend(atoms)

        return self.atoms

    def add_bonds(self, bonds):
        from .mc_bond import MCBond

        if not bonds:
            pass

        if not isinstance(bonds, MCBond) and not isinstance(bonds, list):
            raise Exception(
                f"Expected {MCBond} or list of {MCBond} when assigning atoms but received {bonds}"
            )

        if isinstance(self.bonds, list) and isinstance(bonds, MCBond):
            self.bonds.append(bonds)

        if isinstance(self.bonds, list) and isinstance(bonds, list):
            if not all([isinstance(bond, MCBond) for bond in bonds]):
                raise Exception(
                    f"Expected {MCBond} or list of {MCBond} when assigning atoms but received {bonds}"
                )

            self.bonds.extend(bonds)

        return self.bonds

    def assign_molecule(self, molecule):
        from .mc_molecule import MCMolecule

        if not molecule:
            pass

        if not isinstance(molecule, MCMolecule):
            raise Exception(
                f"Expected {MCMolecule} when assigning molecule but received {molecule}"
            )

        self.molecule = molecule

        return self.molecule

    def assign_molecule_index(self, molecule_index: int):
        if isinstance(molecule_index, None):
            pass

        if not isinstance(molecule_index, int):
            raise Exception(
                f"Expected {int} when assigning molecule_index but received {molecule_index}"
            )

        self.molecule_index = molecule_index

        return self.molecule_index

    @staticmethod
    def construct_from_atom_dict(
        atom_index, atom_data_dict: Dict, elements_data_dict: Dict
    ):
        """
        Given an atom data dict from a parser, returns an MCAtom

        Args:
            atom_dict (Dict): See data_parser function from BaseParser

        Output:
            MCAtom
        """

        if not isinstance(atom_data_dict, dict):
            raise Exception(f"Expected {dict} but received {atom_data_dict}")

        element = atom_data_dict.get("element", None)

        if not element:
            raise Exception(
                f"Atom dict {atom_data_dict} does not contain element data."
            )

        if element not in MC_ELEMENT_DICT:
            raise Exception(
                f"Element {element} does not match any known element by human kind. Is that an alien element?"
            )

        mc_element_dict = MC_ELEMENT_DICT.copy()

        if elements_data_dict:
            mc_element_dict |= elements_data_dict

        mc_element = mc_element_dict.get(element)

        coords = atom_data_dict.get("coords")

        if not isinstance(coords, (np.ndarray, np.generic)) and not isinstance(
            coords, list
        ):
            raise Exception(f"Coordinates {coords} are not correct coordinates.")

        return MCAtom(element=mc_element, coords=coords, molecule_index=atom_index)

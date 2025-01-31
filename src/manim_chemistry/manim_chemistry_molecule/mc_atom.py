from typing import Optional
from .mc_element import *

class MCAtom:
    """
    Abstraction of an atom in a molecule:
    - It's MCElement.
    - The atoms bonded to it.
    - The bonds associated with it.
    - It's molecule.
    - It's index in the molecule.
    """
    def __init__(self, element: MCElement, atoms: Optional[list]=None, bonds: Optional[list]=None, molecule: None=None, molecule_index: Optional[int]=None):
        self.element = element
        self.atoms = atoms
        self.bonds = bonds
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
        if isinstance(atoms, None):
            pass

        if not isinstance(atoms, MCAtom) or not isinstance(atoms, list):
            raise Exception(f"Expected {MCAtom} or list of {MCAtom} when assigning atoms but received {atoms}")

        if isinstance(self.atoms, None):
            self.atoms = atoms

        if isinstance(self.atoms, list) and isinstance(atoms, MCAtom):
            self.atoms.append(atoms)

        if isinstance(self.atoms, list) and isinstance(atoms, list):
            if not all([isinstance(atom, MCAtom) for atom in atoms]):
                raise Exception(f"Expected {MCAtom} or list of {MCAtom} when assigning atoms but received {atoms}")

            self.atoms.extend(atoms)

        return self.atoms

    def assign_bonds(self, bonds):
        from .mc_bond import MCBond
        if isinstance(bonds, None):
            pass

        if not isinstance(bonds, MCBond) or not isinstance(bonds, list):
            raise Exception(f"Expected {MCBond} or list of {MCBond} when assigning atoms but received {bonds}")

        if isinstance(self.bonds, list) and isinstance(bonds, MCAtom):
            self.bonds.append(bonds)

        if isinstance(self.bonds, list) and isinstance(bonds, list):
            if not all([isinstance(bond, MCBond) for bond in bonds]):
                raise Exception(f"Expected {MCBond} or list of {MCBond} when assigning atoms but received {bonds}")

            self.bonds.extend(bonds)

        return self.bonds

    def assign_molecule(self, molecule):
        from .mc_molecule import MCMolecule

        if isinstance(molecule, None):
            pass

        if not isinstance(molecule, MCMolecule):
            raise Exception(f"Expected {MCMolecule} when assigning molecule but received {molecule}")

        self.molecule = molecule

        return self.molecule

    def assign_molecule_index(self, molecule_index: int):
        if isinstance(molecule_index, None):
            pass

        if not isinstance(molecule_index, int):
            raise Exception(f"Expected {int} when assigning molecule_index but received {molecule_index}")

        self.molecule_index = molecule_index

        return self.molecule_index

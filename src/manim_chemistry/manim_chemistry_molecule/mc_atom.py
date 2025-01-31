from typing import Any
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
    def __init__(self, element: MCElement, atoms: list, bonds: list, molecule: Any, molecule_index: int):
        self.element = element
        self.atoms = atoms
        self.bonds = bonds
        self.molecule = molecule
        self.molecule_index = molecule_index
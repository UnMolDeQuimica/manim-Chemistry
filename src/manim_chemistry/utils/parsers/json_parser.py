import json
import os
from typing import Any, Dict, List, Tuple, Union

import numpy as np

from .base_parser import BaseParser

ELEMENTS_BY_ATOMIC_NUMBER = {
    1: "H",
    2: "He",
    3: "Li",
    4: "Be",
    5: "B",
    6: "C",
    7: "N",
    8: "O",
    9: "F",
    10: "Ne",
    11: "Na",
    12: "Mg",
    13: "Al",
    14: "Si",
    15: "P",
    16: "S",
    17: "Cl",
    18: "Ar",
    19: "K",
    20: "Ca",
    21: "Sc",
    22: "Ti",
    23: "V",
    24: "Cr",
    25: "Mn",
    26: "Fe",
    27: "Co",
    28: "Ni",
    29: "Cu",
    30: "Zn",
    31: "Ga",
    32: "Ge",
    33: "As",
    34: "Se",
    35: "Br",
    36: "Kr",
    37: "Rb",
    38: "Sr",
    39: "Y",
    40: "Zr",
    41: "Nb",
    42: "Mo",
    43: "Tc",
    44: "Ru",
    45: "Rh",
    46: "Pd",
    47: "Ag",
    48: "Cd",
    49: "In",
    50: "Sn",
    51: "Sb",
    52: "Te",
    53: "I",
    54: "Xe",
    55: "Cs",
    56: "Ba",
    57: "La",
    58: "Ce",
    59: "Pr",
    60: "Nd",
    61: "Pm",
    62: "Sm",
    63: "Eu",
    64: "Gd",
    65: "Tb",
    66: "Dy",
    67: "Ho",
    68: "Er",
    69: "Tm",
    70: "Yb",
    71: "Lu",
    72: "Hf",
    73: "Ta",
    74: "W",
    75: "Re",
    76: "Os",
    77: "Ir",
    78: "Pt",
    79: "Au",
    80: "Hg",
    81: "Tl",
    82: "Pb",
    83: "Bi",
    84: "Po",
    85: "At",
    86: "Rn",
    87: "Fr",
    88: "Ra",
    89: "Ac",
    90: "Th",
    91: "Pa",
    92: "U",
    93: "Np",
    94: "Pu",
    95: "Am",
    96: "Cm",
    97: "Bk",
    98: "Cf",
    99: "Es",
    100: "Fm",
    101: "Md",
    102: "No",
    103: "Lr",
    104: "Rf",
    105: "Db",
    106: "Sg",
    107: "Bh",
    108: "Hs",
    109: "Mt",
    110: "Ds",
    111: "Rg",
    112: "Cn",
    113: "Nh",
    114: "Fl",
    115: "Mc",
    116: "Lv",
    117: "Ts",
    118: "Og",
}

class JSONParser(BaseParser):
    @staticmethod
    def read_file(filename: Union[str, bytes, os.PathLike]) -> Any:
        """
        Reads the file and converts it to a string.

        Returns:
            str: String with the file data.
        """
        with open(filename) as file:
            json_file = file.read()

        return json_file

    @staticmethod
    def data_parser(data: Any) -> Tuple[Dict, Dict] | List[Tuple[Dict, Dict]]:
        """
        Parses the atoms and bonds data and returns a tuple of dictionaries with each data.
        The Json format usually follows the structure:
        {
            <Origin of the file>: [
                {
                    <Molecule data>
                }
            ]
        }

        The atom data follows the structure:
            {<atom_index>: {"element": <atom_element>, "position": [<x_pos>, <y_pos>, <z_pos>]}}

        The bond data follows the structure:
            {<bond_index>: {"from_atom_index": <from_atom_index>, "to_atom_index": <to_atom_index>, "bond_type": <bond_type>}}
        """
        molecules_data_dicts_list = list(json.loads(data).values())[0]
        molecules_parsed_data = []
        for molecule_data in molecules_data_dicts_list:
            molecules_parsed_data.append(
                JSONParser.parse_single_molecule_data(molecule_data=molecule_data)
            )

        return molecules_parsed_data


    @staticmethod
    def parse_single_molecule_data(molecule_data: Dict) -> Tuple[Dict, Dict]:
        atoms_data = JSONParser.extract_atoms_data(molecule_data=molecule_data)
        bonds_data = JSONParser.extract_bonds_data(molecule_data=molecule_data)

        return atoms_data, bonds_data

    @staticmethod
    def extract_atoms_data(molecule_data: Dict) -> Dict:
        atoms_initial_data_dict = molecule_data.get("atoms")
        if not isinstance(atoms_initial_data_dict, dict):
            raise Exception(f"Wrong atomic data on molecule data: {molecule_data}")

        atoms_indices = atoms_initial_data_dict.get("aid")
        atoms_elements_raw = atoms_initial_data_dict.get("element")

        if not atoms_indices:
            raise Exception(f"No atoms found on molecule data: {molecule_data}")

        if not atoms_elements_raw:
            raise Exception(f"No elements found on molecule data: {molecule_data}")

        atoms_elements = JSONParser.clean_elements_data(atoms_elements_raw)

        atoms_coords_dict = molecule_data.get("coords")[0]
        if not isinstance(atoms_coords_dict, dict):
            raise Exception(f"Atomic coords are not defined as a dictionary: {atoms_coords_dict}")

        conformers_coords = atoms_coords_dict.get("conformers")[0]
        if not isinstance(conformers_coords, dict):
            raise Exception(f"Conformers coords are not defined as a dictionary: {conformers_coords}")

        x_coords = conformers_coords.get("x")
        y_coords = conformers_coords.get("y")
        z_coords = conformers_coords.get("z")

        if not z_coords:
            z_coords = [0 for _ in x_coords]

        atoms_data = {}
        for atom_index, element, x_coord, y_coord, z_coord in zip(atoms_indices, atoms_elements, x_coords, y_coords, z_coords):
            atoms_data[atom_index] = {
                "element": element,
                "coords": np.array([x_coord, y_coord, z_coord])
            }

        return atoms_data

    @staticmethod
    def extract_bonds_data(molecule_data: Dict) -> Dict:
        bonds_data_dict = molecule_data.get("bonds")
        if not isinstance(bonds_data_dict, dict):
            raise Exception(f"Bonds data is not defined correctly: {molecule_data}")

        from_atoms_data = bonds_data_dict.get("aid1")
        to_atoms_data = bonds_data_dict.get("aid2")
        bond_type_list = bonds_data_dict.get("order")

        bonds_data = {}
        for index, bond_data in enumerate(zip(from_atoms_data, to_atoms_data, bond_type_list)):
            from_atom, to_atom, bond_type = bond_data
            bonds_data[index] = {
                "from_atom_index": from_atom,
                "to_atom_index": to_atom,
                "bond_type": bond_type
            }

        return bonds_data


    @staticmethod
    def clean_elements_data(atoms_elements_raw: List[int]):
        return [ELEMENTS_BY_ATOMIC_NUMBER[elemenent_atomic_number] for elemenent_atomic_number in atoms_elements_raw]

    
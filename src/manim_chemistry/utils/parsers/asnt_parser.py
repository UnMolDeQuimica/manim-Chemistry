from typing import Any, Dict, List, Tuple, Union
import os

import numpy as np

from .base_parser import BaseParser

BOND_TYPE_MAPPING = {
    "simple": 1,
    "double": 2,
    "triple": 3,
}

class ASNTParser(BaseParser):
    """
    The ASNT format is weird. It's like a JSON wannabe but ugly.
    Parsing it has been a pain for the last 5 hours and I wish
    to never encounter it again. It will only support a single molecule
    files and fuck it. Yes, fuck it goes to the commit.
    """

    @staticmethod
    def read_file(filename: Union[str, bytes, os.PathLike]) -> List[List[str]]:
        with open(filename, "r") as asnt_file:
            file_list = asnt_file.readlines()

        return file_list

    @staticmethod
    def replace_stuff(line: str):
        line = line.strip().replace("\n", "")
        line = line.replace('"', '¿')
        line = line.replace("'", '¡')
        if line.startswith("{"):
            if len(line) == 1:
                # That means the line is {
                return line

            if line.endswith("}") or line.endswith("},"):
                # That means the line is { value, value, value, }
                line = line.replace("{", "[")
                line = line.replace("}", "]")

                return line

        if line.startswith("}") or line.startswith("},"):
            return line

        line = '"' + line.replace(" ", '" "')

        if line.endswith("{"):
            line = line.replace(' "{', ": {")

        if line.endswith(","):
            line = line.replace(",", '",')

        else:
            line = line + '"'

        if line.endswith('}"') or line.endswith('{"'):
            line = line[:-1]
        line = line.replace('" "', '": "')

        line = line.replace("¿", "'")
        line = line.replace("¡", "'")

        return line

    @staticmethod
    def data_parser(data: Any) -> Tuple[Dict, Dict] | List[Tuple[Dict, Dict]]:
        """
        Parses the atoms and bonds data and returns a tuple of dictionaries with each data.
        The atom data follows the structure:
            {<atom_index>: {"element": <atom_element>, "position": [<x_pos>, <y_pos>, <z_pos>]}}

        The bond data follows the structure:
            {<bond_index>: {"from_atom_index": <from_atom_index>, "to_atom_index": <to_atom_index>, "bond_type": <bond_type>}}
        """
        lines_list = data
        line = lines_list[0]
        while not line.startswith('"atoms"'):
            line = ASNTParser.replace_stuff(lines_list.pop(0))

        atoms_indices = []
        lines_list.pop(0) # Remove atoms line
        line = ASNTParser.replace_stuff(lines_list.pop(0)) # Start atoms
        while not line.startswith("}"):
            atoms_indices.append(line.replace(",", "").replace('"', ""))
            line = ASNTParser.replace_stuff(lines_list.pop(0))

        atoms_indices = atoms_indices
        atoms_elements = []
        lines_list.pop(0) # Remove element line
        line = ASNTParser.replace_stuff(lines_list.pop(0)) # Get first element
        while not line.startswith("}"):
            atoms_elements.append(line.replace(",", "").replace('"', "").capitalize())
            line = ASNTParser.replace_stuff(lines_list.pop(0))

        atoms_data = {int(float(atom_index.strip())): {"element": atom_element} for atom_index, atom_element in zip(atoms_indices, atoms_elements)}


        from_atom_index = []

        lines_list.pop(0) # Remove }, line
        lines_list.pop(0) # Remove bonds line
        lines_list.pop(0) # Remove aid1 line
        line = ASNTParser.replace_stuff(lines_list.pop(0)) # Get first from atom index
        while not line.startswith("}"):
            from_atom_index.append(int(line.replace(",", "").replace('"', "")))
            line = ASNTParser.replace_stuff(lines_list.pop(0))

        to_atom_index = []
        lines_list.pop(0) # Remove aid2 line
        line = ASNTParser.replace_stuff(lines_list.pop(0)) # Get first to atom index
        while not line.startswith("}"):
            to_atom_index.append(int(line.replace(",", "").replace('"', "")))
            line = ASNTParser.replace_stuff(lines_list.pop(0))

        bond_type_list = []
        lines_list.pop(0) # Remove aid2 line
        line = ASNTParser.replace_stuff(lines_list.pop(0)) # Get first bond
        while not line.startswith("}"):
            bond_type_list.append(line.replace(",", ""))
            line = ASNTParser.replace_stuff(lines_list.pop(0))

        while not line.startswith('"conformers"'):
            line = ASNTParser.replace_stuff(lines_list.pop(0))

        bonds_data = {}
        for bond_index, bond_params in enumerate(zip(from_atom_index, to_atom_index, bond_type_list)):
            from_atom, to_atom, bond_type = bond_params
            bonds_data[bond_index] = {
                "from_atom_index": from_atom,
                "to_atom_index": to_atom,
                "bond_type": BOND_TYPE_MAPPING.get(bond_type.replace('"', ""), 1)
                }

        coords_x = {}
        lines_list.pop(0) # Remove { line
        lines_list.pop(0) # Remove x { line
        line = ASNTParser.replace_stuff(lines_list.pop(0))
        for i in atoms_data.keys():
            line = line.replace("[", "").replace("]", "").replace(",", "").strip().split(" ")
            coords_x[i] = int(line[0]) * int(line[1]) ** int(line[2])
            line = ASNTParser.replace_stuff(lines_list.pop(0))

        coords_y = {}
        lines_list.pop(0) # Remove y { line
        line = ASNTParser.replace_stuff(lines_list.pop(0))
        for i in atoms_data.keys():
            line = line.replace("[", "").replace("]", "").replace(",", "").strip().split(" ")
            coords_y[i] = int(line[0]) * int(line[1]) ** int(line[2])
            line = ASNTParser.replace_stuff(lines_list.pop(0))

        for index in atoms_data.keys():
            atoms_data[index]["coords"] = np.array([coords_x[index], coords_y[index], 0])

        return atoms_data, bonds_data


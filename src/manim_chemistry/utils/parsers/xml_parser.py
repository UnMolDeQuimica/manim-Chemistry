from typing import Dict, Tuple, Union
import os

import numpy as np
import xmltodict

from .base_parser import BaseParser


class XMLParser(BaseParser):
    @staticmethod
    def read_file(filename: Union[str, bytes, os.PathLike]) -> list:
        with open(filename) as file:
            xml_file = file.read()

        return xml_file

    @staticmethod
    def data_parser(data: list) -> Tuple[Dict, Dict]:
        """
        Parses the atoms and bonds data and returns a tuple of dictionaries with each data.
        Currently only PubChem xml files are supported.

        The atom data follows the structure:
            {<atom_index>: {"element": <atom_element>, "position": [<x_pos>, <y_pos>, <z_pos>]}}

        The bond data follows the structure:
            {<bond_index>: {"from_atom_index": <from_atom_index>, "to_atom_index": <to_atom_index>, "bond_type": <bond_type>}}
        """
        molecule_data = xmltodict.parse(data).get("PC-Compounds").get("PC-Compound")
        molecule_parsed_data = XMLParser.parse_molecule_data(
            molecule_data=molecule_data
        )

        return molecule_parsed_data

    @staticmethod
    def parse_molecule_data(molecule_data: Dict) -> Tuple[Dict, Dict]:
        atoms_data = XMLParser.extract_atoms_data(molecule_data=molecule_data)
        bonds_data = XMLParser.extract_bonds_data(molecule_data=molecule_data)

        return atoms_data, bonds_data

    @staticmethod
    def extract_atoms_data(molecule_data: Dict) -> Dict:
        atoms_data_dict = molecule_data.get("PC-Compound_atoms").get("PC-Atoms")
        if not isinstance(atoms_data_dict, dict):
            raise Exception(f"Atoms data has no dictionary structure {atoms_data_dict}")

        atoms_indices_raw = atoms_data_dict.get("PC-Atoms_aid").get("PC-Atoms_aid_E")
        atoms_indices = [int(atom_index) for atom_index in atoms_indices_raw]

        atoms_elements_raw = atoms_data_dict.get("PC-Atoms_element").get("PC-Element")
        atoms_elements = []
        for atom_element_dict in atoms_elements_raw:
            atoms_elements.append(atom_element_dict.get("@value"))

        coords_data_dict = molecule_data.get("PC-Compound_coords").get("PC-Coordinates")
        atoms_coords_raw = coords_data_dict.get("PC-Coordinates_conformers").get(
            "PC-Conformer"
        )

        coords_x = [
            float(coord)
            for coord in atoms_coords_raw.get("PC-Conformer_x").get("PC-Conformer_x_E")
        ]
        coords_y = [
            float(coord)
            for coord in atoms_coords_raw.get("PC-Conformer_y").get("PC-Conformer_y_E")
        ]
        if atoms_coords_raw.get("PC-Conformer_z"):
            coords_z = [
                float(coord)
                for coord in atoms_coords_raw.get("PC-Conformer_z").get(
                    "PC-Conformer_z_E"
                )
            ]

        else:
            coords_z = [0 for _ in coords_x]

        atoms_coords = [
            np.array([coord_x, coord_y, coord_z])
            for coord_x, coord_y, coord_z in zip(coords_x, coords_y, coords_z)
        ]

        atoms_data = {
            atom_index: {"element": element.capitalize(), "coords": coord}
            for atom_index, element, coord in zip(
                atoms_indices, atoms_elements, atoms_coords
            )
        }

        return atoms_data

    @staticmethod
    def extract_bonds_data(molecule_data: Dict) -> Dict:
        bonds_data_dict = molecule_data.get("PC-Compound_bonds").get("PC-Bonds")

        from_atoms_raw_data = bonds_data_dict.get("PC-Bonds_aid1").get(
            "PC-Bonds_aid1_E"
        )
        from_atoms_data = [
            int(from_atom_index) for from_atom_index in from_atoms_raw_data
        ]

        to_atoms_raw_data = bonds_data_dict.get("PC-Bonds_aid2").get("PC-Bonds_aid2_E")
        to_atoms_data = [int(to_atom_index) for to_atom_index in to_atoms_raw_data]

        bonds_type_raw_data = bonds_data_dict.get("PC-Bonds_order").get("PC-BondType")
        bonds_type_data = [
            int(bond_type_data.get("#text")) for bond_type_data in bonds_type_raw_data
        ]

        bonds_data = {}
        for index, bond_data in enumerate(
            zip(from_atoms_data, to_atoms_data, bonds_type_data)
        ):
            from_atom_index, to_atom_index, bond_type = bond_data
            bonds_data[index] = {
                "from_atom_index": from_atom_index,
                "to_atom_index": to_atom_index,
                "bond_type": bond_type,
            }

        return bonds_data

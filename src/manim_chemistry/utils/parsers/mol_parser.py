from typing import Dict, Tuple, Union
import os


import numpy as np

from .base_parser import BaseParser


class MolParser(BaseParser):
    """Parses mol files

    Examples
    --------

    .. code-block:: python

        parsed_mol = MolParser(filename="acetone_2d.json")
        print(parsed_mol.atoms_data)
        print(parsed_mol.bonds_data)
        >>> {
            1: {"element": "O", "coords": array([3.732, 0.75, 0.0])},
            2: {"element": "C", "coords": array([2.866, 0.25, 0.0])},
            3: {"element": "C", "coords": array([2.0, 0.75, 0.0])},
            4: {"element": "C", "coords": array([2.866, -0.75, 0.0])},
            5: {"element": "H", "coords": array([2.31, 1.2869, 0.0])},
            6: {"element": "H", "coords": array([1.4631, 1.06, 0.0])},
            7: {"element": "H", "coords": array([1.69, 0.2131, 0.0])},
            8: {"element": "H", "coords": array([2.246, -0.75, 0.0])},
            9: {"element": "H", "coords": array([2.866, -1.37, 0.0])},
            10: {"element": "H", "coords": array([3.486, -0.75, 0.0])},
        }
        >>> {
            0: {"from_atom_index": 1, "to_atom_index": 2, "bond_type": 2},
            1: {"from_atom_index": 2, "to_atom_index": 3, "bond_type": 1},
            2: {"from_atom_index": 2, "to_atom_index": 4, "bond_type": 1},
            3: {"from_atom_index": 3, "to_atom_index": 5, "bond_type": 1},
            4: {"from_atom_index": 3, "to_atom_index": 6, "bond_type": 1},
            5: {"from_atom_index": 3, "to_atom_index": 7, "bond_type": 1},
            6: {"from_atom_index": 4, "to_atom_index": 8, "bond_type": 1},
            7: {"from_atom_index": 4, "to_atom_index": 9, "bond_type": 1},
            8: {"from_atom_index": 4, "to_atom_index": 10, "bond_type": 1},
        }
    """
    @staticmethod
    def read_file(filename: Union[str, bytes, os.PathLike]) -> list:
        with open(filename) as file:
            mol_file = file.readlines()

        return mol_file

    @staticmethod
    def data_parser(data: list) -> Tuple[Dict, Dict]:
        # Get general data
        mol_name = data[0].strip()  # This info is not always available  # noqa F841
        mol_source = data[1].strip()  # This info is not always available  # noqa F841
        mol_comments = data[2].rstrip()  # This info is not always available # noqa F841
        mol_general_info = data[3]  # This info is not always available
        data.remove(mol_general_info)  # This info is not always available
        mol_general_info = (
            mol_general_info.rstrip().split()
        )  # This info is not always available
        number_of_atoms = int(mol_general_info[0])
        number_of_bonds = int(mol_general_info[1])

        atoms = {}
        bonds = {}
        for index, line in enumerate(data[3 : 3 + number_of_atoms]):
            line_data = line.split()
            x_position = float(line_data[0])
            y_position = float(line_data[1])
            z_position = float(line_data[2])
            element = line_data[3]
            atoms[index + 1] = {
                "coords": np.array([x_position, y_position, z_position]),
                "element": element,
            }
        bond_index = 1
        for line in data[3 + number_of_atoms : 3 + number_of_atoms + number_of_bonds]:
            line_data = line.split()
            first_atom_index = int(float(line_data[0]))
            second_atom_index = int(float(line_data[1]))
            bond_type = line_data[2]
            bond_data = {
                "to_atom_index": first_atom_index,
                "from_atom_index": second_atom_index,
                "bond_type": bond_type,
                "bond_index": bond_index,
                "stereo": None,
                "topology": None,
                "reacting_center_status": None,
            }
            bond_index += 1

            try:
                bond_stereo = line_data[3]
            except Exception as _:
                bond_stereo = ""
            else:
                bond_data["stereo"] = int(bond_stereo)

            try:
                bond_topology = line_data[5]
            except Exception as _:
                bond_topology = ""
            else:
                bond_data["topology"] = int(bond_topology)

            try:
                reacting_center_status = line_data[6]
            except Exception as _:
                reacting_center_status = ""
            else:
                bond_data["reacting_center_status"] = int(reacting_center_status)

            if first_atom_index not in bonds:
                bonds[first_atom_index] = [bond_data]
                if not atoms.get(first_atom_index) or not atoms.get(
                    first_atom_index
                ).get("bond_to"):
                    atoms[first_atom_index]["bond_to"] = {
                        second_atom_index: atoms.get(second_atom_index).get("element")
                    }
                else:
                    atoms[first_atom_index]["bond_to"][second_atom_index] = atoms.get(
                        second_atom_index
                    ).get("element")

            else:
                bonds[first_atom_index].append(bond_data)
                atoms[first_atom_index]["bond_to"][second_atom_index] = atoms.get(
                    second_atom_index
                ).get("element")

            if not atoms.get(second_atom_index).get("bond_to"):
                atoms[second_atom_index]["bond_to"] = {
                    first_atom_index: atoms.get(first_atom_index).get("element")
                }
            else:
                atoms[second_atom_index]["bond_to"][first_atom_index] = atoms.get(
                    first_atom_index
                ).get("element")

        new_bonds = {}

        for bonds_data in bonds.values():
            for bond in bonds_data:
                bond_index = bond.pop("bond_index")
                new_bonds[bond_index] = bond

        bonds = new_bonds

        return atoms, bonds

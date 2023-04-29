import numpy as np
from typing import Dict, Any


def mol_parser(file):
    with open(file) as file:
        mol_file = file.readlines()
    # Get general data

    mol_name = mol_file[0].strip()  # This info is not always available
    mol_source = mol_file[1].strip()  # This info is not always available
    mol_comments = mol_file[2].rstrip()  # This info is not always available
    mol_general_info = mol_file[3]  # This info is not always available
    mol_file.remove(mol_general_info)  # This info is not always available
    mol_general_info = (
        mol_general_info.rstrip().split()
    )  # This info is not always available
    number_of_atoms = int(mol_general_info[0])
    number_of_bonds = int(mol_general_info[1])

    atoms = {}
    bonds = {}
    for index, line in enumerate(mol_file[3 : 3 + number_of_atoms]):
        line_data = line.split()
        x_position = float(line_data[0])
        y_position = float(line_data[1])
        z_position = float(line_data[2])
        element = line_data[3]
        atoms[index + 1] = {
            "coords": np.array([x_position, y_position, z_position]),
            "element": element,
        }

    for line in mol_file[3 + number_of_atoms : 3 + number_of_atoms + number_of_bonds]:
        line_data = line.split()
        first_atom_index = int(float(line_data[0]))
        second_atom_index = int(float(line_data[1]))
        bond_type = line_data[2]
        bond_data = {
            "to": second_atom_index,
            "type": bond_type,
            # "stereo": bond_stereo,
            # "topology": bond_topology,
            # "reacting_center_status": reacting_center_status
        }

        try:
            bond_stereo = line_data[3]
        except:
            bond_stereo = ""
        else:
            bond_data["stereo"] = int(bond_stereo)

        try:
            bond_topology = line_data[5]
        except:
            bond_topology = ""
        else:
            bond_data["topology"] = int(bond_topology)

        try:
            reacting_center_status = line_data[6]
        except:
            reacting_center_status = ""
        else:
            bond_data["reacting_center_status"] = int(reacting_center_status)

        if first_atom_index not in bonds:
            bonds[first_atom_index] = [bond_data]
            if not atoms.get(first_atom_index) or not atoms.get(first_atom_index).get(
                "bond_to"
            ):
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

    return atoms, bonds  # Should return atoms and bonds

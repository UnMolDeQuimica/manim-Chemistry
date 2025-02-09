from typing import Dict, List, Tuple, Union
import os

from .mol_parser import MolParser


class SDFParser(MolParser):
    """ Parses sdf files.
    The sdf format is very similar to the mol format. It only contains some
    extra lines. By modifying the read file and removing those extra lines we
    can use the logic already implemented in MolParser.

    The main difference between an sdf file and a mol file is an sdf file
    supports having multiple molecules, so we are returning a list of molecules
    instead of a single molecule.

    Examples
    --------

    .. code-block:: python

        parsed_xml = XMLParser(filename="acetone_2d.json")
        print(parsed_xml.atoms_data)
        print(parsed_xml.bonds_data)
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
    def read_file(filename: Union[str, bytes, os.PathLike]) -> List[List[str]]:
        """
        sdf files might contain multiple molecules, so we return a list of list
        of string when reading a file.

        Args:
            filename (Union[str, bytes, os.PathLike]): Path of the sdf file

        Returns:
            List[List[str]]: List with all the molecules data.
        """
        with open(filename) as file:
            sdf_file_data = file.read()

        sdf_molecules = sdf_file_data.split("$$$$")
        return [molecule.split("\n") for molecule in sdf_molecules if molecule.strip()]

    @staticmethod
    def data_parser(molecules_data: List[List[str]]) -> List[Tuple[Dict, Dict]]:
        return [MolParser.data_parser(data) for data in molecules_data]

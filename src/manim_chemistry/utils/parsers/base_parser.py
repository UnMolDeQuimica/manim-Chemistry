from abc import ABC, abstractmethod
import os
from typing import Any, Dict, Tuple, Union


class BaseParser(ABC):
    def __init__(self, filename: Union[str, bytes, os.PathLike]) -> None:
        """
        Initializas the parser given a file name.

        This is a base  class that must be extended on child classes.

        The purposes of the parser classes are:
            - Read a file with chemical data.
            - Parse the file to extract the atoms and bonds data.
            - Return a dictionary with the atoms and bonds data.

        Args:
            filename (Union[str, bytes, os.PathLike]): Path of the file to be parsed
        """
        self.file_data: str = self.read_file(filename)
        self.atoms_data, self.bonds_data = self.parse_file_data()

    @staticmethod
    @abstractmethod
    def read_file(filename: Union[str, bytes, os.PathLike]) -> Any:
        """
        Reads the file and converts it to a string.

        Returns:
            str: String with the file data.
        """
        ...

    @staticmethod
    @abstractmethod
    def data_parser(data: Any) -> Tuple[Dict, Dict]:
        """
        Parses the atoms and bonds data and returns a tuple of dictionaries with each data.
        The atom data follows the structure:
            {<atom_index>: {"element": <atom_element>, "position": [<x_pos>, <y_pos>, <z_pos>]}}

        The bond data follows the structure:
            {<bond_index>: {"from_atom_index": <from_atom_index>, "to_atom_index": <to_atom_index>, "bond_type": <bond_type>}}
        """
        ...

    def parse_file_data(self) -> Tuple[Dict, Dict]:
        """
        Receives the file data as a string and uses the string_parser.

        Returns:
            Tuple[Dict, Dict]: (atom_data, bond_data)
        """
        return self.data_parser(self.file_data)

    @property
    def molecule_data(self):
        """
        Returns molecule data: atoms_data and bonds_data.
        """

        return self.atoms_data, self.bonds_data

    @property
    def atoms(self):
        """
        Returns atoms data.
        """

        return self.atoms_data

    @property
    def bonds(self):
        """
        Returns bonds data.
        """

        return self.bonds_data

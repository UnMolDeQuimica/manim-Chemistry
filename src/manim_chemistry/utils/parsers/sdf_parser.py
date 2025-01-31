from typing import Dict, List, Tuple, Union
import os

import numpy as np

from .mol_parser import MolParser


class SDFParser(MolParser):
    """
    The sdf format is very similar to the mol format. It only contains some
    extra lines. By modifying the read file and removing those extra lines we
    can use the logic already implemented in MolParser.

    The main difference between an sdf file and a mol file is an sdf file
    supports having multiple molecules, so we are returning a list of molecules
    instead of a single molecule.
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
        return [molecule.strip() for molecule in sdf_molecules if molecule.strip()]

    @staticmethod
    def data_parser(molecules_data: List[List[str]]) -> List[Tuple[Dict, Dict]]:
        return [super.data_parser(data) for data in molecules_data[1:]]

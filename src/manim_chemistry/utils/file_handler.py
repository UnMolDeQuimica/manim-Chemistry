import os
from typing import Dict, Tuple, Union

from .parsers import MolParser, SDFParser, ASNTParser, JSONParser

SUPPORTED_FORMATS = {"mol": MolParser, "sdf": SDFParser, "asnt": ASNTParser, "json": JSONParser}


class IncorrectFormat(Exception): ...


class FileHandler:
    def __init__(self, file_path: Union[str, bytes, os.PathLike]):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File {file_path} does not exist.")

        file_extension = FileHandler.get_file_extension(file_path)

        if file_extension not in SUPPORTED_FORMATS:
            raise IncorrectFormat(
                f"File {file_path} of format {file_extension} is not supported. Supported extensions are {SUPPORTED_FORMATS.keys()}"
            )

        self.parser = SUPPORTED_FORMATS.get(file_extension)(filename=file_path)

    @staticmethod
    def get_file_extension(file_path):
        return os.path.splitext(file_path)[1][1:]

    def parsed_atoms_bonds_data(self) -> Tuple[Dict, Dict]:
        return self.parser.molecule_data

import os

import numpy as np
import pytest

from manim_chemistry.utils import FileHandler

base_files_path = os.path.join("examples", "molecule_files")

FORMATS = ["mol", "sdf", "asnt", "json", "xml"]


def normalize(data):
    """Makes parsed data comparable with == (numpy arrays -> lists)."""
    if isinstance(data, dict):
        return {key: normalize(value) for key, value in data.items()}
    if isinstance(data, (list, tuple)):
        return [normalize(value) for value in data]
    if isinstance(data, np.ndarray):
        return data.tolist()
    return data


@pytest.mark.parametrize("file_format", FORMATS)
@pytest.mark.parametrize("molecule", ["acetone_2d", "morphine_2d"])
def test_parse_from_string_matches_file(file_format, molecule):
    file_path = os.path.join(
        base_files_path, f"{file_format}_files", f"{molecule}.{file_format}"
    )
    with open(file_path) as file:
        string = file.read()

    from_file = FileHandler(file_path).parsed_atoms_bonds_data()
    from_string = FileHandler.parse_from_string(string=string, format=file_format)

    assert normalize(from_string) == normalize(from_file)

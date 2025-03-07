import os

import numpy as np

from manim_chemistry.utils import ASNTParser
from .asnt_parser_fixtures import BaseTestASNTParser

base_files_path = os.path.join("examples", "element_files")


class TestASNTParser(BaseTestASNTParser):
    def compare_read_molecule_and_known_values(self, read_data, molecule_data):
        # Test atoms data
        atoms_data, bonds_data = read_data
        known_atoms_data, known_bonds_data = molecule_data

        assert isinstance(atoms_data, dict)
        assert known_atoms_data.keys() == atoms_data.keys()
        for atom_index, atom_data in atoms_data.items():
            assert atom_index in known_atoms_data

            assert np.array_equal(
                np.round(atom_data["coords"], 4), known_atoms_data[atom_index]["coords"]
            )
            assert atom_data["element"] == known_atoms_data[atom_index]["element"]
            if atom_data.get("bond_to"):
                assert atom_data["bond_to"] == known_atoms_data[atom_index]["bond_to"]

        assert bonds_data == known_bonds_data

    def test_parse_files(
        self,
        acetone_2d_molecule_data,
        acetone_3d_molecule_data,
        morphine_2d_molecule_data,
        morphine_3d_molecule_data,
        heme_3d_molecule_data,
    ):
        # Test parse 2D acetone file
        self.compare_read_molecule_and_known_values(
            ASNTParser(self.acetone_2d).molecule_data, acetone_2d_molecule_data
        )

        # Test parse 3D acetone file
        self.compare_read_molecule_and_known_values(
            ASNTParser(self.acetone_3d).molecule_data,
            acetone_3d_molecule_data,
        )

        # Test parse 2D morphine file
        self.compare_read_molecule_and_known_values(
            ASNTParser(self.morphine_2d).molecule_data,
            morphine_2d_molecule_data,
        )

        # Test parse 3D morphine file
        self.compare_read_molecule_and_known_values(
            ASNTParser(self.morphine_3d).molecule_data,
            morphine_3d_molecule_data,
        )

        # Test parse 3D heme group
        self.compare_read_molecule_and_known_values(
            ASNTParser(self.heme_3d).molecule_data,
            heme_3d_molecule_data,
        )

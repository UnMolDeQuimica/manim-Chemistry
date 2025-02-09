import os

import numpy as np

from manim_chemistry.utils import MolParser
from .mol_parser_fixtures import BaseTestMolParser

base_files_path = os.path.join("examples", "element_files")


class TestMolParser(BaseTestMolParser):

    def compare_read_molecule_and_known_values(
        self, read_data, molecule_data
    ):
        known_atoms_data, known_bonds_data = molecule_data
        # Test atoms data
        atoms_data = read_data.atoms_data
        assert isinstance(atoms_data, dict)
        assert known_atoms_data.keys() == atoms_data.keys()
        for atom_index, atom_data in atoms_data.items():
            assert atom_index in known_atoms_data
            assert np.array_equal(
                atom_data["coords"], known_atoms_data[atom_index]["coords"]
            )
            assert atom_data["element"] == known_atoms_data[atom_index]["element"]
            if atom_data.get("bond_to"):
                assert atom_data["bond_to"] == known_atoms_data[atom_index]["bond_to"]

        assert read_data.bonds_data == known_bonds_data

    def test_read_files(
        self,
        acetone_2d_file_data,
        acetone_3d_file_data,
        morphine_2d_file_data,
        morphine_3d_file_data,
        heme_2d_file_data,
        heme_3d_file_data,
    ):
        # Test read 2D acetone file
        assert acetone_2d_file_data == MolParser.read_file(self.acetone_2d)

        # Test read acetone 3D file
        assert acetone_3d_file_data == MolParser.read_file(self.acetone_3d)

        # Test read 2D morphine file
        assert morphine_2d_file_data == MolParser.read_file(self.morphine_2d)

        # Test read morphine 3D file
        assert morphine_3d_file_data == MolParser.read_file(self.morphine_3d)

        # Test read heme 2d
        assert heme_2d_file_data == MolParser.read_file(self.heme_2d)

        # Test read heme 3d
        assert heme_3d_file_data == MolParser.read_file(self.heme_3d)

    def test_parse_files(
        self,
        acetone_2d_molecule_data,
        acetone_3d_molecule_data,
        morphine_2d_molecule_data,
        morphine_3d_molecule_data,
        heme_2d_molecule_data,
        heme_3d_molecule_data,
    ):
        # Test parse 2D acetone file
        self.compare_read_molecule_and_known_values(
            MolParser(self.acetone_2d), acetone_2d_molecule_data
        )

        # Test parse 3D acetone file
        self.compare_read_molecule_and_known_values(
            MolParser(self.acetone_3d),
            acetone_3d_molecule_data,
        )

        # Test parse 2D morphine file
        self.compare_read_molecule_and_known_values(
            MolParser(self.morphine_2d), morphine_2d_molecule_data,
        )

        # Test parse 3D morphine file
        self.compare_read_molecule_and_known_values(
            MolParser(self.morphine_3d),
            morphine_3d_molecule_data,
        )

        # Test parse 2D Heme group
        self.compare_read_molecule_and_known_values(
            MolParser(self.heme_2d), heme_2d_molecule_data,
        )

        # Test parse 3D heme group
        self.compare_read_molecule_and_known_values(
            MolParser(self.heme_3d),
            heme_3d_molecule_data,
        )

from manim import config
import pytest

from manim_chemistry.threeD import ThreeDMolecule

from ..base_test_molecule import BaseTestMolecule


class TestThreeDMolecule(BaseTestMolecule):
    molecule_class = ThreeDMolecule

    @pytest.mark.parametrize("file", BaseTestMolecule.files)
    def test_molecule_from_file(self, file):
        config.renderer = "opengl"
        molecule = self.molecule_class.molecule_from_file(file)
        assert isinstance(molecule, self.molecule_class)
        config.renderer = "cairo"

    def test_from_pubchem_api_cid(self):
        config.renderer = "opengl"
        molecule = self.molecule_class.molecule_from_pubchem(cid="2244")
        assert isinstance(molecule, self.molecule_class)
        config.renderer = "cairo"

    def test_from_pubchem_api_name(self):
        config.renderer = "opengl"
        molecule = self.molecule_class.molecule_from_pubchem(name="aspirin")
        assert isinstance(molecule, self.molecule_class)
        config.renderer = "cairo"

    def test_from_pubchem_api_smiles(self):
        config.renderer = "opengl"
        molecule = self.molecule_class.molecule_from_pubchem(
            smiles="CC(=O)OC1=CC=CC=C1C(=O)O"
        )
        assert isinstance(molecule, self.molecule_class)
        config.renderer = "cairo"

    def test_from_pubchem_api_inchi(self):
        config.renderer = "opengl"
        molecule = self.molecule_class.molecule_from_pubchem(
            inchi="BSYNRYMUTXBXSQ-UHFFFAOYSA-N"
        )
        assert isinstance(molecule, self.molecule_class)
        config.renderer = "cairo"

    def test_from_pubchem_api_cid_three_d(self):
        config.renderer = "opengl"
        molecule = self.molecule_class.molecule_from_pubchem(cid="2244", three_d=True)
        assert isinstance(molecule, self.molecule_class)
        config.renderer = "cairo"

    def test_from_pubchem_api_name_three_d(self):
        config.renderer = "opengl"
        molecule = self.molecule_class.molecule_from_pubchem(
            name="aspirin", three_d=True
        )
        assert isinstance(molecule, self.molecule_class)
        config.renderer = "cairo"

    def test_from_pubchem_api_smiles_three_d(self):
        config.renderer = "opengl"
        molecule = self.molecule_class.molecule_from_pubchem(
            smiles="CC(=O)OC1=CC=CC=C1C(=O)O", three_d=True
        )
        assert isinstance(molecule, self.molecule_class)
        config.renderer = "cairo"

    def test_from_pubchem_api_inchi_three_d(self):
        config.renderer = "opengl"
        molecule = self.molecule_class.molecule_from_pubchem(
            inchi="BSYNRYMUTXBXSQ-UHFFFAOYSA-N", three_d=True
        )
        assert isinstance(molecule, self.molecule_class)
        config.renderer = "cairo"

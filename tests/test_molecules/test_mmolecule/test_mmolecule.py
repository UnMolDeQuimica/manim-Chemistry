import pytest

from manim import config
from manim_chemistry.twoD import MMoleculeObject

from ..base_test_molecule import BaseTestMolecule

config.renderer = "cairo"


class TestMMolecule(BaseTestMolecule):
    morphine_file_path = "examples/molecule_files/mol_files/morphine_2d.mol"
    molecule_class = MMoleculeObject

    @pytest.mark.parametrize("file", BaseTestMolecule.files)
    def test_molecule_from_file(self, file):
        molecule = self.molecule_class.molecule_from_file(file)
        assert isinstance(molecule, self.molecule_class)

    def test_from_pubchem_api_cid(self):
        molecule = self.molecule_class.molecule_from_pubchem(cid="2244")
        assert isinstance(molecule, self.molecule_class)

    def test_from_pubchem_api_name(self):
        molecule = self.molecule_class.molecule_from_pubchem(name="aspirin")
        assert isinstance(molecule, self.molecule_class)

    def test_from_pubchem_api_smiles(self):
        molecule = self.molecule_class.molecule_from_pubchem(
            smiles="CC(=O)OC1=CC=CC=C1C(=O)O"
        )
        assert isinstance(molecule, self.molecule_class)

    def test_from_pubchem_api_inchi(self):
        molecule = self.molecule_class.molecule_from_pubchem(
            inchi="BSYNRYMUTXBXSQ-UHFFFAOYSA-N"
        )
        assert isinstance(molecule, self.molecule_class)

    def test_from_pubchem_api_cid_three_d(self):
        molecule = self.molecule_class.molecule_from_pubchem(cid="2244", three_d=True)
        assert isinstance(molecule, self.molecule_class)

    def test_from_pubchem_api_name_three_d(self):
        molecule = self.molecule_class.molecule_from_pubchem(
            name="aspirin", three_d=True
        )
        assert isinstance(molecule, self.molecule_class)

    def test_from_pubchem_api_smiles_three_d(self):
        molecule = self.molecule_class.molecule_from_pubchem(
            smiles="CC(=O)OC1=CC=CC=C1C(=O)O", three_d=True
        )
        assert isinstance(molecule, self.molecule_class)

    def test_from_pubchem_api_inchi_three_d(self):
        molecule = self.molecule_class.molecule_from_pubchem(
            inchi="BSYNRYMUTXBXSQ-UHFFFAOYSA-N", three_d=True
        )
        assert isinstance(molecule, self.molecule_class)

    def test_add_name_to_molecule(self):
        molecule = self.molecule_class.molecule_from_file(self.morphine_file_path)
        molecule.add_molecule_name("morphine")

        assert isinstance(molecule, self.molecule_class)

from manim import config
import numpy as np
import pytest

from manim_chemistry.molecule import Molecule
from manim_chemistry.twoD import GraphMolecule, MMoleculeObject
from manim_chemistry.threeD import ThreeDMolecule
from manim_chemistry.manim_chemistry_molecule import (
    MCAtom,
    MCBond,
    MCElement,
    MCMolecule,
)

from ..base_test_molecule import BaseTestMolecule


config.renderer = "cairo"


class TestMoleculeWithGraphMolecule(BaseTestMolecule):
    morphine_file_path = "examples/molecule_files/mol_files/morphine_2d.mol"
    molecule_class = Molecule(molecule_class=GraphMolecule)

    @pytest.fixture
    def mol_mc_molecule(self):
        return MCMolecule.construct_from_file(self.morphine_file_path)

    def test_mc_molecule_to_atoms_and_bonds(self, mol_mc_molecule):
        vertices, edges = Molecule().mc_molecule_to_atoms_and_bonds(mol_mc_molecule)

        assert isinstance(vertices, dict)
        assert isinstance(edges, dict)

        for index, atom in vertices.items():
            assert isinstance(index, int)
            assert isinstance(atom, MCAtom)
            assert isinstance(atom.element, MCElement)
            assert isinstance(atom.coords, np.ndarray)

        for index, bond in edges.items():
            assert isinstance(index, tuple)
            assert len(index) == 2
            assert isinstance(index[0], int)
            assert isinstance(index[1], int)
            assert isinstance(bond, MCBond)
            assert isinstance(bond.to_atom, MCAtom)
            assert isinstance(bond.from_atom, MCAtom)

    @pytest.mark.parametrize("file", BaseTestMolecule.files)
    def test_molecule_from_file(self, file):
        molecule = self.molecule_class.molecule_from_file(file)
        assert isinstance(molecule, GraphMolecule)

    def test_from_pubchem_api_cid(self):
        molecule = self.molecule_class.molecule_from_pubchem(cid="2244")
        assert isinstance(molecule, GraphMolecule)

    def test_from_pubchem_api_name(self):
        molecule = self.molecule_class.molecule_from_pubchem(name="aspirin")
        assert isinstance(molecule, GraphMolecule)

    def test_from_pubchem_api_smiles(self):
        molecule = self.molecule_class.molecule_from_pubchem(
            smiles="CC(=O)OC1=CC=CC=C1C(=O)O"
        )
        assert isinstance(molecule, GraphMolecule)

    def test_from_pubchem_api_inchi(self):
        molecule = self.molecule_class.molecule_from_pubchem(
            inchi="BSYNRYMUTXBXSQ-UHFFFAOYSA-N"
        )
        assert isinstance(molecule, GraphMolecule)

    def test_from_pubchem_api_cid_three_d(self):
        molecule = self.molecule_class.molecule_from_pubchem(cid="2244", three_d=True)
        assert isinstance(molecule, GraphMolecule)

    def test_from_pubchem_api_name_three_d(self):
        molecule = self.molecule_class.molecule_from_pubchem(
            name="aspirin", three_d=True
        )
        assert isinstance(molecule, GraphMolecule)

    def test_from_pubchem_api_smiles_three_d(self):
        molecule = self.molecule_class.molecule_from_pubchem(
            smiles="CC(=O)OC1=CC=CC=C1C(=O)O", three_d=True
        )
        assert isinstance(molecule, GraphMolecule)

    def test_from_pubchem_api_inchi_three_d(self):
        molecule = self.molecule_class.molecule_from_pubchem(
            inchi="BSYNRYMUTXBXSQ-UHFFFAOYSA-N", three_d=True
        )
        assert isinstance(molecule, GraphMolecule)


class TestMoleculeWithMMoleculeObject(BaseTestMolecule):
    morphine_file_path = "examples/molecule_files/mol_files/morphine_2d.mol"
    molecule_class = Molecule(molecule_class=MMoleculeObject)

    @pytest.mark.parametrize("file", BaseTestMolecule.files)
    def test_molecule_from_file(self, file):
        molecule = self.molecule_class.molecule_from_file(file)
        assert isinstance(molecule, MMoleculeObject)

    def test_from_pubchem_api_cid(self):
        molecule = self.molecule_class.molecule_from_pubchem(cid="2244")
        assert isinstance(molecule, MMoleculeObject)

    def test_from_pubchem_api_name(self):
        molecule = self.molecule_class.molecule_from_pubchem(name="aspirin")
        assert isinstance(molecule, MMoleculeObject)

    def test_from_pubchem_api_smiles(self):
        molecule = self.molecule_class.molecule_from_pubchem(
            smiles="CC(=O)OC1=CC=CC=C1C(=O)O"
        )
        assert isinstance(molecule, MMoleculeObject)

    def test_from_pubchem_api_inchi(self):
        molecule = self.molecule_class.molecule_from_pubchem(
            inchi="BSYNRYMUTXBXSQ-UHFFFAOYSA-N"
        )
        assert isinstance(molecule, MMoleculeObject)

    def test_from_pubchem_api_cid_three_d(self):
        molecule = self.molecule_class.molecule_from_pubchem(cid="2244", three_d=True)
        assert isinstance(molecule, MMoleculeObject)

    def test_from_pubchem_api_name_three_d(self):
        molecule = self.molecule_class.molecule_from_pubchem(
            name="aspirin", three_d=True
        )
        assert isinstance(molecule, MMoleculeObject)

    def test_from_pubchem_api_smiles_three_d(self):
        molecule = self.molecule_class.molecule_from_pubchem(
            smiles="CC(=O)OC1=CC=CC=C1C(=O)O", three_d=True
        )
        assert isinstance(molecule, MMoleculeObject)

    def test_from_pubchem_api_inchi_three_d(self):
        molecule = self.molecule_class.molecule_from_pubchem(
            inchi="BSYNRYMUTXBXSQ-UHFFFAOYSA-N", three_d=True
        )
        assert isinstance(molecule, MMoleculeObject)


class TestMoleculeWithThreeDMolecule(BaseTestMolecule):
    morphine_file_path = "examples/molecule_files/mol_files/morphine_2d.mol"
    molecule_class = Molecule(molecule_class=ThreeDMolecule)

    @pytest.mark.parametrize("file", BaseTestMolecule.files)
    def test_molecule_from_file(self, file):
        config.renderer = "opengl"
        molecule = self.molecule_class.molecule_from_file(file)
        assert isinstance(molecule, ThreeDMolecule)
        config.renderer = "cairo"

    def test_from_pubchem_api_cid(self):
        config.renderer = "opengl"
        molecule = self.molecule_class.molecule_from_pubchem(cid="2244")
        assert isinstance(molecule, ThreeDMolecule)
        config.renderer = "cairo"

    def test_from_pubchem_api_name(self):
        config.renderer = "opengl"
        molecule = self.molecule_class.molecule_from_pubchem(name="aspirin")
        assert isinstance(molecule, ThreeDMolecule)
        config.renderer = "cairo"

    def test_from_pubchem_api_smiles(self):
        config.renderer = "opengl"
        molecule = self.molecule_class.molecule_from_pubchem(
            smiles="CC(=O)OC1=CC=CC=C1C(=O)O"
        )
        assert isinstance(molecule, ThreeDMolecule)
        config.renderer = "cairo"

    def test_from_pubchem_api_inchi(self):
        config.renderer = "opengl"
        molecule = self.molecule_class.molecule_from_pubchem(
            inchi="BSYNRYMUTXBXSQ-UHFFFAOYSA-N"
        )
        assert isinstance(molecule, ThreeDMolecule)
        config.renderer = "cairo"

    def test_from_pubchem_api_cid_three_d(self):
        config.renderer = "opengl"
        molecule = self.molecule_class.molecule_from_pubchem(cid="2244", three_d=True)
        assert isinstance(molecule, ThreeDMolecule)
        config.renderer = "cairo"

    def test_from_pubchem_api_name_three_d(self):
        config.renderer = "opengl"
        molecule = self.molecule_class.molecule_from_pubchem(
            name="aspirin", three_d=True
        )
        assert isinstance(molecule, ThreeDMolecule)
        config.renderer = "cairo"

    def test_from_pubchem_api_smiles_three_d(self):
        config.renderer = "opengl"
        molecule = self.molecule_class.molecule_from_pubchem(
            smiles="CC(=O)OC1=CC=CC=C1C(=O)O", three_d=True
        )
        assert isinstance(molecule, ThreeDMolecule)
        config.renderer = "cairo"

    def test_from_pubchem_api_inchi_three_d(self):
        config.renderer = "opengl"
        molecule = self.molecule_class.molecule_from_pubchem(
            inchi="BSYNRYMUTXBXSQ-UHFFFAOYSA-N", three_d=True
        )
        assert isinstance(molecule, ThreeDMolecule)
        config.renderer = "cairo"

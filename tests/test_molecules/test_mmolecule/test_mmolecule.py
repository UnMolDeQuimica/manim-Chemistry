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

    # First bond is O-H, so bond_type used to be read before assignment.
    water_mol = "\n".join(
        [
            "water",
            "  manual",
            "",
            "  3  2  0  0  0  0  0  0  0  0999 V2000",
            "    0.0000    0.0000    0.0000 O   0  0  0  0  0  0  0  0  0  0  0  0",
            "   -0.7600   -0.5900    0.0000 H   0  0  0  0  0  0  0  0  0  0  0  0",
            "    0.7600   -0.5900    0.0000 H   0  0  0  0  0  0  0  0  0  0  0  0",
            "  1  2  1  0",
            "  1  3  1  0",
            "M  END",
        ]
    )

    # C=O comes first, so the C-H bonds used to inherit bond type 2.
    formaldehyde_mol = "\n".join(
        [
            "formaldehyde",
            "  manual",
            "",
            "  4  3  0  0  0  0  0  0  0  0999 V2000",
            "    0.0000    0.6000    0.0000 O   0  0  0  0  0  0  0  0  0  0  0  0",
            "    0.0000   -0.6000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0",
            "   -0.9400   -1.1400    0.0000 H   0  0  0  0  0  0  0  0  0  0  0  0",
            "    0.9400   -1.1400    0.0000 H   0  0  0  0  0  0  0  0  0  0  0  0",
            "  1  2  2  0",
            "  2  3  1  0",
            "  2  4  1  0",
            "M  END",
        ]
    )

    def test_molecule_from_mol_string(self):
        molecule = self.molecule_class.molecule_from_string(
            self.water_mol, format="mol", ignore_hydrogens=False
        )
        assert isinstance(molecule, self.molecule_class)

    def test_explicit_hydrogens_when_first_bond_has_hydrogen(self):
        molecule = self.molecule_class.molecule_from_string(
            self.water_mol,
            format="mol",
            ignore_hydrogens=False,
            explicit_hydrogens=True,
        )
        assert len(molecule.bonds) == 2
        assert all(bond.type == 1 for bond in molecule.bonds)

    def test_explicit_hydrogens_keep_their_own_bond_type(self):
        molecule = self.molecule_class.molecule_from_string(
            self.formaldehyde_mol,
            format="mol",
            ignore_hydrogens=False,
            explicit_hydrogens=True,
        )
        bond_types = sorted(bond.type for bond in molecule.bonds)
        assert bond_types == [1, 1, 2]

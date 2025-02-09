import pytest
import os

from manim_chemistry.manim_chemistry_molecule import MCMolecule

base_files_path = os.path.join("examples", "molecule_files")
files_names = [
    "acetone_2d",
    "acetone_3d",
    "morphine_2d",
    "morphine_3d",
    "heme_2d",
    "heme_3d",
]
mol_files = [
    f"{os.path.join(base_files_path, 'mol_files', file)}.mol" for file in files_names
]
sdf_files = [
    f"{os.path.join(base_files_path, 'sdf_files', file)}.sdf" for file in files_names
]
json_files = [
    f"{os.path.join(base_files_path, 'json_files', file)}.json" for file in files_names
]
asnt_files = [
    f"{os.path.join(base_files_path, 'asnt_files', file)}.asnt"
    for file in files_names
    if file != "heme_2d"
]
xml_files = [
    f"{os.path.join(base_files_path, 'xml_files', file)}.xml" for file in files_names
]

files = []
files.extend(mol_files)
files.extend(sdf_files)
files.extend(json_files)
files.extend(asnt_files)
files.extend(xml_files)


class TestMCMolecule:
    @pytest.mark.parametrize("file", files)
    def test_construct_from_file(self, file):
        assert isinstance(MCMolecule.construct_from_file(file), MCMolecule)

    @pytest.mark.parametrize("file", files)
    def test_construct_from_file_removing_hydrogens(self, file):
        with_hydrogens = MCMolecule.construct_from_file(file, ignore_hydrogens=False)
        without_carbon_hydrogens = MCMolecule.construct_from_file(file)
        without_hydrogens = MCMolecule.construct_from_file(
            file, ignore_all_hydrogens=True
        )

        assert (
            len(with_hydrogens.atoms)
            >= len(without_carbon_hydrogens.atoms)
            >= len(without_hydrogens.atoms)
        )
        assert (
            len(with_hydrogens.bonds)
            >= len(without_carbon_hydrogens.bonds)
            >= len(without_hydrogens.bonds)
        )

    @pytest.mark.parametrize("file", files)
    def test_reindex_molecule_atoms(self, file):
        molecule_a = MCMolecule.construct_from_file(file, ignore_hydrogens=False)
        molecule_b = MCMolecule.construct_from_file(file, ignore_hydrogens=False)
        molecule_b_atom = molecule_b.atoms.pop(0)
        bonds_to_be_removed = []
        for index, bond in enumerate(molecule_b.bonds, start=1):
            if (
                bond.from_atom.molecule_index == molecule_b_atom.molecule_index
                or bond.to_atom.molecule_index == molecule_b_atom.molecule_index
            ):
                bonds_to_be_removed.append(index)

        bonds_to_be_removed.reverse()
        for bond in bonds_to_be_removed:
            molecule_b.bonds.pop(bond)

        molecule_b.reindex_molecule_atoms()

        assert len(molecule_a.atoms) > len(molecule_b.atoms)
        assert len(molecule_a.bonds) >= len(molecule_b.bonds)
        assert molecule_a.atoms_by_index != molecule_b.atoms_by_index

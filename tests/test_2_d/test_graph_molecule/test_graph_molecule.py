import numpy as np
import pytest

from manim_chemistry.twoD import GraphMolecule
from manim_chemistry.manim_chemistry_molecule import (
    MCAtom,
    MCBond,
    MCElement,
    MCMolecule,
)


class TestGraphMolecule:
    morphine_file_path = "examples/element_files/morphine.mol"

    @pytest.fixture
    def mol_mc_molecule(self):
        return MCMolecule.construct_from_file(self.morphine_file_path)

    def test_mc_molecule_to_graph(self, mol_mc_molecule):
        vertices, edges = GraphMolecule.mc_molecule_to_graph(mol_mc_molecule)

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

    def test_molecule_from_file(self):
        graph_molecule = GraphMolecule.molecule_from_file(
            filepath=self.morphine_file_path
        )

        assert isinstance(graph_molecule, GraphMolecule)

import pytest
from manim_chemistry import *
import numpy as np


@pytest.fixture
def dmp_atoms():
    return mol_parser("examples/element_files/dimethylpropane.mol")[0]


@pytest.fixture
def dmp_bonds():
    return mol_parser("examples/element_files/dimethylpropane.mol")[1]


@pytest.fixture
def atoms_dict():
    atoms_dict = {
        1: {
            "coords": np.array([0.0, 0.0, 0.0]),
            "element": "C",
            "bond_to": {2: "C", 3: "C", 4: "C", 5: "C"},
        },
        2: {
            "coords": np.array([-1.3467, 0.3727, 0.6364]),
            "element": "C",
            "bond_to": {1: "C", 6: "H", 7: "H", 8: "H"},
        },
        3: {
            "coords": np.array([0.8961, 1.2449, -0.0677]),
            "element": "C",
            "bond_to": {1: "C", 9: "H", 10: "H", 11: "H"},
        },
        4: {
            "coords": np.array([-0.2359, -0.5385, -1.4183]),
            "element": "C",
            "bond_to": {1: "C", 12: "H", 13: "H", 14: "H"},
        },
        5: {
            "coords": np.array([0.6864, -1.0791, 0.8496]),
            "element": "C",
            "bond_to": {1: "C", 15: "H", 16: "H", 17: "H"},
        },
        6: {
            "coords": np.array([-1.2106, 0.7613, 1.652]),
            "element": "H",
            "bond_to": {2: "C"},
        },
        7: {
            "coords": np.array([-1.8616, 1.1428, 0.051]),
            "element": "H",
            "bond_to": {2: "C"},
        },
        8: {
            "coords": np.array([-2.0095, -0.4977, 0.6985]),
            "element": "H",
            "bond_to": {2: "C"},
        },
        9: {
            "coords": np.array([1.8669, 1.01, -0.5184]),
            "element": "H",
            "bond_to": {3: "C"},
        },
        10: {
            "coords": np.array([1.0828, 1.6532, 0.9319]),
            "element": "H",
            "bond_to": {3: "C"},
        },
        11: {
            "coords": np.array([0.4318, 2.0348, -0.6688]),
            "element": "H",
            "bond_to": {3: "C"},
        },
        12: {
            "coords": np.array([-0.8737, -1.4294, -1.4026]),
            "element": "H",
            "bond_to": {4: "C"},
        },
        13: {
            "coords": np.array([-0.7257, 0.2109, -2.0501]),
            "element": "H",
            "bond_to": {4: "C"},
        },
        14: {
            "coords": np.array([0.7093, -0.8138, -1.8996]),
            "element": "H",
            "bond_to": {4: "C"},
        },
        15: {
            "coords": np.array([0.8684, -0.7234, 1.8699]),
            "element": "H",
            "bond_to": {5: "C"},
        },
        16: {
            "coords": np.array([1.6524, -1.3666, 0.4196]),
            "element": "H",
            "bond_to": {5: "C"},
        },
        17: {
            "coords": np.array([0.0693, -1.9822, 0.9165]),
            "element": "H",
            "bond_to": {5: "C"},
        },
    }

    return atoms_dict


@pytest.fixture
def bonds_dict():
    bonds_dict = {
        1: [
            {
                "to": 2,
                "type": "1",
                "stereo": 0,
                "topology": 0,
                "reacting_center_status": 0,
            },
            {
                "to": 3,
                "type": "1",
                "stereo": 0,
                "topology": 0,
                "reacting_center_status": 0,
            },
            {
                "to": 4,
                "type": "1",
                "stereo": 0,
                "topology": 0,
                "reacting_center_status": 0,
            },
            {
                "to": 5,
                "type": "1",
                "stereo": 0,
                "topology": 0,
                "reacting_center_status": 0,
            },
        ],
        2: [
            {
                "to": 6,
                "type": "1",
                "stereo": 0,
                "topology": 0,
                "reacting_center_status": 0,
            },
            {
                "to": 7,
                "type": "1",
                "stereo": 0,
                "topology": 0,
                "reacting_center_status": 0,
            },
            {
                "to": 8,
                "type": "1",
                "stereo": 0,
                "topology": 0,
                "reacting_center_status": 0,
            },
        ],
        3: [
            {
                "to": 9,
                "type": "1",
                "stereo": 0,
                "topology": 0,
                "reacting_center_status": 0,
            },
            {
                "to": 10,
                "type": "1",
                "stereo": 0,
                "topology": 0,
                "reacting_center_status": 0,
            },
            {
                "to": 11,
                "type": "1",
                "stereo": 0,
                "topology": 0,
                "reacting_center_status": 0,
            },
        ],
        4: [
            {
                "to": 12,
                "type": "1",
                "stereo": 0,
                "topology": 0,
                "reacting_center_status": 0,
            },
            {
                "to": 13,
                "type": "1",
                "stereo": 0,
                "topology": 0,
                "reacting_center_status": 0,
            },
            {
                "to": 14,
                "type": "1",
                "stereo": 0,
                "topology": 0,
                "reacting_center_status": 0,
            },
        ],
        5: [
            {
                "to": 15,
                "type": "1",
                "stereo": 0,
                "topology": 0,
                "reacting_center_status": 0,
            },
            {
                "to": 16,
                "type": "1",
                "stereo": 0,
                "topology": 0,
                "reacting_center_status": 0,
            },
            {
                "to": 17,
                "type": "1",
                "stereo": 0,
                "topology": 0,
                "reacting_center_status": 0,
            },
        ],
    }

    return bonds_dict


def test_atoms_dict(dmp_atoms, atoms_dict):
    np.testing.assert_equal(dmp_atoms, atoms_dict)


def test_bonds_dict(dmp_bonds, bonds_dict):
    np.testing.assert_equal(dmp_bonds, bonds_dict)

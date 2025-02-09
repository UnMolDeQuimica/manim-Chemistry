# Getting Atoms and Bond Positions
Sometimes it is useful to get the atoms and bonds positions. You can do this for `MMoleculeObjects`, `NamedMolecule` and `GraphMolecule` objects:


## Get atoms positions
You can get a single atom position by indicating the index:

```python
molecule = MMoleculeObject.molecule_from_file("examples/molecule_files/mol_files/dimethylpropane.mol")
print(molecule.find_atom_position_by_index(1))
>>> array([ 0.2253 -0.0829  0.    ])
```

Similarly, you can get the position for a list of atoms:
```python
print(molecule.find_atoms_position_by_index([1,2,3]))
>>> [array([ 0.2253, -0.0829,  0.    ]), array([-1.1214,  0.2898,  0.    ]), array([1.1214, 1.162 , 0.    ])]
```

Finally, you can get all the position for all atoms:

```python
molecule = MMoleculeObject.molecule_from_file("examples/molecule_files/mol_files/dimethylpropane.mol", ignore_hydrogens=False)
print(molecule.find_all_atoms_positions())
>>> {1: array([ 0.0713, -0.0263,  0.    ]), 2: array([-1.2754,  0.3464,  0.    ]), 3: array([0.9674, 1.2186, 0.    ]), 4: array([-0.1646, -0.5648,  0.    ]), 5: array([ 0.7577, -1.1054,  0.    ]), 6: array([-1.1393,  0.735 ,  0.    ]), 7: array([-1.7903,  1.1165,  0.    ]), 8: array([-1.9382, -0.524 ,  0.    ]), 9: array([1.9382, 0.9837, 0.    ]), 10: array([1.1541, 1.6269, 0.    ]), 11: array([0.5031, 2.0085, 0.    ]), 12: array([-0.8024, -1.4557,  0.    ]), 13: array([-0.6544,  0.1846,  0.    ]), 14: array([ 0.7806, -0.8401,  0.    ]), 15: array([ 0.9397, -0.7497,  0.    ]), 16: array([ 1.7237, -1.3929,  0.    ]), 17: array([ 0.1406, -2.0085,  0.    ])}
```


## Get bonds positions

You can get the bonds positions using similar functions:

```python
molecule = GraphMolecule.molecule_from_file("examples/molecule_files/mol_files/dimethylpropane.mol", ignore_hydrogens=False)
print(molecule.find_bond_center_by_index((2, 1)))
print(molecule.find_bonds_center_by_index([(2, 1), (3, 1), (4, 1)]))
print(molecule.find_all_bonds_centers())
>>> [-0.60205  0.16005  0.4083 ]
>>> [array([-0.60205,  0.16005,  0.4083 ]), array([0.51935, 0.59615, 0.05625]), array([-0.04665, -0.29555, -0.61905])]
>>> {(2, 1): array([-0.60205,  0.16005,  0.4083 ]), (3, 1): array([0.51935, 0.59615, 0.05625]), (4, 1): array([-0.04665, -0.29555, -0.61905]), (5, 1): array([ 0.4145 , -0.56585,  0.5149 ]), (6, 2): array([-1.20735,  0.5407 ,  1.2343 ]), (7, 2): array([-1.53285,  0.73145,  0.4338 ]), (8, 2): array([-1.6068 , -0.0888 ,  0.75755]), (9, 3): array([ 1.4528 ,  1.10115, -0.20295]), (10, 3): array([1.06075, 1.42275, 0.5222 ]), (11, 3): array([ 0.73525,  1.61355, -0.27815]), (12, 4): array([-0.4835 , -1.01025, -1.32035]), (13, 4): array([-0.4095, -0.1901, -1.6441]), (14, 4): array([ 0.308  , -0.70245, -1.56885]), (15, 5): array([ 0.8487 , -0.92755,  1.44985]), (16, 5): array([ 1.2407 , -1.24915,  0.7247 ]), (17, 5): array([ 0.44915, -1.55695,  0.97315])}
```

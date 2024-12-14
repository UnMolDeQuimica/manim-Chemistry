# Getting Atoms and Bond Positions
Sometimes it is useful to get the atoms and bonds positions. You can do this for `MMoleculeObjects`, `NamedMolecule` and `GraphMolecule` objects:

## MMoleculeObjects

### Get atoms positions
You can get a single atom position by indicating the index:

```python
molecule = MMoleculeObject.from_mol_file("examples/element_files/dimethylpropane.mol")
print(molecule.find_atom_position_by_index(1))
>>> array([ 0.9397, -0.7497,  0.    ])
```

Similarly, you can get the position for a list of atoms:
```python
print(molecule.find_atoms_position_by_index([1,2,3]))
>>> [array([ 0.0713, -0.0263,  0.    ]), array([-1.2754,  0.3464,  0.    ]), array([0.9674, 1.2186, 0.    ])]
```

Finally, you can get all the position for all atoms:

```python
print(molecule.find_atoms_position_by_index([1,2,3]))
>>> {1: array([ 0.0713, -0.0263,  0.0901]), 2: array([-1.2754,  0.3464,  0.7265]), 3: array([0.9674, 1.2186, 0.0224]), 4: array([-0.1646, -0.5648, -1.3282]), 5: array([ 0.7577, -1.1054,  0.9397]), 6: array([-1.1393,  0.735 ,  1.7421]), 7: array([-1.7903,  1.1165,  0.1411]), 8: array([-1.9382, -0.524 ,  0.7886]), 9: array([ 1.9382,  0.9837, -0.4283]), 10: array([1.1541, 1.6269, 1.022 ]), 11: array([ 0.5031,  2.0085, -0.5787]), 12: array([-0.8024, -1.4557, -1.3125]), 13: array([-0.6544,  0.1846, -1.96  ]), 14: array([ 0.7806, -0.8401, -1.8095]), 15: array([ 0.9397, -0.7497,  1.96  ]), 16: array([ 1.7237, -1.3929,  0.5097]), 17: array([ 0.1406, -2.0085,  1.0066])}
```


### Get bonds positions

You can get the bonds positions using similar functions:

```python
molecule = MMoleculeObject.from_mol_file("examples/element_files/dimethylpropane.mol")
        print(molecule.find_bond_center_by_index(0))
        print(molecule.find_bonds_center_by_index([0,1,2]))
        print(molecule.find_all_bonds_centers())
>>> [-0.60205  0.16005  0.     ]
>>> [array([-0.60205,  0.16005,  0.     ]), array([0.51935, 0.59615, 0.     ]), array([-0.04665, -0.29555,  0.     ])]
>>> {0: array([-0.60205,  0.16005,  0.     ]), 1: array([0.51935, 0.59615, 0.     ]), 2: array([-0.04665, -0.29555,  0.     ]), 3: array([ 0.4145 , -0.56585,  0.     ])}
```

## NamedMolecules

The functions are the same as before.


## GraphMolecules

The functions used are similar to the previous ones but they change in the bonds part. As we are using now a tuple to define the vertices of the structure `(<from-atom>, <to-atom>)`, we use the functions `find_bond_center_by_tuple` and `find_bonds_center_by_tuple`


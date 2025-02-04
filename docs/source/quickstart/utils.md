# Utils

## Load mol data from a string

```python
from manim_chemistry import *

class LoadMolDataFromAString(Scene):
    def construct(self):
        mol_data = "..."
        atoms, bonds = mol_parser_string(mol_data)
        molecule = MMolecule(atoms, bonds)
        self.add(molecule)
```

or alternatively:

```python
from manim_chemistry import *

class LoadMolDataFromAString(Scene):
    def construct(self):
        mol_data = "..."
        molecule = MMolecule.from_mol_string(mol_data)
        self.add(molecule)
```

## Load mol data from a file

```python
from manim_chemistry import *

class LoadMolDataFromFile(Scene):
    def construct(self):
        atoms, bonds = mol_parser("path/to/your/file.mol")
        molecule = MMolecule(atoms, bonds)
        self.add(molecule)
```

or alternatively

```python
from manim_chemistry import *

class LoadMolDataFromFile(Scene):
    def construct(self):
        molecule = MMolecule.molecule_from_file("path/to/your/file.mol")
        self.add(molecule)
```

## Load sdf data from a string

```python
from manim_chemistry import *

class LoadSdfDataFromAString(Scene):
    def construct(self):
        sdf_data = "..."
        molecules = sdf_parser_string(sdf_data)
        for molecule in molecules:
            atoms, bonds = molecule
            molecule = MMolecule(atoms, bonds)
            self.add(molecule)
```

or alternatively

```python
from manim_chemistry import *

class LoadSdfDataFromAString(Scene):
    def construct(self):
        sdf_data = "..."
        molecules = MMolecule.from_sdf_string(sdf_data)
        for molecule in molecules:
            self.add(molecule)
```

## Load sdf data from a file

```python
from manim_chemistry import *

class LoadSdfDataFromFile(Scene):
    def construct(self):
        molecules = sdf_parser("path/to/your/file.sdf")
        for molecule in molecules:
            atoms, bonds = molecule
            molecule = MMolecule(atoms, bonds)
            self.add(molecule)
```

or alternatively

```python
from manim_chemistry import *

class LoadSdfDataFromFile(Scene):
    def construct(self):
        molecules = MMolecule.molecule_from_file("path/to/your/file.sdf")
        for molecule in molecules:
            self.add(molecule)
```

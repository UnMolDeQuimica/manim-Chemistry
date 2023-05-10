# Table of contents:
- [Installation](#installation)
- [What is manim-Chemistry](#what-is-manim-chemistry)
- [What can manim-Chemistry do right now?](#what-can-manim-chemistry-do-right-now)
- [Create 2D molecules](#create-2d-molecules)
- [Create 3D molecule](#create-3d-molecule)
- [Create a periodic table](#create-a-periodic-table)
- [Making atomic orbitals](#making-atomic-orbitals)
- [Making Bohr diagrams](#making-bohr-diagrams)
- [Reading .mol files](#reading-mol-files)
- [Typical issues with .mol files](#typical-issues-with-mol-files)
- [Take a look to examples](#)
- [Made with manimChemistry](#made-with-manimchemistry)

# Installation.

Right now this can be installed cloning the repo:

```
git clone https://github.com/UnMolDeQuimica/manim-Chemistry.git
cd manim-Chemistry 
python -m pip install .
```

Soon this will be available in pip.

# What is manim-Chemistry?

manim-Chemistry is a manim plugin designed to make chemistry animations easier.

To my knowledge, there is only another plugin related to chemistry called [chanim](https://github.com/kilacoda/chanim) that aims to import to manim the chemfig package (and does an amazing job!).

The philosophy of manim-Chemistry goes into a different direction: manim-Chemistry tries to use the manim tools in combination with [.mol](https://en.wikipedia.org/wiki/Chemical_table_file) files and [.csv](https://en.wikipedia.org/wiki/Comma-separated_values) databases useful basic classes to create beatufil chemistry related animations such as a Periodic Table or 2d and 3d chemical structures.

Also, manim-Chemistry will try to do as much things from scratch as possible. That means I will also avoid using libraries such as [Mendeleev](https://mendeleev.readthedocs.io/en/stable/), [RDKit](https://www.rdkit.org/), [PyMOL](https://pymol.org/2/), [Open Babel](https://openbabel.org/wiki/Main_Page) ammong others. The reason is avoid depending on 3rd party packages that might need intensive maintenance. However, the users can combine the power of those libraries with manim-Chemistry to make life easier.

This project is still a work in progress and there is no date for a final realease yet.

# What can manim-Chemistry do right now?

This will be a summary of the capabilities of manim-Chemistry. As this project is still in progress this might not be up to date. Check the examples to get a better idea of what you can do. You might want to check the TODO file to know what is comming and yet to be done. Feel free to open issues and pull requests to make this even greater!

## Create 2D molecules

To create 2D molecules you simply need a .mol file with atoms and bonds data. Take a look at the morphine.mol file inside examples to know how should it look.

To create a Scene with a 2D molecule you should have a structure like this:

```
from manim import *
from manim_chemistry import *

class TwoDMoleculeScene(Scene):
   def construct(self):
        morphine = MMoleculeObject.from_mol_file("morphine.mol")
        self.add(morphine)
```

You can run manim as usual:

`manim .\examples.py -ps`

The result looks like this:

![plot](/examples/examples_assets/2D_morphine_bad.png)

Doesn't look really good, right? Double bonds are not in the correct position. We can solve this!

You can set to True an option to see the bonds numbering. You can do a similar thing to the atoms. This numbering is given by the .mol file and is NOT related to the chemical strucure.

```
from manim import *
from manim_chemistry import *

class TwoDMoleculeScene(Scene):
   def construct(self):
        morphine = MMoleculeObject.from_mol_file("morphine.mol")
        self.add(morphine)
```

We get

![plot](/examples/examples_assets/2D_morphine_bond_numbering.png)

So we need to rotate bonds 7 and 20. We can add this adding their index to the rotate_bonds list:

```
from manim import *
from manim_chemistry import *

class TwoDMoleculeScene(Scene):
   def construct(self):
        morphine = MMoleculeObject.from_mol_file("morphine.mol", rotate_bonds=[7, 20])
        self.add(morphine)
```

Result:
![plot](/examples/examples_assets/2D_morphine_corrected_bonds.png)

Now we are talking!

## Create 3D molecule:

Creating a 3D molecule requires a bit more effort. We need two things:

1. A .mol file (like before)
2. A csv data file with data for your atoms. You can find an example inside the examples folder called "Elementos.csv". 

The .mol will be parsed and the .csv will tell manim-Chemistry some data, specially the color. Using the same file as before we can create a 3D structure for morphine:

```
from manim import *
from manim_chemistry import *

class Draw3DMorphine(ThreeDScene):
    def construct(self):
        three_d_morphine = ThreeDMolecule.from_mol_file("morphine.mol", "Elementos.csv")
        self.add(three_d_morphine)
        self.wait()
```

To be able to run this you need to run manim using opengl as renderer:

`manim .\examples.py Draw3DMorphine -ps --renderer=opengl`

Here is the result!

![plot](/examples/examples_assets/Draw3DMorphine_ManimCE_v0.17.3.png)

As you can see, the coloring is defined in the "Elementos.csv" file, but you can make your own source file to customize colors!


## Create a periodic table:
Like before, we need a source file to draw everything. Again, feel free to make your own from a copy of "Elementos.csv"

You can create the frame for an element using:

```
from manim import *
from manim_chemistry import *

class DrawCarbonElement(Scene):
    def construct(self):
        carbon = MElementObject.from_csv_file_data(filename="Elementos.csv", atomic_number=6)
        self.add(carbon)
```

And there you have it!

![plot](/examples/examples_assets/DrawCarbonElement_ManimCE_v0.17.3.png)


To make the whole periodic table you need data for every element inside that data source file. Elementos.csv already has it, so you just have to copy it and adapt to your needs. Using the cpk coloring and the following code we get that beautiful periodic table:

```
from manim import *
from manim_chemistry import *

class DrawPeriodicTable(Scene):
    def construct(self):
        self.add(PeriodicTable(data_file="Elementos.csv"))
```

![plot](/examples/examples_assets/DrawPeriodicTable_ManimCE_v0.17.3.png)


## Making atomic orbitals:

Molecular orbitals are very complex and consuming for a simple python script, but we can get atomic orbitals pretty easily just by selecting the l and m level we want to plot:

```
from manim import *
from manim_chemistry import *

class DrawPOrbital(Scene):
    def construct(self):
        orbital = Orbital(l=1, m=-1)
        self.add(orbital)
```

One again you need to use opengl as renderer:

`manim .\examples.py DrawPOrbital -ps --renderer=opengl`

![plot](/examples/examples_assets/orbitals_example.png)

## Making Bohr diagrams:

Bohr diagrams are very outdated, but drawing them might be usefull to communicate certain ideas. Here all you have to do is set the number of protons, electrons and neutrons and you will get a nice diagram:

```
from manim import *
from manim_chemistry import *

class DrawBohrDiagram(Scene):
    def construct(self):
        diagram = BohrAtom(e=14, p=14,, n=10)
        self.add(diagram)
```
Here you have your nice diagram!

![plot](/examples/examples_assets/BohrDiagram_ManimCE_v0.17.3.png)



## Reading .mol files

manim-Chemistry can parse .mol files to create a dictionary with atoms and bond data. Currently, the data we are getting is:

### Atoms dictionary:

- Index: To know the index in the .mol file, which allows us to keep track of bonding.
- Coordinates: Used to give a position to the atom.
- Element: To know which element is it.
- Bond to. Using the index of other atoms, we get to know to which atoms is bond a certain atom.

### Bonds dictionary:

- From atom: The index of the atom starting the bond
- To atom: The index of the atom ending the bond
- Type: Indicates the type of bond. Check[the bond block specifications](https://en.wikipedia.org/wiki/Chemical_table_file#Bond_block_specification) for further info.
- Stereo: Usefull to know if a cram bond is needed and which kind.

### How to use it:

This is used inside both 2d and 3d molecules but can be used independently importing it from the utils submodule.

```
>>> from manim_chemistry.utils import mol_parser
>>> morphine_parsed = mol_parser("morphine.mol")
>>> morphine_parsed
({1: {'coords': array([ 0.   , -0.825,  0.   ]), 'element': 'C', 'bond_to': {7: 'C', 2: 'C', 3: 'C'}}, 2: {'coords': array([-0.7145, -0.4125,  0.    ]), 'element': 'C', 'bond_to': {1: 'C', 12: 'O', 4: 'C'}}, 3: {'coords': array([ 0.7145, -0.4125,  0.    ]), 'element': 'C', 'bond_to': {1: 'C', 14: 'C', 5: 'C'}}, 4: {'coords': array([-0.7145,  0.4125,  0.    ]), 'element': 'C', 'bond_to': {2: 'C', 18: 'O', 6: 'C'}}, 5: {'coords': array([0.7145, 0.4125, 0.    ]), 'element': 'C', 'bond_to': {3: 'C', 6: 'C'}}, 6: {'coords': array([0.   , 0.825, 0.   ]), 'element': 'C', 'bond_to': {4: 'C', 5: 'C'}}, 7: {'coords': array([ 0.003 , -1.6464,  0.    ]), 'element': 'C', 'bond_to': {1: 'C', 8: 'C', 9: 'C', 22: 'C'}}, 8: {'coords': array([ 0.7109, -2.0631,  0.    ]), 'element': 'C', 'bond_to': {7: 'C', 10: 'C', 11: 'C', 20: 'H'}}, 9: {'coords': array([-0.7127, -2.0511,  0.    ]), 'element': 'C', 'bond_to': {7: 'C', 12: 'O', 13: 'C'}}, 10: {'coords': array([ 1.4268, -1.651 ,  0.    ]), 'element': 'C', 'bond_to': {8: 'C', 15: 'N', 14: 'C'}}, 11: {'coords': array([ 0.7067, -2.8808,  0.    ]), 'element': 'C', 'bond_to': {8: 'C', 16: 'C'}}, 12: {'coords': array([-1.5371, -1.1745,  0.    ]), 'element': 'O', 'bond_to': {2: 'C', 9: 'C'}}, 13: {'coords': array([-0.7206, -2.8689,  0.    ]), 'element': 'C', 'bond_to': {9: 'C', 17: 'O', 16: 'C'}}, 14: {'coords': array([ 1.431 , -0.8297,  0.    ]), 'element': 'C', 'bond_to': {3: 'C', 10: 'C'}}, 15: {'coords': array([ 2.1419, -2.0715,  0.    ]), 'element': 
'N', 'bond_to': {10: 'C', 19: 'C', 21: 'C'}}, 16: {'coords': array([-0.0128, -3.2891,  0.    ]), 'element': 'C', 'bond_to': {11: 'C', 13: 'C'}}, 17: {'coords': array([-1.4365, -3.2845,  0.    ]), 'element': 'O', 'bond_to': {13: 'C'}}, 18: {'coords': array([-1.4262,  0.8296,  0.    ]), 'element': 'O', 'bond_to': {4: 'C'}}, 19: {'coords': array([ 2.9416, -1.853 ,  0.    ]), 'element': 'C', 'bond_to': {15: 'N'}}, 20: {'coords': array([ 1.4954, -2.6258,  0.    ]), 'element': 'H', 'bond_to': {8: 'C'}}, 21: {'coords': array([ 2.1397, -1.2341,  0.    ]), 'element': 'C', 'bond_to': {15: 'N', 22: 'C'}}, 22: {'coords': array([ 0.7183, -1.233 ,  0.    ]), 'element': 'C', 'bond_to': {7: 'C', 21: 'C'}}}, {7: [{'to': 1, 'type': '1', 'stereo': 0, 'topology': 0, 'reacting_center_status': 0}, {'to': 8, 'type': '1', 'stereo': 0, 'topology': 0, 'reacting_center_status': 0}, {'to': 9, 'type': '1', 'stereo': 0, 'topology': 0, 'reacting_center_status': 0}, {'to': 22, 'type': '1', 'stereo': 1, 'topology': 0, 'reacting_center_status': 0}], 1: [{'to': 2, 'type': '1', 'stereo': 0, 'topology': 0, 'reacting_center_status': 0}, {'to': 3, 'type': '2', 'stereo': 0, 'topology': 0, 'reacting_center_status': 0}], 2: [{'to': 12, 'type': '1', 'stereo': 0, 'topology': 0, 'reacting_center_status': 0}, {'to': 4, 'type': '2', 'stereo': 0, 'topology': 0, 'reacting_center_status': 0}], 3: [{'to': 14, 'type': '1', 'stereo': 0, 'topology': 0, 'reacting_center_status': 0}, {'to': 5, 'type': '1', 'stereo': 0, 'topology': 0, 
'reacting_center_status': 0}], 4: [{'to': 18, 'type': '1', 'stereo': 0, 'topology': 0, 'reacting_center_status': 0}, {'to': 6, 'type': '1', 'stereo': 0, 'topology': 0, 'reacting_center_status': 0}], 5: [{'to': 6, 'type': '2', 'stereo': 0, 'topology': 0, 'reacting_center_status': 0}], 8: [{'to': 10, 'type': '1', 'stereo': 0, 'topology': 0, 'reacting_center_status': 0}, {'to': 11, 'type': '1', 'stereo': 0, 'topology': 0, 'reacting_center_status': 0}, {'to': 20, 'type': '1', 'stereo': 1, 'topology': 0, 'reacting_center_status': 0}], 9: [{'to': 12, 'type': '1', 
'stereo': 6, 'topology': 0, 'reacting_center_status': 0}, {'to': 13, 'type': '1', 'stereo': 0, 'topology': 0, 'reacting_center_status': 0}], 10: [{'to': 15, 'type': '1', 'stereo': 1, 'topology': 0, 'reacting_center_status': 0}, {'to': 14, 'type': '1', 'stereo': 0, 'topology': 0, 'reacting_center_status': 0}], 11: [{'to': 16, 'type': '2', 'stereo': 0, 'topology': 0, 'reacting_center_status': 0}], 13: [{'to': 17, 'type': '1', 'stereo': 6, 'topology': 0, 'reacting_center_status': 0}, {'to': 16, 'type': '1', 'stereo': 0, 'topology': 0, 'reacting_center_status': 
0}], 15: [{'to': 19, 'type': '1', 'stereo': 0, 'topology': 0, 'reacting_center_status': 0}], 21: [{'to': 15, 'type': '1', 'stereo': 0, 'topology': 0, 'reacting_center_status': 0}], 22: [{'to': 21, 'type': '1', 'stereo': 0, 'topology': 0, 'reacting_center_status': 0}]}
```

# Typical issues with .mol files

Sometimes you are trying to draw a molecule with a lot of atoms and bonds. This results in a file that looks like this:

```
  ACD/LABS04302300463D

216265  0  0  0  0  0  0  0  0  1 V2000
   16.2474   -9.9960    2.4976 P   0  0  0  0  0  0  0  0  0  0  0  0
   17.2414   -9.9960    1.6140 P   0  0  0  0  0  0  0  0  0  0  0  0
   16.2474  -11.2601    0.2434 P   0  0  0  0  0  0  0  0  0  0  0  0
   17.2414  -11.2601    1.1271 P   0  0  0  0  0  0  0  0  0  0  0  0
.
.
.
```

See that 216265? This is a problem. manimChemistry will think this is the number of atoms we have and this is a problem. At this stage of the development we need to manually correct this. In this example, we have 216 atoms and 265 bonds, so we have to separate it:

```
  ACD/LABS04302300463D

216 265  0  0  0  0  0  0  0  0  1 V2000 
   16.2474   -9.9960    2.4976 P   0  0  0  0  0  0  0  0  0  0  0  0
   17.2414   -9.9960    1.6140 P   0  0  0  0  0  0  0  0  0  0  0  0
   16.2474  -11.2601    0.2434 P   0  0  0  0  0  0  0  0  0  0  0  0
   17.2414  -11.2601    1.1271 P   0  0  0  0  0  0  0  0  0  0  0  0
.
.
.
```

Our problems are not solved. Probably some bonds will look like this:

```
213215  1  0  0  0  0
201207  1  0  0  0  0
214202  1  0  0  0  0
214216  1  0  0  0  0

```

This 213215, 201207, 214202, 214216 are, in fact, bonds pointing from atom 213 to 215, 201 to 207, 214 to 202 and 214 to 216. We must solve this manually again:

```
213 215  1  0  0  0  0
201 207  1  0  0  0  0
214 202  1  0  0  0  0
214 216  1  0  0  0  0

```


# Take a look to examples:

Inside this repo there is a folder examples with assets and basic files that might be useful. Make sure to check them!

# Made with manimChemistry

Here you have some examples using manimChemistry. Feel free to contribute with your own animations and videos!

Fullerene:
![plot](/examples/examples_assets/Fullerene.png)

Beta and alpha tin structures:
![plot](/examples/examples_assets/TinPhases.png)

A video using both and more examples:

https://www.youtube.com/watch?v=L7OXe94_WmA


# How to contact
You can open issues and pull requests, but if you want to contact me directly you can go to:
- Email: unmoldequimica@gmail.com
- YouTube: https://www.youtube.com/@unmoldequimica
- Twitter: https://twitter.com/unmoldequimica

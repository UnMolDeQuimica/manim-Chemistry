# Docs
Check the [documentation](https://manim-chemistry.readthedocs.io/en/latest/) for a more in depht explanation!


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
- [How to contact](#how-to-contact)
- [Great contributers](#great-contributers)

# Installation.

You can install via pip:

```
pip install manim_chemistry
```

You can also clone the repo and install it from here:

```
git clone https://github.com/UnMolDeQuimica/manim-Chemistry.git
cd manim-Chemistry
python -m pip install .
```

or

```
git clone https://github.com/UnMolDeQuimica/manim-Chemistry.git
cd manim-Chemistry 
python -m pip install -e .
```

If you already have the package installed and just want to upgrade to the latest version, you can should use this command:

```
python -m pip install --upgrade manim_chemistry
```

# What is manim-Chemistry?

manim-Chemistry is a manim plugin designed to make chemistry animations easier.

To my knowledge, there is only another plugin related to chemistry called [chanim](https://github.com/kilacoda/chanim) that aims to import to manim the chemfig package (and does an amazing job!).

The philosophy of manim-Chemistry goes into a different direction: manim-Chemistry tries to use the manim tools in combination with chemical data files (`.mol`, `.sdf`, `.json`, `.asnt` and `.xlm`) with basic yet useful classes to create beautiful chemistry related animations such as a Periodic Table or 2d and 3d chemical structures.

Also, manim-Chemistry will try to do as much things from scratch as possible. That means I will also avoid using libraries such as [Mendeleev](https://mendeleev.readthedocs.io/en/stable/), [RDKit](https://www.rdkit.org/), [PyMOL](https://pymol.org/2/), [Open Babel](https://openbabel.org/wiki/Main_Page) ammong others. The reason is avoid depending on 3rd party packages that might need intensive maintenance. However, the users can combine the power of those libraries with manim-Chemistry to make life easier. The only third party included is PubChem due to its ease to include molecules directly from their website.

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
        morphine = MMoleculeObject.molecule_from_file("morphine.mol")
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
        morphine = MMoleculeObject.molecule_from_file("morphine.mol", add_bonds_numbering=True)
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
        morphine = MMoleculeObject.molecule_from_file("morphine.mol", rotate_bonds=[7, 20])
        self.add(morphine)
```

Result:
![plot](/examples/examples_assets/2D_morphine_corrected_bonds.png)

Now we are talking!

### Named Molecules:

You may want to add a name to a molecule. It is very simple, but it is handy to do all in the same object. You can create a NamedMolecule similarly to how you create a MMoleculeObject:

```
from manim import *
from manim_chemistry import *

class NamedMoleculeExample(Scene):
    def construct(self):
        named_molecule = NamedMolecule.molecule_from_file(name="Morphine", filename="morphine.mol")
        self.add(diagram)
```
![plot](/examples/examples_assets/NamedMoleculeExample_ManimCE_v0.17.3.png)

You can also provided an already created molecule or an already created text and the NamedMolecule class will group them. This allows greater control for the user.

### GraphMolecule:
Another variant of 2D molecules are the GraphMolecules. Those are based on Manim's Graph class, which gives them a lot of superpowers!

You can use them in a very similar way as you did with MMolecules and NamedMolecules:

```
from manim import *
from manim_chemistry import *

class GraphMoleculeExample(Scene):
    def construct(self):
        graph_molecule = GraphMolecule.molecule_from_file(filepath="morphine.mol")
        self.add(graph_molecule)
```
![plot](/examples/examples_assets/DrawGraphMorphine_ManimCE_v0.17.3.png)

There you go!

You can also add a label by setting `label=True` when building the GraphMolecule:
```
from manim import *
from manim_chemistry import *

class GraphMoleculeExample(Scene):
    def construct(self):
        graph_molecule = GraphMolecule.molecule_from_file(
            mol_file="morphine.mol",
            label=True
        )
        self.add(graph_molecule)
```
![plot](/examples/examples_assets/DrawLabeledGraphMorphine_ManimCE_v0.17.3.png)

Using `label=True` and `numeric_label=True` you will get the molecule drawn with is atoms labeled using the molfile:
```
from manim import *
from manim_chemistry import *

class GraphMoleculeExample(Scene):
    def construct(self):
        graph_molecule = GraphMolecule.molecule_from_file(
            mol_file="morphine.mol",
            label=True,
            numeric_label=True
        )
        self.add(graph_molecule)
```
![plot](/examples/examples_assets/DrawLabeledWithIndexGraphMorphine_ManimCE_v0.17.3.png)

### Partial molecule selection and custom animations in GraphMolecules:
The power of graphs really shows in GraphMolecules. One of the examples of this power is using `networkx` to get parts of the molecules given a starting atom and ending atom. For example, we could color a part of the molecule:


```python
class GraphMoleculeExample(Scene):
    def construct(self):
        molecule = GraphMolecule.molecule_from_file(asset, label=True, numeric_label=True)
        atoms_and_bonds = molecule.get_connected_atoms_and_bonds(1, 3)
        atoms_and_bonds.set_color(GREEN)
        self.add(molecule)
```
![plot](/examples/examples_assets/PartiallyColoredGraphMolecule.png)



It is also possible to perform some custom animations using GMAnimationBuilder: rotate_atoms_about_bond and change_color:

![plot](/examples/examples_assets/CustomGraphMoleculeAnimation.gif)



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
        config.renderer = "opengl"
        three_d_morphine = ThreeDMolecule.molecule_from_file("morphine.mol")
        self.add(three_d_morphine)
        self.wait()
```

To be able to run this you need to run manim using opengl as renderer:

`manim .\examples.py Draw3DMorphine -ps --renderer=opengl`

Here is the result!

![plot](/examples/examples_assets/Draw3DMorphine_ManimCE_v0.17.3.png)


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


# Take a look to examples:

Inside this repo there is a folder examples with assets and basic files that might be useful. Make sure to check them!

# Made with manim_chemistry

Here you have some examples using manim_chemistry. Feel free to contribute with your own animations and videos!

Fullerene:
![plot](/examples/examples_assets/Fullerene.png)

Beta and alpha tin structures:
![plot](/examples/examples_assets/TinPhases.png)

Videos using manimChemistry:

https://www.youtube.com/watch?v=L7OXe94_WmA

https://youtu.be/KgiCl_o_Aws


# How to contact
You can open issues and pull requests, but if you want to contact me directly you can go to:
- Email: unmoldequimica@gmail.com
- YouTube: https://www.youtube.com/@unmoldequimica
- Twitter: https://twitter.com/unmoldequimica


# Great contributers!
- [@chemnerd28](https://github.com/chemnerd28)
- [@Ant-28](https://github.com/Ant-28)


Special thanks to [@Rodrigo-Tenorio](https://github.com/Rodrigo-Tenorio) for his help in the creation of this releasable package.
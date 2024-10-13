# Drawing a molecule
Manim Chemistry uses [.mol](https://chem.libretexts.org/Courses/University_of_Arkansas_Little_Rock/ChemInformatics_(2017)%3A_Chem_4399_5399/2.2%3A_Chemical_Representations_on_Computer%3A_Part_II/2.2.2%3A_Anatomy_of_a_MOL_file) files to get atoms and bonds in an easy way. 

Check out the [philosophy](/philosophy) entry to know more about why we do this that way.

## Using a mol file
You can go to the [Working with mol files](/mol_files) section to get a better understanding on what is going on and how you should write your mol files. 

As per this quickstart guide, you can simply download the example [morphine 2d](../../../examples/element_files/morphine.mol) molfile and use it.

## MMoleculeObjects

You can create a MMoleculeObject Using a mol file and the static method `from_mol_file` and then perform all your animations as you would with any MObject:

```python
from manim import *
from manim_chemistry import *

class TwoDMoleculeScene(Scene):
   def construct(self):
        morphine = MMoleculeObject.from_mol_file("morphine.mol")
        self.add(morphine)
```
![plot](../../../examples/examples_assets/2D_morphine_bad.png)

As you can see, it is pretty ugly and can be improved. Go check the [MMoleculeObject] (TODO) section to see how to solve it and improve your drawings.

## NamedMolecules
You can add names to molecules using the class `NamedMolecule`. It includes a name parameter to introduce your molecule name:

```python
from manim import *
from manim_chemistry import *

class NamedMoleculeExample(Scene):
    def construct(self):
        named_molecule = NamedMolecule.from_mol_file(name="Morphine", filename="morphine.mol")
        self.add(diagram)
```
![plot](../../../examples/examples_assets/NamedMoleculeExample_ManimCE_v0.17.3.png)


## GraphMolecules: The beautiful ones
Normal MMoleculeObjects follow the common structure of academia. GraphMolecules are a little bit less correct but they are way prettier. 

Also, they inherit from Manim's [`Graph`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html), which itself inherits from a [networkx graph](https://networkx.org/documentation/stable/reference/classes/graph.html). All this inheritance makes easier to animate and explore more functionality.

Similarly to what you can do with MMoleculeObjects, you can use mol files to create a GraphMolecule:

```python
from manim import *
from manim_chemistry import *

class GraphMoleculeExample(Scene):
    def construct(self):
        graph_molecule = GraphMolecule.build_from_mol(mol_file="morphine.mol")
        self.add(graph_molecule)
```
![plot](../../../examples/examples_assets/DrawGraphMorphine_ManimCE_v0.17.3.png)

### Rotating and changing molecule colors.

One of the powerful tools of graphs is the possibility of selecting atoms and bonds that branch from a certain bond in a certain direction. This, combined with Manim, helps us to animate rotations, movements and color changes of certain parts of the molecule using GMAnimationBuilder:

```python
from manim import *
from manim_chemistry import *

class GraphMoleculeExample(Scene):
    def construct(self):
        molecule = GraphMolecule.build_from_mol(asset, label=True, numeric_label=True)
        atoms_and_bonds = molecule.get_connected_atoms_and_bonds(1, 3)
        animation_builder = GMAnimationBuilder(
            molecule=molecule, atoms=atoms_and_bonds[0], bonds=atoms_and_bonds[1]
        )
        self.add(molecule)
        self.wait()
        self.play(animation_builder.rotate_atoms_about_bond(1, 3))
        self.wait()
        self.play(
            animation_builder.change_color(
                atoms_color=BLUE, bonds_color=RED, label_color=PINK
            )
        )
        self.wait()

```
![plot](../../../examples/examples_assets/CustomGraphMoleculeAnimation.gif)


## ThreeDMolecules
Using the opengl renderer, we can achieve drawing a molecule in three d. All we need are three things:
1. Run the animation using the `opengl` renderer.
2. A .mol file (just like before).
3. A csv data file with data for your atoms. It should contain the following data in the columns:
    - AtomicNumber
    - Name
    - Symbol
    - AtomicMass
    - Color

[Here](../../../assets/Elements_EN.csv) you can download an example of the data file and [there](../../../examples/element_files/morphine3d.mol) you can get the morphine 3d structure to use as an example.


```python
from manim import *
from manim_chemistry import *

config.renderer = opengl # You can set this here or as a flag when running manim.
class Draw3DMorphine(ThreeDScene):
    def construct(self):
        three_d_morphine = ThreeDMolecule.from_mol_file("morphine.mol", "Elementos.csv")
        self.add(three_d_morphine)
        self.wait()
```

```{attention}
Remember to use the opengl renderer:
`manim .\examples.py Draw3DMorphine -ps --renderer=opengl`
```
Here is the result!

![plot](../../../examples/examples_assets/Draw3DMorphine_ManimCE_v0.17.3.png)

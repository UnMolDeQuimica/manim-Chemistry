# Installation.

Right now this can be installed cloning the repo:

```
git clone https://github.com/UnMolDeQuimica/manim-Chemistry.git
cd manim-Chemistry 
pip install .
```

Soon this will be available in pip.

# What is manim-Chemistry?

manim-Chemistry is a manim plugin designed to make chemistry animations easier.

To my knowledge, there is only another plugin related to chemistry called [chanim](https://github.com/kilacoda/chanim) that aims to import to manim the chemfig package (and does an amazing job!).

The philosophy of manim-Chemistry goes into a different direction: Molnim tries to use the manim tools in combination with [.mol](https://en.wikipedia.org/wiki/Chemical_table_file) files and [.csv](https://en.wikipedia.org/wiki/Comma-separated_values) databases useful basic classes to create beatufil chemistry related animations such as a Periodic Table or 2d and 3d chemical structures.

Also, manim-Chemistry will try to do as much things from scratch as possible. That means I will also avoid using libraries such as [Mendeleev](https://mendeleev.readthedocs.io/en/stable/), [RDKit](https://www.rdkit.org/), [PyMOL](https://pymol.org/2/), [Open Babel](https://openbabel.org/wiki/Main_Page) ammong others. The reason is avoid depending on 3rd party packages that might need intensive maintenance. However, the users can combine the power of those libraries with manim-Chemistry to make life easier.

This project is still a work in progress and there is no date for a final realease yet.

# What can manim-Chemistry do right now?

This will be a summary of the capabilities of manim-Chemistry. As this project is still in progress this might not be up to date. Check the examples to get a better idea of what you can do. You might want to check the TODO file to know what is comming and yet to be done. Feel free to open issues and pull requests to make this even greater!

## Reading .mol files

Molnim can parse .mol files to create a dictionary with atoms and bond data. Currently, the data we are getting is:

### Atoms dictionary:

- Index: To know the index in the .mol file, which allows us to keep track of bonding.
- Coordinates: Used to give a position to the atom.
- Element: To know which element is it.
- Bond to. Using the index of other atoms, we get to know to which atoms is bond a certain atom.

### Bonds dictionary:

- From atom: The index of the atom starting the bond
- To atom: The index of the atom ending the bond
- Type: Indicates the type of bond. Check [the bond block specifications](https://en.wikipedia.org/wiki/Chemical_table_file#Bond_block_specification) for further info.
- Stereo: Usefull to know if a cram bond is needed and which kind.

### How to use it:

This is used inside both 2d and 3d molecules but can be used independently importing it from the utils submodule.

```
>>> from manim_chemistry.utils import mol_parser
>>> morphine = 
```

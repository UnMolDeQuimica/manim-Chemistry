# Philosophy

To my knowledge, there is only another plugin related to chemistry called [chanim](https://github.com/kilacoda/chanim) that aims to import to manim the chemfig package (and does an amazing job!).

The philosophy of Manim Chemistry goes into a different direction: manim-Chemistry tries to use the manim tools in combination with [.mol](https://en.wikipedia.org/wiki/Chemical_table_file) files and [.csv](https://en.wikipedia.org/wiki/Comma-separated_values) databases useful basic classes to create beatufil chemistry related animations such as a Periodic Table or 2d and 3d chemical structures.

Also, manim-Chemistry will try to do as much things from scratch as possible. That means I will also avoid using libraries such as [Mendeleev](https://mendeleev.readthedocs.io/en/stable/), [RDKit](https://www.rdkit.org/), [PyMOL](https://pymol.org/2/), [Open Babel](https://openbabel.org) ammong others. The reason is avoid depending on 3rd party packages that might need intensive maintenance. However, the users can combine the power of those libraries with manim-Chemistry to make life easier.

That also means that some cool features such as rendering Molecular Orbitals, parsing other formats such as SMILES, optimizing structures or similarity checks between molecules are out of the scope of this package (by the time). 

Personally, I use those 3rd party packages to get some of the work done, so I might release a plugin for the plugin if I ever build it buut I will not mantain it properly.

Still, Manim Chemistry is quite powerful and easy to use. Need any help? Want a new feature? Something is broken? [Contact me!](contributing/contact)
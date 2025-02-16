from ..twoD import GraphMolecule


class Molecule:
    """Works as a proxy between different types of molecules with the same methods.

    Supported types of molecules are:
        - GraphMolecule
        - MMoleculeObject
        - ThreeDMolecule

    Examples
    ---------
    .. manim:: GraphMoleculeFromMolecule

        from manim_chemistry import *

        class GraphMoleculeFromMolecule(Scene):
            def construct(self):
                molecule = Molecule(GraphMolecule).molecule_from_pubchem(name="acetone")
                self.wait()
                self.play(Write(molecule))
                self.wait()


    .. manim:: MMoleculeObjectFromMolecule

        from manim_chemistry import *

        class MMoleculeObjectFromMolecule(Scene):
            def construct(self):
                molecule = Molecule(MMoleculeObject).molecule_from_pubchem(name="acetone")
                self.wait()
                self.play(Write(molecule))
                self.wait()
    """

    def __init__(self, molecule_class=GraphMolecule):
        self.molecule_class = molecule_class

    def molecule_from_file(self, *args, **kwargs):
        return self.molecule_class.molecule_from_file(*args, **kwargs)

    def multiple_molecules_from_file(self, *args, **kwargs):
        return self.molecule_class.multiple_molecules_from_file(*args, **kwargs)

    def molecule_from_string(self, *args, **kwargs):
        return self.molecule_class.molecule_from_string(*args, **kwargs)

    def multiple_molecules_from_string(self, *args, **kwargs):
        return self.molecule_class.multiple_molecules_from_string(*args, **kwargs)

    def molecule_from_pubchem(self, *args, **kwargs):
        return self.molecule_class.molecule_from_pubchem(*args, **kwargs)

    def mc_molecule_to_atoms_and_bonds(self, *args, **kwargs):
        return self.molecule_class.mc_molecule_to_atoms_and_bonds(*args, **kwargs)

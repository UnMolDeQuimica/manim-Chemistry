from manim import *
from src.manim_chemistry import *

class Test(Scene):
    def construct(self):
        mol = GraphMolecule.build_from_mol("et.mol")
        self.add(mol)
from manim import Scene, ThreeDScene
from manim_chemistry import MMoleculeObject, ThreeDMolecule, MElementObject, PeriodicTable 
# 2D Molecule example
class Draw2DMorphine(Scene):
    def construct(self):
        self.add(MMoleculeObject.from_mol_file(filename="element_files/morphine.mol"))

# 3D Molecule example
class Draw3DMorphine(ThreeDScene):
    def construct(self):
        self.add(ThreeDMolecule.from_mol_file(filename="element_files/morphine3d.mol"))
        self.wait()
        

# Element example 
class DrawCarbonElement(Scene):
    def construct(self):
        self.add(MElementObject.from_csv_file_data(filename="element_files/Elementos.csv", atomic_number=6))
        
# Periodic Table example 
class DrawPeriodicTable(Scene):
    def construct(self):
        self.add(PeriodicTable(data_file="element_files/Elementos.csv"))
        
# Orbitals example #TODO

from pathlib import Path

from manim import Scene, ThreeDScene, config

from manim_chemistry import (BohrAtom, GraphMolecule, MElementObject,
                             MMoleculeObject, Orbital, PeriodicTable,
                             ThreeDMolecule, sdf_parser)

script_path = Path(__file__).absolute().parent
files_path = script_path / "element_files"


# 2D Molecule example
class Draw2DMorphine(Scene):
    # Two D Manim Chemistry objects require Cairo renderer
    config.renderer = "cairo"

    def construct(self):
        morphine = MMoleculeObject.from_mol_file(filename=files_path / "morphine.mol")
        self.add(morphine)

# 2D Molecule from SDF file
class Draw2DMorphineSDF(Scene):
    config.renderer = "cairo"

    def construct(self):
        parts = sdf_parser(file=files_path / "morphine.sdf")
        atoms, bonds = parts[0]
        morphine = MMoleculeObject(atoms, bonds)
        self.add(morphine)


# 2D Graph Molecule example
class DrawGraphMorphine(Scene):
    # Two D Manim Chemistry objects require Cairo renderer
    config.renderer = "cairo"

    def construct(self):
        self.add(GraphMolecule.build_from_mol(mol_file=files_path / "morphine.mol"))

# 2D Graph Molecule example
class DrawLabeledGraphMorphine(Scene):
    # Two D Manim Chemistry objects require Cairo renderer
    config.renderer = "cairo"

    def construct(self):
        self.add(
            GraphMolecule.build_from_mol(
                mol_file=files_path / "morphine.mol", label=True
            )
        )


# 3D Molecule example
class Draw3DMorphine(ThreeDScene):
    # Three D Manim Chemistry objects require Opengl renderer
    config.renderer = "opengl"

    def construct(self):
        self.add(
            ThreeDMolecule.from_mol_file(
                filename=files_path / "morphine3d.mol",
                source_csv=files_path / "Elementos.csv",
            )
        )
        self.wait()


# Element example
class DrawCarbonElement(Scene):
    # Two D Manim Chemistry objects require Cairo renderer
    config.renderer = "cairo"

    def construct(self):
        self.add(
            MElementObject.from_csv_file_data(
                filename=files_path / "Elementos.csv", atomic_number=6
            )
        )


# Periodic Table example
class DrawPeriodicTable(Scene):
    # Two D Manim Chemistry objects require Cairo renderer
    config.renderer = "cairo"

    def construct(self):
        self.add(PeriodicTable(data_file=files_path / "Elementos.csv"))


# Orbitals example
class DrawPOrbital(ThreeDScene):
    # Three D Manim Chemistry objects require Opengl renderer
    config.renderer = "opengl"

    def construct(self):
        self.add(Orbital(l=1, m=-1))


# Bohr diagram example
class BohrDiagram(Scene):
    # Two D Manim Chemistry objects require Cairo renderer
    config.renderer = "cairo"

    def construct(self):
        self.add(BohrAtom())

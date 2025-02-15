from pathlib import Path

from manim import Scene, ThreeDScene, config

from manim_chemistry import (
    BohrAtom,
    GraphMolecule,
    MElementObject,
    MMoleculeObject,
    Orbital,
    PeriodicTable,
    ThreeDMolecule,
)

script_path = Path(__file__).absolute().parent
files_path = script_path / "molecule_files/mol_files"


# 2D Molecule example
class Draw2DMorphine(Scene):
    # Two D Manim Chemistry objects require Cairo renderer
    config.renderer = "cairo"

    def construct(self):
        morphine = MMoleculeObject.molecule_from_file(
            filename=files_path / "morphine.mol"
        )
        self.add(morphine)


# 2D Graph Molecule example
class DrawGraphMorphine(Scene):
    # Two D Manim Chemistry objects require Cairo renderer

    def construct(self):
        config.renderer = "cairo"
        self.add(GraphMolecule.molecule_from_file(filepath=files_path / "morphine.mol"))


# 2D Graph Molecule example
class DrawLabeledGraphMorphine(Scene):
    # Two D Manim Chemistry objects require Cairo renderer

    def construct(self):
        config.renderer = "cairo"
        self.add(
            GraphMolecule.molecule_from_file(
                mol_file=files_path / "morphine.mol", label=True
            )
        )


# 3D Molecule example
class Draw3DMorphine(ThreeDScene):
    # Three D Manim Chemistry objects require Opengl renderer

    def construct(self):
        config.renderer = "opengl"
        self.add(
            ThreeDMolecule.molecule_from_file(
                filename=files_path / "morphine3d.mol",
                source_csv=files_path / "Elementos.csv",
            )
        )
        self.wait()

        # Set the renderer back to cairo to prevent issues with other examples
        config.renderer = "cairo"


# Element example
class DrawCarbonElement(Scene):
    # Two D Manim Chemistry objects require Cairo renderer

    def construct(self):
        config.renderer = "cairo"
        self.add(
            MElementObject.from_csv_file_data(
                filename=files_path / "Elementos.csv", atomic_number=6
            )
        )


# Periodic Table example
class DrawPeriodicTable(Scene):
    # Two D Manim Chemistry objects require Cairo renderer

    def construct(self):
        config.renderer = "cairo"
        self.add(PeriodicTable(data_file=files_path / "Elementos.csv"))


# Orbitals example
class DrawPOrbital(ThreeDScene):
    # Three D Manim Chemistry objects require Opengl renderer

    def construct(self):
        config.renderer = "opengl"
        self.add(Orbital(l=1, m=-1))
        config.renderer = "cairo"


# Bohr diagram example
class BohrDiagram(Scene):
    # Two D Manim Chemistry objects require Cairo renderer
    config.renderer = "cairo"

    def construct(self):
        self.add(BohrAtom())

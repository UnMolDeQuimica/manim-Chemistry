import logging

from manim import *
from manim_chemistry import *

logger = logging.getLogger(__name__)


class TestGraphMoleculeCreationUncreation(Scene):
    def construct(self):
        graph_molecule = GraphMolecule.build_from_mol(
            "examples/element_files/double_triple_bonds_molecule.mol"
        )

        self.wait()
        self.play(Create(graph_molecule))
        self.wait()
        self.play(Uncreate(graph_molecule))


class TestGraphMoleculeFadeInOut(Scene):
    def construct(self):
        graph_molecule = GraphMolecule.build_from_mol(
            "examples/element_files/double_triple_bonds_molecule.mol"
        )

        self.wait()
        self.play(FadeIn(graph_molecule))
        self.wait()
        self.play(FadeOut(graph_molecule))


class TestGraphMoleculeWriteUnwrite(Scene):
    def construct(self):
        graph_molecule = GraphMolecule.build_from_mol(
            "examples/element_files/double_triple_bonds_molecule.mol"
        )

        self.wait()
        self.play(Write(graph_molecule))
        self.wait()
        self.play(Unwrite(graph_molecule))


class TestGraphMoleculeShift(Scene):
    def construct(self):
        graph_molecule = GraphMolecule.build_from_mol(
            "examples/element_files/double_triple_bonds_molecule.mol"
        )

        self.add(graph_molecule)
        self.wait()
        self.play(graph_molecule.animate.shift(RIGHT))
        self.wait()
        self.play(graph_molecule.animate.shift(LEFT))


class TestGraphMoleculeRotate(Scene):
    def construct(self):
        graph_molecule = GraphMolecule.build_from_mol(
            "examples/element_files/double_triple_bonds_molecule.mol"
        )

        self.add(graph_molecule)
        self.wait()
        self.play(Rotate(graph_molecule, angle=2 * PI))
        self.wait()


class TestGraphMoleculeScale(Scene):
    def construct(self):
        graph_molecule = GraphMolecule.build_from_mol(
            "examples/element_files/double_triple_bonds_molecule.mol"
        )

        self.add(graph_molecule)
        self.wait()
        self.play(graph_molecule.animate.scale(2))
        self.wait()
        self.play(graph_molecule.animate.scale(0.5))


class TestGraphMoleculeLabelsAreAdded(Scene):
    def construct(self):
        graph_molecule = GraphMolecule.build_from_mol(
            "examples/element_files/double_triple_bonds_molecule.mol", label=True
        )

        self.add(graph_molecule)


class TestGraphMoleculeNumericLabelsAreAdded(Scene):
    def construct(self):
        graph_molecule = GraphMolecule.build_from_mol(
            "examples/element_files/double_triple_bonds_molecule.mol",
            label=True,
            numeric_label=True,
        )

        self.add(graph_molecule)


class TestGraphMoleculeAnimationBuilder(Scene):
    def construct(self):
        graph_molecule = GraphMolecule.build_from_mol(
            "examples/element_files/double_triple_bonds_molecule.mol",
            label=True,
        )

        atoms_and_bonds = graph_molecule.get_connected_atoms_and_bonds(2, 6)
        animation_builder = GMAnimationBuilder(
            molecule=graph_molecule, atoms=atoms_and_bonds[0], bonds=atoms_and_bonds[1]
        )

        self.add(graph_molecule)
        self.wait()
        self.play(animation_builder.rotate_atoms_about_bond(2, 6))
        self.wait()
        self.play(
            animation_builder.change_color(
                atoms_color=BLUE, bonds_color=RED, label_color=PINK
            )
        )


class TestGraphMoleculeMoveAllAtoms(Scene):
    def construct(self):
        graph_molecule = GraphMolecule.build_from_mol(
            "examples/element_files/double_triple_bonds_molecule.mol",
            label=True,
        )

        self.add(graph_molecule)
        self.wait()

        for atom in graph_molecule:
            self.play(atom.animate.shift(UP), run_time=0.25)
            self.play(atom.animate.shift(DOWN), run_time=0.25)


def run_graph_molecule_animation_tests():
    animations = [
        TestGraphMoleculeCreationUncreation,
        TestGraphMoleculeFadeInOut,
        TestGraphMoleculeWriteUnwrite,
        TestGraphMoleculeShift,
        TestGraphMoleculeRotate,
        TestGraphMoleculeScale,
        TestGraphMoleculeLabelsAreAdded,
        TestGraphMoleculeNumericLabelsAreAdded,
        TestGraphMoleculeAnimationBuilder,
        TestGraphMoleculeMoveAllAtoms,
    ]

    errors = {}
    for animation in animations:
        logger.info(f"Starting {animation} animation.")
        try:
            animation().render()
            logger.info(f"Animation {animation} finished successfully.")

        except Exception as error:
            errors[animation] = error

    if not errors:
        logger.info("All GraphMolecule animations finished successfuilly.")

    else:
        logger.error(f"The following animations were unsuccessful: {errors}")

from manim import VGroup, PI, BLACK

from .graph_molecule import GraphMolecule


class GMAnimationBuilder:
    def __init__(
        self,
        molecule: GraphMolecule,
        atoms: VGroup | None = None,
        bonds: VGroup | None = None,
    ):
        self.molecule = molecule
        self.atoms = atoms or self.molecule.vertices.values()
        self.atoms_copy = self.atoms.copy()
        self.bonds = bonds or self.molecule.edges.values()
        self.bonds_copy = self.bonds.copy()

    def bonds_from_atoms(self, atom_a, atom_b):
        for bond in self.molecule.edges:
            if atom_a in bond and atom_b in bond:
                return bond

        raise Exception(f"No bond found for atoms {atom_a}, {atom_b}")

    def rotate_atoms_about_bond(self, atom_a, atom_b, angle=PI / 4):
        bond = self.bonds_from_atoms(atom_a=atom_a, atom_b=atom_b)
        axis = self.molecule.edges[bond].sheen_direction
        self.atoms_copy.rotate(axis=axis, angle=angle)

        return [
            atom.animate.move_to(atom_copy)
            for atom, atom_copy in zip(self.atoms, self.atoms_copy)
        ]

    def change_color(self, atoms_color=BLACK, bonds_color=None, label_color=None):
        animations = []

        if label_color:
            for atom in self.atoms:
                animations.append(atom[0].animate.set_color(atoms_color))
                animations.append(atom[1].animate.set_color(label_color))

        else:
            for atom in self.atoms:
                animations.append(atom[0].animate.set_color(atoms_color))
                animations.append(atom[1].animate.set_color(atom[1].color))

        if bonds_color:
            for bond in self.bonds:
                animations.append(bond.animate.set_color(bonds_color))

        return animations

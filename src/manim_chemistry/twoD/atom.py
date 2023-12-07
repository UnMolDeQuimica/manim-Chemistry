from manim import VGroup, WHITE, MarkupText, RIGHT, LEFT, Dot
import numpy as np
from typing import Dict, Any


class MAtomObject(VGroup):
    def __str__(self):
        return f"MAtomObject of element {self.element}"

    def __repr__(self):
        return f"MAtomObject of element {self.element}"

    def __init__(
        self,
        coords: np.array = np.array([0, 0, 0]),
        element: str = "H",
        explicit_carbons: bool = False,
        explicit_hydrogens: bool = False,
        bond_to: Dict[int, Any] = {},
        representation_type: str or None = None,
        color: str = WHITE,
        charge: int = 0,
        index: int = 0,
        planar: bool = True,
        **kwargs,
    ):
        VGroup.__init__(self, **kwargs)
        self.coords = coords
        self.element = element
        self.explicit_carbons = explicit_carbons
        self.explicit_hydrogens = explicit_hydrogens
        self.bond_to = bond_to
        self.representation_type = representation_type
        self.representation = self.set_representation(representation_type)
        self.charge = charge
        self.index = index
        self.planar = planar
        self.color = color
        self.atom = self.add_atom()

        if self.planar:
            self.coords[2] = 0

        if self.atom:
            self.add(self.atom)

        else:
            self.add(Dot(radius=0))
        self.move_to(self.coords)
        self.set_atom_color(self.color)

    def set_representation(self, representation_type):
        """
        - 'complete': Adds the element symbol.
        - 'skeleton': Does not add the symbol
        - 'over_bond': Adds the symbol above the bond
        """
        if representation_type:
            return representation_type

        if self.element == "C":  # and not self.explicit_carbons:
            representation_type = "skeleton"

        elif self.element == "H":
            if self.explicit_hydrogens:
                representation_type = "complete"
            elif self.bond_to and "C" not in self.bond_to.values():
                representation_type = "complete"
            elif not self.explicit_hydrogens:  # TODO: Rethink this logic
                representation_type = "skeleton"
        else:
            representation_type = "complete"

        return representation_type

    def add_atom(self):
        """
        Adds an atom depending on the representation
        """
        if self.representation != "skeleton":
            return MarkupText(self.element).scale(0.8)

    def bonds_fulfilled(self):
        minimum_bonds = {"O": 2, "S": 2, "N": 3, "P": 3}
        minimum_bond = minimum_bonds.get(self.element)
        if self.bond_to and minimum_bond:
            return len(self.bond_to) == minimum_bonds.get(self)

        return True

    def make_copy(self):
        copy = MAtomObject(
            coords=self.coords,
            element=self.element,
            explicit_carbons=self.explicit_carbons,
            explicit_hydrogens=self.explicit_hydrogens,
            bond_to=self.bond_to,
            representation_type=self.representation_type,
            color=self.color,
            charge=self.charge,
            index=self.index,
            planar=self.planar,
        )
        return copy

    def rename_atom(self, new_element, bonds_direction):
        self.element = new_element
        renamed_atom = self.make_copy()

        original_width = self.width
        new_width = renamed_atom.width

        width_difference = new_width - original_width
        if bonds_direction > 0:
            renamed_atom.shift(width_difference / 1.5 * RIGHT)

        else:
            renamed_atom.shift(width_difference / 1.5 * LEFT)

        return renamed_atom

    def copy_with_explicit_hydrogens(self):
        self.explicit_hydrogens = True

        return self.make_copy()

    def set_atom_color(self, color):
        """
        TODO: Add the color depending on cpk convention
        """
        pass

from manim import VGroup, WHITE, Line, Polygram, PI, VMobject
import numpy as np
from .atom import MAtomObject


class BaseMBondObject(VGroup):
    def __str__(self):
        return f"MBondObject bonding {self.from_atom} with {self.to_atom}"

    def __repr__(self):
        return f"MBondObject bonding {self.from_atom} with {self.to_atom}"

    def __init__(
        self,
        from_atom: MAtomObject,
        to_atom: MAtomObject,
        type: int = 0,
        subtype: str = "",
        color: str = WHITE,
        index: int = 0,
        **kwargs,
    ):
        VGroup.__init__(self, **kwargs)
        self.from_atom = from_atom
        self.to_atom = to_atom
        self.type = type
        self.color = color
        self.subtype = self.define_subtype(subtype) or subtype
        self.bond = self.create_line()
        self.index = index
        self.add(self.bond)

    def define_subtype(self, subtype: str) -> str or bool:
        """
        Defines the subtype based on atoms' representations. Input options:
            - 'complete'
            - 'skeleton'
            - 'over_bond'

        Output options:
            - shorter: Does not touch the cener of the atoms.
            - shorter_from: Does not touch the center of the from atom.
            - shorter_to: Does not touch the center of the to atom.
            - None or false: Touches both atoms center
        """
        from_representation = self.from_atom.representation
        to_representation = self.to_atom.representation
        if from_representation == "complete":
            if to_representation == "complete":
                return "shorter"
            elif to_representation == "skeleton" or to_representation == "over_bond":
                return "shorter_from"

        if from_representation == "skeleton" or to_representation == "over_bond":
            if to_representation == "complete":
                return "shorter_to"
            elif to_representation == "skeleton" or to_representation == "over_bond":
                return False

        return False

    def atoms_in_bond(self):
        return self.from_atom, self.to_atom

    def atom_is_in_bond(self, atom):
        if self.from_atom == atom or self.to_atom == atom:
            return True
        else:
            return False

    def get_bond_index_by_atom(self, atom):
        if self.atom_is_in_bond(atom):
            return self.index

        return

    def add_bond_index_by_atom_to_list(self, atom, list):
        index = self.get_bond_index_by_atom(atom)

        if index is not None:
            list.append(index)

        return list

    def get_perpendicular_unit_vector(self, point_a, point_b):
        direction = point_b - point_a
        if direction[0] == 0 and direction[1] == 0:
            perp_vector = np.cross(direction, np.array([0, 1, 0]))

        else:
            perp_vector = np.cross(direction, np.array([0, 0, 1]))

        return perp_vector / np.linalg.norm(perp_vector)

    def no_subtype(self):
        """
        To be implemented in every bond subclass.
        """
        pass

    def shorter_subtype(self):
        """
        To be implemented in every bond subclass.
        """
        pass

    def shorter_from_subtype(self):
        """
        To be implemented in every bond subclass.
        """
        pass

    def shorter_to_subtype(self):
        """
        To be implemented in every bond subclass.
        """
        pass

    def longer_subtype(self):
        """
        To be implemented in every bond subclass.
        """
        pass

    def create_line(self):
        """
        To be implemented in every bond subclass.
        """
        pass

    def get_vector(self):
        """
        All bonds should contain at least a Line. This line can return the corresponding vector.
        """
        try:
            return self[0].get_vector()
        
        except Exception as exception:
            raise exception

class SimpleBond(BaseMBondObject):
    def no_subtype(self):
        return Line(self.from_atom.coords, self.to_atom.coords)

    def shorter_subtype(self):
        return Line(self.from_atom.coords, self.to_atom.coords, buff=0.2)

    def shorter_from_subtype(self, direction):
        return Line(self.to_atom.coords + direction * 0.8, self.to_atom.coords)

    def shorter_to_subtype(self, direction):
        return Line(self.from_atom.coords, self.from_atom.coords - direction * 0.8)

    def longer_subtype(self):
        return Line(self.from_atom.coords, self.from_atom.coords)

    def create_line(self):
        direction = self.from_atom.coords - self.to_atom.coords

        if not self.subtype:
            return self.no_subtype()

        else:
            subtypes = {
                "shorter": self.shorter_subtype(),
                "shorter_from": self.shorter_from_subtype(direction),
                "shorter_to": self.shorter_to_subtype(direction),
                "longer": self.longer_subtype(),
            }

            return subtypes.get(self.subtype) or VMobject()


class DoubleBond(BaseMBondObject):
    def __init__(
        self, from_atom, to_atom, side=0, distance=0.15, double_bond_scale=0.7, **kwargs
    ):
        self.side = side
        self.distance = distance
        self.double_bond_scale = double_bond_scale
        super().__init__(from_atom, to_atom, **kwargs)

    def no_subtype(self):
        unit_vector = (
            self.get_perpendicular_unit_vector(
                self.from_atom.coords, self.to_atom.coords
            )
            * 0.15
        )  # TODO: Make this product value an option
        long_line = Line(self.from_atom.coords, self.to_atom.coords)
        short_line = Line(self.from_atom.coords, self.to_atom.coords, buff=0.15).shift(
            -unit_vector
        )  # TODO: Make the buff an option

        return VGroup(long_line, short_line)

    def shorter_subtype(self):
        unit_vector = (
            self.get_perpendicular_unit_vector(
                self.from_atom.coords, self.to_atom.coords
            )
            * 0.1
        )  # TODO: Make this product an option
        base_line = Line(self.from_atom.coords, self.to_atom.coords, buff=0.3).shift(
            unit_vector
        )  # Make this buff an option
        double_line = Line(self.from_atom.coords, self.to_atom.coords, buff=0.3).shift(
            -unit_vector
        )  # Make this buff an option

        return VGroup(base_line, double_line)

    def shorter_from_subtype(self, direction, from_surroundings, to_surroundings):
        unit_vector = (
            self.get_perpendicular_unit_vector(
                self.from_atom.coords, self.to_atom.coords
            )
            * 0.1
        )  # TODO: Make this product an option

        if not from_surroundings and not to_surroundings:
            base_line = (
                Line(self.to_atom.coords - 0.2 * direction, self.from_atom.coords)
                .scale(self.double_bond_scale)
                .shift(unit_vector)
            )
            double_line = base_line.copy().shift(-2 * unit_vector)

        else:
            base_line = Line(
                self.to_atom.coords, self.from_atom.coords - 0.25 * direction
            )
            double_line = (
                base_line.copy().scale(self.double_bond_scale).shift(1.5 * unit_vector)
            )  # TODO: Make this scale an option

        return VGroup(base_line, double_line)

    def shorter_to_subtype(self, direction, from_surroundings, to_surroundings):
        unit_vector = (
            self.get_perpendicular_unit_vector(
                self.from_atom.coords, self.to_atom.coords
            )
            * 0.1
        )  # TODO: Make this product an option

        if not from_surroundings and not to_surroundings:
            base_line = Line(
                self.from_atom.coords, self.to_atom.coords + 0.2 * direction
            ).shift(unit_vector)
            double_line = base_line.copy().shift(-2 * unit_vector)

        else:
            base_line = Line(
                self.from_atom.coords, self.to_atom.coords + 0.25 * direction
            )
            double_line = (
                base_line.copy().scale(self.double_bond_scale).shift(1.5 * unit_vector)
            )  # TODO: Make this scale an option

        return VGroup(base_line, double_line)
    
    def get_vector(self):
        """
        This contains a VGroup with two lines, we just get the vector from one of them
        """
        try:
            return self[0][0].get_vector()
        
        except Exception as exception:
            raise exception

    def get_surroundings(self):
        """
        Checks the number of bonds of C atoms.
        Returns False if the C has a structure like central C in acetone:
            - Not bonded to H atoms.
            - Double bond to at least another atom.

        Otherwise returns True, resulting in a structure like the C with
        double bond to imidazole.

        TODO: Refactor this to make it more logical and way less verbose.
        """
        from_surroundings, to_surroundings = (False, False)
        if self.from_atom.bond_to:
            from_surroundings = (
                self.from_atom.element == "C"
                and len(self.from_atom.bond_to) < 4
                and "H" in self.from_atom.bond_to.values()
            )
        if self.to_atom.bond_to:
            to_surroundings = (
                self.to_atom.element == "C"
                and len(self.to_atom.bond_to) < 4
                and "H" in self.to_atom.bond_to.values()
            )

        return from_surroundings, to_surroundings

    def create_line(self):
        from_surroundings, to_surroundings = self.get_surroundings()
        direction = self.from_atom.coords - self.to_atom.coords

        if not self.subtype:
            return self.no_subtype()

        else:
            subtypes = {
                "shorter": self.shorter_subtype(),
                "shorter_from": self.shorter_from_subtype(
                    direction=direction,
                    from_surroundings=from_surroundings,
                    to_surroundings=to_surroundings,
                ),
                "shorter_to": self.shorter_to_subtype(
                    direction,
                    from_surroundings=from_surroundings,
                    to_surroundings=to_surroundings,
                ),
            }

            return subtypes.get(self.subtype) or VMobject()


class TripleBond(BaseMBondObject):
    def __init__(
        self, from_atom, to_atom, side=0, distance=0.3, triple_bond_scale=0.8, **kwargs
    ):
        self.distance = distance
        self.triple_bond_scale = triple_bond_scale
        super().__init__(from_atom, to_atom, **kwargs)

    def no_subtype(self):
        unit_vector = (
            self.get_perpendicular_unit_vector(
                self.from_atom.coords, self.to_atom.coords
            )
            * 0.15
        )  # TODO: Make this value an option
        base_line = Line(self.from_atom.coords, self.to_atom.coords)
        double_line = base_line.copy().scale(self.triple_bond_scale).shift(unit_vector)
        triple_line = base_line.copy().scale(self.triple_bond_scale).shift(-unit_vector)

        return VGroup(base_line, double_line, triple_line)

    def shorter_subtype(self):
        unit_vector = (
            self.get_perpendicular_unit_vector(
                self.from_atom.coords, self.to_atom.coords
            )
            * 0.15
        )  # TODO: Make this value an option
        base_line = Line(self.from_atom.coords, self.to_atom.coords, buff=0.25)
        double_line = base_line.copy().shift(unit_vector)
        triple_line = base_line.copy().shift(-unit_vector)

        return VGroup(base_line, double_line, triple_line)

    def shorter_from_subtype(self, direction):
        unit_vector = (
            self.get_perpendicular_unit_vector(
                self.from_atom.coords, self.to_atom.coords
            )
            * 0.15
        )  # TODO: Make this value an option
        base_line = Line(
            self.to_atom.coords - 0.1 * direction,
            self.to_atom.coords + 0.85 * direction,
        ).scale(self.triple_bond_scale)
        double_line = base_line.copy().scale(self.triple_bond_scale).shift(unit_vector)
        triple_line = base_line.copy().scale(self.triple_bond_scale).shift(-unit_vector)

        return VGroup(base_line, double_line, triple_line)

    def shorter_to_subtype(self, direction):
        unit_vector = (
            self.get_perpendicular_unit_vector(
                self.from_atom.coords, self.to_atom.coords
            )
            * 0.15
        )  # TODO: Make this value an option
        base_line = Line(
            self.from_atom.coords + 0.1 * direction,
            self.from_atom.coords - 0.85 * direction,
        ).scale(self.triple_bond_scale)
        double_line = base_line.copy().scale(self.triple_bond_scale).shift(unit_vector)
        triple_line = base_line.copy().scale(self.triple_bond_scale).shift(-unit_vector)

        return VGroup(base_line, double_line, triple_line)

    def longer_subtype(self, bond, base_line):
        bond.add(base_line)
        double_line = base_line.copy().scale(self.triple_bond_scale)
        triple_line = base_line.copy().scale(self.triple_bond_scale)
        pivot_line = (
            base_line.copy()
            .rotate(angle=PI / 2, about_point=base_line.get_center())
            .scale(self.distance)
        )
        double_line.move_to(pivot_line.get_end())
        triple_line.move_to(pivot_line.get_start())
        bond.add(double_line, triple_line)

    def create_line(self):
        direction = self.from_atom.coords - self.to_atom.coords

        if not self.subtype:
            return self.no_subtype()

        else:
            subtypes = {
                "shorter": self.shorter_subtype(),
                "shorter_from": self.shorter_from_subtype(direction=direction),
                "shorter_to": self.shorter_to_subtype(direction=direction),
            }

            return subtypes.get(self.subtype) or VMobject()

    def get_vector(self):
        """
        This contains a VGroup with two lines, we just get the vector from one of them
        """
        try:
            return self[0][0].get_vector()
        
        except Exception as exception:
            raise exception

class PlainCramBond(BaseMBondObject):
    def no_subtype(self):
        direction = self.to_atom.coords - self.from_atom.coords
        base_line = Line(self.from_atom.coords, self.to_atom.coords)
        pivot_line = (
            base_line.copy().rotate(angle=PI / 2).scale(0.3).shift(direction / 2)
        )
        cram_bond = Polygram(
            np.array([base_line.start, pivot_line.get_start(), pivot_line.get_end()]),
            color=self.color,
            fill_opacity=1,
        )

        return cram_bond

    def shorter_subtype(self):
        direction = self.to_atom.coords - self.from_atom.coords
        base_line = Line(self.from_atom.coords, self.to_atom.coords, buff=0.2)
        pivot_line = (
            base_line.copy().rotate(angle=PI / 2).scale(0.3).shift(direction / 2)
        )
        cram_bond = Polygram(
            np.array([base_line.start, pivot_line.get_start(), pivot_line.get_end()]),
            color=self.color,
            fill_opacity=1,
        )

        return cram_bond

    def shorter_from_subtype(self):
        direction = self.to_atom.coords - self.from_atom.coords
        base_line = Line(self.to_atom.coords + direction * 0.2, self.to_atom.coords)
        pivot_line = (
            base_line.copy().rotate(angle=PI / 2).scale(0.4).shift(direction / 2)
        )
        cram_bond = Polygram(
            np.array([base_line.start, pivot_line.get_start(), pivot_line.get_end()]),
            color=self.color,
            fill_opacity=1,
        )

        return cram_bond

    def shorter_to_subtype(self):
        direction = self.to_atom.coords - self.from_atom.coords
        base_line = Line(self.from_atom.coords, self.from_atom.coords + direction * 0.2)
        pivot_line = (
            base_line.copy().rotate(angle=PI / 2).scale(0.6).shift(direction / 2)
        )
        cram_bond = Polygram(
            np.array([base_line.start, pivot_line.get_start(), pivot_line.get_end()]),
            color=self.color,
            fill_opacity=1,
        )
        return cram_bond

    def longer_subtype(self):
        direction = self.to_atom.coords - self.from_atom.coords
        base_line = Line(self.from_atom.coords, self.from_atom.coords)
        pivot_line = (
            base_line.copy().rotate(angle=PI / 2).scale(0.3).shift(direction / 2)
        )
        cram_bond = Polygram(
            np.array([base_line.start, pivot_line.get_start(), pivot_line.get_end()]),
            color=self.color,
            fill_opacity=1,
        )

        return cram_bond

    def create_line(self):
        if not self.subtype:
            return self.no_subtype()

        else:
            subtypes = {
                "shorter": self.shorter_subtype(),
                "shorter_from": self.shorter_from_subtype(),
                "shorter_to": self.shorter_to_subtype(),
                "longer": self.longer_subtype(),
            }
            return subtypes.get(self.subtype) or VMobject()
        
    def get_vector(self):
        try:
            atom_a, atom_b = self.atoms_in_bond()
            
            return atom_b.get_center() - atom_a.get_center()
        
        except Exception as exception:
            raise exception


class DashedCramBond(BaseMBondObject):
    def add_dashed_cram_bond(self, base_line, direction):
        pivot_line = base_line.copy().rotate(angle=PI / 2).scale(0.2)
        cram_bond = VGroup()
        direction_modulus = (
            direction[0] ** 2 + direction[1] ** 2 + direction[2] ** 2
        ) ** 0.5  # TODO: For sure numpy knows how to do this. Find how.
        increase = 0.05 / direction_modulus  # TODO: Change this 0.05 to be an option
        for i in range(
            int(direction_modulus * 5)
        ):  # TODO: Change this 5 to be an option
            cram_bond.add(Line(pivot_line.get_start(), pivot_line.get_end()))
            pivot_line.shift(direction * 0.16 / direction_modulus).scale(
                1 + increase / pivot_line.get_length()
            )  # TODO: Change this 5 to be an option
        return cram_bond

    def no_subtype(self):
        direction = self.to_atom.coords - self.from_atom.coords
        base_line = Line(self.from_atom.coords, self.to_atom.coords)
        cram_bond = self.add_dashed_cram_bond(base_line=base_line, direction=direction)
        return cram_bond

    def shorter_subtype(self):
        direction = self.to_atom.coords - self.from_atom.coords
        base_line = Line(self.from_atom.coords, self.to_atom.coords, buff=0.2)
        cram_bond = self.add_dashed_cram_bond(base_line=base_line, direction=direction)

        return cram_bond

    def shorter_from_subtype(self):
        direction = self.to_atom.coords - self.from_atom.coords
        base_line = Line(self.to_atom.coords + direction * 0.2, self.to_atom.coords)
        cram_bond = self.add_dashed_cram_bond(base_line=base_line, direction=direction)

        return cram_bond

    def shorter_to_subtype(self):
        direction = self.to_atom.coords - self.from_atom.coords
        base_line = Line(self.from_atom.coords, self.from_atom.coords + direction * 0.2)
        cram_bond = self.add_dashed_cram_bond(base_line=base_line, direction=direction)

        return cram_bond

    def longer_subtype(self):
        direction = self.to_atom.coords - self.from_atom.coords
        base_line = Line(self.from_atom.coords, self.from_atom.coords)
        cram_bond = self.add_dashed_cram_bond(base_line=base_line, direction=direction)

        return cram_bond

    def create_line(self):
        if not self.subtype:
            return self.no_subtype()

        else:
            subtypes = {
                "shorter": self.shorter_subtype(),
                "shorter_from": self.shorter_from_subtype(),
                "shorter_to": self.shorter_to_subtype(),
                "longer": self.longer_subtype(),
            }

            return subtypes.get(self.subtype) or VMobject()
    
    def get_vector(self):
        """
        This contains a VGroup with two lines, we just get the vector from one of them
        """
        try:
            starting_line = self[0][0]
            ending_line = self[0][len(self[0]) - 1]
            return ending_line.get_center() - starting_line.get_center()
        
        except Exception as exception:
            raise exception

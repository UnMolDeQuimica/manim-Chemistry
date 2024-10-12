import numpy as np
import random
from manim import VGroup, WHITE, BLUE, RED, Circle, Dot, TAU, RIGHT


class BohrAtom(VGroup):
    """
    Creates a Bohr like diagram
    """

    def __init__(
        self,
        e=14,  # Electrons
        p=14,  # Protons
        n=10,  # Neutrons
        level=None,  # Levels
        orbit_color=WHITE,
        electron_color=BLUE,
        proton_color=RED,
        neutron_color=WHITE,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.e = e
        self.p = p
        self.n = n
        self.level = level
        self.occupied_levels = self.calculate_levels()
        self.orbit_color = orbit_color
        self.electron_color = electron_color
        self.proton_color = proton_color
        self.neutron_color = neutron_color
        self.add(self.orbitals_group(), self.electrons_group(), self.nuclei_groups())
        self.TOTAL_ELECTRONS_PER_LEVEL = {
            # Electrons that fit in total: Level
            2: 1,
            10: 2,
            28: 3,
            60: 4,
            110: 5,
            182: 6,
        }

    def calculate_levels(self):
        TOTAL_ELECTRONS_PER_LEVEL = {
            # Electrons that fit in total: Level
            2: 1,
            10: 2,
            28: 3,
            60: 4,
            110: 5,
            182: 6,
        }
        if self.level:
            return self.level

        return TOTAL_ELECTRONS_PER_LEVEL[
            next(x for x in list(TOTAL_ELECTRONS_PER_LEVEL.keys()) if x >= self.e)
        ]

    def orbitals_group(self):
        return VGroup(
            *[
                Circle(radius=1 + i, color=self.orbit_color)
                for i in range(self.occupied_levels)
            ]
        )

    def nuclei_groups(self):
        protons = [
            Dot(color=self.proton_color)
            .scale(2)
            .shift(np.random.uniform(-0.25, 0.25, 3))
            for i in range(self.p)
        ]
        neutrons = [
            Dot(color=self.neutron_color)
            .scale(2)
            .shift(np.random.uniform(-0.25, 0.25, 3))
            for i in range(self.n)
        ]
        nuclei = protons + neutrons
        random.shuffle(nuclei)

        return VGroup(*nuclei)

    def electrons_group(self):
        ELECTRONS_PER_LEVEL = {
            # Level: Electrons that fit in each level
            1: 2,
            2: 8,
            3: 18,
            4: 32,
            5: 50,
            6: 72,
        }
        level = self.calculate_levels()
        remaining_electrons = self.e
        electrons_group = VGroup()
        for level in ELECTRONS_PER_LEVEL:
            level_electrons = ELECTRONS_PER_LEVEL[level]
            if remaining_electrons > level_electrons:
                group = self.arrange_electrons(level_electrons, level)
            else:
                group = self.arrange_electrons(remaining_electrons, level)
                electrons_group.add(group)
                break

            remaining_electrons -= level_electrons
            electrons_group.add(group)

        return electrons_group

    def arrange_electrons(self, n_electrons, level):
        level_group = VGroup()
        for angle in np.arange(0, TAU, TAU / n_electrons):
            electron = Dot(color=self.electron_color).scale(2)
            electron.shift(level * RIGHT)
            electron.rotate(angle, about_point=[0, 0, 0])
            level_group.add(electron)

        return level_group

    def get_orbitals(self):
        return self[0]

    def get_electrons(self):
        return self[1]

    def get_nuclei(self):
        return self[2]

from manim import *
from manim.mobject.opengl.opengl_surface import OpenGLSurface
import random
import scipy.special as spe
from functools import wraps

# Useful classes


class BohrAtom(VGroup):
    """
    Hay que mirar una serie de cosas:
        1) Levels: n = 1, 2, 3, 4, 5, etc.
        2) Nucleo: Protones + Neutrones
        3) Electrones por level
        4) Poder decidir el tamaño del nucleo y la distancia entre niveles
        5) Poder elegir cuantos electrones se muestran
        6) Mostrar solo los niveles ocupados o elegir cuantos niveles se muestran
    """

    def __init__(
        self,
        e=14,  # Electrones
        p=14,  # Protones
        n=10,  # Neutrones
        level=None,  # Niveles
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


class OrbitalBase(OpenGLSurface):
    def add_background_rectangle_to_family_members_with_points(self):
        pass

    def __init__(
        self,
        center=ORIGIN,
        resolution=(100, 50),
        u_range=(0, PI),
        v_range=(0, TAU),
        n_value=1,
        l_value=0,
        m_value=0,
        size=1,
        **kwargs,
    ):
        self.n_value = n_value
        self.l_value = l_value
        self.m_value = m_value
        self.size = size

        super().__init__(
            self.uv_func,
            resolution=resolution,
            u_range=u_range,
            v_range=v_range,
            **kwargs,
        )

        self.shift(center)

    def psi_ang(self, phi, theta, l=0, m=0):
        sphHarm = spe.sph_harm(m, l, phi, theta)

        return sphHarm.real

    def calculate_coordinates(self, psi, u, v):
        x = np.sin(u) * np.cos(v) * abs(psi)
        y = np.sin(u) * np.sin(v) * abs(psi)
        z = np.cos(u) * abs(psi)

        return self.size * np.array([x, y, z])

    def uv_func(self, u, v):
        psi = self.psi_ang(v, u, l=self.l_value, m=self.m_value)

        return self.calculate_coordinates(psi, u, v)


class OrbitalPositive(OrbitalBase):
    def uv_func(self, u, v):
        psi = self.psi_ang(v, u, l=self.l_value, m=self.m_value)
        if psi < 0:
            psi = 0

        return self.calculate_coordinates(psi, u, v)


class OrbitalNegative(OrbitalBase):
    def uv_func(self, u, v):
        psi = self.psi_ang(v, u, l=self.l_value, m=self.m_value)
        if psi > 0:
            psi = 0

        return self.calculate_coordinates(psi, u, v)


class Orbital(OpenGLSurface):
    def __init__(self, n=None, l=0, m=0, size=3, **kwargs):
        super().__init__(self.uv_func, **kwargs)
        if not n:
            self.n = l + 1
        else:
            self.n = n
        self.l = l
        self.m = m
        self.size = size
        pos = OrbitalPositive(
            n_value=self.n, l_value=self.l, m_value=self.m, size=self.size
        ).set_color(RED)
        neg = OrbitalNegative(
            n_value=self.n, l_value=self.l, m_value=self.m, size=self.size
        ).set_color(BLUE)
        self.add(pos, neg)
        self.needs_new_bounding_box = True

    def uv_func(self, u, v):
        return np.array([0, 0, 0])


class EnergyLevel(VGroup):
    # TODO: Add electrons option (one or two per line, giving possibility of low or high spin, etc.)
    def __init__(self, index=None, level: str = "s", electrons: int = 1, **kwargs):
        super().__init__(**kwargs)
        self.index = index
        self.level = level
        self.electrons = electrons
        self.number_of_lines = {
            # level: number of lines
            "s": 1,
            "p": 3,
            "d": 5,
            "f": 7,
        }
        self.check_number_of_electrons()
        self.add(self.level_lines())
        self.add(self.level_index())

    def level_lines(self):
        lines = VGroup(
            *[
                Line(0.5 * LEFT, 0.5 * RIGHT)
                for i in range(self.number_of_lines[self.level])
            ]
        )

        return lines.arrange()

    def level_index(self):
        buff = 1
        if self.index:
            label = VGroup(
                *[
                    MathTex(str(self.index) + str(self.level))
                    for i in range(self.number_of_lines[self.level])
                ]
            )
            buff = 0.75
        else:
            label = VGroup(
                *[
                    MathTex(str(self.level))
                    for i in range(self.number_of_lines[self.level])
                ]
            )

        return label.arrange(buff=buff).shift(0.3 * DOWN)

    def check_number_of_electrons(self):
        if self.electrons > 2 * self.number_of_lines[self.level]:
            raise Exception(
                "You did something wrong, you can not have this much electrons at this level"
            )

    def get_level_lines(self):
        return self[0]

    def get_level_index(self):
        return self[1]


class Hole(VMobject):
    def __init__(self, radius=0.25, color=WHITE, **kwargs):
        super().__init__(**kwargs)
        self.add(DashedVMobject(Circle(radius=radius, color=color), num_dashes=7))


class Electron(VMobject):
    def __init__(self, radius=0.2, color=BLUE_E, **kwargs):
        super().__init__(**kwargs)
        self.add(Circle(radius=radius, fill_opacity=1, color=color))


class Element(VGroup):
    def __init__(
        self,
        element: str = "H",
        radius: float = 1,
        color: str = ORANGE,
        label_color: str = BLACK,
        n_electrons: int = 2,
        n_holes: int = 2,
        add_electrons: bool = True,
        add_holes: bool = True,
        subelectron_holes: bool = True,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.element_label = element
        self.label_color = label_color
        self.color = color
        self.radius = radius
        self.n_electrons = n_electrons
        self.n_holes = n_holes
        self.add_electrons = add_electrons
        self.add_holes = add_holes
        self.subelectron_holes = subelectron_holes
        self.electrons = self.get_electrons()
        self.holes = self.get_holes()
        self.particles = self.get_particles()
        self.atom = self.central_atom()
        self.add(self.atom.shift([0, 0, 0]))
        self.arrange_particles()
        self.subelectron_holes_group = self.make_subelectron_holes()
        if self.subelectron_holes:
            self.particles.add(self.subelectron_holes_group.shift([0, 0, 0]))
            self.add(self.subelectron_holes_group.shift([0, 0, 0]))

    def central_atom(self):
        label = Text(self.element_label)
        base_radius = 0.4 + max(label.width, label.height) / 2

        base_dot = LabeledDot(
            radius=base_radius,
            label=label,
            color=self.label_color,
            fill_color=self.color,
        )

        scale_ratio = self.radius / base_dot.radius
        return base_dot.scale(scale_ratio)

    def get_electrons(self):
        if self.add_electrons and self.n_electrons > 0:
            return VGroup(*[Electron() for i in range(self.n_electrons)])

        return None

    def get_holes(self):
        if self.add_holes and self.n_holes > 0:
            return VGroup(*[Hole() for i in range(self.n_holes)])

        return None

    def get_particles(self):
        particles = VGroup()
        if self.electrons:
            particles.add(*self.electrons.submobjects)

        if self.holes:
            particles.add(*self.holes.submobjects)

        return particles

    def arrange_particles(self):
        if len(self.particles) == 0:
            return self.particles
        self.add(self.particles.shift([0, 0, 0]))
        angles = np.arange(0, TAU, TAU / len(self.particles))

        for index, particle in enumerate(self.particles):
            particle.shift(self.radius * RIGHT + 1.2 * particle.width * RIGHT)
            particle.rotate(angles[index], about_point=self.atom.get_center())

    def make_subelectron_holes(self):
        if self.subelectron_holes:
            return VGroup(
                *[Hole().move_to(electron.get_center()) for electron in self.electrons]
            )

    def get_subelectron_holes(self):
        return self.subelectron_holes_group


class ElementFrame(VGroup):
    def __init__(
        self,
        element_symbol: str = "H",
        element_name: str = "Hidrógeno",
        frame_colors: list = [BLUE, BLUE_B],
        **kwargs,
    ):
        super().__init__(**kwargs)
        # Not the most elegant way to do this but good enought for the lightning

        self.frame = Rectangle(
            height=2, width=1.5, fill_opacity=1
        ).set_color_by_gradient(frame_colors)
        self.symbol = Text(element_symbol, color=BLACK).scale(1.5).shift(0.2 * UP)
        self.name = Text(element_name, color=BLACK).shift(0.75 * DOWN)

        name_rescaling_factor = 0.75 * self.frame.width / self.name.width

        self.name.scale(name_rescaling_factor)
        self.add(self.frame, self.symbol, self.name)


class NPNTransistor(VGroup):
    def __init__(self, regions_opacity=0.8, **kwargs):
        super().__init__(**kwargs)
        self.regions_opacity = regions_opacity
        self.left_n_region = Rectangle(
            color=BLUE, fill_opacity=self.regions_opacity, width=3
        ).shift(2 * LEFT)
        self.right_n_region = Rectangle(
            color=BLUE, fill_opacity=self.regions_opacity, width=3
        ).shift(2 * RIGHT)
        self.p_region = Rectangle(color=RED, fill_opacity=self.regions_opacity, width=1)
        self.left_electrons = self.make_particles(Electron).move_to(
            self.left_n_region.get_center()
        )
        self.right_electrons = self.make_particles(Electron).move_to(
            self.right_n_region.get_center()
        )
        self.holes = self.make_particles(
            Hole, n_copies=2, horizontal_boundary=[0.32 * LEFT, 0.32 * RIGHT]
        )

        self.add(
            self.left_n_region,
            self.right_n_region,
            self.p_region,
            self.left_electrons,
            self.right_electrons,
            self.holes,
        )

    def make_particles(
        self,
        particle_type,
        n_copies=5,
        vertical_boundary=[0.8 * UP, 0.8 * DOWN],
        horizontal_boundary=[LEFT, RIGHT],
    ):
        particles = VGroup(*[particle_type().scale(0.5) for i in range(5)])
        particles = arrange_copies_in_rectangle(
            particles, n_copies, vertical_boundary, horizontal_boundary
        )
        return particles


class BatterySchema(VGroup):
    # TODO: This is not working as intended, rebuild this.
    def __init__(
        self, mob=Square(), schema_type="horizontal", inverted_terminals=False, **kwargs
    ):
        super().__init__(**kwargs)

        self.mob = mob
        self.schema_type = schema_type
        self.schema = self.select_schema()
        self.inverted_terminals = inverted_terminals
        if self.inverted_terminals:
            self.invert_terminals()

        self.add(self.schema)

    def get_start_finish_positions(self):
        options_dict = {
            "horizontal": [self.mob.get_left(), self.mob.get_right()],
            "corner": [self.mob.get_left(), self.mob.get_top()],
        }

        return options_dict[self.schema_type]

    def horizontal_schema(self):
        if self.schema_type != "horizontal":
            pass
        schema_start, schema_end = self.get_start_finish_positions()

        schema = VGroup()

        # Left side
        starting_line = Line(schema_start, schema_start + 0.2 * LEFT)
        left_line = Line(starting_line.get_left(), starting_line.get_left() + 3 * DOWN)
        left_bottom_line = Line(
            left_line.get_bottom(),
            left_line.get_bottom() + 0.45 * self.mob.width * RIGHT,
        )

        self.left_side = VGroup(starting_line, left_line, left_bottom_line)

        # Right side
        ending_line = Line(schema_end, schema_end + 0.2 * RIGHT)
        right_line = Line(ending_line.get_right(), ending_line.get_right() + 3 * DOWN)
        right_bottom_line = Line(
            right_line.get_bottom(),
            right_line.get_bottom() + 0.45 * self.mob.width * LEFT,
        )

        self.right_side = VGroup(ending_line, right_line, right_bottom_line)

        # Terminals
        positive_terminal = Line(
            left_bottom_line.get_right() + 0.5 * LEFT,
            left_bottom_line.get_right() + 0.5 * RIGHT,
        ).rotate(PI / 2)
        positive_symbol = MathTex("+").next_to(positive_terminal, UP, buff=0.5)
        self.plus_terminal = VGroup(positive_terminal, positive_symbol)

        negative_terminal = Line(
            right_bottom_line.get_left() + 0.25 * LEFT,
            right_bottom_line.get_left() + 0.25 * RIGHT,
        ).rotate(PI / 2)
        negative_symbol = MathTex("-").next_to(negative_terminal, UP, buff=0.9)
        self.minus_terminal = VGroup(negative_terminal, negative_symbol)

        schema.add(
            self.left_side, self.right_side, self.plus_terminal, self.minus_terminal
        )

        return schema

    def corner_schema(self):
        if self.schema_type != "corner":
            pass
        schema_start, schema_end = self.get_start_finish_positions()

        schema = VGroup()

        # Left side
        starting_line = Line(schema_start, schema_start + 0.2 * LEFT)
        left_line = Line(
            starting_line.get_left(),
            starting_line.get_left() + (self.mob.height / 2 + 1) * UP,
        )
        left_top_line = Line(
            left_line.get_top(), left_line.get_top() + 0.2 * self.mob.width * RIGHT
        )

        self.l_side = VGroup(starting_line, left_line, left_top_line)

        # Top side
        ending_line = Line(schema_end, schema_end + UP)
        top_line = Line(
            ending_line.get_top(), ending_line.get_top() + 0.2 * self.mob.width * LEFT
        )

        self.top_side = VGroup(ending_line, top_line)

        # Terminals
        positive_terminal = Line(
            left_top_line.get_right() + 0.5 * LEFT,
            left_top_line.get_right() + 0.5 * RIGHT,
        ).rotate(PI / 2)
        positive_symbol = MathTex("+").next_to(positive_terminal, UP, buff=0.5)
        self.plus_terminal = VGroup(positive_terminal, positive_symbol)

        negative_terminal = Line(
            top_line.get_left() + 0.25 * LEFT, top_line.get_left() + 0.25 * RIGHT
        ).rotate(PI / 2)
        negative_symbol = MathTex("-").next_to(negative_terminal, UP, buff=0.9)
        self.minus_terminal = VGroup(negative_terminal, negative_symbol)

        schema.add(self.l_side, self.top_side, self.plus_terminal, self.minus_terminal)

        return schema

    def select_schema(self):
        schema_options = {
            "horizontal": self.horizontal_schema(),
            "corner": self.corner_schema(),
        }

        selected_schema = schema_options[self.schema_type]
        return selected_schema

    def invert_terminals(self):
        terminals = VGroup(self.plus_terminal, self.minus_terminal)

        terminals.rotate(PI, UP, terminals.get_center())

        return self


class MOSFETTransistor(VGroup):
    def __init__(self, show_holes=False, show_battery=False, **kwargs):
        super().__init__(**kwargs)

        self.main_board = self.make_main_board()
        self.left_n_side = self.make_n_region(side=LEFT)
        self.right_n_side = self.make_n_region(side=RIGHT)
        self.show_holes = show_holes
        self.show_battery = show_battery
        self.holes = self.add_holes()
        self.terminals = self.add_battery_terminals()
        self.negative_terminal = self.terminals[0]
        self.positive_terminal = self.terminals[1]
        self.battery_elbows = self.add_battery_sides()
        self.negative_elbow = self.battery_elbows[0]
        self.positive_elbow = self.battery_elbows[1]
        self.battery = self.add_battery()

        self.add(
            self.battery,
            self.main_board,
            self.holes,
            self.left_n_side,
            self.right_n_side,
        )

    def make_main_board(self):
        return Rectangle(fill_opacity=0.8).set_color(RED).scale(2)

    def make_n_region(self, side=LEFT):
        region = (
            Rectangle(fill_opacity=1)
            .set_color(BLUE)
            .scale(0.5)
            .move_to(self.main_board.get_top())
            .shift(2 * side + 0.5 * DOWN)
        )

        return region

    def add_holes(self):
        if not self.show_holes:
            return VGroup()
        holes = VGroup(*[Hole().scale(0.5) for i in range(4)])

        holes = arrange_copies_in_rectangle(
            holes,
            7,
            vertical_boundary=[1.8 * UP, 1.8 * DOWN],
            horizontal_boundary=[3.5 * LEFT, 3.5 * RIGHT],
        )

        return holes

    def add_battery_terminals(self):
        negative_terminal = (
            Line(0.25 * UP, 0.25 * DOWN)
            .next_to(self.main_board, UP, buff=1.25)
            .shift(0.25 * LEFT)
        )
        positive_terminal = (
            Line(0.5 * UP, 0.5 * DOWN)
            .next_to(self.main_board, UP, buff=1)
            .shift(0.25 * RIGHT)
        )

        return VGroup(negative_terminal, positive_terminal)

    def add_battery_sides(self):
        negative_elbow = BatterySide(self.negative_terminal, self.left_n_side)
        positive_elbow = BatterySide(self.positive_terminal, self.right_n_side)

        return VGroup(negative_elbow, positive_elbow)

    def add_battery(self):
        if not self.show_battery:
            return VGroup()

        return VGroup(
            self.negative_terminal,
            self.positive_terminal,
            self.negative_elbow,
            self.positive_elbow,
        )


class BatterySide(VMobject):
    def __init__(self, terminal, anchor, **kwargs):
        super().__init__(**kwargs)
        self.terminal = terminal
        self.anchor = anchor
        self.make_points()

    def make_points(self):
        terminal_points = self.terminal.get_center()
        anchor_points = self.anchor.get_top() + [0, -0.2, 0]
        intermediate_point = [anchor_points[0], terminal_points[1], 0]

        return self.set_points_as_corners(
            [terminal_points, intermediate_point, anchor_points]
        )


# Useful functions


def arrange_in_1D_boundary(mobs, boundary=[LEFT, RIGHT]):
    divisions = len(mobs)
    positions = np.linspace(boundary[0], boundary[1], divisions)

    for index, mob in enumerate(mobs):
        mob.move_to(positions[index])


def duplicate_and_rearrange(mobs, boundary=[LEFT, RIGHT]):
    if isinstance(mobs, VGroup):
        group = VGroup(*mobs.copy().submobjects, *mobs.copy().submobjects)
    else:
        group = VGroup(mobs, mobs)
    arrange_in_1D_boundary(group, boundary)
    return group


def add_over_rectangular_surface(mobtype=Dot(), amount=10, height=5, width=5):
    group = VGroup()
    for i in range(amount):
        group.add(
            mobtype.copy().shift(
                [
                    np.random.randint(-50 * width, 50 * width) / 100,
                    np.random.randint(-50 * height, 50 * height) / 100,
                    0,
                ]
            )
        )

    return group


def get_element_by_data(element: dict):
    return Element(
        element=element["symbol"],
        color=element["color"],
        n_electrons=element["electrons"],
        n_holes=element["holes"],
    )


def randomly_distributed_in_2D(mobs, left=1, right=1, down=1, up=1):
    n_mobs = len(mobs)
    horizontal = np.random.uniform(-left, right, n_mobs)
    vertical = np.random.uniform(up, -down, n_mobs)

    for index, mob in enumerate(mobs):
        mob.shift([horizontal[index], vertical[index], 0])

    return mobs


def arrange_copies_in_rectangle(
    mobs, n_copies=2, vertical_boundary=[UP, DOWN], horizontal_boundary=[LEFT, RIGHT]
):
    arrange_in_1D_boundary(mobs, vertical_boundary)
    copies_group = VGroup(mobs)
    for i in range(n_copies):
        copies_group.add(mobs.copy())

    arrange_in_1D_boundary(copies_group, horizontal_boundary)

    return copies_group


def make_subpaths(group):
    for mob in group:
        group.add_subpath(mob.get_points())

    return group


def zero(function):
    @wraps(function)
    def wrapper(t, *args, **kwargs):
        if 0 <= t <= 1:
            return function(t, *args, **kwargs)
        else:
            return 0

    return wrapper


@zero
def inverse_smooth(t: float, inflection: float = 10.0):
    new_t = 1 - t
    return smooth(new_t, inflection)


@zero
def inverse_linear(t: float, inflection: float = 10.0):
    return 1 - t


def concat_mobjects(mobject, concats, buff=0):
    group = VGroup(mobject.copy())
    sides = {0: RIGHT, 1: LEFT}
    for i in range(concats):
        side = sides[i % 2]
        concat_mobject = mobject.copy().next_to(group, side, buff=buff)
        group.add(concat_mobject)

    return group

from manim import (
    VGroup,
    WHITE,
    BLACK,
    BLUE,
    Rectangle,
    color_gradient,
    Text,
    Tex,
    RIGHT,
    ORIGIN,
    DOWN,
)
import pandas as pd
import numpy as np


class MElementObject(VGroup):
    def __init__(
        self,
        atomic_number=1,
        atomic_mass=1,
        element_name="Hydrogen",
        element_symbol="H",
        coloring=BLACK,
        fill_colors=(WHITE, BLUE),
        gradient=10,
        opacity=1,
        text_color=BLACK,
        **kwargs,
    ):
        VGroup.__init__(self, **kwargs)
        self.atomic_number = atomic_number
        self.atomic_mass = atomic_mass
        self.element_name = element_name
        self.element_symbol = element_symbol
        self.coloring = coloring
        self.fill_colors = fill_colors
        self.gradient = gradient
        self.opacity = opacity
        self.text_color = text_color

        element_frame = self.create_frame_with_text()

        self.add(element_frame)

    def frame_name_width_ratio(self, frame, name_text):
        return frame.get_width() / (1.25 * name_text.get_width())

    def max_height_ratio(self, name_text):
        text_height = name_text.get_height()
        if text_height > 0.3:
            ratio = 0.3 / text_height
            name_text.scale(ratio)

        return name_text

    def create_frame_base(self):
        frame_rectangle = (
            Rectangle(
                height=2.8,
                width=2,
                color=self.coloring,
                stroke_width=0.2,
                fill_opacity=self.opacity,
            )
            .scale(0.8)
            .set_fill(color_gradient(self.fill_colors, self.gradient))
        )

        return frame_rectangle

    def create_frame_with_text(self):
        frame_rectangle = self.create_frame_base()
        symbol_text = (
            Text(self.element_symbol, color=self.text_color)
            .scale(1.1)
            .move_to(frame_rectangle.get_center())
        )
        name_text = (
            Text(self.element_name, color=self.text_color)
            .scale(0.2)
            .next_to(frame_rectangle, DOWN, buff=-0.4)
        )
        atomic_number_text = (
            Tex(str(self.atomic_number), color=self.text_color)
            .scale(0.65)
            .next_to(
                frame_rectangle,
                frame_rectangle.get_top() + frame_rectangle.get_left(),
                buff=-0.35,
            )
        )

        ratio = self.frame_name_width_ratio(frame=frame_rectangle, name_text=name_text)
        name_text.scale(ratio)
        name_text = self.max_height_ratio(name_text)

        shifting_ammount = 0
        if 10 <= self.atomic_number:
            shifting_ammount += 0.15

        if self.atomic_number > 100:
            shifting_ammount += 0.15

        atomic_number_text.shift(shifting_ammount * RIGHT)

        return VGroup(frame_rectangle, symbol_text, name_text, atomic_number_text)

    def from_csv_file_data(filename, atomic_number, **kwargs):
        # TODO: Add option to set manually colors.
        # TODO: Create a table that adds this data in a prettier way.
        df = pd.read_csv(filename)
        element = df.loc[df["AtomicNumber"] == atomic_number].squeeze().to_dict()

        return MElementObject(
            atomic_number=atomic_number,
            atomic_mass=element.get("AtomicMass"),
            element_name=element.get("Name"),
            element_symbol=element.get("Symbol"),
            fill_colors=[element.get("Color"), WHITE],
        )


class PeriodicTable(VGroup):
    # TODO Change to english database
    def __init__(self, data_file, *vmobjects, **kwargs):
        VGroup.__init__(self, *vmobjects, **kwargs)
        self.data_file = data_file
        self.table = self.add_elements()

        self.add(self.table)

    def add_elements(self):
        positions = self.elements_position_dict()
        base_element = MElementObject()
        mult_array = np.array([base_element.get_width(), -base_element.get_height(), 0])

        table = VGroup()
        for element, position in positions.items():
            new_position = np.multiply(mult_array, np.array(position))
            new_element = MElementObject.from_csv_file_data(
                self.data_file, element
            ).move_to(new_position)

            table.add(new_element)

        table.move_to(ORIGIN).scale(0.25)
        return table

    def elements_position_dict(self):
        # TODO: Think of a better way of doing this. However, it works and looks good
        positions = {
            1: [0, 0, 0],
            2: [17, 0, 0],
            3: [0, 1, 0],
            4: [1, 1, 0],
            5: [12, 1, 0],
            6: [13, 1, 0],
            7: [14, 1, 0],
            8: [15, 1, 0],
            9: [16, 1, 0],
            10: [17, 1, 0],
            11: [0, 2, 0],
            12: [1, 2, 0],
            13: [12, 2, 0],
            14: [13, 2, 0],
            15: [14, 2, 0],
            16: [15, 2, 0],
            17: [16, 2, 0],
            18: [17, 2, 0],
            19: [0, 3, 0],
            20: [1, 3, 0],
            21: [2, 3, 0],
            22: [3, 3, 0],
            23: [4, 3, 0],
            24: [5, 3, 0],
            25: [6, 3, 0],
            26: [7, 3, 0],
            27: [8, 3, 0],
            28: [9, 3, 0],
            29: [10, 3, 0],
            30: [11, 3, 0],
            31: [12, 3, 0],
            32: [13, 3, 0],
            33: [14, 3, 0],
            34: [15, 3, 0],
            35: [16, 3, 0],
            36: [17, 3, 0],
            37: [0, 4, 0],
            38: [1, 4, 0],
            39: [2, 4, 0],
            40: [3, 4, 0],
            41: [4, 4, 0],
            42: [5, 4, 0],
            43: [6, 4, 0],
            44: [7, 4, 0],
            45: [8, 4, 0],
            46: [9, 4, 0],
            47: [10, 4, 0],
            48: [11, 4, 0],
            49: [12, 4, 0],
            50: [13, 4, 0],
            51: [14, 4, 0],
            52: [15, 4, 0],
            53: [16, 4, 0],
            54: [17, 4, 0],
            55: [0, 5, 0],
            56: [1, 5, 0],
            57: [2, 7.5, 0],
            58: [3, 7.5, 0],
            59: [4, 7.5, 0],
            60: [5, 7.5, 0],
            61: [6, 7.5, 0],
            62: [7, 7.5, 0],
            63: [8, 7.5, 0],
            64: [9, 7.5, 0],
            65: [10, 7.5, 0],
            66: [11, 7.5, 0],
            67: [12, 7.5, 0],
            68: [13, 7.5, 0],
            69: [14, 7.5, 0],
            70: [15, 7.5, 0],
            71: [2, 5, 0],
            72: [3, 5, 0],
            73: [4, 5, 0],
            74: [5, 5, 0],
            75: [6, 5, 0],
            76: [7, 5, 0],
            77: [8, 5, 0],
            78: [9, 5, 0],
            79: [10, 5, 0],
            80: [11, 5, 0],
            81: [12, 5, 0],
            82: [13, 5, 0],
            83: [14, 5, 0],
            84: [15, 5, 0],
            85: [16, 5, 0],
            86: [17, 5, 0],
            87: [0, 6, 0],
            88: [1, 6, 0],
            89: [2, 8.5, 0],
            90: [3, 8.5, 0],
            91: [4, 8.5, 0],
            92: [5, 8.5, 0],
            93: [6, 8.5, 0],
            94: [7, 8.5, 0],
            95: [8, 8.5, 0],
            96: [9, 8.5, 0],
            97: [10, 8.5, 0],
            98: [11, 8.5, 0],
            99: [12, 8.5, 0],
            100: [13, 8.5, 0],
            101: [14, 8.5, 0],
            102: [15, 8.5, 0],
            103: [2, 6, 0],
            104: [3, 6, 0],
            105: [4, 6, 0],
            106: [5, 6, 0],
            107: [6, 6, 0],
            108: [7, 6, 0],
            109: [8, 6, 0],
            110: [9, 6, 0],
            111: [10, 6, 0],
            112: [11, 6, 0],
            113: [12, 6, 0],
            114: [13, 6, 0],
            115: [14, 6, 0],
            116: [15, 6, 0],
            117: [16, 6, 0],
            118: [17, 6, 0],
        }
        return positions

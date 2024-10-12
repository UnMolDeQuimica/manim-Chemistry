import re

from manim import *


class ChemicalFormula(MarkupText):
    """
    Mostly usefull for simple compounds like binary salts or oxoanions.
    """

    def __init__(
        self,
        formula: str,
        metal_color: str = WHITE,
        non_metal_color: str = WHITE,
        oxygen_color: str = WHITE,
        *args,
        **kwargs,
    ):
        self.formula = formula
        self.metal_color = metal_color
        self.non_metal_color = non_metal_color
        self.oxygen_color = oxygen_color
        self.parsed_formula = self.parse_formula(self.formula)
        markup = self.make_markup(
            parsed_formula=self.parsed_formula,
            metal_color=self.metal_color,
            non_metal_color=self.non_metal_color,
            oxygen_color=self.oxygen_color,
        )

        super().__init__(markup, *args, **kwargs)

    def parse_formula(self, formula: str):
        FORMULA_PATTERN = r"([A-Z][a-z]*)(\d*)"
        elements = re.findall(FORMULA_PATTERN, formula)
        parsed_formula = {}
        for element, count in elements:
            count = int(count) if count else 1
            parsed_formula[element] = count

        return parsed_formula

    def make_markup(
        self,
        parsed_formula,
        metal_color: str = WHITE,
        non_metal_color: str = WHITE,
        oxygen_color: str = WHITE,
    ):
        parsed_list = enumerate(list(parsed_formula))
        markup = ""

        for index, atom in parsed_list:
            if atom == "O":
                markup += self.set_atom_color(atom, parsed_formula[atom], oxygen_color)
            elif index == 0:
                markup += self.set_atom_color(atom, parsed_formula[atom], metal_color)
            elif index == 1:
                markup += self.set_atom_color(
                    atom, parsed_formula[atom], non_metal_color
                )

        return markup

    def set_atom_color(self, atom, subindex, color):
        colored_atom = f"<span fgcolor='{color}'>{atom}"

        if subindex > 1:
            colored_atom += f"<sub>{str(subindex)}</sub>"

        colored_atom += "</span>"

        return colored_atom


class NamedFormula(VGroup):
    def __init__(
        self,
        metal_name: str,
        non_metal_name: str,
        formula: str,
        metal_color: str = WHITE,
        non_metal_color: str = WHITE,
        oxygen_color: str = WHITE,
        font: str = "",
        spanish_structure=False,
        buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER,
        direction=DOWN,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.metal_name = metal_name
        self.non_metal_name = non_metal_name
        self.formula = formula
        self.metal_color = metal_color
        self.non_metal_color = non_metal_color
        self.oxygen_color = oxygen_color
        self.spanish_structure = spanish_structure
        self.font = font
        chemical_formula = ChemicalFormula(
            formula=self.formula,
            metal_color=self.metal_color,
            non_metal_color=self.non_metal_color,
            oxygen_color=self.oxygen_color,
            *args,
            **kwargs,
        )
        self.add(chemical_formula)
        self.name = self.make_name().next_to(
            chemical_formula, direction=direction, buff=buff
        )
        self.add(self.name)

    def make_name(self):
        """
        Not all languages use the same naming structure.
        For example, in english NaCl is Sodium (Na) Chloride (Cl)
        while in spanish it is Cloruro (Cl) Sódico (Na). Reimplement it
        as you need.
        """

        metal_text = None
        non_metal_text = None

        if self.metal_name:
            metal_text = f"<span fgcolor='{self.metal_color}'>{self.metal_name}</span>"

        if self.non_metal_name:
            non_metal_text = (
                f"<span fgcolor='{self.non_metal_color}'>{self.non_metal_name}</span>"
            )

        if self.spanish_structure:
            return MarkupText(
                " ".join(filter(None, [non_metal_text, metal_text])), font=self.font
            )

        return MarkupText(
            " ".join(filter(None, [metal_text, non_metal_text])), font=self.font
        )


class ComplexFormula(MarkupText):
    """
    Allows the creation of more complex molecular formulas
    using a dictionary. The key is the string to be written
    and the value is a color.
    """

    def __init__(self, formula_dict: dict, *args, **kwargs):
        markup = ""
        for formula, color in formula_dict.items():
            markup += (
                f"<span fgcolor='{color}'>{self.make_formula_structure(formula)}</span>"
            )

        super().__init__(markup, *args, **kwargs)

    def add_tags_around_numbers(self, formula_part):
        pattern = r"([^\d\s]+)(\d+)"
        replacement = r"\1<sub>\2</sub>"
        result = re.sub(pattern, replacement, formula_part)
        return result

    def add_tags_around_charges(self, formula_part):
        pattern = re.compile(r"(\w*?)\^\{([^}]+)\}")
        substitution = r"\1<sup>\2</sup>"
        result_string = re.sub(pattern, substitution, formula_part)

        return result_string

    def make_formula_structure(self, formula_part):
        result = self.add_tags_around_numbers(formula_part)
        result = self.add_tags_around_charges(result)

        return result


class NamedComplexFormula(VGroup):
    """
    Complex formula build with two dicts.
    """

    def __init__(
        self,
        name_dict: dict,
        formula_dict: dict,
        direction=DOWN,
        buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER,
        *args,
        **kwargs,
    ):
        self.name_dict = name_dict
        self.formula_dict = formula_dict
        super().__init__(*args, **kwargs)

        complex_formula = ComplexFormula(formula_dict)
        self.add(complex_formula)
        name = MarkupText(self.build_name()).next_to(complex_formula, direction, buff)

        self.add(name)

    def build_name(self):
        markup = ""
        for name, color in self.name_dict.items():
            markup += f"<span fgcolor='{color}'>{name} </span>"

        return markup

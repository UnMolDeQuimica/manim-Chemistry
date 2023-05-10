from manim import VGroup, VDict, MarkupText, RIGHT, RED, GREEN, ORIGIN
from typing import Dict, Any
from .atom import MAtomObject
from .bond import *
from ..utils import mol_parser


class MMoleculeObject(VGroup):
    def __init__(
        self,
        atoms_dict: dict,
        bonds_dict: dict,
        representation_type: str or None = None,
        explicit_carbons: bool = False,
        explicit_hydrogens: bool = False,
        planar: bool = True,
        add_atoms_numbering: bool = False,
        add_bonds_numbering: bool = False,
        rotate_bonds: list = [],
        **kwargs,
    ):
        VGroup.__init__(self, **kwargs)
        self.atoms_dict = atoms_dict
        self.bonds_dict = bonds_dict
        self.representation_type = representation_type
        self.explicit_carbons = explicit_carbons
        self.explicit_hydrogens = explicit_hydrogens
        self.planar = planar
        self.atoms, self.atoms_by_index = self.get_atoms()
        self.bonds = self.get_bonds()
        self.add(self.atoms, self.bonds)
        if add_atoms_numbering:
            self.add_atom_numbering()
        if add_bonds_numbering:
            self.add_bond_numbering()
        self.rotate_bond(rotate_bonds)
        self.complete_missing_hydrogens()
        self.move_to(ORIGIN)

    def get_atoms(self):
        atoms = VDict()
        atoms_by_index = {}
        for index, atom in self.atoms_dict.items():
            matom = MAtomObject(
                coords=atom["coords"],
                element=atom["element"],
                explicit_carbons=self.explicit_carbons,
                explicit_hydrogens=self.explicit_hydrogens,
                representation_type=self.representation_type,
                planar=self.planar,
                bond_to=atom.get("bond_to"),
                index=index,
            )
            atoms.add([(index, matom)])
            atoms_by_index[index] = matom

        return atoms, atoms_by_index

    def get_bonds(self):
        bonds = VGroup()
        bond_index = 0
        for index, bond_list in self.bonds_dict.items():
            for bond in bond_list:
                # TODO: Add logic to check type of bond
                from_atom = self.atoms_by_index.get(index)
                to_atom = self.atoms_by_index.get(bond.get("to"))
                if from_atom.element == "H" or to_atom.element == "H":
                    stereo = bond.get("stereo")
                    if stereo:
                        if int(stereo) == 1 or int(stereo) == 4:
                            self.atoms[
                                from_atom.index
                            ] = from_atom.copy_with_explicit_hydrogens()
                            self.atoms[
                                to_atom.index
                            ] = to_atom.copy_with_explicit_hydrogens()
                            from_atom = self.atoms[from_atom.index]
                            to_atom = self.atoms[to_atom.index]
                            new_bond = PlainCramBond(
                                from_atom=from_atom,
                                to_atom=to_atom,
                                index=bond_index,
                                type=bond_type,
                            )

                            bond_index += 1
                            bonds.add(new_bond)

                        elif int(stereo) == 6:
                            self.atoms[
                                from_atom.index
                            ] = from_atom.copy_with_explicit_hydrogens()
                            self.atoms[
                                to_atom.index
                            ] = to_atom.copy_with_explicit_hydrogens()
                            from_atom = self.atoms[from_atom.index]
                            to_atom = self.atoms[to_atom.index]
                            new_bond = DashedCramBond(
                                from_atom=from_atom,
                                to_atom=to_atom,
                                index=bond_index,
                                type=bond_type,
                            )

                            bond_index += 1
                            bonds.add(new_bond)

                        else:
                            continue

                    elif (not from_atom.explicit_hydrogens) and (
                        not to_atom.explicit_hydrogens
                    ):
                        continue

                else:
                    bond_type = int(bond.get("type"))
                    if bond_type == 2 or bond_type == 5 or bond_type == 7:
                        new_bond = DoubleBond(  # TODO: Add function inside bond to create it from data
                            from_atom=from_atom,
                            to_atom=to_atom,
                            index=bond_index,
                            type=bond_type,
                        )
                    elif bond_type == 3:
                        new_bond = TripleBond(
                            from_atom=from_atom,
                            to_atom=to_atom,
                            index=bond_index,
                            type=bond_type,
                        )
                    else:
                        if bond.get("stereo"):
                            if int(bond.get("stereo")) == 1:
                                new_bond = PlainCramBond(
                                    from_atom=from_atom,
                                    to_atom=to_atom,
                                    index=bond_index,
                                    type=bond_type,
                                )

                            else:
                                new_bond = DashedCramBond(
                                    from_atom=from_atom,
                                    to_atom=to_atom,
                                    index=bond_index,
                                    type=bond_type,
                                )
                        else:
                            new_bond = SimpleBond(
                                from_atom=from_atom,
                                to_atom=to_atom,
                                index=bond_index,
                                type=bond_type,
                            )
                    bond_index += 1
                    bonds.add(new_bond)
        return bonds

    def add_atom_numbering(self):
        numbering = VGroup()
        for atom in self.atoms:
            if not self.explicit_hydrogens:
                if atom.element != "H":
                    numbering.add(
                        MarkupText(str(atom.index))
                        .scale(0.5)
                        .move_to(atom.coords + 0.5 * RIGHT)
                        .set_color(RED)
                    )
            else:
                numbering.add(
                    MarkupText(str(atom.index))
                    .scale(0.5)
                    .move_to(atom.coords + 0.5 * RIGHT)
                    .set_color(RED)
                )

        self.add(numbering)

    def add_bond_numbering(self):
        numbering = VGroup()
        for bond in self.bonds:
            if (
                not bond.from_atom.explicit_hydrogens
                and not bond.to_atom.explicit_hydrogens
            ):
                if bond.from_atom.element != "H" and bond.to_atom.element != "H":
                    numbering.add(
                        MarkupText(str(bond.index))
                        .set_color(GREEN)
                        .move_to(bond.get_center())
                        .scale(0.5)
                    )

        self.add(numbering)

    def rotate_bond(self, rotate_bonds):
        for bond in rotate_bonds:
            direction = self.bonds[bond][0][0].end - self.bonds[bond][0][0].start
            self.bonds[bond].rotate(
                PI, about_point=self.bonds[bond][0][0].get_center(), axis=direction
            )

    def complete_missing_hydrogens(self):
        supported_atoms = ["O", "S", "N", "P"]

        for atom in self.atoms:
            if atom.element not in supported_atoms:
                continue

            total_bonds = len(atom.bond_to)
            bonds_direction = 0
            if not atom.bonds_fulfilled():
                minimum_bonds = {"O": 2, "S": 2, "N": 3, "P": 3}
                for bond in self.bonds:
                    if bond.atom_is_in_bond(atom) and 0 < bond.type <= 4:
                        total_bonds += bond.type - 1
                        bonds_direction += (
                            bond.to_atom.coords[0] - bond.from_atom.coords[0]
                        )

                if total_bonds < minimum_bonds.get(atom.element):
                    needed_hydrogens = minimum_bonds.get(atom.element) - total_bonds
                    if bonds_direction < 0:
                        if needed_hydrogens > 1:
                            self.atoms[atom.index] = atom.rename_atom(
                                f"H<sub>{needed_hydrogens}</sub>" + atom.element,
                                bonds_direction,
                            )
                        else:
                            self.atoms[atom.index] = atom.rename_atom(
                                "H" + atom.element, bonds_direction
                            )
                    else:
                        if needed_hydrogens > 1:
                            self.atoms[atom.index] = atom.rename_atom(
                                atom.element + f"H<sub>{needed_hydrogens}</sub>",
                                bonds_direction,
                            )
                        else:
                            self.atoms[atom.index] = atom.rename_atom(
                                atom.element + "H", bonds_direction
                            )

    def from_mol_file(filename, *args, **kwargs):
        atoms, bonds = mol_parser(filename)
        return MMoleculeObject(atoms, bonds, *args, **kwargs)

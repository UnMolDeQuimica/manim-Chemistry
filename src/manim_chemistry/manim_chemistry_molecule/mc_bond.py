from typing import Dict, Optional

BOND_TYPES = {
    1: "simple",
    2: "double",
    3: "triple",
}

STEREO_TYPES = {
    1: "plain_cram",
    2: "dash_cram",
}


class MCBond:
    """
    MCBond: Abstraction of a bond in a molecule: Type of bond, from and to atoms.
    """

    def __init__(
        self,
        bond_type: int,
        from_atom=None,
        to_atom=None,
        stereo: Optional[int] = None,
        molecule_index: Optional[int] = None,
        topology: Optional[int] = None,
        reacting_center_status: Optional[int] = None,
    ):
        self.bond_type = bond_type
        self.from_atom = from_atom
        self.to_atom = to_atom
        self.stereo = stereo
        self.molecule_index = molecule_index
        self.topology = topology
        self.reacting_center_status = reacting_center_status

    def assign_from_atom(self, from_atom):
        self.from_atom = from_atom

    def assign_to_atom(self, to_atom):
        self.to_atom = to_atom

    def assign_stereo(self, stereo):
        self.stereo = stereo

    @staticmethod
    def construct_from_bond_dict(bond_index, bond_data_dict: Dict, molecule):
        """
        Given a bond data dict from a parser, returns an MCBond

        Args:
            atom_dict (Dict): See data_parser function from BaseParser
            molecule: MCMolecule: Required to get the atoms by their index and
            create the MCBond using MCAtoms.

        Output:
            MCBond
        """

        if not isinstance(bond_data_dict, dict):
            raise Exception(f"Expected {dict} but received {bond_data_dict}")

        bond_type = bond_data_dict.get("bond_type", None)

        if not bond_type:
            raise Exception(
                f"Bond with index {bond_index} does not contain bond type data. Bond data: {bond_data_dict}"
            )

        try:
            from_atom_index = bond_data_dict.get("from_atom_index", None)
            from_mc_atom = molecule.atoms_by_index[from_atom_index]

            to_atom_index = bond_data_dict.get("to_atom_index", None)
            to_mc_atom = molecule.atoms_by_index[to_atom_index]

        except Exception as error:
            raise Exception(
                f"Bond dict {bond_data_dict} does not contain the expected data for molecule {molecule}. Error: {error}"
            )

        return MCBond(
            bond_type=bond_type,
            from_atom=from_mc_atom,
            to_atom=to_mc_atom,
            molecule_index=bond_index,
            stereo=bond_data_dict.get("stereo"),
            topology=bond_data_dict.get("topology"),
            reacting_center_status=bond_data_dict.get("reacting_center_status"),
        )

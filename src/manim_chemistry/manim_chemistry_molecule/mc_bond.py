
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

    def __init__(self, bond_type: int, from_atom=None, to_atom=None, stereo: int | None = None):
        self.bond_type = bond_type
        self.from_atom = from_atom,
        self.to_atom = to_atom,
        self.stereo = stereo

    def assign_from_atom(self, from_atom):
        self.from_atom = from_atom

    def assign_to_atom(self, to_atom):
        self.to_atom = to_atom

    def assign_stereo(self, stereo):
        self.stereo = stereo

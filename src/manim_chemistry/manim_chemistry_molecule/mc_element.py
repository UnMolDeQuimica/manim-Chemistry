from dataclasses import dataclass
from typing import Optional


@dataclass
class MCElement:
    """Used to abstract the properties of elements.

    The properties can be overwritten using custom MCElements and
    passing them as a dictionary to the molecule classes.

    Example
    ---------
    .. manim:: OverwrittenCarbonElement
        :save_last_frame:
        from manim_chemistry import *

        class OverwrittenCarbonElement(Scene):
            def construct(self):
                custom_carbon_element = MCElement(symbol="C", color=PURPLE)
                elements_data_dict = {"C": custom_carbon_element}
                molecule = GraphMolecule.molecule_from_pubchem(name="acetone", elements_data_dict=elements_data_dict)
                self.add(molecule)
    """

    symbol: Optional[str] = None
    name: Optional[str] = None
    atomic_number: Optional[int] = None
    mass: Optional[float] = None
    color: Optional[str] = None
    cpk_color: Optional[str] = None
    jmol_color: Optional[str] = None
    pubchem_color: Optional[str] = None


# Generic Elements
H = MCElement(
    symbol="H",
    name="Hydrogen",
    atomic_number=1,
    mass=1.007,
    color="#ffffff",
)
He = MCElement(
    symbol="He",
    name="Helium",
    atomic_number=2,
    mass=4.002,
    color="#d9ffff",
)
Li = MCElement(
    symbol="Li",
    name="Lithium",
    atomic_number=3,
    mass=6.941,
    color="#cc80ff",
)
Be = MCElement(
    symbol="Be",
    name="Beryllium",
    atomic_number=4,
    mass=9.012,
    color="#c2ff00",
)
B = MCElement(
    symbol="B",
    name="Boron",
    atomic_number=5,
    mass=10.811,
    color="#ffb5b5",
)
C = MCElement(
    symbol="C",
    name="Carbon",
    atomic_number=6,
    mass=12.011,
    color="#909090",
)
N = MCElement(
    symbol="N",
    name="Nitrogen",
    atomic_number=7,
    mass=14.007,
    color="#3050f8",
)
O = MCElement(
    symbol="O",
    name="Oxygen",
    atomic_number=8,
    mass=15.999,
    color="#ff0d0d",
)
F = MCElement(
    symbol="F",
    name="Fluorine",
    atomic_number=9,
    mass=18.998,
    color="#90e050",
)
Ne = MCElement(
    symbol="Ne",
    name="Neon",
    atomic_number=10,
    mass=20.18,
    color="#b3e3f5",
)
Na = MCElement(
    symbol="Na",
    name="Sodium",
    atomic_number=11,
    mass=22.99,
    color="#ab5cf2",
)
Mg = MCElement(
    symbol="Mg",
    name="Magnesium",
    atomic_number=12,
    mass=24.305,
    color="#8aff00",
)
Al = MCElement(
    symbol="Al",
    name="Aluminum",
    atomic_number=13,
    mass=26.982,
    color="#bfa6a6",
)
Si = MCElement(
    symbol="Si",
    name="Silicon",
    atomic_number=14,
    mass=28.086,
    color="#f0c8a0",
)
P = MCElement(
    symbol="P",
    name="Phosphorus",
    atomic_number=15,
    mass=30.974,
    color="#ff8000",
)
S = MCElement(
    symbol="S",
    name="Sulfur",
    atomic_number=16,
    mass=32.065,
    color="#ffff30",
)
Cl = MCElement(
    symbol="Cl",
    name="Chlorine",
    atomic_number=17,
    mass=35.453,
    color="#1ff01f",
)
Ar = MCElement(
    symbol="Ar",
    name="Argon",
    atomic_number=18,
    mass=39.948,
    color="#80d1e3",
)
K = MCElement(
    symbol="K",
    name="Potassium",
    atomic_number=19,
    mass=39.098,
    color="#8f40d4",
)
Ca = MCElement(
    symbol="Ca",
    name="Caclium",
    atomic_number=20,
    mass=40.078,
    color="#3dff00",
)
Sc = MCElement(
    symbol="Sc",
    name="Scandium",
    atomic_number=21,
    mass=44.956,
    color="#e6e6e6",
)
Ti = MCElement(
    symbol="Ti",
    name="Titanium",
    atomic_number=22,
    mass=47.867,
    color="#bfc2c7",
)
V = MCElement(
    symbol="V",
    name="Vanadium",
    atomic_number=23,
    mass=50.942,
    color="#a6a6ab",
)
Cr = MCElement(
    symbol="Cr",
    name="Chromium",
    atomic_number=24,
    mass=51.996,
    color="#8a99c7",
)
Mn = MCElement(
    symbol="Mn",
    name="Manganese",
    atomic_number=25,
    mass=54.938,
    color="#9c7ac7",
)
Fe = MCElement(
    symbol="Fe",
    name="Iron",
    atomic_number=26,
    mass=55.845,
    color="#e06633",
)
Co = MCElement(
    symbol="Co",
    name="Cobalt",
    atomic_number=27,
    mass=58.933,
    color="#f090a0",
)
Ni = MCElement(
    symbol="Ni",
    name="Nickel",
    atomic_number=28,
    mass=58.693,
    color="#50d050",
)
Cu = MCElement(
    symbol="Cu",
    name="Copper",
    atomic_number=29,
    mass=63.546,
    color="#c88033",
)
Zn = MCElement(
    symbol="Zn",
    name="Zinc",
    atomic_number=30,
    mass=65.38,
    color="#7d80b0",
)
Ga = MCElement(
    symbol="Ga",
    name="Gallium",
    atomic_number=31,
    mass=69.723,
    color="#c28f8f",
)
Ge = MCElement(
    symbol="Ge",
    name="Germanium",
    atomic_number=32,
    mass=72.64,
    color="#668f8f",
)
As = MCElement(
    symbol="As",
    name="Arsenic",
    atomic_number=33,
    mass=74.922,
    color="#bd80e3",
)
Se = MCElement(
    symbol="Se",
    name="Selenium",
    atomic_number=34,
    mass=78.96,
    color="#ffa100",
)
Br = MCElement(
    symbol="Br",
    name="Bromine",
    atomic_number=35,
    mass=79.904,
    color="#a62929",
)
Kr = MCElement(
    symbol="Kr",
    name="Krypton",
    atomic_number=36,
    mass=83.798,
    color="#5cb8d1",
)
Rb = MCElement(
    symbol="Rb",
    name="Rubidium",
    atomic_number=37,
    mass=85.468,
    color="#702eb0",
)
Sr = MCElement(
    symbol="Sr",
    name="Strontium",
    atomic_number=38,
    mass=87.62,
    color="#00ff00",
)
Y = MCElement(
    symbol="Y",
    name="Yttrium",
    atomic_number=39,
    mass=88.906,
    color="#94ffff",
)
Zr = MCElement(
    symbol="Zr",
    name="Zirconium",
    atomic_number=40,
    mass=91.224,
    color="#94e0e0",
)
Nb = MCElement(
    symbol="Nb",
    name="Niobium",
    atomic_number=41,
    mass=92.906,
    color="#73c2c9",
)
Mo = MCElement(
    symbol="Mo",
    name="Molybdenum",
    atomic_number=42,
    mass=95.96,
    color="#54b5b5",
)
Tc = MCElement(
    symbol="Tc",
    name="Technitium",
    atomic_number=43,
    mass=98.0,
    color="#3b9e9e",
)
Ru = MCElement(
    symbol="Ru",
    name="Ruthenium",
    atomic_number=44,
    mass=101.07,
    color="#248f8f",
)
Rh = MCElement(
    symbol="Rh",
    name="Rhodium",
    atomic_number=45,
    mass=102.906,
    color="#0a7d8c",
)
Pd = MCElement(
    symbol="Pd",
    name="Palladium",
    atomic_number=46,
    mass=106.42,
    color="#006985",
)
Ag = MCElement(
    symbol="Ag",
    name="Silver",
    atomic_number=47,
    mass=107.868,
    color="#c0c0c0",
)
Cd = MCElement(
    symbol="Cd",
    name="Cadmium",
    atomic_number=48,
    mass=112.411,
    color="#ffd98f",
)
In = MCElement(
    symbol="In",
    name="Indium",
    atomic_number=49,
    mass=114.818,
    color="#a67573",
)
Sn = MCElement(
    symbol="Sn",
    name="Tin",
    atomic_number=50,
    mass=118.71,
    color="#668080",
)
Sb = MCElement(
    symbol="Sb",
    name="Antimony",
    atomic_number=51,
    mass=121.76,
    color="#9e63b5",
)
Te = MCElement(
    symbol="Te",
    name="Tellerium",
    atomic_number=52,
    mass=127.6,
    color="#d47a00",
)
I = MCElement(
    symbol="I",
    name="Iodine",
    atomic_number=53,
    mass=126.904,
    color="#940094",
)
Xe = MCElement(
    symbol="Xe",
    name="Xeon",
    atomic_number=54,
    mass=131.293,
    color="#429eb0",
)
Cs = MCElement(
    symbol="Cs",
    name="Cesium",
    atomic_number=55,
    mass=132.905,
    color="#57178f",
)
Ba = MCElement(
    symbol="Ba",
    name="Barium",
    atomic_number=56,
    mass=137.327,
    color="#00c900",
)
La = MCElement(
    symbol="La",
    name="Lanthanum",
    atomic_number=57,
    mass=138.905,
    color="#70d4ff",
)
Ce = MCElement(
    symbol="Ce",
    name="Cerium",
    atomic_number=58,
    mass=140.116,
    color="#ffffc7",
)
Pr = MCElement(
    symbol="Pr",
    name="Praseodymium",
    atomic_number=59,
    mass=140.908,
    color="#d9ffc7",
)
Nd = MCElement(
    symbol="Nd",
    name="Neodymium",
    atomic_number=60,
    mass=144.242,
    color="#c7ffc7",
)
Pm = MCElement(
    symbol="Pm",
    name="Promethium",
    atomic_number=61,
    mass=145.0,
    color="#a3ffc7",
)
Sm = MCElement(
    symbol="Sm",
    name="Samarium",
    atomic_number=62,
    mass=150.36,
    color="#8fffc7",
)
Eu = MCElement(
    symbol="Eu",
    name="Europium",
    atomic_number=63,
    mass=151.964,
    color="#61ffc7",
)
Gd = MCElement(
    symbol="Gd",
    name="Gadolinium",
    atomic_number=64,
    mass=157.25,
    color="#45ffc7",
)
Tb = MCElement(
    symbol="Tb",
    name="Terbium",
    atomic_number=65,
    mass=158.925,
    color="#30ffc7",
)
Dy = MCElement(
    symbol="Dy",
    name="Dysprosium",
    atomic_number=66,
    mass=162.5,
    color="#1fffc7",
)
Ho = MCElement(
    symbol="Ho",
    name="Holmium",
    atomic_number=67,
    mass=164.93,
    color="#00ff9c",
)
Er = MCElement(
    symbol="Er",
    name="Erbium",
    atomic_number=68,
    mass=167.259,
    color="#00e675",
)
Tm = MCElement(
    symbol="Tm",
    name="Thulium",
    atomic_number=69,
    mass=168.934,
    color="#00d452",
)
Yb = MCElement(
    symbol="Yb",
    name="Ytterbium",
    atomic_number=70,
    mass=173.054,
    color="#00bf38",
)
Lu = MCElement(
    symbol="Lu",
    name="Lutetium",
    atomic_number=71,
    mass=174.967,
    color="#00ab24",
)
Hf = MCElement(
    symbol="Hf",
    name="Hafnium",
    atomic_number=72,
    mass=178.49,
    color="#4dc2ff",
)
Ta = MCElement(
    symbol="Ta",
    name="Tantalum",
    atomic_number=73,
    mass=180.948,
    color="#4da6ff",
)
W = MCElement(
    symbol="W",
    name="Tungsten",
    atomic_number=74,
    mass=183.84,
    color="#2194d6",
)
Re = MCElement(
    symbol="Re",
    name="Rhenium",
    atomic_number=75,
    mass=186.207,
    color="#267dab",
)
Os = MCElement(
    symbol="Os",
    name="Osmium",
    atomic_number=76,
    mass=190.23,
    color="#266696",
)
Ir = MCElement(
    symbol="Ir",
    name="Iridium",
    atomic_number=77,
    mass=192.217,
    color="#175487",
)
Pt = MCElement(
    symbol="Pt",
    name="Platinum",
    atomic_number=78,
    mass=195.084,
    color="#d0d0e0",
)
Au = MCElement(
    symbol="Au",
    name="Gold",
    atomic_number=79,
    mass=196.967,
    color="#ffd123",
)
Hg = MCElement(
    symbol="Hg",
    name="Mercury",
    atomic_number=80,
    mass=200.59,
    color="#b8b8d0",
)
Tl = MCElement(
    symbol="Tl",
    name="Thallium",
    atomic_number=81,
    mass=204.383,
    color="#a6544d",
)
Pb = MCElement(
    symbol="Pb",
    name="Lead",
    atomic_number=82,
    mass=207.2,
    color="#575961",
)
Bi = MCElement(
    symbol="Bi",
    name="Bismuth",
    atomic_number=83,
    mass=208.98,
    color="#9e4fb5",
)
Po = MCElement(
    symbol="Po",
    name="Polonium",
    atomic_number=84,
    mass=210.0,
    color="#ab5c00",
)
At = MCElement(
    symbol="At",
    name="Astatine",
    atomic_number=85,
    mass=210.0,
    color="#754f45",
)
Rn = MCElement(
    symbol="Rn",
    name="Radon",
    atomic_number=86,
    mass=222.0,
    color="#428296",
)
Fr = MCElement(
    symbol="Fr",
    name="Francium",
    atomic_number=87,
    mass=223.0,
    color="#420066",
)
Ra = MCElement(
    symbol="Ra",
    name="Radium",
    atomic_number=88,
    mass=226.0,
    color="#007d00",
)
Ac = MCElement(
    symbol="Ac",
    name="Actinium",
    atomic_number=89,
    mass=227.0,
    color="#70abfa",
)
Th = MCElement(
    symbol="Th",
    name="Thorium",
    atomic_number=90,
    mass=232.038,
    color="#00baff",
)
Pa = MCElement(
    symbol="Pa",
    name="Protactinium",
    atomic_number=91,
    mass=231.036,
    color="#00a1ff",
)
U = MCElement(
    symbol="U",
    name="Uranium",
    atomic_number=92,
    mass=238.029,
    color="#008fff",
)
Np = MCElement(
    symbol="Np",
    name="Neptunium",
    atomic_number=93,
    mass=237.0,
    color="#0080ff",
)
Pu = MCElement(
    symbol="Pu",
    name="Plutonium",
    atomic_number=94,
    mass=244.0,
    color="#006bff",
)
Am = MCElement(
    symbol="Am",
    name="Americium",
    atomic_number=95,
    mass=243.0,
    color="#545cf2",
)
Cm = MCElement(
    symbol="Cm",
    name="Curium",
    atomic_number=96,
    mass=247.0,
    color="#785ce3",
)
Bk = MCElement(
    symbol="Bk",
    name="Berkelium",
    atomic_number=97,
    mass=247.0,
    color="#8a4fe3",
)
Cf = MCElement(
    symbol="Cf",
    name="Californium",
    atomic_number=98,
    mass=251.0,
    color="#a136d4",
)
Es = MCElement(
    symbol="Es",
    name="Einsteinium",
    atomic_number=99,
    mass=252.0,
    color="#b31fd4",
)
Fm = MCElement(
    symbol="Fm",
    name="Fermium",
    atomic_number=100,
    mass=257.0,
    color="#b31fba",
)
Md = MCElement(
    symbol="Md",
    name="Mendelevium",
    atomic_number=101,
    mass=258.0,
    color="#b30da6",
)
No = MCElement(
    symbol="No",
    name="Nobelium",
    atomic_number=102,
    mass=259.0,
    color="#bd0d87",
)
Lr = MCElement(
    symbol="Lr",
    name="Lawrencium",
    atomic_number=103,
    mass=262.0,
    color="#c70066",
)
Rf = MCElement(
    symbol="Rf",
    name="Rutherfordium",
    atomic_number=104,
    mass=261.0,
    color="#cc0059",
)
Db = MCElement(
    symbol="Db",
    name="Dubnium",
    atomic_number=105,
    mass=262.0,
    color="#d1004f",
)
Sg = MCElement(
    symbol="Sg",
    name="Seaborgium",
    atomic_number=106,
    mass=266.0,
    color="#d90045",
)
Bh = MCElement(
    symbol="Bh",
    name="Bohrium",
    atomic_number=107,
    mass=264.0,
    color="#e00038",
)
Hs = MCElement(
    symbol="Hs",
    name="Hassium",
    atomic_number=108,
    mass=267.0,
    color="#e6002e",
)
Mt = MCElement(
    symbol="Mt",
    name="Meitnerium",
    atomic_number=109,
    mass=268.0,
    color="#eb0026",
)
Ds = MCElement(
    symbol="Ds",
    name="Darmstadtium",
    atomic_number=110,
    mass=271.0,
    color="#eb0026",
)
Rg = MCElement(
    symbol="Rg",
    name="Roentgenium",
    atomic_number=111,
    mass=272.0,
    color="#eb0026",
)
Cn = MCElement(
    symbol="Cn",
    name="Copernicium",
    atomic_number=112,
    mass=285.0,
    color="#eb0026",
)
Nh = MCElement(
    symbol="Nh",
    name="Nihonium",
    atomic_number=113,
    mass=284.0,
    color="#eb0026",
)
Fl = MCElement(
    symbol="Fl",
    name="Flerovium",
    atomic_number=114,
    mass=289.0,
    color="#eb0026",
)
Mc = MCElement(
    symbol="Mc",
    name="Moscovium",
    atomic_number=115,
    mass=288.0,
    color="#eb0026",
)
Lv = MCElement(
    symbol="Lv",
    name="Livermorium",
    atomic_number=116,
    mass=292.0,
    color="#eb0026",
)
Ts = MCElement(
    symbol="Ts",
    name="Tennessine",
    atomic_number=117,
    mass=295.0,
    color="#eb0026",
)
Og = MCElement(
    symbol="Og",
    name="Oganesson",
    atomic_number=118,
    mass=294.0,
    color="#eb0026",
)


MC_ELEMENT_DICT = {
    "H": H,
    "He": He,
    "Li": Li,
    "Be": Be,
    "B": B,
    "C": C,
    "N": N,
    "O": O,
    "F": F,
    "Ne": Ne,
    "Na": Na,
    "Mg": Mg,
    "Al": Al,
    "Si": Si,
    "P": P,
    "S": S,
    "Cl": Cl,
    "Ar": Ar,
    "K": K,
    "Ca": Ca,
    "Sc": Sc,
    "Ti": Ti,
    "V": V,
    "Cr": Cr,
    "Mn": Mn,
    "Fe": Fe,
    "Co": Co,
    "Ni": Ni,
    "Cu": Cu,
    "Zn": Zn,
    "Ga": Ga,
    "Ge": Ge,
    "As": As,
    "Se": Se,
    "Br": Br,
    "Kr": Kr,
    "Rb": Rb,
    "Sr": Sr,
    "Y": Y,
    "Zr": Zr,
    "Nb": Nb,
    "Mo": Mo,
    "Tc": Tc,
    "Ru": Ru,
    "Rh": Rh,
    "Pd": Pd,
    "Ag": Ag,
    "Cd": Cd,
    "In": In,
    "Sn": Sn,
    "Sb": Sb,
    "Te": Te,
    "I": I,
    "Xe": Xe,
    "Cs": Cs,
    "Ba": Ba,
    "La": La,
    "Ce": Ce,
    "Pr": Pr,
    "Nd": Nd,
    "Pm": Pm,
    "Sm": Sm,
    "Eu": Eu,
    "Gd": Gd,
    "Tb": Tb,
    "Dy": Dy,
    "Ho": Ho,
    "Er": Er,
    "Tm": Tm,
    "Yb": Yb,
    "Lu": Lu,
    "Hf": Hf,
    "Ta": Ta,
    "W": W,
    "Re": Re,
    "Os": Os,
    "Ir": Ir,
    "Pt": Pt,
    "Au": Au,
    "Hg": Hg,
    "Tl": Tl,
    "Pb": Pb,
    "Bi": Bi,
    "Po": Po,
    "At": At,
    "Rn": Rn,
    "Fr": Fr,
    "Ra": Ra,
    "Ac": Ac,
    "Th": Th,
    "Pa": Pa,
    "U": U,
    "Np": Np,
    "Pu": Pu,
    "Am": Am,
    "Cm": Cm,
    "Bk": Bk,
    "Cf": Cf,
    "Es": Es,
    "Fm": Fm,
    "Md": Md,
    "No": No,
    "Lr": Lr,
    "Rf": Rf,
    "Db": Db,
    "Sg": Sg,
    "Bh": Bh,
    "Hs": Hs,
    "Mt": Mt,
    "Ds": Ds,
    "Rg": Rg,
    "Cn": Cn,
    "Nh": Nh,
    "Fl": Fl,
    "Mc": Mc,
    "Lv": Lv,
    "Ts": Ts,
    "Og": Og,
}

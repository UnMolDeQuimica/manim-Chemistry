
from dataclasses import dataclass


@dataclass
class MCElement:
    symbol: str
    name: str
    name_spanish: str
    atomic_number: int
    mass: float
    cpk_color: str
    jmol_color: str
    pubchem_color: str


# Generic Elements
H = MCElement(
    symbol="H",
    name="Hydrogen",
    name_spanish="Hidrógeno",
    atomic_number=1,
    mass=1.007,
    color="#ffffff"
    )
He = MCElement(
    symbol="He",
    name="Helium",
    name_spanish="Helio",
    atomic_number=2,
    mass=4.002,
    color="#d9ffff"
    )
Li = MCElement(
    symbol="Li",
    name="Lithium",
    name_spanish="Litio",
    atomic_number=3,
    mass=6.941,
    color="#cc80ff"
    )
Be = MCElement(
    symbol="Be",
    name="Beryllium",
    name_spanish="Berilio",
    atomic_number=4,
    mass=9.012,
    color="#c2ff00"
    )
B = MCElement(
    symbol="B",
    name="Boron",
    name_spanish="Boro",
    atomic_number=5,
    mass=10.811,
    color="#ffb5b5"
    )
C = MCElement(
    symbol="C",
    name="Carbon",
    name_spanish="Carbono",
    atomic_number=6,
    mass=12.011,
    color="#909090"
    )
N = MCElement(
    symbol="N",
    name="Nitrogen",
    name_spanish="Nitrógeno",
    atomic_number=7,
    mass=14.007,
    color="#3050f8"
    )
O = MCElement(
    symbol="O",
    name="Oxygen",
    name_spanish="Oxígeno",
    atomic_number=8,
    mass=15.999,
    color="#ff0d0d"
    )
F = MCElement(
    symbol="F",
    name="Fluorine",
    name_spanish="Flúor",
    atomic_number=9,
    mass=18.998,
    color="#90e050"
    )
Ne = MCElement(
    symbol="Ne",
    name="Neon",
    name_spanish="Neón",
    atomic_number=10,
    mass=20.18,
    color="#b3e3f5"
    )
Na = MCElement(
    symbol="Na",
    name="Sodium",
    name_spanish="Sodio",
    atomic_number=11,
    mass=22.99,
    color="#ab5cf2"
    )
Mg = MCElement(
    symbol="Mg",
    name="Magnesium",
    name_spanish="Magnesio",
    atomic_number=12,
    mass=24.305,
    color="#8aff00"
    )
Al = MCElement(
    symbol="Al",
    name="Aluminum",
    name_spanish="Aluminio",
    atomic_number=13,
    mass=26.982,
    color="#bfa6a6"
    )
Si = MCElement(
    symbol="Si",
    name="Silicon",
    name_spanish="Silicio",
    atomic_number=14,
    mass=28.086,
    color="#f0c8a0"
    )
P = MCElement(
    symbol="P",
    name="Phosphorus",
    name_spanish="Fósforo",
    atomic_number=15,
    mass=30.974,
    color="#ff8000"
    )
S = MCElement(
    symbol="S",
    name="Sulfur",
    name_spanish="Azufre",
    atomic_number=16,
    mass=32.065,
    color="#ffff30"
    )
Cl = MCElement(
    symbol="Cl",
    name="Chlorine",
    name_spanish="Cloro",
    atomic_number=17,
    mass=35.453,
    color="#1ff01f"
    )
Ar = MCElement(
    symbol="Ar",
    name="Argon",
    name_spanish="Argón",
    atomic_number=18,
    mass=39.948,
    color="#80d1e3"
    )
K = MCElement(
    symbol="K",
    name="Potassium",
    name_spanish="Potasio",
    atomic_number=19,
    mass=39.098,
    color="#8f40d4"
    )
Ca = MCElement(
    symbol="Ca",
    name="Caclium",
    name_spanish="Calcio",
    atomic_number=20,
    mass=40.078,
    color="#3dff00"
    )
Sc = MCElement(
    symbol="Sc",
    name="Scandium",
    name_spanish="Escandio",
    atomic_number=21,
    mass=44.956,
    color="#e6e6e6"
    )
Ti = MCElement(
    symbol="Ti",
    name="Titanium",
    name_spanish="Titanio",
    atomic_number=22,
    mass=47.867,
    color="#bfc2c7"
    )
V = MCElement(
    symbol="V",
    name="Vanadium",
    name_spanish="Vanadio",
    atomic_number=23,
    mass=50.942,
    color="#a6a6ab"
    )
Cr = MCElement(
    symbol="Cr",
    name="Chromium",
    name_spanish="Cromo",
    atomic_number=24,
    mass=51.996,
    color="#8a99c7"
    )
Mn = MCElement(
    symbol="Mn",
    name="Manganese",
    name_spanish="Manganeso",
    atomic_number=25,
    mass=54.938,
    color="#9c7ac7"
    )
Fe = MCElement(
    symbol="Fe",
    name="Iron",
    name_spanish="Hierro",
    atomic_number=26,
    mass=55.845,
    color="#e06633"
    )
Co = MCElement(
    symbol="Co",
    name="Cobalt",
    name_spanish="Cobalto",
    atomic_number=27,
    mass=58.933,
    color="#f090a0"
    )
Ni = MCElement(
    symbol="Ni",
    name="Nickel",
    name_spanish="Níquel",
    atomic_number=28,
    mass=58.693,
    color="#50d050"
    )
Cu = MCElement(
    symbol="Cu",
    name="Copper",
    name_spanish="Cobre",
    atomic_number=29,
    mass=63.546,
    color="#c88033"
    )
Zn = MCElement(
    symbol="Zn",
    name="Zinc",
    name_spanish="Zinc",
    atomic_number=30,
    mass=65.38,
    color="#7d80b0"
    )
Ga = MCElement(
    symbol="Ga",
    name="Gallium",
    name_spanish="Galio",
    atomic_number=31,
    mass=69.723,
    color="#c28f8f"
    )
Ge = MCElement(
    symbol="Ge",
    name="Germanium",
    name_spanish="Germanio",
    atomic_number=32,
    mass=72.64,
    color="#668f8f"
    )
As = MCElement(
    symbol="As",
    name="Arsenic",
    name_spanish="Arsénico",
    atomic_number=33,
    mass=74.922,
    color="#bd80e3"
    )
Se = MCElement(
    symbol="Se",
    name="Selenium",
    name_spanish="Selenio",
    atomic_number=34,
    mass=78.96,
    color="#ffa100"
    )
Br = MCElement(
    symbol="Br",
    name="Bromine",
    name_spanish="Bromo",
    atomic_number=35,
    mass=79.904,
    color="#a62929"
    )
Kr = MCElement(
    symbol="Kr",
    name="Krypton",
    name_spanish="Kripton",
    atomic_number=36,
    mass=83.798,
    color="#5cb8d1"
    )
Rb = MCElement(
    symbol="Rb",
    name="Rubidium",
    name_spanish="Rubidio",
    atomic_number=37,
    mass=85.468,
    color="#702eb0"
    )
Sr = MCElement(
    symbol="Sr",
    name="Strontium",
    name_spanish="Estroncio",
    atomic_number=38,
    mass=87.62,
    color="#00ff00"
    )
Y = MCElement(
    symbol="Y",
    name="Yttrium",
    name_spanish="Itrio",
    atomic_number=39,
    mass=88.906,
    color="#94ffff"
    )
Zr = MCElement(
    symbol="Zr",
    name="Zirconium",
    name_spanish="Zirconio",
    atomic_number=40,
    mass=91.224,
    color="#94e0e0"
    )
Nb = MCElement(
    symbol="Nb",
    name="Niobium",
    name_spanish="Niobio",
    atomic_number=41,
    mass=92.906,
    color="#73c2c9"
    )
Mo = MCElement(
    symbol="Mo",
    name="Molybdenum",
    name_spanish="Molybdeno",
    atomic_number=42,
    mass=95.96,
    color="#54b5b5"
    )
Tc = MCElement(
    symbol="Tc",
    name="Technitium",
    name_spanish="Tecnecio",
    atomic_number=43,
    mass=98.0,
    color="#3b9e9e"
    )
Ru = MCElement(
    symbol="Ru",
    name="Ruthenium",
    name_spanish="Rutenio",
    atomic_number=44,
    mass=101.07,
    color="#248f8f"
    )
Rh = MCElement(
    symbol="Rh",
    name="Rhodium",
    name_spanish="Rodio",
    atomic_number=45,
    mass=102.906,
    color="#0a7d8c"
    )
Pd = MCElement(
    symbol="Pd",
    name="Palladium",
    name_spanish="Paladio",
    atomic_number=46,
    mass=106.42,
    color="#006985"
    )
Ag = MCElement(
    symbol="Ag",
    name="Silver",
    name_spanish="Plata",
    atomic_number=47,
    mass=107.868,
    color="#c0c0c0"
    )
Cd = MCElement(
    symbol="Cd",
    name="Cadmium",
    name_spanish="Cadmio",
    atomic_number=48,
    mass=112.411,
    color="#ffd98f"
    )
In = MCElement(
    symbol="In",
    name="Indium",
    name_spanish="Indio",
    atomic_number=49,
    mass=114.818,
    color="#a67573"
    )
Sn = MCElement(
    symbol="Sn",
    name="Tin",
    name_spanish="Estaño",
    atomic_number=50,
    mass=118.71,
    color="#668080"
    )
Sb = MCElement(
    symbol="Sb",
    name="Antimony",
    name_spanish="Antimonio",
    atomic_number=51,
    mass=121.76,
    color="#9e63b5"
    )
Te = MCElement(
    symbol="Te",
    name="Tellerium",
    name_spanish="Telurio",
    atomic_number=52,
    mass=127.6,
    color="#d47a00"
    )
I = MCElement(
    symbol="I",
    name="Iodine",
    name_spanish="Yodo",
    atomic_number=53,
    mass=126.904,
    color="#940094"
    )
Xe = MCElement(
    symbol="Xe",
    name="Xeon",
    name_spanish="Xenón",
    atomic_number=54,
    mass=131.293,
    color="#429eb0"
    )
Cs = MCElement(
    symbol="Cs",
    name="Cesium",
    name_spanish="Cesio",
    atomic_number=55,
    mass=132.905,
    color="#57178f"
    )
Ba = MCElement(
    symbol="Ba",
    name="Barium",
    name_spanish="Bario",
    atomic_number=56,
    mass=137.327,
    color="#00c900"
    )
La = MCElement(
    symbol="La",
    name="Lanthanum",
    name_spanish="Lantano",
    atomic_number=57,
    mass=138.905,
    color="#70d4ff"
    )
Ce = MCElement(
    symbol="Ce",
    name="Cerium",
    name_spanish="Cerio",
    atomic_number=58,
    mass=140.116,
    color="#ffffc7"
    )
Pr = MCElement(
    symbol="Pr",
    name="Praseodymium",
    name_spanish="Praseodimio",
    atomic_number=59,
    mass=140.908,
    color="#d9ffc7"
    )
Nd = MCElement(
    symbol="Nd",
    name="Neodymium",
    name_spanish="Neodimio",
    atomic_number=60,
    mass=144.242,
    color="#c7ffc7"
    )
Pm = MCElement(
    symbol="Pm",
    name="Promethium",
    name_spanish="Prometio",
    atomic_number=61,
    mass=145.0,
    color="#a3ffc7"
    )
Sm = MCElement(
    symbol="Sm",
    name="Samarium",
    name_spanish="Samario",
    atomic_number=62,
    mass=150.36,
    color="#8fffc7"
    )
Eu = MCElement(
    symbol="Eu",
    name="Europium",
    name_spanish="Europio",
    atomic_number=63,
    mass=151.964,
    color="#61ffc7"
    )
Gd = MCElement(
    symbol="Gd",
    name="Gadolinium",
    name_spanish="Gadolinio",
    atomic_number=64,
    mass=157.25,
    color="#45ffc7"
    )
Tb = MCElement(
    symbol="Tb",
    name="Terbium",
    name_spanish="Terbio",
    atomic_number=65,
    mass=158.925,
    color="#30ffc7"
    )
Dy = MCElement(
    symbol="Dy",
    name="Dysprosium",
    name_spanish="Disprosio",
    atomic_number=66,
    mass=162.5,
    color="#1fffc7"
    )
Ho = MCElement(
    symbol="Ho",
    name="Holmium",
    name_spanish="Holmio",
    atomic_number=67,
    mass=164.93,
    color="#00ff9c"
    )
Er = MCElement(
    symbol="Er",
    name="Erbium",
    name_spanish="Erbio",
    atomic_number=68,
    mass=167.259,
    color="#00e675"
    )
Tm = MCElement(
    symbol="Tm",
    name="Thulium",
    name_spanish="Tulio",
    atomic_number=69,
    mass=168.934,
    color="#00d452"
    )
Yb = MCElement(
    symbol="Yb",
    name="Ytterbium",
    name_spanish="Iterbio",
    atomic_number=70,
    mass=173.054,
    color="#00bf38"
    )
Lu = MCElement(
    symbol="Lu",
    name="Lutetium",
    name_spanish="Lutecio",
    atomic_number=71,
    mass=174.967,
    color="#00ab24"
    )
Hf = MCElement(
    symbol="Hf",
    name="Hafnium",
    name_spanish="Hafnio",
    atomic_number=72,
    mass=178.49,
    color="#4dc2ff"
    )
Ta = MCElement(
    symbol="Ta",
    name="Tantalum",
    name_spanish="Tántalo",
    atomic_number=73,
    mass=180.948,
    color="#4da6ff"
    )
W = MCElement(
    symbol="W",
    name="Tungsten",
    name_spanish="Wolframio",
    atomic_number=74,
    mass=183.84,
    color="#2194d6"
    )
Re = MCElement(
    symbol="Re",
    name="Rhenium",
    name_spanish="Renio",
    atomic_number=75,
    mass=186.207,
    color="#267dab"
    )
Os = MCElement(
    symbol="Os",
    name="Osmium",
    name_spanish="Osmio",
    atomic_number=76,
    mass=190.23,
    color="#266696"
    )
Ir = MCElement(
    symbol="Ir",
    name="Iridium",
    name_spanish="Iridio",
    atomic_number=77,
    mass=192.217,
    color="#175487"
    )
Pt = MCElement(
    symbol="Pt",
    name="Platinum",
    name_spanish="Platino",
    atomic_number=78,
    mass=195.084,
    color="#d0d0e0"
    )
Au = MCElement(
    symbol="Au",
    name="Gold",
    name_spanish="Oro",
    atomic_number=79,
    mass=196.967,
    color="#ffd123"
    )
Hg = MCElement(
    symbol="Hg",
    name="Mercury",
    name_spanish="Mercurio",
    atomic_number=80,
    mass=200.59,
    color="#b8b8d0"
    )
Tl = MCElement(
    symbol="Tl",
    name="Thallium",
    name_spanish="Talio",
    atomic_number=81,
    mass=204.383,
    color="#a6544d"
    )
Pb = MCElement(
    symbol="Pb",
    name="Lead",
    name_spanish="Plomo",
    atomic_number=82,
    mass=207.2,
    color="#575961"
    )
Bi = MCElement(
    symbol="Bi",
    name="Bismuth",
    name_spanish="Bismuto",
    atomic_number=83,
    mass=208.98,
    color="#9e4fb5"
    )
Po = MCElement(
    symbol="Po",
    name="Polonium",
    name_spanish="Polonio",
    atomic_number=84,
    mass=210.0,
    color="#ab5c00"
    )
At = MCElement(
    symbol="At",
    name="Astatine",
    name_spanish="Astato",
    atomic_number=85,
    mass=210.0,
    color="#754f45"
    )
Rn = MCElement(
    symbol="Rn",
    name="Radon",
    name_spanish="Radón",
    atomic_number=86,
    mass=222.0,
    color="#428296"
    )
Fr = MCElement(
    symbol="Fr",
    name="Francium",
    name_spanish="Francio",
    atomic_number=87,
    mass=223.0,
    color="#420066"
    )
Ra = MCElement(
    symbol="Ra",
    name="Radium",
    name_spanish="Radio",
    atomic_number=88,
    mass=226.0,
    color="#007d00"
    )
Ac = MCElement(
    symbol="Ac",
    name="Actinium",
    name_spanish="Actinio",
    atomic_number=89,
    mass=227.0,
    color="#70abfa"
    )
Th = MCElement(
    symbol="Th",
    name="Thorium",
    name_spanish="Torio",
    atomic_number=90,
    mass=232.038,
    color="#00baff"
    )
Pa = MCElement(
    symbol="Pa",
    name="Protactinium",
    name_spanish="Protactinio",
    atomic_number=91,
    mass=231.036,
    color="#00a1ff"
    )
U = MCElement(
    symbol="U",
    name="Uranium",
    name_spanish="Uranio",
    atomic_number=92,
    mass=238.029,
    color="#008fff"
    )
Np = MCElement(
    symbol="Np",
    name="Neptunium",
    name_spanish="Neptunio",
    atomic_number=93,
    mass=237.0,
    color="#0080ff"
    )
Pu = MCElement(
    symbol="Pu",
    name="Plutonium",
    name_spanish="Plutonio",
    atomic_number=94,
    mass=244.0,
    color="#006bff"
    )
Am = MCElement(
    symbol="Am",
    name="Americium",
    name_spanish="Americio",
    atomic_number=95,
    mass=243.0,
    color="#545cf2"
    )
Cm = MCElement(
    symbol="Cm",
    name="Curium",
    name_spanish="Curio",
    atomic_number=96,
    mass=247.0,
    color="#785ce3"
    )
Bk = MCElement(
    symbol="Bk",
    name="Berkelium",
    name_spanish="Berkelio",
    atomic_number=97,
    mass=247.0,
    color="#8a4fe3"
    )
Cf = MCElement(
    symbol="Cf",
    name="Californium",
    name_spanish="Californio",
    atomic_number=98,
    mass=251.0,
    color="#a136d4"
    )
Es = MCElement(
    symbol="Es",
    name="Einsteinium",
    name_spanish="Einsteinio",
    atomic_number=99,
    mass=252.0,
    color="#b31fd4"
    )
Fm = MCElement(
    symbol="Fm",
    name="Fermium",
    name_spanish="Fermio",
    atomic_number=100,
    mass=257.0,
    color="#b31fba"
    )
Md = MCElement(
    symbol="Md",
    name="Mendelevium",
    name_spanish="Mendelevio",
    atomic_number=101,
    mass=258.0,
    color="#b30da6"
    )
No = MCElement(
    symbol="No",
    name="Nobelium",
    name_spanish="Nobelio",
    atomic_number=102,
    mass=259.0,
    color="#bd0d87"
    )
Lr = MCElement(
    symbol="Lr",
    name="Lawrencium",
    name_spanish="Lawrencio",
    atomic_number=103,
    mass=262.0,
    color="#c70066"
    )
Rf = MCElement(
    symbol="Rf",
    name="Rutherfordium",
    name_spanish="Rutherfordio",
    atomic_number=104,
    mass=261.0,
    color="#cc0059"
    )
Db = MCElement(
    symbol="Db",
    name="Dubnium",
    name_spanish="Dubnio",
    atomic_number=105,
    mass=262.0,
    color="#d1004f"
    )
Sg = MCElement(
    symbol="Sg",
    name="Seaborgium",
    name_spanish="Seaborgio",
    atomic_number=106,
    mass=266.0,
    color="#d90045"
    )
Bh = MCElement(
    symbol="Bh",
    name="Bohrium",
    name_spanish="Bohrio",
    atomic_number=107,
    mass=264.0,
    color="#e00038"
    )
Hs = MCElement(
    symbol="Hs",
    name="Hassium",
    name_spanish="Hassio",
    atomic_number=108,
    mass=267.0,
    color="#e6002e"
    )
Mt = MCElement(
    symbol="Mt",
    name="Meitnerium",
    name_spanish="Meitnerio",
    atomic_number=109,
    mass=268.0,
    color="#eb0026"
    )
Ds = MCElement(
    symbol="Ds",
    name="Darmstadtium",
    name_spanish="Darmstadtio",
    atomic_number=110,
    mass=271.0,
    color="#eb0026"
    )
Rg = MCElement(
    symbol="Rg",
    name="Roentgenium",
    name_spanish="Roentgenio",
    atomic_number=111,
    mass=272.0,
    color="#eb0026"
    )
Cn = MCElement(
    symbol="Cn",
    name="Copernicium",
    name_spanish="Copernicio",
    atomic_number=112,
    mass=285.0,
    color="#eb0026"
    )
Nh = MCElement(
    symbol="Nh",
    name="Nihonium",
    name_spanish="Nihonio",
    atomic_number=113,
    mass=284.0,
    color="#eb0026"
    )
Fl = MCElement(
    symbol="Fl",
    name="Flerovium",
    name_spanish="Flerovio",
    atomic_number=114,
    mass=289.0,
    color="#eb0026"
    )
Mc = MCElement(
    symbol="Mc",
    name="Moscovium",
    name_spanish="Moscovio",
    atomic_number=115,
    mass=288.0,
    color="#eb0026"
    )
Lv = MCElement(
    symbol="Lv",
    name="Livermorium",
    name_spanish="Livermorio",
    atomic_number=116,
    mass=292.0,
    color="#eb0026"
    )
Ts = MCElement(
    symbol="Ts",
    name="Tennessine",
    name_spanish="Teneso",
    atomic_number=117,
    mass=295.0,
    color="#eb0026"
    )
Og = MCElement(
    symbol="Og",
    name="Oganesson",
    name_spanish="Oganesón",
    atomic_number=118,
    mass=294.0,
    color="#eb0026"
    )

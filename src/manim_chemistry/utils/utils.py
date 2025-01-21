import numpy as np

from manim_chemistry.element import *


def mol_parser_string(mol_string):
    # Get general data
    mol_name = mol_string[0].strip()  # This info is not always available  # noqa F841
    mol_source = mol_string[1].strip()  # This info is not always available  # noqa F841
    mol_comments = mol_string[  # noqa F841
        2
    ].rstrip()  # This info is not always available
    mol_general_info = mol_string[3]  # This info is not always available
    mol_string.remove(mol_general_info)  # This info is not always available
    mol_general_info = (
        mol_general_info.rstrip().split()
    )  # This info is not always available
    number_of_atoms = int(mol_general_info[0])
    number_of_bonds = int(mol_general_info[1])

    atoms = {}
    bonds = {}
    for index, line in enumerate(mol_string[3 : 3 + number_of_atoms]):
        line_data = line.split()
        x_position = float(line_data[0])
        y_position = float(line_data[1])
        z_position = float(line_data[2])
        element = line_data[3]
        atoms[index + 1] = {
            "coords": np.array([x_position, y_position, z_position]),
            "element": element,
        }

    for line in mol_string[3 + number_of_atoms : 3 + number_of_atoms + number_of_bonds]:
        line_data = line.split()
        first_atom_index = int(float(line_data[0]))
        second_atom_index = int(float(line_data[1]))
        bond_type = line_data[2]
        bond_data = {
            "to": second_atom_index,
            "type": bond_type,
            # "stereo": bond_stereo,
            # "topology": bond_topology,
            # "reacting_center_status": reacting_center_status
        }

        try:
            bond_stereo = line_data[3]
        except Exception as _:
            bond_stereo = ""
        else:
            bond_data["stereo"] = int(bond_stereo)

        try:
            bond_topology = line_data[5]
        except Exception as _:
            bond_topology = ""
        else:
            bond_data["topology"] = int(bond_topology)

        try:
            reacting_center_status = line_data[6]
        except Exception as _:
            reacting_center_status = ""
        else:
            bond_data["reacting_center_status"] = int(reacting_center_status)

        if first_atom_index not in bonds:
            bonds[first_atom_index] = [bond_data]
            if not atoms.get(first_atom_index) or not atoms.get(first_atom_index).get(
                "bond_to"
            ):
                atoms[first_atom_index]["bond_to"] = {
                    second_atom_index: atoms.get(second_atom_index).get("element")
                }
            else:
                atoms[first_atom_index]["bond_to"][second_atom_index] = atoms.get(
                    second_atom_index
                ).get("element")

        else:
            bonds[first_atom_index].append(bond_data)
            atoms[first_atom_index]["bond_to"][second_atom_index] = atoms.get(
                second_atom_index
            ).get("element")

        if not atoms.get(second_atom_index).get("bond_to"):
            atoms[second_atom_index]["bond_to"] = {
                first_atom_index: atoms.get(first_atom_index).get("element")
            }
        else:
            atoms[second_atom_index]["bond_to"][first_atom_index] = atoms.get(
                first_atom_index
            ).get("element")

    return atoms, bonds  # Should return atoms and bonds

def mol_parser(file):
    with open(file) as file:
        mol_file = file.readlines()
    return mol_parser_string(mol_file)

def sdf_parser_string(sdf_string):
    molecules = sdf_string.split("$$$$")
    molecules = [m.strip() for m in molecules if m.strip()]

    mol_list = []
    for i, mol in enumerate(molecules, 1):
        mol_list.append(mol_parser_string(mol.split("\n")))

    return mol_list

def sdf_parser(file):
    with open(file) as file:
        sdf_file = file.read()
    return sdf_parser_string(sdf_file)


def get_element(element, language="ENG"):
    if language == "ENG":
        element_dict = ELEMENT_DICT
    elif language == "ESP":
        element_dict = ELEMENT_DICT_ESP

    return element_dict[element]


def mol_to_graph(file, language="ENG"):
    with open(file) as file:
        mol_file = file.readlines()
    # Get general data

    mol_general_info = mol_file[3]  # This info is not always available
    mol_file.remove(mol_general_info)  # This info is not always available
    mol_general_info = (
        mol_general_info.rstrip().split()
    )  # This info is not always available
    number_of_atoms = int(mol_general_info[0])
    number_of_bonds = int(mol_general_info[1])

    atoms = {}
    bonds = {}
    for index, line in enumerate(mol_file[3 : 3 + number_of_atoms]):
        line_data = line.split()
        x_position = float(line_data[0])
        y_position = float(line_data[1])
        z_position = float(line_data[2])
        element = line_data[3]
        atoms[index + 1] = {
            "position": np.array([x_position, y_position, z_position]),
            "element": get_element(element, language),
        }

    for line in mol_file[3 + number_of_atoms : 3 + number_of_atoms + number_of_bonds]:
        line_data = line.split()
        first_atom_index = int(float(line_data[0]))
        second_atom_index = int(float(line_data[1]))
        bond_type = line_data[2]
        bonds[(first_atom_index, second_atom_index)] = {"type": bond_type}

    return atoms, bonds  # Should return atoms and bonds


ELEMENT_DICT = {
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

ELEMENT_DICT_ESP = {
    "H_ESP": H_ESP,
    "He_ESP": He_ESP,
    "Li_ESP": Li_ESP,
    "Be_ESP": Be_ESP,
    "B_ESP": B_ESP,
    "C_ESP": C_ESP,
    "N_ESP": N_ESP,
    "O_ESP": O_ESP,
    "F_ESP": F_ESP,
    "Ne_ESP": Ne_ESP,
    "Na_ESP": Na_ESP,
    "Mg_ESP": Mg_ESP,
    "Al_ESP": Al_ESP,
    "Si_ESP": Si_ESP,
    "P_ESP": P_ESP,
    "S_ESP": S_ESP,
    "Cl_ESP": Cl_ESP,
    "Ar_ESP": Ar_ESP,
    "K_ESP": K_ESP,
    "Ca_ESP": Ca_ESP,
    "Sc_ESP": Sc_ESP,
    "Ti_ESP": Ti_ESP,
    "V_ESP": V_ESP,
    "Cr_ESP": Cr_ESP,
    "Mn_ESP": Mn_ESP,
    "Fe_ESP": Fe_ESP,
    "Co_ESP": Co_ESP,
    "Ni_ESP": Ni_ESP,
    "Cu_ESP": Cu_ESP,
    "Zn_ESP": Zn_ESP,
    "Ga_ESP": Ga_ESP,
    "Ge_ESP": Ge_ESP,
    "As_ESP": As_ESP,
    "Se_ESP": Se_ESP,
    "Br_ESP": Br_ESP,
    "Kr_ESP": Kr_ESP,
    "Rb_ESP": Rb_ESP,
    "Sr_ESP": Sr_ESP,
    "Y_ESP": Y_ESP,
    "Zr_ESP": Zr_ESP,
    "Nb_ESP": Nb_ESP,
    "Mo_ESP": Mo_ESP,
    "Tc_ESP": Tc_ESP,
    "Ru_ESP": Ru_ESP,
    "Rh_ESP": Rh_ESP,
    "Pd_ESP": Pd_ESP,
    "Ag_ESP": Ag_ESP,
    "Cd_ESP": Cd_ESP,
    "In_ESP": In_ESP,
    "Sn_ESP": Sn_ESP,
    "Sb_ESP": Sb_ESP,
    "Te_ESP": Te_ESP,
    "I_ESP": I_ESP,
    "Xe_ESP": Xe_ESP,
    "Cs_ESP": Cs_ESP,
    "Ba_ESP": Ba_ESP,
    "La_ESP": La_ESP,
    "Ce_ESP": Ce_ESP,
    "Pr_ESP": Pr_ESP,
    "Nd_ESP": Nd_ESP,
    "Pm_ESP": Pm_ESP,
    "Sm_ESP": Sm_ESP,
    "Eu_ESP": Eu_ESP,
    "Gd_ESP": Gd_ESP,
    "Tb_ESP": Tb_ESP,
    "Dy_ESP": Dy_ESP,
    "Ho_ESP": Ho_ESP,
    "Er_ESP": Er_ESP,
    "Tm_ESP": Tm_ESP,
    "Yb_ESP": Yb_ESP,
    "Lu_ESP": Lu_ESP,
    "Hf_ESP": Hf_ESP,
    "Ta_ESP": Ta_ESP,
    "W_ESP": W_ESP,
    "Re_ESP": Re_ESP,
    "Os_ESP": Os_ESP,
    "Ir_ESP": Ir_ESP,
    "Pt_ESP": Pt_ESP,
    "Au_ESP": Au_ESP,
    "Hg_ESP": Hg_ESP,
    "Tl_ESP": Tl_ESP,
    "Pb_ESP": Pb_ESP,
    "Bi_ESP": Bi_ESP,
    "Po_ESP": Po_ESP,
    "At_ESP": At_ESP,
    "Rn_ESP": Rn_ESP,
    "Fr_ESP": Fr_ESP,
    "Ra_ESP": Ra_ESP,
    "Ac_ESP": Ac_ESP,
    "Th_ESP": Th_ESP,
    "Pa_ESP": Pa_ESP,
    "U_ESP": U_ESP,
    "Np_ESP": Np_ESP,
    "Pu_ESP": Pu_ESP,
    "Am_ESP": Am_ESP,
    "Cm_ESP": Cm_ESP,
    "Bk_ESP": Bk_ESP,
    "Cf_ESP": Cf_ESP,
    "Es_ESP": Es_ESP,
    "Fm_ESP": Fm_ESP,
    "Md_ESP": Md_ESP,
    "No_ESP": No_ESP,
    "Lr_ESP": Lr_ESP,
    "Rf_ESP": Rf_ESP,
    "Db_ESP": Db_ESP,
    "Sg_ESP": Sg_ESP,
    "Bh_ESP": Bh_ESP,
    "Hs_ESP": Hs_ESP,
    "Mt_ESP": Mt_ESP,
    "Ds_ESP": Ds_ESP,
    "Rg_ESP": Rg_ESP,
    "Cn_ESP": Cn_ESP,
    "Nh_ESP": Nh_ESP,
    "Fl_ESP": Fl_ESP,
    "Mc_ESP": Mc_ESP,
    "Lv_ESP": Lv_ESP,
    "Ts_ESP": Ts_ESP,
    "Og_ESP": Og_ESP,
}

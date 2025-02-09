import os


class BaseTestMolecule:
    molecule_class = ...
    base_files_path = os.path.join("examples", "molecule_files")
    files_names = [
        "acetone_2d",
        "acetone_3d",
        "morphine_2d",
        "morphine_3d",
        "heme_2d",
        "heme_3d",
    ]
    mol_files = [
        f"{os.path.join('examples', 'molecule_files', 'mol_files', file)}.mol"
        for file in files_names
    ]
    sdf_files = [
        f"{os.path.join('examples', 'molecule_files', 'sdf_files', file)}.sdf"
        for file in files_names
    ]
    json_files = [
        f"{os.path.join('examples', 'molecule_files', 'json_files', file)}.json"
        for file in files_names
    ]
    asnt_files = [
        f"{os.path.join('examples', 'molecule_files', 'asnt_files', file)}.asnt"
        for file in files_names
        if file != "heme_2d"
    ]
    xml_files = [
        f"{os.path.join('examples', 'molecule_files', 'xml_files', file)}.xml"
        for file in files_names
    ]

    files = []
    files.extend(mol_files)
    files.extend(sdf_files)
    files.extend(json_files)
    files.extend(asnt_files)
    files.extend(xml_files)

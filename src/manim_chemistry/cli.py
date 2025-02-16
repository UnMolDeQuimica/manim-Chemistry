import os

import click

from .utils import PubchemAPIManager


@click.group
def cli(): ...


@click.command()
@click.option(
    "--format",
    "-f",
    default="sdf",
    help="Format of the file to be downloaded. Defaults to 'sdf'. Options are 'asnt', 'json', 'sdf' and 'xlm'.",
)
@click.option("--cid", "-c", multiple=True, help="cid of the molecule.")
@click.option("--name", "-n", multiple=True, help="name of the molecule.")
@click.option("--smiles", "-s", multiple=True, help="smiles of the molecule.")
@click.option("--inchi", "-i", multiple=True, help="inchi of the molecule.")
@click.option(
    "--three_d", "-td", default=False, help="Use three d data of the molecule."
)
@click.option("--output_folder", "-o", default=".", help="Output folder.")
def pubchem_molecule(format, cid, name, smiles, inchi, three_d, output_folder):
    """
    Download molecule from pubchem.

    Supports downloading multiple files from a single request.

    Example
    -------

    .. code-block:: console

        manim_chemistry pubchem-molecule --format sdf -n acetone -n morphine

    Result:

    .. code-block:: console

        >>> Retrieving molecule data for ('acetone', 'morphine').
        >>> Retrieved molecule data for ('acetone', 'morphine'). Saving file(s) to . folder.
        >>> File .\\acetone.sdf is ready!!
        >>> File .\\morphine.sdf is ready!!
        >>> Finished
    """

    identifier = cid or name or smiles or inchi
    click.echo(f"Retrieving molecule data for {identifier}.")

    if not identifier:
        raise Exception(
            "No identifier provided. Options are 'cid', 'name', 'smile' and 'inchi'."
        )

    molecules = {}
    if cid:
        for molecule in cid:
            molecule_data = PubchemAPIManager(
                cid=molecule, three_d=three_d, format=format
            ).get_molecule()

            molecules[molecule] = molecule_data

    elif name:
        for molecule in name:
            molecule_data = PubchemAPIManager(
                name=molecule, three_d=three_d, format=format
            ).get_molecule()

            molecules[molecule] = molecule_data

    elif smiles:
        for molecule in smiles:
            molecule_data = PubchemAPIManager(
                smiles=molecule, three_d=three_d, format=format
            ).get_molecule()

            molecules[molecule] = molecule_data

    else:
        # InChI is used
        for molecule in inchi:
            molecule_data = PubchemAPIManager(
                inchi=molecule, three_d=three_d, format=format
            ).get_molecule()

            molecules[molecule] = molecule_data

    click.echo(
        f"Retrieved molecule data for {identifier}. Saving file(s) to {output_folder} folder."
    )

    for molecule_identifier, molecule_data in molecules.items():
        output_file = os.path.join(output_folder, f"{molecule_identifier}.{format}")
        with open(output_file, "w") as file:
            file.write(molecule_data)

        click.echo(f"File {output_file} is ready!!")

    click.echo("Finished")


cli.add_command(pubchem_molecule)

if __name__ == "__main__":
    cli()

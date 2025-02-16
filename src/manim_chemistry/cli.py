import os

import click

from .utils import PubchemAPIManager


@click.group
def cli(): ...


@click.command()
@click.option(
    "--format",
    default="sdf",
    help="Format of the file to be downloaded. Defaults to 'sdf'. Options are 'asnt', 'json', 'sdf' and 'xlm'.",
)
@click.option("--cid", default=None, help="cid of the molecule.")
@click.option("--name", default=None, help="name of the molecule.")
@click.option("--smiles", default=None, help="smiles of the molecule.")
@click.option("--inchi", default=None, help="inchi of the molecule.")
@click.option("--three_d", default=False, help="Use three d data of the molecule.")
@click.option("--output_folder", default=".", help="Output folder.")
def pubchem_molecule(format, cid, name, smiles, inchi, three_d, output_folder):
    """
    Download molecule from pubchem.
    """

    identifier = cid or name or smiles or inchi
    click.echo(f"Retrieving molecule data for {identifier}.")

    if not identifier:
        raise Exception(
            "No identifier provided. Options are 'cid', 'name', 'smile' and 'inchi'."
        )

    if cid:
        molecule_data = PubchemAPIManager(
            cid=cid, three_d=three_d, format=format
        ).get_molecule()

    elif name:
        molecule_data = PubchemAPIManager(
            name=name, three_d=three_d, format=format
        ).get_molecule()

    elif smiles:
        molecule_data = PubchemAPIManager(
            smiles=smiles, three_d=three_d, format=format
        ).get_molecule()

    else:
        # InChI is used
        molecule_data = PubchemAPIManager(
            inchi=inchi, three_d=three_d, format=format
        ).get_molecule()

    output_file = os.path.join(output_folder, f"{identifier}.{format}")
    click.echo(
        f"Retrieved molecule data for {identifier}. Saving file to {output_file}."
    )

    with open(output_file, "w") as file:
        file.write(molecule_data)

    click.echo(f"File {output_file} is ready!!")


cli.add_command(pubchem_molecule)

if __name__ == "__main__":
    cli()

from typing import Optional
import json

import requests


class PubchemAPIManager:
    BASE_URL = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/"

    def __init__(
        self,
        cid: Optional[int] = None,
        name: Optional[str] = None,
        smiles: Optional[str] = None,
        inchi: Optional[str] = None,
    ):
        if not any([cid, name, smiles, inchi]):
            raise Exception(
                "You should provide an identifier. Available identifiers are cid, name, smiles and inchi"
            )

        self.cid = cid
        self.name = name
        self.smiles = smiles
        self.inchi = inchi

    def handle_request(self, request: requests.models.Response, identifier):
        if request.status_code == 200:
            return json.dumps(request.json())

        if request.status_code == 404:
            raise Exception(f"Compound {identifier} not found")

        raise Exception(
            f"An error occurred when calling the Pub Chem API. Status code: {request.status_code}. Request response: {request.response}"
        )

    def from_cid(self):
        request = requests.get(f"{PubchemAPIManager.BASE_URL}/cid/{self.cid}/json")
        return self.handle_request(request=request, identifier=self.cid)

    def from_name(self):
        request = requests.get(f"{PubchemAPIManager.BASE_URL}/name/{self.name}/json")
        return self.handle_request(request=request, identifier=self.name)

    def from_smiles(self):
        request = requests.get(f"{PubchemAPIManager.BASE_URL}/smiles/{self.smiles}/json")
        return self.handle_request(request=request, identifier=self.smiles)

    def from_inchi(self):
        request = requests.get(f"{PubchemAPIManager.BASE_URL}/inchikey/{self.inchi}/json")
        return self.handle_request(request=request, identifier=self.inchi)

    def get_molecule(self):
        if self.cid:
            return self.from_cid()

        elif self.name:
            return self.from_name()

        elif self.smiles:
            return self.from_smiles()

        elif self.inchi:
            return self.from_inchi()

        else:
            raise Exception("No identifier provided")

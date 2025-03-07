from typing import Optional
import json
import time

import requests


class PubchemAPIManager:
    BASE_URL = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/"

    def __init__(
        self,
        cid: Optional[int] = None,
        name: Optional[str] = None,
        smiles: Optional[str] = None,
        inchi: Optional[str] = None,
        three_d: bool = False,
        format: str = "json",
    ):
        if not any([cid, name, smiles, inchi]):
            raise Exception(
                "You should provide an identifier. Available identifiers are cid, name, smiles and inchi"
            )
        self.cid = cid
        self.name = name
        self.smiles = smiles
        self.inchi = inchi
        self.three_d = three_d
        self.format = format

    def handle_request(self, request: requests.models.Response, identifier):
        # Added sleep to prevent overloading the PubChem API
        time.sleep(0.25)
        if request.status_code == 200:
            try:
                return json.dumps(request.json())

            except requests.exceptions.JSONDecodeError:
                return request.content.decode()

            except Exception as error:
                raise error

        if request.status_code == 404:
            raise Exception(f"Compound {identifier} not found")

        raise Exception(
            f"An error occurred when calling the Pub Chem API. Status code: {request.status_code}. Request response: {request.json}"
        )

    def from_cid(self):
        request_url = f"{PubchemAPIManager.BASE_URL}/cid/{self.cid}/{self.format}"
        if self.three_d:
            request_url += "?record_type=3d"

        request = requests.get(request_url)
        return self.handle_request(request=request, identifier=self.cid)

    def from_name(self):
        request_url = f"{PubchemAPIManager.BASE_URL}/name/{self.name}/{self.format}"
        if self.three_d:
            request_url += "?record_type=3d"

        request = requests.get(request_url)
        return self.handle_request(request=request, identifier=self.name)

    def from_smiles(self):
        request_url = f"{PubchemAPIManager.BASE_URL}/smiles/{self.smiles}/{self.format}"
        if self.three_d:
            request_url += "?record_type=3d"

        request = requests.get(request_url)
        return self.handle_request(request=request, identifier=self.smiles)

    def from_inchi(self):
        request_url = (
            f"{PubchemAPIManager.BASE_URL}/inchikey/{self.inchi}/{self.format}"
        )
        if self.three_d:
            request_url += "?record_type=3d"

        request = requests.get(request_url)
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

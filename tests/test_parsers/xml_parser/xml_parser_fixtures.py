import pytest
import os

import numpy as np

base_files_path = os.path.join("examples", "molecule_files", "xml_files")


class BaseTestXMLParser:
    acetone_2d = os.path.join(base_files_path, "acetone_2d.xml")
    acetone_3d = os.path.join(base_files_path, "acetone_3d.xml")
    morphine_2d = os.path.join(base_files_path, "morphine_2d.xml")
    morphine_3d = os.path.join(base_files_path, "morphine_3d.xml")
    heme_2d = os.path.join(base_files_path, "heme_2d.xml")
    heme_3d = os.path.join(base_files_path, "heme_3d.xml")

    @pytest.fixture
    def acetone_2d_file_data(self):
        return """<?xml version="1.0"?>
<PC-Compounds
    xmlns="http://www.ncbi.nlm.nih.gov"
    xmlns:xs="http://www.w3.org/2001/XMLSchema-instance"
    xs:schemaLocation="http://www.ncbi.nlm.nih.gov ftp://ftp.ncbi.nlm.nih.gov/pubchem/specifications/pubchem.xsd"
>
  <PC-Compound>
    <PC-Compound_id>
      <PC-CompoundType>
        <PC-CompoundType_id>
          <PC-CompoundType_id_cid>180</PC-CompoundType_id_cid>
        </PC-CompoundType_id>
      </PC-CompoundType>
    </PC-Compound_id>
    <PC-Compound_atoms>
      <PC-Atoms>
        <PC-Atoms_aid>
          <PC-Atoms_aid_E>1</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>2</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>3</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>4</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>5</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>6</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>7</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>8</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>9</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>10</PC-Atoms_aid_E>
        </PC-Atoms_aid>
        <PC-Atoms_element>
          <PC-Element value="o">8</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
        </PC-Atoms_element>
      </PC-Atoms>
    </PC-Compound_atoms>
    <PC-Compound_bonds>
      <PC-Bonds>
        <PC-Bonds_aid1>
          <PC-Bonds_aid1_E>1</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>2</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>2</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>3</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>3</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>3</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>4</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>4</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>4</PC-Bonds_aid1_E>
        </PC-Bonds_aid1>
        <PC-Bonds_aid2>
          <PC-Bonds_aid2_E>2</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>3</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>4</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>5</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>6</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>7</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>8</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>9</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>10</PC-Bonds_aid2_E>
        </PC-Bonds_aid2>
        <PC-Bonds_order>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
        </PC-Bonds_order>
      </PC-Bonds>
    </PC-Compound_bonds>
    <PC-Compound_coords>
      <PC-Coordinates>
        <PC-Coordinates_type>
          <PC-CoordinateType value="twod">1</PC-CoordinateType>
          <PC-CoordinateType value="computed">5</PC-CoordinateType>
          <PC-CoordinateType value="units-unknown">255</PC-CoordinateType>
        </PC-Coordinates_type>
        <PC-Coordinates_aid>
          <PC-Coordinates_aid_E>1</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>2</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>3</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>4</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>5</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>6</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>7</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>8</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>9</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>10</PC-Coordinates_aid_E>
        </PC-Coordinates_aid>
        <PC-Coordinates_conformers>
          <PC-Conformer>
            <PC-Conformer_x>
              <PC-Conformer_x_E>3.732</PC-Conformer_x_E>
              <PC-Conformer_x_E>2.866</PC-Conformer_x_E>
              <PC-Conformer_x_E>2</PC-Conformer_x_E>
              <PC-Conformer_x_E>2.866</PC-Conformer_x_E>
              <PC-Conformer_x_E>2.31</PC-Conformer_x_E>
              <PC-Conformer_x_E>1.4631</PC-Conformer_x_E>
              <PC-Conformer_x_E>1.69</PC-Conformer_x_E>
              <PC-Conformer_x_E>2.246</PC-Conformer_x_E>
              <PC-Conformer_x_E>2.866</PC-Conformer_x_E>
              <PC-Conformer_x_E>3.486</PC-Conformer_x_E>
            </PC-Conformer_x>
            <PC-Conformer_y>
              <PC-Conformer_y_E>0.75</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.25</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.75</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.75</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.2869</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.06</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.2131</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.75</PC-Conformer_y_E>
              <PC-Conformer_y_E>-1.37</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.75</PC-Conformer_y_E>
            </PC-Conformer_y>
          </PC-Conformer>
        </PC-Coordinates_conformers>
      </PC-Coordinates>
    </PC-Compound_coords>
    <PC-Compound_charge>0</PC-Compound_charge>
    <PC-Compound_props>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Compound</PC-Urn_label>
            <PC-Urn_name>Canonicalized</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="uint">5</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_ival>1</PC-InfoData_value_ival>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Compound Complexity</PC-Urn_label>
            <PC-Urn_datatype>
              <PC-UrnDataType value="double">7</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_implementation>E_COMPLEXITY</PC-Urn_implementation>
            <PC-Urn_version>3.4.8.18</PC-Urn_version>
            <PC-Urn_software>Cactvs</PC-Urn_software>
            <PC-Urn_source>Xemistry GmbH</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_fval>26.3</PC-InfoData_value_fval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Count</PC-Urn_label>
            <PC-Urn_name>Hydrogen Bond Acceptor</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="uint">5</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_implementation>E_NHACCEPTORS</PC-Urn_implementation>
            <PC-Urn_version>3.4.8.18</PC-Urn_version>
            <PC-Urn_software>Cactvs</PC-Urn_software>
            <PC-Urn_source>Xemistry GmbH</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_ival>1</PC-InfoData_value_ival>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Count</PC-Urn_label>
            <PC-Urn_name>Hydrogen Bond Donor</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="uint">5</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_implementation>E_NHDONORS</PC-Urn_implementation>
            <PC-Urn_version>3.4.8.18</PC-Urn_version>
            <PC-Urn_software>Cactvs</PC-Urn_software>
            <PC-Urn_source>Xemistry GmbH</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_ival>0</PC-InfoData_value_ival>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Count</PC-Urn_label>
            <PC-Urn_name>Rotatable Bond</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="uint">5</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_implementation>E_NROTBONDS</PC-Urn_implementation>
            <PC-Urn_version>3.4.8.18</PC-Urn_version>
            <PC-Urn_software>Cactvs</PC-Urn_software>
            <PC-Urn_source>Xemistry GmbH</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_ival>0</PC-InfoData_value_ival>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Fingerprint</PC-Urn_label>
            <PC-Urn_name>SubStructure Keys</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="fingerprint">16</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_parameters>extended 2</PC-Urn_parameters>
            <PC-Urn_implementation>E_SCREEN</PC-Urn_implementation>
            <PC-Urn_version>3.4.8.18</PC-Urn_version>
            <PC-Urn_software>Cactvs</PC-Urn_software>
            <PC-Urn_source>Xemistry GmbH</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_binary>0000037180402000000000000000000000000000000000000000000000000000000000000000001A000000000008048080000200000000000800801000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000</PC-InfoData_value_binary>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>IUPAC Name</PC-Urn_label>
            <PC-Urn_name>Allowed</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.7.0</PC-Urn_version>
            <PC-Urn_software>Lexichem TK</PC-Urn_software>
            <PC-Urn_source>OpenEye Scientific Software</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>acetone</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>IUPAC Name</PC-Urn_label>
            <PC-Urn_name>CAS-like Style</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.7.0</PC-Urn_version>
            <PC-Urn_software>Lexichem TK</PC-Urn_software>
            <PC-Urn_source>OpenEye Scientific Software</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>2-propanone</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>IUPAC Name</PC-Urn_label>
            <PC-Urn_name>Markup</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.7.0</PC-Urn_version>
            <PC-Urn_software>Lexichem TK</PC-Urn_software>
            <PC-Urn_source>OpenEye Scientific Software</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>propan-2-one</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>IUPAC Name</PC-Urn_label>
            <PC-Urn_name>Preferred</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.7.0</PC-Urn_version>
            <PC-Urn_software>Lexichem TK</PC-Urn_software>
            <PC-Urn_source>OpenEye Scientific Software</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>propan-2-one</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>IUPAC Name</PC-Urn_label>
            <PC-Urn_name>Systematic</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.7.0</PC-Urn_version>
            <PC-Urn_software>Lexichem TK</PC-Urn_software>
            <PC-Urn_source>OpenEye Scientific Software</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>propan-2-one</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>IUPAC Name</PC-Urn_label>
            <PC-Urn_name>Traditional</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.7.0</PC-Urn_version>
            <PC-Urn_software>Lexichem TK</PC-Urn_software>
            <PC-Urn_source>OpenEye Scientific Software</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>acetone</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>InChI</PC-Urn_label>
            <PC-Urn_name>Standard</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>1.0.6</PC-Urn_version>
            <PC-Urn_software>InChI</PC-Urn_software>
            <PC-Urn_source>iupac.org</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>InChI=1S/C3H6O/c1-3(2)4/h1-2H3</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>InChIKey</PC-Urn_label>
            <PC-Urn_name>Standard</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>1.0.6</PC-Urn_version>
            <PC-Urn_software>InChI</PC-Urn_software>
            <PC-Urn_source>iupac.org</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>CSCPPACGZOOCGX-UHFFFAOYSA-N</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Log P</PC-Urn_label>
            <PC-Urn_name>XLogP3-AA</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="double">7</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>3.0</PC-Urn_version>
            <PC-Urn_source>sioc-ccbg.ac.cn</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_fval>-0.1</PC-InfoData_value_fval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Mass</PC-Urn_label>
            <PC-Urn_name>Exact</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.2</PC-Urn_version>
            <PC-Urn_software>PubChem</PC-Urn_software>
            <PC-Urn_source>ncbi.nlm.nih.gov</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>58.041864811</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Molecular Formula</PC-Urn_label>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.2</PC-Urn_version>
            <PC-Urn_software>PubChem</PC-Urn_software>
            <PC-Urn_source>ncbi.nlm.nih.gov</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>C3H6O</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Molecular Weight</PC-Urn_label>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.2</PC-Urn_version>
            <PC-Urn_software>PubChem</PC-Urn_software>
            <PC-Urn_source>ncbi.nlm.nih.gov</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>58.08</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>SMILES</PC-Urn_label>
            <PC-Urn_name>Absolute</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.3.0</PC-Urn_version>
            <PC-Urn_software>OEChem</PC-Urn_software>
            <PC-Urn_source>OpenEye Scientific Software</PC-Urn_source>
            <PC-Urn_release>2024.12.12</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>CC(=O)C</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>SMILES</PC-Urn_label>
            <PC-Urn_name>Canonical</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.3.0</PC-Urn_version>
            <PC-Urn_software>OEChem</PC-Urn_software>
            <PC-Urn_source>OpenEye Scientific Software</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>CC(=O)C</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>SMILES</PC-Urn_label>
            <PC-Urn_name>Isomeric</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.3.0</PC-Urn_version>
            <PC-Urn_software>OEChem</PC-Urn_software>
            <PC-Urn_source>OpenEye Scientific Software</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>CC(=O)C</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Topological</PC-Urn_label>
            <PC-Urn_name>Polar Surface Area</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="double">7</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_implementation>E_TPSA</PC-Urn_implementation>
            <PC-Urn_version>3.4.8.18</PC-Urn_version>
            <PC-Urn_software>Cactvs</PC-Urn_software>
            <PC-Urn_source>Xemistry GmbH</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_fval>17.1</PC-InfoData_value_fval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Weight</PC-Urn_label>
            <PC-Urn_name>MonoIsotopic</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.2</PC-Urn_version>
            <PC-Urn_software>PubChem</PC-Urn_software>
            <PC-Urn_source>ncbi.nlm.nih.gov</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>58.041864811</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
    </PC-Compound_props>
    <PC-Compound_count>
      <PC-Count>
        <PC-Count_heavy-atom>4</PC-Count_heavy-atom>
        <PC-Count_atom-chiral>0</PC-Count_atom-chiral>
        <PC-Count_atom-chiral-def>0</PC-Count_atom-chiral-def>
        <PC-Count_atom-chiral-undef>0</PC-Count_atom-chiral-undef>
        <PC-Count_bond-chiral>0</PC-Count_bond-chiral>
        <PC-Count_bond-chiral-def>0</PC-Count_bond-chiral-def>
        <PC-Count_bond-chiral-undef>0</PC-Count_bond-chiral-undef>
        <PC-Count_isotope-atom>0</PC-Count_isotope-atom>
        <PC-Count_covalent-unit>1</PC-Count_covalent-unit>
        <PC-Count_tautomers>-1</PC-Count_tautomers>
      </PC-Count>
    </PC-Compound_count>
  </PC-Compound>
</PC-Compounds>
"""

    @pytest.fixture
    def acetone_3d_file_data(self):
        return """<?xml version="1.0"?>
<PC-Compounds
    xmlns="http://www.ncbi.nlm.nih.gov"
    xmlns:xs="http://www.w3.org/2001/XMLSchema-instance"
    xs:schemaLocation="http://www.ncbi.nlm.nih.gov ftp://ftp.ncbi.nlm.nih.gov/pubchem/specifications/pubchem.xsd"
>
  <PC-Compound>
    <PC-Compound_id>
      <PC-CompoundType>
        <PC-CompoundType_id>
          <PC-CompoundType_id_cid>180</PC-CompoundType_id_cid>
        </PC-CompoundType_id>
      </PC-CompoundType>
    </PC-Compound_id>
    <PC-Compound_atoms>
      <PC-Atoms>
        <PC-Atoms_aid>
          <PC-Atoms_aid_E>1</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>2</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>3</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>4</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>5</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>6</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>7</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>8</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>9</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>10</PC-Atoms_aid_E>
        </PC-Atoms_aid>
        <PC-Atoms_element>
          <PC-Element value="o">8</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
        </PC-Atoms_element>
      </PC-Atoms>
    </PC-Compound_atoms>
    <PC-Compound_bonds>
      <PC-Bonds>
        <PC-Bonds_aid1>
          <PC-Bonds_aid1_E>1</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>2</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>2</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>3</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>3</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>3</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>4</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>4</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>4</PC-Bonds_aid1_E>
        </PC-Bonds_aid1>
        <PC-Bonds_aid2>
          <PC-Bonds_aid2_E>2</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>3</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>4</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>5</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>6</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>7</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>8</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>9</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>10</PC-Bonds_aid2_E>
        </PC-Bonds_aid2>
        <PC-Bonds_order>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
        </PC-Bonds_order>
      </PC-Bonds>
    </PC-Compound_bonds>
    <PC-Compound_coords>
      <PC-Coordinates>
        <PC-Coordinates_type>
          <PC-CoordinateType value="threed">2</PC-CoordinateType>
          <PC-CoordinateType value="computed">5</PC-CoordinateType>
          <PC-CoordinateType value="units-angstroms">10</PC-CoordinateType>
        </PC-Coordinates_type>
        <PC-Coordinates_aid>
          <PC-Coordinates_aid_E>1</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>2</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>3</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>4</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>5</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>6</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>7</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>8</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>9</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>10</PC-Coordinates_aid_E>
        </PC-Coordinates_aid>
        <PC-Coordinates_conformers>
          <PC-Conformer>
            <PC-Conformer_x>
              <PC-Conformer_x_E>0.0003</PC-Conformer_x_E>
              <PC-Conformer_x_E>0</PC-Conformer_x_E>
              <PC-Conformer_x_E>1.281</PC-Conformer_x_E>
              <PC-Conformer_x_E>-1.2813</PC-Conformer_x_E>
              <PC-Conformer_x_E>1.3279</PC-Conformer_x_E>
              <PC-Conformer_x_E>1.326</PC-Conformer_x_E>
              <PC-Conformer_x_E>2.1351</PC-Conformer_x_E>
              <PC-Conformer_x_E>-2.1352</PC-Conformer_x_E>
              <PC-Conformer_x_E>-1.3284</PC-Conformer_x_E>
              <PC-Conformer_x_E>-1.3266</PC-Conformer_x_E>
            </PC-Conformer_x>
            <PC-Conformer_y>
              <PC-Conformer_y_E>-1.3171</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.0872</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.7024</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.7019</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.3235</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.3282</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.0196</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.0187</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.323</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.3278</PC-Conformer_y_E>
            </PC-Conformer_y>
            <PC-Conformer_z>
              <PC-Conformer_z_E>-0.0002</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.0006</PC-Conformer_z_E>
              <PC-Conformer_z_E>-0.0002</PC-Conformer_z_E>
              <PC-Conformer_z_E>-0.0002</PC-Conformer_z_E>
              <PC-Conformer_z_E>-0.898</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.8945</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.0027</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.0027</PC-Conformer_z_E>
              <PC-Conformer_z_E>-0.898</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.8945</PC-Conformer_z_E>
            </PC-Conformer_z>
            <PC-Conformer_data>
              <PC-InfoData>
                <PC-InfoData_urn>
                  <PC-Urn>
                    <PC-Urn_label>Conformer</PC-Urn_label>
                    <PC-Urn_name>ID</PC-Urn_name>
                    <PC-Urn_datatype>
                      <PC-UrnDataType value="uint64">11</PC-UrnDataType>
                    </PC-Urn_datatype>
                    <PC-Urn_version>2.1</PC-Urn_version>
                    <PC-Urn_software>PubChem</PC-Urn_software>
                    <PC-Urn_source>ncbi.nlm.nih.gov</PC-Urn_source>
                    <PC-Urn_release>2009.12.11</PC-Urn_release>
                  </PC-Urn>
                </PC-InfoData_urn>
                <PC-InfoData_value>
                  <PC-InfoData_value_sval>000000B400000001</PC-InfoData_value_sval>
                </PC-InfoData_value>
              </PC-InfoData>
              <PC-InfoData>
                <PC-InfoData_urn>
                  <PC-Urn>
                    <PC-Urn_label>Energy</PC-Urn_label>
                    <PC-Urn_name>MMFF94 NoEstat</PC-Urn_name>
                    <PC-Urn_datatype>
                      <PC-UrnDataType value="double">7</PC-UrnDataType>
                    </PC-Urn_datatype>
                    <PC-Urn_version>1.6.0</PC-Urn_version>
                    <PC-Urn_software>Szybki</PC-Urn_software>
                    <PC-Urn_source>openeye.com</PC-Urn_source>
                    <PC-Urn_release>2012.01.18</PC-Urn_release>
                  </PC-Urn>
                </PC-InfoData_urn>
                <PC-InfoData_value>
                  <PC-InfoData_value_fval>1.6523</PC-InfoData_value_fval>
                </PC-InfoData_value>
              </PC-InfoData>
              <PC-InfoData>
                <PC-InfoData_urn>
                  <PC-Urn>
                    <PC-Urn_label>Feature</PC-Urn_label>
                    <PC-Urn_name>Self Overlap</PC-Urn_name>
                    <PC-Urn_datatype>
                      <PC-UrnDataType value="double">7</PC-UrnDataType>
                    </PC-Urn_datatype>
                    <PC-Urn_version>2.1</PC-Urn_version>
                    <PC-Urn_software>PubChem</PC-Urn_software>
                    <PC-Urn_source>ncbi.nlm.nih.gov</PC-Urn_source>
                    <PC-Urn_release>2012.01.18</PC-Urn_release>
                  </PC-Urn>
                </PC-InfoData_urn>
                <PC-InfoData_value>
                  <PC-InfoData_value_fval>5.074</PC-InfoData_value_fval>
                </PC-InfoData_value>
              </PC-InfoData>
              <PC-InfoData>
                <PC-InfoData_urn>
                  <PC-Urn>
                    <PC-Urn_label>Fingerprint</PC-Urn_label>
                    <PC-Urn_name>Shape</PC-Urn_name>
                    <PC-Urn_datatype>
                      <PC-UrnDataType value="stringlist">2</PC-UrnDataType>
                    </PC-Urn_datatype>
                    <PC-Urn_version>2.1</PC-Urn_version>
                    <PC-Urn_software>PubChem</PC-Urn_software>
                    <PC-Urn_source>ncbi.nlm.nih.gov</PC-Urn_source>
                    <PC-Urn_release>2012.11.26</PC-Urn_release>
                  </PC-Urn>
                </PC-InfoData_urn>
                <PC-InfoData_value>
                  <PC-InfoData_value_slist>
                    <PC-InfoData_value_slist_E>139733 1 9290717673991302211</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>20096714 4 18411138026090193976</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>21015797 1 9007056889502236007</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>5943 1 13610069792663804549</PC-InfoData_value_slist_E>
                  </PC-InfoData_value_slist>
                </PC-InfoData_value>
              </PC-InfoData>
              <PC-InfoData>
                <PC-InfoData_urn>
                  <PC-Urn>
                    <PC-Urn_label>Shape</PC-Urn_label>
                    <PC-Urn_name>Multipoles</PC-Urn_name>
                    <PC-Urn_datatype>
                      <PC-UrnDataType value="doublevec">8</PC-UrnDataType>
                    </PC-Urn_datatype>
                    <PC-Urn_version>1.8.1</PC-Urn_version>
                    <PC-Urn_software>OEShape</PC-Urn_software>
                    <PC-Urn_source>openeye.com</PC-Urn_source>
                    <PC-Urn_release>2012.01.18</PC-Urn_release>
                  </PC-Urn>
                </PC-InfoData_urn>
                <PC-InfoData_value>
                  <PC-InfoData_value_fvec>
                    <PC-InfoData_value_fvec_E>76.45</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>1.48</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>1.18</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>0.59</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>0</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>0.33</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>0</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>-0.56</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>0</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>0</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>0</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>0</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>-0.03</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>0</PC-InfoData_value_fvec_E>
                  </PC-InfoData_value_fvec>
                </PC-InfoData_value>
              </PC-InfoData>
              <PC-InfoData>
                <PC-InfoData_urn>
                  <PC-Urn>
                    <PC-Urn_label>Shape</PC-Urn_label>
                    <PC-Urn_name>Self Overlap</PC-Urn_name>
                    <PC-Urn_datatype>
                      <PC-UrnDataType value="double">7</PC-UrnDataType>
                    </PC-Urn_datatype>
                    <PC-Urn_version>2.1</PC-Urn_version>
                    <PC-Urn_software>PubChem</PC-Urn_software>
                    <PC-Urn_source>ncbi.nlm.nih.gov</PC-Urn_source>
                    <PC-Urn_release>2012.01.18</PC-Urn_release>
                  </PC-Urn>
                </PC-InfoData_urn>
                <PC-InfoData_value>
                  <PC-InfoData_value_fval>128.735</PC-InfoData_value_fval>
                </PC-InfoData_value>
              </PC-InfoData>
              <PC-InfoData>
                <PC-InfoData_urn>
                  <PC-Urn>
                    <PC-Urn_label>Shape</PC-Urn_label>
                    <PC-Urn_name>Volume</PC-Urn_name>
                    <PC-Urn_datatype>
                      <PC-UrnDataType value="double">7</PC-UrnDataType>
                    </PC-Urn_datatype>
                    <PC-Urn_version>1.8.1</PC-Urn_version>
                    <PC-Urn_software>OEShape</PC-Urn_software>
                    <PC-Urn_source>openeye.com</PC-Urn_source>
                    <PC-Urn_release>2012.01.18</PC-Urn_release>
                  </PC-Urn>
                </PC-InfoData_urn>
                <PC-InfoData_value>
                  <PC-InfoData_value_fval>52.8</PC-InfoData_value_fval>
                </PC-InfoData_value>
              </PC-InfoData>
            </PC-Conformer_data>
          </PC-Conformer>
        </PC-Coordinates_conformers>
        <PC-Coordinates_data>
          <PC-InfoData>
            <PC-InfoData_urn>
              <PC-Urn>
                <PC-Urn_label>Conformer</PC-Urn_label>
                <PC-Urn_name>RMSD</PC-Urn_name>
                <PC-Urn_datatype>
                  <PC-UrnDataType value="double">7</PC-UrnDataType>
                </PC-Urn_datatype>
                <PC-Urn_release>2009.12.11</PC-Urn_release>
              </PC-Urn>
            </PC-InfoData_urn>
            <PC-InfoData_value>
              <PC-InfoData_value_fval>0.4</PC-InfoData_value_fval>
            </PC-InfoData_value>
          </PC-InfoData>
          <PC-InfoData>
            <PC-InfoData_urn>
              <PC-Urn>
                <PC-Urn_label>Diverse Conformer</PC-Urn_label>
                <PC-Urn_name>ID List</PC-Urn_name>
                <PC-Urn_datatype>
                  <PC-UrnDataType value="uintvec">6</PC-UrnDataType>
                </PC-Urn_datatype>
                <PC-Urn_release>2010.05.05</PC-Urn_release>
              </PC-Urn>
            </PC-InfoData_urn>
            <PC-InfoData_value>
              <PC-InfoData_value_ivec>
                <PC-InfoData_value_ivec_E>1</PC-InfoData_value_ivec_E>
              </PC-InfoData_value_ivec>
            </PC-InfoData_value>
          </PC-InfoData>
        </PC-Coordinates_data>
      </PC-Coordinates>
    </PC-Compound_coords>
    <PC-Compound_props>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Charge</PC-Urn_label>
            <PC-Urn_name>MMFF94 Partial</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="stringlist">2</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>1.9.0</PC-Urn_version>
            <PC-Urn_software>OEChem</PC-Urn_software>
            <PC-Urn_source>openeye.com</PC-Urn_source>
            <PC-Urn_release>2012.11.26</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_slist>
            <PC-InfoData_value_slist_E>4</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>1 -0.57</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>2 0.45</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>3 0.06</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>4 0.06</PC-InfoData_value_slist_E>
          </PC-InfoData_value_slist>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Count</PC-Urn_label>
            <PC-Urn_name>Effective Rotor</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="double">7</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>1.7.6</PC-Urn_version>
            <PC-Urn_software>OEChem</PC-Urn_software>
            <PC-Urn_source>ncbi.nlm.nih.gov</PC-Urn_source>
            <PC-Urn_release>2012.01.18</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_fval>0</PC-InfoData_value_fval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Features</PC-Urn_label>
            <PC-Urn_name>Pharmacophore</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="stringlist">2</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_parameters>ImplicitMillsDean merged</PC-Urn_parameters>
            <PC-Urn_version>1.8.3</PC-Urn_version>
            <PC-Urn_software>OEShape</PC-Urn_software>
            <PC-Urn_source>openeye.com</PC-Urn_source>
            <PC-Urn_release>2012.11.26</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_slist>
            <PC-InfoData_value_slist_E>1</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>1 1 acceptor</PC-InfoData_value_slist_E>
          </PC-InfoData_value_slist>
        </PC-InfoData_value>
      </PC-InfoData>
    </PC-Compound_props>
    <PC-Compound_count>
      <PC-Count>
        <PC-Count_heavy-atom>4</PC-Count_heavy-atom>
        <PC-Count_atom-chiral>0</PC-Count_atom-chiral>
        <PC-Count_atom-chiral-def>0</PC-Count_atom-chiral-def>
        <PC-Count_atom-chiral-undef>0</PC-Count_atom-chiral-undef>
        <PC-Count_bond-chiral>0</PC-Count_bond-chiral>
        <PC-Count_bond-chiral-def>0</PC-Count_bond-chiral-def>
        <PC-Count_bond-chiral-undef>0</PC-Count_bond-chiral-undef>
        <PC-Count_isotope-atom>0</PC-Count_isotope-atom>
        <PC-Count_covalent-unit>1</PC-Count_covalent-unit>
        <PC-Count_tautomers>2</PC-Count_tautomers>
      </PC-Count>
    </PC-Compound_count>
  </PC-Compound>
</PC-Compounds>
"""

    @pytest.fixture
    def morphine_2d_file_data(self):
        return """<?xml version="1.0"?>
<PC-Compounds
    xmlns="http://www.ncbi.nlm.nih.gov"
    xmlns:xs="http://www.w3.org/2001/XMLSchema-instance"
    xs:schemaLocation="http://www.ncbi.nlm.nih.gov ftp://ftp.ncbi.nlm.nih.gov/pubchem/specifications/pubchem.xsd"
>
  <PC-Compound>
    <PC-Compound_id>
      <PC-CompoundType>
        <PC-CompoundType_id>
          <PC-CompoundType_id_cid>5288826</PC-CompoundType_id_cid>
        </PC-CompoundType_id>
      </PC-CompoundType>
    </PC-Compound_id>
    <PC-Compound_atoms>
      <PC-Atoms>
        <PC-Atoms_aid>
          <PC-Atoms_aid_E>1</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>2</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>3</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>4</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>5</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>6</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>7</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>8</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>9</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>10</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>11</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>12</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>13</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>14</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>15</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>16</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>17</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>18</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>19</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>20</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>21</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>22</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>23</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>24</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>25</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>26</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>27</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>28</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>29</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>30</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>31</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>32</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>33</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>34</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>35</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>36</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>37</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>38</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>39</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>40</PC-Atoms_aid_E>
        </PC-Atoms_aid>
        <PC-Atoms_element>
          <PC-Element value="o">8</PC-Element>
          <PC-Element value="o">8</PC-Element>
          <PC-Element value="o">8</PC-Element>
          <PC-Element value="n">7</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
        </PC-Atoms_element>
      </PC-Atoms>
    </PC-Compound_atoms>
    <PC-Compound_bonds>
      <PC-Bonds>
        <PC-Bonds_aid1>
          <PC-Bonds_aid1_E>1</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>1</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>2</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>2</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>3</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>3</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>4</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>4</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>4</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>5</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>5</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>5</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>5</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>6</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>6</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>6</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>7</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>7</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>8</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>8</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>9</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>9</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>9</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>10</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>10</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>11</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>11</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>11</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>12</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>12</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>13</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>14</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>14</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>15</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>15</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>16</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>17</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>18</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>18</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>18</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>19</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>19</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>20</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>21</PC-Bonds_aid1_E>
        </PC-Bonds_aid1>
        <PC-Bonds_aid2>
          <PC-Bonds_aid2_E>8</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>16</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>14</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>39</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>20</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>40</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>7</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>12</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>18</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>6</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>8</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>9</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>10</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>7</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>15</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>22</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>11</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>23</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>14</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>24</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>12</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>25</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>26</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>13</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>16</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>13</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>27</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>28</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>29</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>30</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>19</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>17</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>31</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>17</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>32</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>20</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>33</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>34</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>35</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>36</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>21</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>37</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>21</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>38</PC-Bonds_aid2_E>
        </PC-Bonds_aid2>
        <PC-Bonds_order>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
        </PC-Bonds_order>
      </PC-Bonds>
    </PC-Compound_bonds>
    <PC-Compound_stereo>
      <PC-StereoCenter>
        <PC-StereoCenter_tetrahedral>
          <PC-StereoTetrahedral>
            <PC-StereoTetrahedral_center>5</PC-StereoTetrahedral_center>
            <PC-StereoTetrahedral_above>6</PC-StereoTetrahedral_above>
            <PC-StereoTetrahedral_top>8</PC-StereoTetrahedral_top>
            <PC-StereoTetrahedral_bottom>9</PC-StereoTetrahedral_bottom>
            <PC-StereoTetrahedral_below>10</PC-StereoTetrahedral_below>
            <PC-StereoTetrahedral_parity value="clockwise">1</PC-StereoTetrahedral_parity>
            <PC-StereoTetrahedral_type value="tetrahedral">1</PC-StereoTetrahedral_type>
          </PC-StereoTetrahedral>
        </PC-StereoCenter_tetrahedral>
      </PC-StereoCenter>
      <PC-StereoCenter>
        <PC-StereoCenter_tetrahedral>
          <PC-StereoTetrahedral>
            <PC-StereoTetrahedral_center>6</PC-StereoTetrahedral_center>
            <PC-StereoTetrahedral_above>5</PC-StereoTetrahedral_above>
            <PC-StereoTetrahedral_top>15</PC-StereoTetrahedral_top>
            <PC-StereoTetrahedral_bottom>7</PC-StereoTetrahedral_bottom>
            <PC-StereoTetrahedral_below>22</PC-StereoTetrahedral_below>
            <PC-StereoTetrahedral_parity value="counterclockwise">2</PC-StereoTetrahedral_parity>
            <PC-StereoTetrahedral_type value="tetrahedral">1</PC-StereoTetrahedral_type>
          </PC-StereoTetrahedral>
        </PC-StereoCenter_tetrahedral>
      </PC-StereoCenter>
      <PC-StereoCenter>
        <PC-StereoCenter_tetrahedral>
          <PC-StereoTetrahedral>
            <PC-StereoTetrahedral_center>7</PC-StereoTetrahedral_center>
            <PC-StereoTetrahedral_above>4</PC-StereoTetrahedral_above>
            <PC-StereoTetrahedral_top>6</PC-StereoTetrahedral_top>
            <PC-StereoTetrahedral_bottom>11</PC-StereoTetrahedral_bottom>
            <PC-StereoTetrahedral_below>23</PC-StereoTetrahedral_below>
            <PC-StereoTetrahedral_parity value="clockwise">1</PC-StereoTetrahedral_parity>
            <PC-StereoTetrahedral_type value="tetrahedral">1</PC-StereoTetrahedral_type>
          </PC-StereoTetrahedral>
        </PC-StereoCenter_tetrahedral>
      </PC-StereoCenter>
      <PC-StereoCenter>
        <PC-StereoCenter_tetrahedral>
          <PC-StereoTetrahedral>
            <PC-StereoTetrahedral_center>8</PC-StereoTetrahedral_center>
            <PC-StereoTetrahedral_above>1</PC-StereoTetrahedral_above>
            <PC-StereoTetrahedral_top>14</PC-StereoTetrahedral_top>
            <PC-StereoTetrahedral_bottom>5</PC-StereoTetrahedral_bottom>
            <PC-StereoTetrahedral_below>24</PC-StereoTetrahedral_below>
            <PC-StereoTetrahedral_parity value="counterclockwise">2</PC-StereoTetrahedral_parity>
            <PC-StereoTetrahedral_type value="tetrahedral">1</PC-StereoTetrahedral_type>
          </PC-StereoTetrahedral>
        </PC-StereoCenter_tetrahedral>
      </PC-StereoCenter>
      <PC-StereoCenter>
        <PC-StereoCenter_tetrahedral>
          <PC-StereoTetrahedral>
            <PC-StereoTetrahedral_center>14</PC-StereoTetrahedral_center>
            <PC-StereoTetrahedral_above>2</PC-StereoTetrahedral_above>
            <PC-StereoTetrahedral_top>17</PC-StereoTetrahedral_top>
            <PC-StereoTetrahedral_bottom>8</PC-StereoTetrahedral_bottom>
            <PC-StereoTetrahedral_below>31</PC-StereoTetrahedral_below>
            <PC-StereoTetrahedral_parity value="counterclockwise">2</PC-StereoTetrahedral_parity>
            <PC-StereoTetrahedral_type value="tetrahedral">1</PC-StereoTetrahedral_type>
          </PC-StereoTetrahedral>
        </PC-StereoCenter_tetrahedral>
      </PC-StereoCenter>
    </PC-Compound_stereo>
    <PC-Compound_coords>
      <PC-Coordinates>
        <PC-Coordinates_type>
          <PC-CoordinateType value="twod">1</PC-CoordinateType>
          <PC-CoordinateType value="computed">5</PC-CoordinateType>
          <PC-CoordinateType value="units-unknown">255</PC-CoordinateType>
        </PC-Coordinates_type>
        <PC-Coordinates_aid>
          <PC-Coordinates_aid_E>1</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>2</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>3</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>4</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>5</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>6</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>7</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>8</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>9</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>10</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>11</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>12</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>13</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>14</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>15</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>16</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>17</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>18</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>19</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>20</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>21</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>22</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>23</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>24</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>25</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>26</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>27</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>28</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>29</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>30</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>31</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>32</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>33</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>34</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>35</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>36</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>37</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>38</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>39</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>40</PC-Coordinates_aid_E>
        </PC-Coordinates_aid>
        <PC-Coordinates_conformers>
          <PC-Conformer>
            <PC-Conformer_x>
              <PC-Conformer_x_E>2.2314</PC-Conformer_x_E>
              <PC-Conformer_x_E>2</PC-Conformer_x_E>
              <PC-Conformer_x_E>2</PC-Conformer_x_E>
              <PC-Conformer_x_E>6.1607</PC-Conformer_x_E>
              <PC-Conformer_x_E>3.6897</PC-Conformer_x_E>
              <PC-Conformer_x_E>4.5133</PC-Conformer_x_E>
              <PC-Conformer_x_E>5.337</PC-Conformer_x_E>
              <PC-Conformer_x_E>2.866</PC-Conformer_x_E>
              <PC-Conformer_x_E>4.2392</PC-Conformer_x_E>
              <PC-Conformer_x_E>3.6897</PC-Conformer_x_E>
              <PC-Conformer_x_E>5.337</PC-Conformer_x_E>
              <PC-Conformer_x_E>5.5918</PC-Conformer_x_E>
              <PC-Conformer_x_E>4.5133</PC-Conformer_x_E>
              <PC-Conformer_x_E>2.866</PC-Conformer_x_E>
              <PC-Conformer_x_E>4.5133</PC-Conformer_x_E>
              <PC-Conformer_x_E>2.866</PC-Conformer_x_E>
              <PC-Conformer_x_E>3.6897</PC-Conformer_x_E>
              <PC-Conformer_x_E>6.8418</PC-Conformer_x_E>
              <PC-Conformer_x_E>4.5133</PC-Conformer_x_E>
              <PC-Conformer_x_E>2.866</PC-Conformer_x_E>
              <PC-Conformer_x_E>3.6897</PC-Conformer_x_E>
              <PC-Conformer_x_E>5.0597</PC-Conformer_x_E>
              <PC-Conformer_x_E>5.6284</PC-Conformer_x_E>
              <PC-Conformer_x_E>2.0496</PC-Conformer_x_E>
              <PC-Conformer_x_E>4.376</PC-Conformer_x_E>
              <PC-Conformer_x_E>3.6795</PC-Conformer_x_E>
              <PC-Conformer_x_E>5.9476</PC-Conformer_x_E>
              <PC-Conformer_x_E>5.549</PC-Conformer_x_E>
              <PC-Conformer_x_E>6.184</PC-Conformer_x_E>
              <PC-Conformer_x_E>5.4989</PC-Conformer_x_E>
              <PC-Conformer_x_E>2.866</PC-Conformer_x_E>
              <PC-Conformer_x_E>5.0503</PC-Conformer_x_E>
              <PC-Conformer_x_E>3.6897</PC-Conformer_x_E>
              <PC-Conformer_x_E>6.3879</PC-Conformer_x_E>
              <PC-Conformer_x_E>7.2641</PC-Conformer_x_E>
              <PC-Conformer_x_E>7.2957</PC-Conformer_x_E>
              <PC-Conformer_x_E>5.0503</PC-Conformer_x_E>
              <PC-Conformer_x_E>3.6897</PC-Conformer_x_E>
              <PC-Conformer_x_E>2</PC-Conformer_x_E>
              <PC-Conformer_x_E>2</PC-Conformer_x_E>
            </PC-Conformer_x>
            <PC-Conformer_y>
              <PC-Conformer_y_E>0.0528</PC-Conformer_y_E>
              <PC-Conformer_y_E>-2.4021</PC-Conformer_y_E>
              <PC-Conformer_y_E>2.4021</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.9511</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.4755</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.9511</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.4755</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.9511</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.2219</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.4755</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.4755</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.2219</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.9511</PC-Conformer_y_E>
              <PC-Conformer_y_E>-1.9022</PC-Conformer_y_E>
              <PC-Conformer_y_E>-1.9022</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.9511</PC-Conformer_y_E>
              <PC-Conformer_y_E>-2.3777</PC-Conformer_y_E>
              <PC-Conformer_y_E>-1.6832</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.9022</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.9022</PC-Conformer_y_E>
              <PC-Conformer_y_E>2.3777</PC-Conformer_y_E>
              <PC-Conformer_y_E>-1.6022</PC-Conformer_y_E>
              <PC-Conformer_y_E>-1.274</PC-Conformer_y_E>
              <PC-Conformer_y_E>-1.1875</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.8266</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.4887</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.3679</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.0581</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.4057</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.8349</PC-Conformer_y_E>
              <PC-Conformer_y_E>-2.5222</PC-Conformer_y_E>
              <PC-Conformer_y_E>-2.2122</PC-Conformer_y_E>
              <PC-Conformer_y_E>-2.9977</PC-Conformer_y_E>
              <PC-Conformer_y_E>-2.1055</PC-Conformer_y_E>
              <PC-Conformer_y_E>-2.1371</PC-Conformer_y_E>
              <PC-Conformer_y_E>-1.2609</PC-Conformer_y_E>
              <PC-Conformer_y_E>2.2122</PC-Conformer_y_E>
              <PC-Conformer_y_E>2.9977</PC-Conformer_y_E>
              <PC-Conformer_y_E>-3.0222</PC-Conformer_y_E>
              <PC-Conformer_y_E>3.0222</PC-Conformer_y_E>
            </PC-Conformer_y>
            <PC-Conformer_style>
              <PC-DrawAnnotations>
                <PC-DrawAnnotations_annotation>
                  <PC-BondAnnotation value="wedge-up">5</PC-BondAnnotation>
                  <PC-BondAnnotation value="wedge-up">5</PC-BondAnnotation>
                  <PC-BondAnnotation value="wedge-down">6</PC-BondAnnotation>
                  <PC-BondAnnotation value="wedge-up">5</PC-BondAnnotation>
                  <PC-BondAnnotation value="aromatic">8</PC-BondAnnotation>
                  <PC-BondAnnotation value="aromatic">8</PC-BondAnnotation>
                  <PC-BondAnnotation value="aromatic">8</PC-BondAnnotation>
                  <PC-BondAnnotation value="wedge-down">6</PC-BondAnnotation>
                  <PC-BondAnnotation value="aromatic">8</PC-BondAnnotation>
                  <PC-BondAnnotation value="aromatic">8</PC-BondAnnotation>
                  <PC-BondAnnotation value="aromatic">8</PC-BondAnnotation>
                </PC-DrawAnnotations_annotation>
                <PC-DrawAnnotations_aid1>
                  <PC-DrawAnnotations_aid1_E>5</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>6</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>7</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>8</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>10</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>10</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>13</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>14</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>16</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>19</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>20</PC-DrawAnnotations_aid1_E>
                </PC-DrawAnnotations_aid1>
                <PC-DrawAnnotations_aid2>
                  <PC-DrawAnnotations_aid2_E>9</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>22</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>23</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>24</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>13</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>16</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>19</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>2</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>20</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>21</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>21</PC-DrawAnnotations_aid2_E>
                </PC-DrawAnnotations_aid2>
              </PC-DrawAnnotations>
            </PC-Conformer_style>
          </PC-Conformer>
        </PC-Coordinates_conformers>
      </PC-Coordinates>
    </PC-Compound_coords>
    <PC-Compound_charge>0</PC-Compound_charge>
    <PC-Compound_props>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Compound</PC-Urn_label>
            <PC-Urn_name>Canonicalized</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="uint">5</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_ival>1</PC-InfoData_value_ival>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Compound Complexity</PC-Urn_label>
            <PC-Urn_datatype>
              <PC-UrnDataType value="double">7</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_implementation>E_COMPLEXITY</PC-Urn_implementation>
            <PC-Urn_version>3.4.8.18</PC-Urn_version>
            <PC-Urn_software>Cactvs</PC-Urn_software>
            <PC-Urn_source>Xemistry GmbH</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_fval>494</PC-InfoData_value_fval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Count</PC-Urn_label>
            <PC-Urn_name>Hydrogen Bond Acceptor</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="uint">5</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_implementation>E_NHACCEPTORS</PC-Urn_implementation>
            <PC-Urn_version>3.4.8.18</PC-Urn_version>
            <PC-Urn_software>Cactvs</PC-Urn_software>
            <PC-Urn_source>Xemistry GmbH</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_ival>4</PC-InfoData_value_ival>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Count</PC-Urn_label>
            <PC-Urn_name>Hydrogen Bond Donor</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="uint">5</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_implementation>E_NHDONORS</PC-Urn_implementation>
            <PC-Urn_version>3.4.8.18</PC-Urn_version>
            <PC-Urn_software>Cactvs</PC-Urn_software>
            <PC-Urn_source>Xemistry GmbH</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_ival>2</PC-InfoData_value_ival>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Count</PC-Urn_label>
            <PC-Urn_name>Rotatable Bond</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="uint">5</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_implementation>E_NROTBONDS</PC-Urn_implementation>
            <PC-Urn_version>3.4.8.18</PC-Urn_version>
            <PC-Urn_software>Cactvs</PC-Urn_software>
            <PC-Urn_source>Xemistry GmbH</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_ival>0</PC-InfoData_value_ival>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Fingerprint</PC-Urn_label>
            <PC-Urn_name>SubStructure Keys</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="fingerprint">16</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_parameters>extended 2</PC-Urn_parameters>
            <PC-Urn_implementation>E_SCREEN</PC-Urn_implementation>
            <PC-Urn_version>3.4.8.18</PC-Urn_version>
            <PC-Urn_software>Cactvs</PC-Urn_software>
            <PC-Urn_source>Xemistry GmbH</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_binary>00000371E07A30000000000000000000000000000001200000003C6081000000160048C10000001E00000800000F3CE198063206830006008002204200000208002020000888000E88880D362286B11B867823A4C0118BB807B0F0F70FA000010000184000D000068000348000000000000000</PC-InfoData_value_binary>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>IUPAC Name</PC-Urn_label>
            <PC-Urn_name>Allowed</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.7.0</PC-Urn_version>
            <PC-Urn_software>Lexichem TK</PC-Urn_software>
            <PC-Urn_source>OpenEye Scientific Software</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>(4R,4aR,7S,7aR,12bS)-3-methyl-2,4,4a,7,7a,13-hexahydro-1H-4,12-methanobenzofuro[3,2-e]isoquinoline-7,9-diol</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>IUPAC Name</PC-Urn_label>
            <PC-Urn_name>CAS-like Style</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.7.0</PC-Urn_version>
            <PC-Urn_software>Lexichem TK</PC-Urn_software>
            <PC-Urn_source>OpenEye Scientific Software</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>(4R,4aR,7S,7aR,12bS)-3-methyl-2,4,4a,7,7a,13-hexahydro-1H-4,12-methanobenzofuro[3,2-e]isoquinoline-7,9-diol</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>IUPAC Name</PC-Urn_label>
            <PC-Urn_name>Markup</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.7.0</PC-Urn_version>
            <PC-Urn_software>Lexichem TK</PC-Urn_software>
            <PC-Urn_source>OpenEye Scientific Software</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>(4&lt;I&gt;R&lt;/I&gt;,4&lt;I&gt;a&lt;/I&gt;&lt;I&gt;R&lt;/I&gt;,7&lt;I&gt;S&lt;/I&gt;,7&lt;I&gt;a&lt;/I&gt;&lt;I&gt;R&lt;/I&gt;,12&lt;I&gt;b&lt;/I&gt;&lt;I&gt;S&lt;/I&gt;)-3-methyl-2,4,4&lt;I&gt;a&lt;/I&gt;,7,7&lt;I&gt;a&lt;/I&gt;,13-hexahydro-1&lt;I&gt;H&lt;/I&gt;-4,12-methanobenzofuro[3,2-e]isoquinoline-7,9-diol</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>IUPAC Name</PC-Urn_label>
            <PC-Urn_name>Preferred</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.7.0</PC-Urn_version>
            <PC-Urn_software>Lexichem TK</PC-Urn_software>
            <PC-Urn_source>OpenEye Scientific Software</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>(4R,4aR,7S,7aR,12bS)-3-methyl-2,4,4a,7,7a,13-hexahydro-1H-4,12-methanobenzofuro[3,2-e]isoquinoline-7,9-diol</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>IUPAC Name</PC-Urn_label>
            <PC-Urn_name>Systematic</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.7.0</PC-Urn_version>
            <PC-Urn_software>Lexichem TK</PC-Urn_software>
            <PC-Urn_source>OpenEye Scientific Software</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>(4R,4aR,7S,7aR,12bS)-3-methyl-2,4,4a,7,7a,13-hexahydro-1H-4,12-methanobenzofuro[3,2-e]isoquinoline-7,9-diol</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>IUPAC Name</PC-Urn_label>
            <PC-Urn_name>Traditional</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.7.0</PC-Urn_version>
            <PC-Urn_software>Lexichem TK</PC-Urn_software>
            <PC-Urn_source>OpenEye Scientific Software</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>(4R,4aR,7S,7aR,12bS)-3-methyl-2,4,4a,7,7a,13-hexahydro-1H-4,12-methanobenzofuro[3,2-e]isoquinoline-7,9-diol</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>InChI</PC-Urn_label>
            <PC-Urn_name>Standard</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>1.0.6</PC-Urn_version>
            <PC-Urn_software>InChI</PC-Urn_software>
            <PC-Urn_source>iupac.org</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>InChI=1S/C17H19NO3/c1-18-7-6-17-10-3-5-13(20)16(17)21-15-12(19)4-2-9(14(15)17)8-11(10)18/h2-5,10-11,13,16,19-20H,6-8H2,1H3/t10-,11+,13-,16-,17-/m0/s1</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>InChIKey</PC-Urn_label>
            <PC-Urn_name>Standard</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>1.0.6</PC-Urn_version>
            <PC-Urn_software>InChI</PC-Urn_software>
            <PC-Urn_source>iupac.org</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>BQJCRHHNABKAKU-KBQPJGBKSA-N</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Log P</PC-Urn_label>
            <PC-Urn_name>XLogP3</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="double">7</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>3.0</PC-Urn_version>
            <PC-Urn_source>sioc-ccbg.ac.cn</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_fval>0.8</PC-InfoData_value_fval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Mass</PC-Urn_label>
            <PC-Urn_name>Exact</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.2</PC-Urn_version>
            <PC-Urn_software>PubChem</PC-Urn_software>
            <PC-Urn_source>ncbi.nlm.nih.gov</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>285.13649347</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Molecular Formula</PC-Urn_label>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.2</PC-Urn_version>
            <PC-Urn_software>PubChem</PC-Urn_software>
            <PC-Urn_source>ncbi.nlm.nih.gov</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>C17H19NO3</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Molecular Weight</PC-Urn_label>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.2</PC-Urn_version>
            <PC-Urn_software>PubChem</PC-Urn_software>
            <PC-Urn_source>ncbi.nlm.nih.gov</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>285.34</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>SMILES</PC-Urn_label>
            <PC-Urn_name>Absolute</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.3.0</PC-Urn_version>
            <PC-Urn_software>OEChem</PC-Urn_software>
            <PC-Urn_source>OpenEye Scientific Software</PC-Urn_source>
            <PC-Urn_release>2024.12.12</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>CN1CC[C@]23[C@@H]4[C@H]1CC5=C2C(=C(C=C5)O)O[C@H]3[C@H](C=C4)O</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>SMILES</PC-Urn_label>
            <PC-Urn_name>Canonical</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.3.0</PC-Urn_version>
            <PC-Urn_software>OEChem</PC-Urn_software>
            <PC-Urn_source>OpenEye Scientific Software</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>CN1CCC23C4C1CC5=C2C(=C(C=C5)O)OC3C(C=C4)O</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>SMILES</PC-Urn_label>
            <PC-Urn_name>Isomeric</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.3.0</PC-Urn_version>
            <PC-Urn_software>OEChem</PC-Urn_software>
            <PC-Urn_source>OpenEye Scientific Software</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>CN1CC[C@]23[C@@H]4[C@H]1CC5=C2C(=C(C=C5)O)O[C@H]3[C@H](C=C4)O</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Topological</PC-Urn_label>
            <PC-Urn_name>Polar Surface Area</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="double">7</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_implementation>E_TPSA</PC-Urn_implementation>
            <PC-Urn_version>3.4.8.18</PC-Urn_version>
            <PC-Urn_software>Cactvs</PC-Urn_software>
            <PC-Urn_source>Xemistry GmbH</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_fval>52.9</PC-InfoData_value_fval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Weight</PC-Urn_label>
            <PC-Urn_name>MonoIsotopic</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.2</PC-Urn_version>
            <PC-Urn_software>PubChem</PC-Urn_software>
            <PC-Urn_source>ncbi.nlm.nih.gov</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>285.13649347</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
    </PC-Compound_props>
    <PC-Compound_count>
      <PC-Count>
        <PC-Count_heavy-atom>21</PC-Count_heavy-atom>
        <PC-Count_atom-chiral>5</PC-Count_atom-chiral>
        <PC-Count_atom-chiral-def>5</PC-Count_atom-chiral-def>
        <PC-Count_atom-chiral-undef>0</PC-Count_atom-chiral-undef>
        <PC-Count_bond-chiral>0</PC-Count_bond-chiral>
        <PC-Count_bond-chiral-def>0</PC-Count_bond-chiral-def>
        <PC-Count_bond-chiral-undef>0</PC-Count_bond-chiral-undef>
        <PC-Count_isotope-atom>0</PC-Count_isotope-atom>
        <PC-Count_covalent-unit>1</PC-Count_covalent-unit>
        <PC-Count_tautomers>-1</PC-Count_tautomers>
      </PC-Count>
    </PC-Compound_count>
  </PC-Compound>
</PC-Compounds>
"""

    @pytest.fixture
    def morphine_3d_file_data(self):
        return """<?xml version="1.0"?>
<PC-Compounds
    xmlns="http://www.ncbi.nlm.nih.gov"
    xmlns:xs="http://www.w3.org/2001/XMLSchema-instance"
    xs:schemaLocation="http://www.ncbi.nlm.nih.gov ftp://ftp.ncbi.nlm.nih.gov/pubchem/specifications/pubchem.xsd"
>
  <PC-Compound>
    <PC-Compound_id>
      <PC-CompoundType>
        <PC-CompoundType_id>
          <PC-CompoundType_id_cid>5288826</PC-CompoundType_id_cid>
        </PC-CompoundType_id>
      </PC-CompoundType>
    </PC-Compound_id>
    <PC-Compound_atoms>
      <PC-Atoms>
        <PC-Atoms_aid>
          <PC-Atoms_aid_E>1</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>2</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>3</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>4</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>5</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>6</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>7</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>8</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>9</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>10</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>11</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>12</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>13</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>14</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>15</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>16</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>17</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>18</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>19</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>20</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>21</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>22</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>23</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>24</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>25</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>26</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>27</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>28</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>29</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>30</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>31</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>32</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>33</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>34</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>35</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>36</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>37</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>38</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>39</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>40</PC-Atoms_aid_E>
        </PC-Atoms_aid>
        <PC-Atoms_element>
          <PC-Element value="o">8</PC-Element>
          <PC-Element value="o">8</PC-Element>
          <PC-Element value="o">8</PC-Element>
          <PC-Element value="n">7</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
        </PC-Atoms_element>
      </PC-Atoms>
    </PC-Compound_atoms>
    <PC-Compound_bonds>
      <PC-Bonds>
        <PC-Bonds_aid1>
          <PC-Bonds_aid1_E>1</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>1</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>2</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>2</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>3</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>3</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>4</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>4</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>4</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>5</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>5</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>5</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>5</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>6</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>6</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>6</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>7</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>7</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>8</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>8</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>9</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>9</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>9</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>10</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>10</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>11</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>11</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>11</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>12</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>12</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>13</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>14</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>14</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>15</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>15</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>16</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>17</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>18</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>18</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>18</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>19</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>19</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>20</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>21</PC-Bonds_aid1_E>
        </PC-Bonds_aid1>
        <PC-Bonds_aid2>
          <PC-Bonds_aid2_E>8</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>16</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>14</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>39</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>20</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>40</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>7</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>12</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>18</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>6</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>8</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>9</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>10</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>7</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>15</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>22</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>11</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>23</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>14</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>24</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>12</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>25</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>26</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>13</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>16</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>13</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>27</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>28</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>29</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>30</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>19</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>17</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>31</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>17</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>32</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>20</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>33</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>34</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>35</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>36</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>21</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>37</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>21</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>38</PC-Bonds_aid2_E>
        </PC-Bonds_aid2>
        <PC-Bonds_order>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
        </PC-Bonds_order>
      </PC-Bonds>
    </PC-Compound_bonds>
    <PC-Compound_stereo>
      <PC-StereoCenter>
        <PC-StereoCenter_tetrahedral>
          <PC-StereoTetrahedral>
            <PC-StereoTetrahedral_center>5</PC-StereoTetrahedral_center>
            <PC-StereoTetrahedral_above>6</PC-StereoTetrahedral_above>
            <PC-StereoTetrahedral_top>8</PC-StereoTetrahedral_top>
            <PC-StereoTetrahedral_bottom>9</PC-StereoTetrahedral_bottom>
            <PC-StereoTetrahedral_below>10</PC-StereoTetrahedral_below>
            <PC-StereoTetrahedral_parity value="clockwise">1</PC-StereoTetrahedral_parity>
            <PC-StereoTetrahedral_type value="tetrahedral">1</PC-StereoTetrahedral_type>
          </PC-StereoTetrahedral>
        </PC-StereoCenter_tetrahedral>
      </PC-StereoCenter>
      <PC-StereoCenter>
        <PC-StereoCenter_tetrahedral>
          <PC-StereoTetrahedral>
            <PC-StereoTetrahedral_center>6</PC-StereoTetrahedral_center>
            <PC-StereoTetrahedral_above>5</PC-StereoTetrahedral_above>
            <PC-StereoTetrahedral_top>15</PC-StereoTetrahedral_top>
            <PC-StereoTetrahedral_bottom>7</PC-StereoTetrahedral_bottom>
            <PC-StereoTetrahedral_below>22</PC-StereoTetrahedral_below>
            <PC-StereoTetrahedral_parity value="counterclockwise">2</PC-StereoTetrahedral_parity>
            <PC-StereoTetrahedral_type value="tetrahedral">1</PC-StereoTetrahedral_type>
          </PC-StereoTetrahedral>
        </PC-StereoCenter_tetrahedral>
      </PC-StereoCenter>
      <PC-StereoCenter>
        <PC-StereoCenter_tetrahedral>
          <PC-StereoTetrahedral>
            <PC-StereoTetrahedral_center>7</PC-StereoTetrahedral_center>
            <PC-StereoTetrahedral_above>4</PC-StereoTetrahedral_above>
            <PC-StereoTetrahedral_top>6</PC-StereoTetrahedral_top>
            <PC-StereoTetrahedral_bottom>11</PC-StereoTetrahedral_bottom>
            <PC-StereoTetrahedral_below>23</PC-StereoTetrahedral_below>
            <PC-StereoTetrahedral_parity value="clockwise">1</PC-StereoTetrahedral_parity>
            <PC-StereoTetrahedral_type value="tetrahedral">1</PC-StereoTetrahedral_type>
          </PC-StereoTetrahedral>
        </PC-StereoCenter_tetrahedral>
      </PC-StereoCenter>
      <PC-StereoCenter>
        <PC-StereoCenter_tetrahedral>
          <PC-StereoTetrahedral>
            <PC-StereoTetrahedral_center>8</PC-StereoTetrahedral_center>
            <PC-StereoTetrahedral_above>1</PC-StereoTetrahedral_above>
            <PC-StereoTetrahedral_top>14</PC-StereoTetrahedral_top>
            <PC-StereoTetrahedral_bottom>5</PC-StereoTetrahedral_bottom>
            <PC-StereoTetrahedral_below>24</PC-StereoTetrahedral_below>
            <PC-StereoTetrahedral_parity value="counterclockwise">2</PC-StereoTetrahedral_parity>
            <PC-StereoTetrahedral_type value="tetrahedral">1</PC-StereoTetrahedral_type>
          </PC-StereoTetrahedral>
        </PC-StereoCenter_tetrahedral>
      </PC-StereoCenter>
      <PC-StereoCenter>
        <PC-StereoCenter_tetrahedral>
          <PC-StereoTetrahedral>
            <PC-StereoTetrahedral_center>14</PC-StereoTetrahedral_center>
            <PC-StereoTetrahedral_above>2</PC-StereoTetrahedral_above>
            <PC-StereoTetrahedral_top>17</PC-StereoTetrahedral_top>
            <PC-StereoTetrahedral_bottom>8</PC-StereoTetrahedral_bottom>
            <PC-StereoTetrahedral_below>31</PC-StereoTetrahedral_below>
            <PC-StereoTetrahedral_parity value="counterclockwise">2</PC-StereoTetrahedral_parity>
            <PC-StereoTetrahedral_type value="tetrahedral">1</PC-StereoTetrahedral_type>
          </PC-StereoTetrahedral>
        </PC-StereoCenter_tetrahedral>
      </PC-StereoCenter>
    </PC-Compound_stereo>
    <PC-Compound_coords>
      <PC-Coordinates>
        <PC-Coordinates_type>
          <PC-CoordinateType value="threed">2</PC-CoordinateType>
          <PC-CoordinateType value="computed">5</PC-CoordinateType>
          <PC-CoordinateType value="units-angstroms">10</PC-CoordinateType>
        </PC-Coordinates_type>
        <PC-Coordinates_aid>
          <PC-Coordinates_aid_E>1</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>2</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>3</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>4</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>5</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>6</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>7</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>8</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>9</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>10</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>11</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>12</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>13</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>14</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>15</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>16</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>17</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>18</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>19</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>20</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>21</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>22</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>23</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>24</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>25</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>26</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>27</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>28</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>29</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>30</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>31</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>32</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>33</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>34</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>35</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>36</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>37</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>38</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>39</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>40</PC-Coordinates_aid_E>
        </PC-Coordinates_aid>
        <PC-Coordinates_conformers>
          <PC-Conformer>
            <PC-Conformer_x>
              <PC-Conformer_x_E>-1.993</PC-Conformer_x_E>
              <PC-Conformer_x_E>-2.7826</PC-Conformer_x_E>
              <PC-Conformer_x_E>-3.622</PC-Conformer_x_E>
              <PC-Conformer_x_E>3.1777</PC-Conformer_x_E>
              <PC-Conformer_x_E>0.3699</PC-Conformer_x_E>
              <PC-Conformer_x_E>1.2913</PC-Conformer_x_E>
              <PC-Conformer_x_E>2.3441</PC-Conformer_x_E>
              <PC-Conformer_x_E>-0.9377</PC-Conformer_x_E>
              <PC-Conformer_x_E>1.1988</PC-Conformer_x_E>
              <PC-Conformer_x_E>-0.2516</PC-Conformer_x_E>
              <PC-Conformer_x_E>1.6887</PC-Conformer_x_E>
              <PC-Conformer_x_E>2.4315</PC-Conformer_x_E>
              <PC-Conformer_x_E>0.3384</PC-Conformer_x_E>
              <PC-Conformer_x_E>-1.3631</PC-Conformer_x_E>
              <PC-Conformer_x_E>0.5066</PC-Conformer_x_E>
              <PC-Conformer_x_E>-1.5672</PC-Conformer_x_E>
              <PC-Conformer_x_E>-0.7155</PC-Conformer_x_E>
              <PC-Conformer_x_E>4.3733</PC-Conformer_x_E>
              <PC-Conformer_x_E>-0.4184</PC-Conformer_x_E>
              <PC-Conformer_x_E>-2.331</PC-Conformer_x_E>
              <PC-Conformer_x_E>-1.7382</PC-Conformer_x_E>
              <PC-Conformer_x_E>1.8278</PC-Conformer_x_E>
              <PC-Conformer_x_E>3.0029</PC-Conformer_x_E>
              <PC-Conformer_x_E>-0.8451</PC-Conformer_x_E>
              <PC-Conformer_x_E>1.5366</PC-Conformer_x_E>
              <PC-Conformer_x_E>0.5899</PC-Conformer_x_E>
              <PC-Conformer_x_E>1.5474</PC-Conformer_x_E>
              <PC-Conformer_x_E>2.353</PC-Conformer_x_E>
              <PC-Conformer_x_E>2.1271</PC-Conformer_x_E>
              <PC-Conformer_x_E>3.0801</PC-Conformer_x_E>
              <PC-Conformer_x_E>-1.0772</PC-Conformer_x_E>
              <PC-Conformer_x_E>0.9601</PC-Conformer_x_E>
              <PC-Conformer_x_E>-1.23</PC-Conformer_x_E>
              <PC-Conformer_x_E>4.15</PC-Conformer_x_E>
              <PC-Conformer_x_E>4.938</PC-Conformer_x_E>
              <PC-Conformer_x_E>5.0444</PC-Conformer_x_E>
              <PC-Conformer_x_E>-0.0062</PC-Conformer_x_E>
              <PC-Conformer_x_E>-2.3121</PC-Conformer_x_E>
              <PC-Conformer_x_E>-3.1557</PC-Conformer_x_E>
              <PC-Conformer_x_E>-3.8483</PC-Conformer_x_E>
            </PC-Conformer_x>
            <PC-Conformer_y>
              <PC-Conformer_y_E>-0.474</PC-Conformer_y_E>
              <PC-Conformer_y_E>-2.5168</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.8421</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.0101</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.7149</PC-Conformer_y_E>
              <PC-Conformer_y_E>-1.3046</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.2023</PC-Conformer_y_E>
              <PC-Conformer_y_E>-1.475</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.3907</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.5302</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.1052</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.4754</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.4306</PC-Conformer_y_E>
              <PC-Conformer_y_E>-2.5067</PC-Conformer_y_E>
              <PC-Conformer_y_E>-1.8183</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.6306</PC-Conformer_y_E>
              <PC-Conformer_y_E>-2.3492</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.7916</PC-Conformer_y_E>
              <PC-Conformer_y_E>2.5415</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.7217</PC-Conformer_y_E>
              <PC-Conformer_y_E>2.6936</PC-Conformer_y_E>
              <PC-Conformer_y_E>-2.1759</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.6035</PC-Conformer_y_E>
              <PC-Conformer_y_E>-2.0128</PC-Conformer_y_E>
              <PC-Conformer_y_E>-1.3335</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.1174</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.9596</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.968</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.5205</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.4584</PC-Conformer_y_E>
              <PC-Conformer_y_E>-3.5067</PC-Conformer_y_E>
              <PC-Conformer_y_E>-1.7947</PC-Conformer_y_E>
              <PC-Conformer_y_E>-2.7505</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.8479</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.4055</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.7352</PC-Conformer_y_E>
              <PC-Conformer_y_E>3.2824</PC-Conformer_y_E>
              <PC-Conformer_y_E>3.5638</PC-Conformer_y_E>
              <PC-Conformer_y_E>-2.6446</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.0686</PC-Conformer_y_E>
            </PC-Conformer_y>
            <PC-Conformer_z>
              <PC-Conformer_z_E>1.2005</PC-Conformer_z_E>
              <PC-Conformer_z_E>-0.2218</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.5579</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.4474</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.6616</PC-Conformer_z_E>
              <PC-Conformer_z_E>-0.417</PC-Conformer_z_E>
              <PC-Conformer_z_E>-0.764</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.9848</PC-Conformer_z_E>
              <PC-Conformer_z_E>1.9201</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.1205</PC-Conformer_z_E>
              <PC-Conformer_z_E>-1.3279</PC-Conformer_z_E>
              <PC-Conformer_z_E>1.6126</PC-Conformer_z_E>
              <PC-Conformer_z_E>-0.748</PC-Conformer_z_E>
              <PC-Conformer_z_E>-0.0924</PC-Conformer_z_E>
              <PC-Conformer_z_E>-1.5971</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.5136</PC-Conformer_z_E>
              <PC-Conformer_z_E>-1.4425</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.2084</PC-Conformer_z_E>
              <PC-Conformer_z_E>-1.1246</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.162</PC-Conformer_z_E>
              <PC-Conformer_z_E>-0.6541</PC-Conformer_z_E>
              <PC-Conformer_z_E>-0.0118</PC-Conformer_z_E>
              <PC-Conformer_z_E>-1.5465</PC-Conformer_z_E>
              <PC-Conformer_z_E>1.9373</PC-Conformer_z_E>
              <PC-Conformer_z_E>2.3712</PC-Conformer_z_E>
              <PC-Conformer_z_E>2.679</PC-Conformer_z_E>
              <PC-Conformer_z_E>-2.4075</PC-Conformer_z_E>
              <PC-Conformer_z_E>-1.2194</PC-Conformer_z_E>
              <PC-Conformer_z_E>1.476</PC-Conformer_z_E>
              <PC-Conformer_z_E>2.4975</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.2593</PC-Conformer_z_E>
              <PC-Conformer_z_E>-2.5831</PC-Conformer_z_E>
              <PC-Conformer_z_E>-2.3109</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.0287</PC-Conformer_z_E>
              <PC-Conformer_z_E>-0.6472</PC-Conformer_z_E>
              <PC-Conformer_z_E>1.073</PC-Conformer_z_E>
              <PC-Conformer_z_E>-1.8043</PC-Conformer_z_E>
              <PC-Conformer_z_E>-0.9645</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.6672</PC-Conformer_z_E>
              <PC-Conformer_z_E>1.1031</PC-Conformer_z_E>
            </PC-Conformer_z>
            <PC-Conformer_data>
              <PC-InfoData>
                <PC-InfoData_urn>
                  <PC-Urn>
                    <PC-Urn_label>Conformer</PC-Urn_label>
                    <PC-Urn_name>ID</PC-Urn_name>
                    <PC-Urn_datatype>
                      <PC-UrnDataType value="uint64">11</PC-UrnDataType>
                    </PC-Urn_datatype>
                    <PC-Urn_version>2.1</PC-Urn_version>
                    <PC-Urn_software>PubChem</PC-Urn_software>
                    <PC-Urn_source>ncbi.nlm.nih.gov</PC-Urn_source>
                    <PC-Urn_release>2009.12.11</PC-Urn_release>
                  </PC-Urn>
                </PC-InfoData_urn>
                <PC-InfoData_value>
                  <PC-InfoData_value_sval>0050B37A00000001</PC-InfoData_value_sval>
                </PC-InfoData_value>
              </PC-InfoData>
              <PC-InfoData>
                <PC-InfoData_urn>
                  <PC-Urn>
                    <PC-Urn_label>Energy</PC-Urn_label>
                    <PC-Urn_name>MMFF94 NoEstat</PC-Urn_name>
                    <PC-Urn_datatype>
                      <PC-UrnDataType value="double">7</PC-UrnDataType>
                    </PC-Urn_datatype>
                    <PC-Urn_version>1.6.0</PC-Urn_version>
                    <PC-Urn_software>Szybki</PC-Urn_software>
                    <PC-Urn_source>openeye.com</PC-Urn_source>
                    <PC-Urn_release>2012.01.18</PC-Urn_release>
                  </PC-Urn>
                </PC-InfoData_urn>
                <PC-InfoData_value>
                  <PC-InfoData_value_fval>74.8429</PC-InfoData_value_fval>
                </PC-InfoData_value>
              </PC-InfoData>
              <PC-InfoData>
                <PC-InfoData_urn>
                  <PC-Urn>
                    <PC-Urn_label>Feature</PC-Urn_label>
                    <PC-Urn_name>Self Overlap</PC-Urn_name>
                    <PC-Urn_datatype>
                      <PC-UrnDataType value="double">7</PC-UrnDataType>
                    </PC-Urn_datatype>
                    <PC-Urn_version>2.1</PC-Urn_version>
                    <PC-Urn_software>PubChem</PC-Urn_software>
                    <PC-Urn_source>ncbi.nlm.nih.gov</PC-Urn_source>
                    <PC-Urn_release>2012.01.18</PC-Urn_release>
                  </PC-Urn>
                </PC-InfoData_urn>
                <PC-InfoData_value>
                  <PC-InfoData_value_fval>52.873</PC-InfoData_value_fval>
                </PC-InfoData_value>
              </PC-InfoData>
              <PC-InfoData>
                <PC-InfoData_urn>
                  <PC-Urn>
                    <PC-Urn_label>Fingerprint</PC-Urn_label>
                    <PC-Urn_name>Shape</PC-Urn_name>
                    <PC-Urn_datatype>
                      <PC-UrnDataType value="stringlist">2</PC-UrnDataType>
                    </PC-Urn_datatype>
                    <PC-Urn_version>2.1</PC-Urn_version>
                    <PC-Urn_software>PubChem</PC-Urn_software>
                    <PC-Urn_source>ncbi.nlm.nih.gov</PC-Urn_source>
                    <PC-Urn_release>2012.11.26</PC-Urn_release>
                  </PC-Urn>
                </PC-InfoData_urn>
                <PC-InfoData_value>
                  <PC-InfoData_value_slist>
                    <PC-InfoData_value_slist_E>10165383 225 18201451224619826784</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>10863032 1 18271807882738128182</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>10871710 139 17975427020448559044</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>10948715 1 18269553840856601268</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>11578080 2 17916862543033451120</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>12035758 1 17979921506076134602</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>12326174 3 16761939621672351259</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>12403814 3 18127127700562790162</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>12423570 1 13554306196661771698</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>13132413 78 16832327581639147097</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>13140716 1 18188786057421996321</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>13172582 1 18260836951273720209</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>13681431 1 17258466355483259718</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>141345 1 11468367428490074574</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>144361 1 17623048910753830566</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>14817 1 13651070280742688743</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>15852999 172 18199182901892535827</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>16945 1 18189637062236146638</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>17357779 13 17772166846782183447</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>18393751 57 17187542376137546200</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>19868273 325 18263924500288743760</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>21524375 3 18267574711299526024</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>22112679 90 18121790679236681172</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>22182313 1 18194427527483256583</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>2334 1 17972616638225251261</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>23388829 49 17833828657105785732</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>23402539 116 18338509850163596911</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>23419403 2 15694871661581035675</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>23557571 272 18270408299151999272</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>23559900 14 18059580127798590934</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>238 59 17618764874292193101</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>2748010 2 17975155161707925181</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>34934 24 18113338621838265964</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>495365 180 17547829890269334821</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>7364860 26 17256519721717681045</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>81228 2 18194937829152466419</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>84936 31 17124492616027647943</PC-InfoData_value_slist_E>
                  </PC-InfoData_value_slist>
                </PC-InfoData_value>
              </PC-InfoData>
              <PC-InfoData>
                <PC-InfoData_urn>
                  <PC-Urn>
                    <PC-Urn_label>Shape</PC-Urn_label>
                    <PC-Urn_name>Multipoles</PC-Urn_name>
                    <PC-Urn_datatype>
                      <PC-UrnDataType value="doublevec">8</PC-UrnDataType>
                    </PC-Urn_datatype>
                    <PC-Urn_version>1.8.1</PC-Urn_version>
                    <PC-Urn_software>OEShape</PC-Urn_software>
                    <PC-Urn_source>openeye.com</PC-Urn_source>
                    <PC-Urn_release>2012.01.18</PC-Urn_release>
                  </PC-Urn>
                </PC-InfoData_urn>
                <PC-InfoData_value>
                  <PC-InfoData_value_fvec>
                    <PC-InfoData_value_fvec_E>409.58</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>4.45</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>3.02</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>1.55</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>2.3</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>0.24</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>-0.13</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>-1.6</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>-0.99</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>-2.59</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>1.17</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>0.46</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>0.26</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>-0.03</PC-InfoData_value_fvec_E>
                  </PC-InfoData_value_fvec>
                </PC-InfoData_value>
              </PC-InfoData>
              <PC-InfoData>
                <PC-InfoData_urn>
                  <PC-Urn>
                    <PC-Urn_label>Shape</PC-Urn_label>
                    <PC-Urn_name>Self Overlap</PC-Urn_name>
                    <PC-Urn_datatype>
                      <PC-UrnDataType value="double">7</PC-UrnDataType>
                    </PC-Urn_datatype>
                    <PC-Urn_version>2.1</PC-Urn_version>
                    <PC-Urn_software>PubChem</PC-Urn_software>
                    <PC-Urn_source>ncbi.nlm.nih.gov</PC-Urn_source>
                    <PC-Urn_release>2012.01.18</PC-Urn_release>
                  </PC-Urn>
                </PC-InfoData_urn>
                <PC-InfoData_value>
                  <PC-InfoData_value_fval>930.437</PC-InfoData_value_fval>
                </PC-InfoData_value>
              </PC-InfoData>
              <PC-InfoData>
                <PC-InfoData_urn>
                  <PC-Urn>
                    <PC-Urn_label>Shape</PC-Urn_label>
                    <PC-Urn_name>Volume</PC-Urn_name>
                    <PC-Urn_datatype>
                      <PC-UrnDataType value="double">7</PC-UrnDataType>
                    </PC-Urn_datatype>
                    <PC-Urn_version>1.8.1</PC-Urn_version>
                    <PC-Urn_software>OEShape</PC-Urn_software>
                    <PC-Urn_source>openeye.com</PC-Urn_source>
                    <PC-Urn_release>2012.01.18</PC-Urn_release>
                  </PC-Urn>
                </PC-InfoData_urn>
                <PC-InfoData_value>
                  <PC-InfoData_value_fval>211.2</PC-InfoData_value_fval>
                </PC-InfoData_value>
              </PC-InfoData>
            </PC-Conformer_data>
          </PC-Conformer>
        </PC-Coordinates_conformers>
        <PC-Coordinates_data>
          <PC-InfoData>
            <PC-InfoData_urn>
              <PC-Urn>
                <PC-Urn_label>Conformer</PC-Urn_label>
                <PC-Urn_name>RMSD</PC-Urn_name>
                <PC-Urn_datatype>
                  <PC-UrnDataType value="double">7</PC-UrnDataType>
                </PC-Urn_datatype>
                <PC-Urn_release>2009.12.11</PC-Urn_release>
              </PC-Urn>
            </PC-InfoData_urn>
            <PC-InfoData_value>
              <PC-InfoData_value_fval>0.6</PC-InfoData_value_fval>
            </PC-InfoData_value>
          </PC-InfoData>
          <PC-InfoData>
            <PC-InfoData_urn>
              <PC-Urn>
                <PC-Urn_label>Diverse Conformer</PC-Urn_label>
                <PC-Urn_name>ID List</PC-Urn_name>
                <PC-Urn_datatype>
                  <PC-UrnDataType value="uintvec">6</PC-UrnDataType>
                </PC-Urn_datatype>
                <PC-Urn_release>2010.05.05</PC-Urn_release>
              </PC-Urn>
            </PC-InfoData_urn>
            <PC-InfoData_value>
              <PC-InfoData_value_ivec>
                <PC-InfoData_value_ivec_E>1</PC-InfoData_value_ivec_E>
              </PC-InfoData_value_ivec>
            </PC-InfoData_value>
          </PC-InfoData>
        </PC-Coordinates_data>
      </PC-Coordinates>
    </PC-Compound_coords>
    <PC-Compound_props>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Charge</PC-Urn_label>
            <PC-Urn_name>MMFF94 Partial</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="stringlist">2</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>1.9.0</PC-Urn_version>
            <PC-Urn_software>OEChem</PC-Urn_software>
            <PC-Urn_source>openeye.com</PC-Urn_source>
            <PC-Urn_release>2012.11.26</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_slist>
            <PC-InfoData_value_slist_E>26</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>1 -0.36</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>10 -0.14</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>11 0.14</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>12 0.27</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>13 -0.14</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>14 0.42</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>15 -0.29</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>16 0.08</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>17 -0.29</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>18 0.27</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>19 -0.15</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>2 -0.68</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>20 0.08</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>21 -0.15</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>3 -0.53</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>32 0.15</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>33 0.15</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>37 0.15</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>38 0.15</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>39 0.4</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>4 -0.81</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>40 0.45</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>5 0.14</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>6 0.14</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>7 0.27</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>8 0.28</PC-InfoData_value_slist_E>
          </PC-InfoData_value_slist>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Count</PC-Urn_label>
            <PC-Urn_name>Effective Rotor</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="double">7</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>1.7.6</PC-Urn_version>
            <PC-Urn_software>OEChem</PC-Urn_software>
            <PC-Urn_source>ncbi.nlm.nih.gov</PC-Urn_source>
            <PC-Urn_release>2012.01.18</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_fval>1.2</PC-InfoData_value_fval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Features</PC-Urn_label>
            <PC-Urn_name>Pharmacophore</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="stringlist">2</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_parameters>ImplicitMillsDean merged</PC-Urn_parameters>
            <PC-Urn_version>1.8.3</PC-Urn_version>
            <PC-Urn_software>OEShape</PC-Urn_software>
            <PC-Urn_source>openeye.com</PC-Urn_source>
            <PC-Urn_release>2012.11.26</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_slist>
            <PC-InfoData_value_slist_E>10</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>1 1 acceptor</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>1 2 acceptor</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>1 2 donor</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>1 3 donor</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>1 4 cation</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>5 1 5 8 10 16 rings</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>6 10 13 16 19 20 21 rings</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>6 4 5 6 7 9 12 rings</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>6 5 6 7 10 11 13 rings</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>6 5 6 8 14 15 17 rings</PC-InfoData_value_slist_E>
          </PC-InfoData_value_slist>
        </PC-InfoData_value>
      </PC-InfoData>
    </PC-Compound_props>
    <PC-Compound_count>
      <PC-Count>
        <PC-Count_heavy-atom>21</PC-Count_heavy-atom>
        <PC-Count_atom-chiral>5</PC-Count_atom-chiral>
        <PC-Count_atom-chiral-def>5</PC-Count_atom-chiral-def>
        <PC-Count_atom-chiral-undef>0</PC-Count_atom-chiral-undef>
        <PC-Count_bond-chiral>0</PC-Count_bond-chiral>
        <PC-Count_bond-chiral-def>0</PC-Count_bond-chiral-def>
        <PC-Count_bond-chiral-undef>0</PC-Count_bond-chiral-undef>
        <PC-Count_isotope-atom>0</PC-Count_isotope-atom>
        <PC-Count_covalent-unit>1</PC-Count_covalent-unit>
        <PC-Count_tautomers>3</PC-Count_tautomers>
      </PC-Count>
    </PC-Compound_count>
  </PC-Compound>
</PC-Compounds>
"""

    @pytest.fixture
    def heme_2d_file_data(self):
        return """<?xml version="1.0"?>
<PC-Compounds
    xmlns="http://www.ncbi.nlm.nih.gov"
    xmlns:xs="http://www.w3.org/2001/XMLSchema-instance"
    xs:schemaLocation="http://www.ncbi.nlm.nih.gov ftp://ftp.ncbi.nlm.nih.gov/pubchem/specifications/pubchem.xsd"
>
  <PC-Compound>
    <PC-Compound_id>
      <PC-CompoundType>
        <PC-CompoundType_id>
          <PC-CompoundType_id_cid>26945</PC-CompoundType_id_cid>
        </PC-CompoundType_id>
      </PC-CompoundType>
    </PC-Compound_id>
    <PC-Compound_atoms>
      <PC-Atoms>
        <PC-Atoms_aid>
          <PC-Atoms_aid_E>1</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>2</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>3</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>4</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>5</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>6</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>7</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>8</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>9</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>10</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>11</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>12</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>13</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>14</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>15</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>16</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>17</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>18</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>19</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>20</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>21</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>22</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>23</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>24</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>25</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>26</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>27</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>28</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>29</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>30</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>31</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>32</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>33</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>34</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>35</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>36</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>37</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>38</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>39</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>40</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>41</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>42</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>43</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>44</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>45</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>46</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>47</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>48</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>49</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>50</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>51</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>52</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>53</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>54</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>55</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>56</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>57</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>58</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>59</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>60</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>61</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>62</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>63</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>64</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>65</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>66</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>67</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>68</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>69</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>70</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>71</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>72</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>73</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>74</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>75</PC-Atoms_aid_E>
        </PC-Atoms_aid>
        <PC-Atoms_element>
          <PC-Element value="fe">26</PC-Element>
          <PC-Element value="o">8</PC-Element>
          <PC-Element value="o">8</PC-Element>
          <PC-Element value="o">8</PC-Element>
          <PC-Element value="o">8</PC-Element>
          <PC-Element value="n">7</PC-Element>
          <PC-Element value="n">7</PC-Element>
          <PC-Element value="n">7</PC-Element>
          <PC-Element value="n">7</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
        </PC-Atoms_element>
        <PC-Atoms_charge>
          <PC-AtomInt>
            <PC-AtomInt_aid>1</PC-AtomInt_aid>
            <PC-AtomInt_value>2</PC-AtomInt_value>
          </PC-AtomInt>
          <PC-AtomInt>
            <PC-AtomInt_aid>6</PC-AtomInt_aid>
            <PC-AtomInt_value>-1</PC-AtomInt_value>
          </PC-AtomInt>
          <PC-AtomInt>
            <PC-AtomInt_aid>7</PC-AtomInt_aid>
            <PC-AtomInt_value>-1</PC-AtomInt_value>
          </PC-AtomInt>
        </PC-Atoms_charge>
      </PC-Atoms>
    </PC-Compound_atoms>
    <PC-Compound_bonds>
      <PC-Bonds>
        <PC-Bonds_aid1>
          <PC-Bonds_aid1_E>2</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>2</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>3</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>3</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>4</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>5</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>6</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>6</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>7</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>7</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>8</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>8</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>9</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>9</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>10</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>10</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>10</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>11</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>11</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>11</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>12</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>13</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>14</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>14</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>15</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>15</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>16</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>16</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>16</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>17</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>17</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>17</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>18</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>19</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>20</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>21</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>21</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>22</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>22</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>23</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>23</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>23</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>24</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>24</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>24</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>25</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>26</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>27</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>27</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>27</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>28</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>28</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>28</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>29</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>29</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>30</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>30</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>31</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>31</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>32</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>33</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>33</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>34</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>35</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>36</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>36</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>36</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>37</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>37</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>37</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>40</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>40</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>41</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>41</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>42</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>42</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>43</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>43</PC-Bonds_aid1_E>
        </PC-Bonds_aid1>
        <PC-Bonds_aid2>
          <PC-Bonds_aid2_E>38</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>74</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>39</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>75</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>38</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>39</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>12</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>18</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>13</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>19</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>25</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>33</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>26</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>31</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>12</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>14</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>16</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>13</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>15</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>17</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>20</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>20</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>18</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>27</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>19</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>28</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>23</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>44</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>45</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>24</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>46</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>47</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>21</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>22</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>48</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>25</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>49</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>26</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>50</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>38</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>51</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>52</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>39</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>53</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>54</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>29</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>30</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>55</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>56</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>57</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>58</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>59</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>60</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>34</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>36</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>32</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>40</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>32</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>35</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>37</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>34</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>35</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>41</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>61</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>62</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>63</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>64</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>65</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>66</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>67</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>42</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>68</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>43</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>69</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>70</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>71</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>72</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>73</PC-Bonds_aid2_E>
        </PC-Bonds_aid2>
        <PC-Bonds_order>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
        </PC-Bonds_order>
      </PC-Bonds>
    </PC-Compound_bonds>
    <PC-Compound_coords>
      <PC-Coordinates>
        <PC-Coordinates_type>
          <PC-CoordinateType value="twod">1</PC-CoordinateType>
          <PC-CoordinateType value="computed">5</PC-CoordinateType>
          <PC-CoordinateType value="units-unknown">255</PC-CoordinateType>
        </PC-Coordinates_type>
        <PC-Coordinates_aid>
          <PC-Coordinates_aid_E>1</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>2</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>3</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>4</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>5</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>6</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>7</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>8</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>9</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>10</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>11</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>12</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>13</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>14</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>15</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>16</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>17</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>18</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>19</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>20</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>21</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>22</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>23</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>24</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>25</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>26</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>27</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>28</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>29</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>30</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>31</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>32</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>33</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>34</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>35</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>36</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>37</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>38</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>39</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>40</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>41</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>42</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>43</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>44</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>45</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>46</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>47</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>48</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>49</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>50</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>51</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>52</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>53</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>54</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>55</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>56</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>57</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>58</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>59</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>60</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>61</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>62</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>63</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>64</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>65</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>66</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>67</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>68</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>69</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>70</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>71</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>72</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>73</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>74</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>75</PC-Coordinates_aid_E>
        </PC-Coordinates_aid>
        <PC-Coordinates_conformers>
          <PC-Conformer>
            <PC-Conformer_x>
              <PC-Conformer_x_E>6.7437</PC-Conformer_x_E>
              <PC-Conformer_x_E>7.6407</PC-Conformer_x_E>
              <PC-Conformer_x_E>13.2337</PC-Conformer_x_E>
              <PC-Conformer_x_E>9.0357</PC-Conformer_x_E>
              <PC-Conformer_x_E>12.191</PC-Conformer_x_E>
              <PC-Conformer_x_E>6.7568</PC-Conformer_x_E>
              <PC-Conformer_x_E>8.2586</PC-Conformer_x_E>
              <PC-Conformer_x_E>5.2534</PC-Conformer_x_E>
              <PC-Conformer_x_E>6.7233</PC-Conformer_x_E>
              <PC-Conformer_x_E>7.2574</PC-Conformer_x_E>
              <PC-Conformer_x_E>9.7955</PC-Conformer_x_E>
              <PC-Conformer_x_E>7.5588</PC-Conformer_x_E>
              <PC-Conformer_x_E>8.8596</PC-Conformer_x_E>
              <PC-Conformer_x_E>6.2562</PC-Conformer_x_E>
              <PC-Conformer_x_E>9.7955</PC-Conformer_x_E>
              <PC-Conformer_x_E>7.8502</PC-Conformer_x_E>
              <PC-Conformer_x_E>10.594</PC-Conformer_x_E>
              <PC-Conformer_x_E>5.9549</PC-Conformer_x_E>
              <PC-Conformer_x_E>8.8261</PC-Conformer_x_E>
              <PC-Conformer_x_E>8.5599</PC-Conformer_x_E>
              <PC-Conformer_x_E>4.9872</PC-Conformer_x_E>
              <PC-Conformer_x_E>8.5265</PC-Conformer_x_E>
              <PC-Conformer_x_E>7.4491</PC-Conformer_x_E>
              <PC-Conformer_x_E>11.5146</PC-Conformer_x_E>
              <PC-Conformer_x_E>4.6858</PC-Conformer_x_E>
              <PC-Conformer_x_E>7.5588</PC-Conformer_x_E>
              <PC-Conformer_x_E>5.5855</PC-Conformer_x_E>
              <PC-Conformer_x_E>10.5912</PC-Conformer_x_E>
              <PC-Conformer_x_E>3.7182</PC-Conformer_x_E>
              <PC-Conformer_x_E>7.2239</PC-Conformer_x_E>
              <PC-Conformer_x_E>5.9214</PC-Conformer_x_E>
              <PC-Conformer_x_E>6.2228</PC-Conformer_x_E>
              <PC-Conformer_x_E>4.6858</PC-Conformer_x_E>
              <PC-Conformer_x_E>3.7182</PC-Conformer_x_E>
              <PC-Conformer_x_E>4.9537</PC-Conformer_x_E>
              <PC-Conformer_x_E>2.8521</PC-Conformer_x_E>
              <PC-Conformer_x_E>5.63</PC-Conformer_x_E>
              <PC-Conformer_x_E>8.0418</PC-Conformer_x_E>
              <PC-Conformer_x_E>12.3131</PC-Conformer_x_E>
              <PC-Conformer_x_E>7.7995</PC-Conformer_x_E>
              <PC-Conformer_x_E>2.9223</PC-Conformer_x_E>
              <PC-Conformer_x_E>7.3791</PC-Conformer_x_E>
              <PC-Conformer_x_E>2</PC-Conformer_x_E>
              <PC-Conformer_x_E>8.3663</PC-Conformer_x_E>
              <PC-Conformer_x_E>8.2781</PC-Conformer_x_E>
              <PC-Conformer_x_E>10.1405</PC-Conformer_x_E>
              <PC-Conformer_x_E>10.9316</PC-Conformer_x_E>
              <PC-Conformer_x_E>8.9897</PC-Conformer_x_E>
              <PC-Conformer_x_E>4.551</PC-Conformer_x_E>
              <PC-Conformer_x_E>8.963</PC-Conformer_x_E>
              <PC-Conformer_x_E>6.9329</PC-Conformer_x_E>
              <PC-Conformer_x_E>7.0211</PC-Conformer_x_E>
              <PC-Conformer_x_E>11.9681</PC-Conformer_x_E>
              <PC-Conformer_x_E>11.177</PC-Conformer_x_E>
              <PC-Conformer_x_E>5.1257</PC-Conformer_x_E>
              <PC-Conformer_x_E>5.1697</PC-Conformer_x_E>
              <PC-Conformer_x_E>6.0454</PC-Conformer_x_E>
              <PC-Conformer_x_E>10.9667</PC-Conformer_x_E>
              <PC-Conformer_x_E>11.0846</PC-Conformer_x_E>
              <PC-Conformer_x_E>10.2157</PC-Conformer_x_E>
              <PC-Conformer_x_E>4.5153</PC-Conformer_x_E>
              <PC-Conformer_x_E>2.5421</PC-Conformer_x_E>
              <PC-Conformer_x_E>2.3152</PC-Conformer_x_E>
              <PC-Conformer_x_E>3.1622</PC-Conformer_x_E>
              <PC-Conformer_x_E>6.1293</PC-Conformer_x_E>
              <PC-Conformer_x_E>5.2625</PC-Conformer_x_E>
              <PC-Conformer_x_E>5.1307</PC-Conformer_x_E>
              <PC-Conformer_x_E>8.417</PC-Conformer_x_E>
              <PC-Conformer_x_E>3.0007</PC-Conformer_x_E>
              <PC-Conformer_x_E>7.736</PC-Conformer_x_E>
              <PC-Conformer_x_E>6.7616</PC-Conformer_x_E>
              <PC-Conformer_x_E>1.5066</PC-Conformer_x_E>
              <PC-Conformer_x_E>1.9216</PC-Conformer_x_E>
              <PC-Conformer_x_E>8.0082</PC-Conformer_x_E>
              <PC-Conformer_x_E>13.7288</PC-Conformer_x_E>
            </PC-Conformer_x>
            <PC-Conformer_y>
              <PC-Conformer_y_E>0.7222</PC-Conformer_y_E>
              <PC-Conformer_y_E>-5.2892</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.2017</PC-Conformer_y_E>
              <PC-Conformer_y_E>-4.2626</PC-Conformer_y_E>
              <PC-Conformer_y_E>-1.1813</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.2777</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.0918</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.0918</PC-Conformer_y_E>
              <PC-Conformer_y_E>2.4613</PC-Conformer_y_E>
              <PC-Conformer_y_E>-1.8464</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.6247</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.8787</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.3568</PC-Conformer_y_E>
              <PC-Conformer_y_E>-1.8464</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.6259</PC-Conformer_y_E>
              <PC-Conformer_y_E>-2.6518</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.0227</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.9122</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.8938</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.6109</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.6109</PC-Conformer_y_E>
              <PC-Conformer_y_E>2.828</PC-Conformer_y_E>
              <PC-Conformer_y_E>-3.5678</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.4132</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.3233</PC-Conformer_y_E>
              <PC-Conformer_y_E>3.1293</PC-Conformer_y_E>
              <PC-Conformer_y_E>-2.5881</PC-Conformer_y_E>
              <PC-Conformer_y_E>2.2315</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.5912</PC-Conformer_y_E>
              <PC-Conformer_y_E>4.0635</PC-Conformer_y_E>
              <PC-Conformer_y_E>3.0958</PC-Conformer_y_E>
              <PC-Conformer_y_E>4.0635</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.8603</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.5924</PC-Conformer_y_E>
              <PC-Conformer_y_E>2.828</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.0912</PC-Conformer_y_E>
              <PC-Conformer_y_E>4.8689</PC-Conformer_y_E>
              <PC-Conformer_y_E>-4.3732</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.1888</PC-Conformer_y_E>
              <PC-Conformer_y_E>4.8812</PC-Conformer_y_E>
              <PC-Conformer_y_E>2.1979</PC-Conformer_y_E>
              <PC-Conformer_y_E>5.7886</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.8114</PC-Conformer_y_E>
              <PC-Conformer_y_E>-2.9953</PC-Conformer_y_E>
              <PC-Conformer_y_E>-2.2032</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.4</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.4974</PC-Conformer_y_E>
              <PC-Conformer_y_E>-1.0577</PC-Conformer_y_E>
              <PC-Conformer_y_E>-1.0515</PC-Conformer_y_E>
              <PC-Conformer_y_E>3.2682</PC-Conformer_y_E>
              <PC-Conformer_y_E>-3.2243</PC-Conformer_y_E>
              <PC-Conformer_y_E>-4.0165</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.8359</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.9333</PC-Conformer_y_E>
              <PC-Conformer_y_E>-2.1723</PC-Conformer_y_E>
              <PC-Conformer_y_E>-3.048</PC-Conformer_y_E>
              <PC-Conformer_y_E>-3.004</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.7382</PC-Conformer_y_E>
              <PC-Conformer_y_E>2.607</PC-Conformer_y_E>
              <PC-Conformer_y_E>2.7249</PC-Conformer_y_E>
              <PC-Conformer_y_E>3.2664</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.6281</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.2188</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.4457</PC-Conformer_y_E>
              <PC-Conformer_y_E>5.2364</PC-Conformer_y_E>
              <PC-Conformer_y_E>5.3682</PC-Conformer_y_E>
              <PC-Conformer_y_E>4.5014</PC-Conformer_y_E>
              <PC-Conformer_y_E>4.8257</PC-Conformer_y_E>
              <PC-Conformer_y_E>2.8129</PC-Conformer_y_E>
              <PC-Conformer_y_E>6.2956</PC-Conformer_y_E>
              <PC-Conformer_y_E>5.8441</PC-Conformer_y_E>
              <PC-Conformer_y_E>2.1868</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.1963</PC-Conformer_y_E>
              <PC-Conformer_y_E>-5.7886</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.1715</PC-Conformer_y_E>
            </PC-Conformer_y>
            <PC-Conformer_style>
              <PC-DrawAnnotations>
                <PC-DrawAnnotations_annotation>
                  <PC-BondAnnotation value="aromatic">8</PC-BondAnnotation>
                  <PC-BondAnnotation value="aromatic">8</PC-BondAnnotation>
                  <PC-BondAnnotation value="aromatic">8</PC-BondAnnotation>
                  <PC-BondAnnotation value="aromatic">8</PC-BondAnnotation>
                  <PC-BondAnnotation value="aromatic">8</PC-BondAnnotation>
                  <PC-BondAnnotation value="aromatic">8</PC-BondAnnotation>
                  <PC-BondAnnotation value="aromatic">8</PC-BondAnnotation>
                  <PC-BondAnnotation value="aromatic">8</PC-BondAnnotation>
                  <PC-BondAnnotation value="aromatic">8</PC-BondAnnotation>
                  <PC-BondAnnotation value="aromatic">8</PC-BondAnnotation>
                  <PC-BondAnnotation value="aromatic">8</PC-BondAnnotation>
                  <PC-BondAnnotation value="aromatic">8</PC-BondAnnotation>
                  <PC-BondAnnotation value="aromatic">8</PC-BondAnnotation>
                  <PC-BondAnnotation value="aromatic">8</PC-BondAnnotation>
                  <PC-BondAnnotation value="aromatic">8</PC-BondAnnotation>
                  <PC-BondAnnotation value="aromatic">8</PC-BondAnnotation>
                  <PC-BondAnnotation value="aromatic">8</PC-BondAnnotation>
                  <PC-BondAnnotation value="aromatic">8</PC-BondAnnotation>
                  <PC-BondAnnotation value="aromatic">8</PC-BondAnnotation>
                  <PC-BondAnnotation value="aromatic">8</PC-BondAnnotation>
                  <PC-BondAnnotation value="aromatic">8</PC-BondAnnotation>
                  <PC-BondAnnotation value="aromatic">8</PC-BondAnnotation>
                </PC-DrawAnnotations_annotation>
                <PC-DrawAnnotations_aid1>
                  <PC-DrawAnnotations_aid1_E>6</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>6</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>7</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>7</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>8</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>8</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>9</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>9</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>10</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>10</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>11</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>11</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>12</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>13</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>14</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>15</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>18</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>19</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>21</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>22</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>31</PC-DrawAnnotations_aid1_E>
                  <PC-DrawAnnotations_aid1_E>33</PC-DrawAnnotations_aid1_E>
                </PC-DrawAnnotations_aid1>
                <PC-DrawAnnotations_aid2>
                  <PC-DrawAnnotations_aid2_E>12</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>18</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>13</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>19</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>25</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>33</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>26</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>31</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>12</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>14</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>13</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>15</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>20</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>20</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>18</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>19</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>21</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>22</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>25</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>26</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>35</PC-DrawAnnotations_aid2_E>
                  <PC-DrawAnnotations_aid2_E>35</PC-DrawAnnotations_aid2_E>
                </PC-DrawAnnotations_aid2>
              </PC-DrawAnnotations>
            </PC-Conformer_style>
          </PC-Conformer>
        </PC-Coordinates_conformers>
      </PC-Coordinates>
    </PC-Compound_coords>
    <PC-Compound_charge>0</PC-Compound_charge>
    <PC-Compound_props>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Compound</PC-Urn_label>
            <PC-Urn_name>Canonicalized</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="uint">5</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_ival>1</PC-InfoData_value_ival>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Compound Complexity</PC-Urn_label>
            <PC-Urn_datatype>
              <PC-UrnDataType value="double">7</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_implementation>E_COMPLEXITY</PC-Urn_implementation>
            <PC-Urn_version>3.4.8.18</PC-Urn_version>
            <PC-Urn_software>Cactvs</PC-Urn_software>
            <PC-Urn_source>Xemistry GmbH</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_fval>1010</PC-InfoData_value_fval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Count</PC-Urn_label>
            <PC-Urn_name>Hydrogen Bond Acceptor</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="uint">5</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_implementation>E_NHACCEPTORS</PC-Urn_implementation>
            <PC-Urn_version>3.4.8.18</PC-Urn_version>
            <PC-Urn_software>Cactvs</PC-Urn_software>
            <PC-Urn_source>Xemistry GmbH</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_ival>8</PC-InfoData_value_ival>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Count</PC-Urn_label>
            <PC-Urn_name>Hydrogen Bond Donor</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="uint">5</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_implementation>E_NHDONORS</PC-Urn_implementation>
            <PC-Urn_version>3.4.8.18</PC-Urn_version>
            <PC-Urn_software>Cactvs</PC-Urn_software>
            <PC-Urn_source>Xemistry GmbH</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_ival>2</PC-InfoData_value_ival>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Count</PC-Urn_label>
            <PC-Urn_name>Rotatable Bond</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="uint">5</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_implementation>E_NROTBONDS</PC-Urn_implementation>
            <PC-Urn_version>3.4.8.18</PC-Urn_version>
            <PC-Urn_software>Cactvs</PC-Urn_software>
            <PC-Urn_source>Xemistry GmbH</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_ival>8</PC-InfoData_value_ival>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Fingerprint</PC-Urn_label>
            <PC-Urn_name>SubStructure Keys</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="fingerprint">16</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_parameters>extended 2</PC-Urn_parameters>
            <PC-Urn_implementation>E_SCREEN</PC-Urn_implementation>
            <PC-Urn_version>3.4.8.18</PC-Urn_version>
            <PC-Urn_software>Cactvs</PC-Urn_software>
            <PC-Urn_source>Xemistry GmbH</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_binary>00000371F07FB800000000200000000000000000000162C58B0000000000000000000001FE00001E00000800000C08819E0032C8B2081200A80324F24C00828020210220089821306498082072C0D0D1846408648000C8C80798D9F39E80000000000000000000000000000000000000000000</PC-InfoData_value_binary>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>IUPAC Name</PC-Urn_label>
            <PC-Urn_name>Allowed</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.7.0</PC-Urn_version>
            <PC-Urn_software>Lexichem TK</PC-Urn_software>
            <PC-Urn_source>OpenEye Scientific Software</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>ferrous;3-[18-(2-carboxyethyl)-3,7,12,17-tetramethyl-8,13-divinyl-porphyrin-21,24-diid-2-yl]propanoic acid</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>IUPAC Name</PC-Urn_label>
            <PC-Urn_name>CAS-like Style</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.7.0</PC-Urn_version>
            <PC-Urn_software>Lexichem TK</PC-Urn_software>
            <PC-Urn_source>OpenEye Scientific Software</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>3-[18-(2-carboxyethyl)-8,13-bis(ethenyl)-3,7,12,17-tetramethyl-2-porphyrin-21,24-diidyl]propanoic acid;iron(2+)</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>IUPAC Name</PC-Urn_label>
            <PC-Urn_name>Markup</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.7.0</PC-Urn_version>
            <PC-Urn_software>Lexichem TK</PC-Urn_software>
            <PC-Urn_source>OpenEye Scientific Software</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>3-[18-(2-carboxyethyl)-8,13-bis(ethenyl)-3,7,12,17-tetramethylporphyrin-21,24-diid-2-yl]propanoic acid;iron(2+)</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>IUPAC Name</PC-Urn_label>
            <PC-Urn_name>Preferred</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.7.0</PC-Urn_version>
            <PC-Urn_software>Lexichem TK</PC-Urn_software>
            <PC-Urn_source>OpenEye Scientific Software</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>3-[18-(2-carboxyethyl)-8,13-bis(ethenyl)-3,7,12,17-tetramethylporphyrin-21,24-diid-2-yl]propanoic acid;iron(2+)</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>IUPAC Name</PC-Urn_label>
            <PC-Urn_name>Systematic</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.7.0</PC-Urn_version>
            <PC-Urn_software>Lexichem TK</PC-Urn_software>
            <PC-Urn_source>OpenEye Scientific Software</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>3-[8,13-bis(ethenyl)-18-(3-hydroxy-3-oxopropyl)-3,7,12,17-tetramethyl-porphyrin-21,24-diid-2-yl]propanoic acid;iron(2+)</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>IUPAC Name</PC-Urn_label>
            <PC-Urn_name>Traditional</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.7.0</PC-Urn_version>
            <PC-Urn_software>Lexichem TK</PC-Urn_software>
            <PC-Urn_source>OpenEye Scientific Software</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>ferrous;3-[18-(2-carboxyethyl)-3,7,12,17-tetramethyl-8,13-divinyl-porphine-21,24-diid-2-yl]propionic acid</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>InChI</PC-Urn_label>
            <PC-Urn_name>Standard</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>1.0.6</PC-Urn_version>
            <PC-Urn_software>InChI</PC-Urn_software>
            <PC-Urn_source>iupac.org</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>InChI=1S/C34H34N4O4.Fe/c1-7-21-17(3)25-13-26-19(5)23(9-11-33(39)40)31(37-26)16-32-24(10-12-34(41)42)20(6)28(38-32)15-30-22(8-2)18(4)27(36-30)14-29(21)35-25;/h7-8,13-16H,1-2,9-12H2,3-6H3,(H4,35,36,37,38,39,40,41,42);/q;+2/p-2</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>InChIKey</PC-Urn_label>
            <PC-Urn_name>Standard</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>1.0.6</PC-Urn_version>
            <PC-Urn_software>InChI</PC-Urn_software>
            <PC-Urn_source>iupac.org</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>KABFMIBPWCXCRK-UHFFFAOYSA-L</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Mass</PC-Urn_label>
            <PC-Urn_name>Exact</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.2</PC-Urn_version>
            <PC-Urn_software>PubChem</PC-Urn_software>
            <PC-Urn_source>ncbi.nlm.nih.gov</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>616.177291</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Molecular Formula</PC-Urn_label>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.2</PC-Urn_version>
            <PC-Urn_software>PubChem</PC-Urn_software>
            <PC-Urn_source>ncbi.nlm.nih.gov</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>C34H32FeN4O4</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Molecular Weight</PC-Urn_label>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.2</PC-Urn_version>
            <PC-Urn_software>PubChem</PC-Urn_software>
            <PC-Urn_source>ncbi.nlm.nih.gov</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>616.5</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>SMILES</PC-Urn_label>
            <PC-Urn_name>Absolute</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.3.0</PC-Urn_version>
            <PC-Urn_software>OEChem</PC-Urn_software>
            <PC-Urn_source>OpenEye Scientific Software</PC-Urn_source>
            <PC-Urn_release>2024.12.12</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>CC1=C(C2=CC3=C(C(=C([N-]3)C=C4C(=C(C(=N4)C=C5C(=C(C(=N5)C=C1[N-]2)C)C=C)C)C=C)C)CCC(=O)O)CCC(=O)O.[Fe+2]</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>SMILES</PC-Urn_label>
            <PC-Urn_name>Canonical</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.3.0</PC-Urn_version>
            <PC-Urn_software>OEChem</PC-Urn_software>
            <PC-Urn_source>OpenEye Scientific Software</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>CC1=C(C2=CC3=C(C(=C([N-]3)C=C4C(=C(C(=N4)C=C5C(=C(C(=N5)C=C1[N-]2)C)C=C)C)C=C)C)CCC(=O)O)CCC(=O)O.[Fe+2]</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>SMILES</PC-Urn_label>
            <PC-Urn_name>Isomeric</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.3.0</PC-Urn_version>
            <PC-Urn_software>OEChem</PC-Urn_software>
            <PC-Urn_source>OpenEye Scientific Software</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>CC1=C(C2=CC3=C(C(=C([N-]3)C=C4C(=C(C(=N4)C=C5C(=C(C(=N5)C=C1[N-]2)C)C=C)C)C=C)C)CCC(=O)O)CCC(=O)O.[Fe+2]</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Topological</PC-Urn_label>
            <PC-Urn_name>Polar Surface Area</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="double">7</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_implementation>E_TPSA</PC-Urn_implementation>
            <PC-Urn_version>3.4.8.18</PC-Urn_version>
            <PC-Urn_software>Cactvs</PC-Urn_software>
            <PC-Urn_source>Xemistry GmbH</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_fval>102</PC-InfoData_value_fval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Weight</PC-Urn_label>
            <PC-Urn_name>MonoIsotopic</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="string">1</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>2.2</PC-Urn_version>
            <PC-Urn_software>PubChem</PC-Urn_software>
            <PC-Urn_source>ncbi.nlm.nih.gov</PC-Urn_source>
            <PC-Urn_release>2021.10.14</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_sval>616.177291</PC-InfoData_value_sval>
        </PC-InfoData_value>
      </PC-InfoData>
    </PC-Compound_props>
    <PC-Compound_count>
      <PC-Count>
        <PC-Count_heavy-atom>43</PC-Count_heavy-atom>
        <PC-Count_atom-chiral>0</PC-Count_atom-chiral>
        <PC-Count_atom-chiral-def>0</PC-Count_atom-chiral-def>
        <PC-Count_atom-chiral-undef>0</PC-Count_atom-chiral-undef>
        <PC-Count_bond-chiral>0</PC-Count_bond-chiral>
        <PC-Count_bond-chiral-def>0</PC-Count_bond-chiral-def>
        <PC-Count_bond-chiral-undef>0</PC-Count_bond-chiral-undef>
        <PC-Count_isotope-atom>0</PC-Count_isotope-atom>
        <PC-Count_covalent-unit>2</PC-Count_covalent-unit>
        <PC-Count_tautomers>-1</PC-Count_tautomers>
      </PC-Count>
    </PC-Compound_count>
  </PC-Compound>
</PC-Compounds>
"""

    @pytest.fixture
    def heme_3d_file_data(self):
        return """<?xml version="1.0"?>
<PC-Compounds
    xmlns="http://www.ncbi.nlm.nih.gov"
    xmlns:xs="http://www.w3.org/2001/XMLSchema-instance"
    xs:schemaLocation="http://www.ncbi.nlm.nih.gov ftp://ftp.ncbi.nlm.nih.gov/pubchem/specifications/pubchem.xsd"
>
  <PC-Compound>
    <PC-Compound_id>
      <PC-CompoundType>
        <PC-CompoundType_id>
          <PC-CompoundType_id_cid>4971</PC-CompoundType_id_cid>
        </PC-CompoundType_id>
      </PC-CompoundType>
    </PC-Compound_id>
    <PC-Compound_atoms>
      <PC-Atoms>
        <PC-Atoms_aid>
          <PC-Atoms_aid_E>1</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>2</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>3</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>4</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>5</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>6</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>7</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>8</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>9</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>10</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>11</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>12</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>13</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>14</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>15</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>16</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>17</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>18</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>19</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>20</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>21</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>22</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>23</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>24</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>25</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>26</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>27</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>28</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>29</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>30</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>31</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>32</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>33</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>34</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>35</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>36</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>37</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>38</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>39</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>40</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>41</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>42</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>43</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>44</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>45</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>46</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>47</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>48</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>49</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>50</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>51</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>52</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>53</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>54</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>55</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>56</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>57</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>58</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>59</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>60</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>61</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>62</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>63</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>64</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>65</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>66</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>67</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>68</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>69</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>70</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>71</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>72</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>73</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>74</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>75</PC-Atoms_aid_E>
          <PC-Atoms_aid_E>76</PC-Atoms_aid_E>
        </PC-Atoms_aid>
        <PC-Atoms_element>
          <PC-Element value="o">8</PC-Element>
          <PC-Element value="o">8</PC-Element>
          <PC-Element value="o">8</PC-Element>
          <PC-Element value="o">8</PC-Element>
          <PC-Element value="n">7</PC-Element>
          <PC-Element value="n">7</PC-Element>
          <PC-Element value="n">7</PC-Element>
          <PC-Element value="n">7</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="c">6</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
          <PC-Element value="h">1</PC-Element>
        </PC-Atoms_element>
      </PC-Atoms>
    </PC-Compound_atoms>
    <PC-Compound_bonds>
      <PC-Bonds>
        <PC-Bonds_aid1>
          <PC-Bonds_aid1_E>1</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>1</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>2</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>2</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>3</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>4</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>5</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>5</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>5</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>6</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>6</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>6</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>7</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>7</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>8</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>8</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>9</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>9</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>9</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>10</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>10</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>10</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>11</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>12</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>12</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>13</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>14</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>14</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>15</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>16</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>17</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>17</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>18</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>18</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>19</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>19</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>20</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>20</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>21</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>21</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>21</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>22</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>22</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>22</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>23</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>24</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>24</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>25</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>25</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>26</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>27</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>28</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>29</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>30</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>31</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>31</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>31</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>32</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>32</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>32</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>33</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>33</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>33</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>34</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>34</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>34</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>35</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>35</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>35</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>36</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>36</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>36</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>37</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>37</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>38</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>38</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>41</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>41</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>42</PC-Bonds_aid1_E>
          <PC-Bonds_aid1_E>42</PC-Bonds_aid1_E>
        </PC-Bonds_aid1>
        <PC-Bonds_aid2>
          <PC-Bonds_aid2_E>39</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>75</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>40</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>76</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>39</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>40</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>17</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>20</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>50</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>18</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>19</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>51</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>11</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>15</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>13</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>16</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>11</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>12</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>21</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>13</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>14</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>22</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>23</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>15</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>31</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>23</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>16</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>34</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>28</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>29</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>24</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>28</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>25</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>30</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>27</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>29</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>26</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>30</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>32</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>43</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>44</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>33</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>45</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>46</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>47</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>26</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>35</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>27</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>36</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>37</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>38</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>48</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>49</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>52</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>53</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>54</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>55</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>39</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>56</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>57</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>40</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>58</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>59</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>60</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>61</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>62</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>63</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>64</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>65</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>66</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>67</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>68</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>41</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>69</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>42</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>70</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>71</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>72</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>73</PC-Bonds_aid2_E>
          <PC-Bonds_aid2_E>74</PC-Bonds_aid2_E>
        </PC-Bonds_aid2>
        <PC-Bonds_order>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="double">2</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
          <PC-BondType value="single">1</PC-BondType>
        </PC-Bonds_order>
      </PC-Bonds>
    </PC-Compound_bonds>
    <PC-Compound_coords>
      <PC-Coordinates>
        <PC-Coordinates_type>
          <PC-CoordinateType value="threed">2</PC-CoordinateType>
          <PC-CoordinateType value="computed">5</PC-CoordinateType>
          <PC-CoordinateType value="units-angstroms">10</PC-CoordinateType>
        </PC-Coordinates_type>
        <PC-Coordinates_aid>
          <PC-Coordinates_aid_E>1</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>2</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>3</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>4</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>5</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>6</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>7</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>8</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>9</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>10</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>11</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>12</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>13</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>14</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>15</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>16</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>17</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>18</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>19</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>20</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>21</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>22</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>23</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>24</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>25</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>26</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>27</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>28</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>29</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>30</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>31</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>32</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>33</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>34</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>35</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>36</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>37</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>38</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>39</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>40</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>41</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>42</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>43</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>44</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>45</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>46</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>47</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>48</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>49</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>50</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>51</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>52</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>53</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>54</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>55</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>56</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>57</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>58</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>59</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>60</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>61</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>62</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>63</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>64</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>65</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>66</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>67</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>68</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>69</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>70</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>71</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>72</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>73</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>74</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>75</PC-Coordinates_aid_E>
          <PC-Coordinates_aid_E>76</PC-Coordinates_aid_E>
        </PC-Coordinates_aid>
        <PC-Coordinates_conformers>
          <PC-Conformer>
            <PC-Conformer_x>
              <PC-Conformer_x_E>7.1385</PC-Conformer_x_E>
              <PC-Conformer_x_E>5.7615</PC-Conformer_x_E>
              <PC-Conformer_x_E>6.7154</PC-Conformer_x_E>
              <PC-Conformer_x_E>6.1372</PC-Conformer_x_E>
              <PC-Conformer_x_E>-2.525</PC-Conformer_x_E>
              <PC-Conformer_x_E>-2.6939</PC-Conformer_x_E>
              <PC-Conformer_x_E>0.4051</PC-Conformer_x_E>
              <PC-Conformer_x_E>0.1811</PC-Conformer_x_E>
              <PC-Conformer_x_E>2.507</PC-Conformer_x_E>
              <PC-Conformer_x_E>2.0591</PC-Conformer_x_E>
              <PC-Conformer_x_E>1.6482</PC-Conformer_x_E>
              <PC-Conformer_x_E>1.6304</PC-Conformer_x_E>
              <PC-Conformer_x_E>1.5429</PC-Conformer_x_E>
              <PC-Conformer_x_E>1.0549</PC-Conformer_x_E>
              <PC-Conformer_x_E>0.3143</PC-Conformer_x_E>
              <PC-Conformer_x_E>-0.1068</PC-Conformer_x_E>
              <PC-Conformer_x_E>-2.0505</PC-Conformer_x_E>
              <PC-Conformer_x_E>-3.9963</PC-Conformer_x_E>
              <PC-Conformer_x_E>-2.5688</PC-Conformer_x_E>
              <PC-Conformer_x_E>-3.7828</PC-Conformer_x_E>
              <PC-Conformer_x_E>3.9475</PC-Conformer_x_E>
              <PC-Conformer_x_E>3.5095</PC-Conformer_x_E>
              <PC-Conformer_x_E>2.2658</PC-Conformer_x_E>
              <PC-Conformer_x_E>-3.0486</PC-Conformer_x_E>
              <PC-Conformer_x_E>-4.7892</PC-Conformer_x_E>
              <PC-Conformer_x_E>-4.1304</PC-Conformer_x_E>
              <PC-Conformer_x_E>-3.9471</PC-Conformer_x_E>
              <PC-Conformer_x_E>-0.7823</PC-Conformer_x_E>
              <PC-Conformer_x_E>-1.4551</PC-Conformer_x_E>
              <PC-Conformer_x_E>-4.5176</PC-Conformer_x_E>
              <PC-Conformer_x_E>1.9005</PC-Conformer_x_E>
              <PC-Conformer_x_E>4.852</PC-Conformer_x_E>
              <PC-Conformer_x_E>3.9112</PC-Conformer_x_E>
              <PC-Conformer_x_E>1.0259</PC-Conformer_x_E>
              <PC-Conformer_x_E>-2.9926</PC-Conformer_x_E>
              <PC-Conformer_x_E>-6.2814</PC-Conformer_x_E>
              <PC-Conformer_x_E>-5.36</PC-Conformer_x_E>
              <PC-Conformer_x_E>-4.3596</PC-Conformer_x_E>
              <PC-Conformer_x_E>6.3128</PC-Conformer_x_E>
              <PC-Conformer_x_E>5.3729</PC-Conformer_x_E>
              <PC-Conformer_x_E>-6.1715</PC-Conformer_x_E>
              <PC-Conformer_x_E>-4.6339</PC-Conformer_x_E>
              <PC-Conformer_x_E>4.1938</PC-Conformer_x_E>
              <PC-Conformer_x_E>4.1687</PC-Conformer_x_E>
              <PC-Conformer_x_E>3.7406</PC-Conformer_x_E>
              <PC-Conformer_x_E>4.1341</PC-Conformer_x_E>
              <PC-Conformer_x_E>3.3403</PC-Conformer_x_E>
              <PC-Conformer_x_E>-0.7083</PC-Conformer_x_E>
              <PC-Conformer_x_E>-1.5138</PC-Conformer_x_E>
              <PC-Conformer_x_E>-2.0287</PC-Conformer_x_E>
              <PC-Conformer_x_E>-1.9035</PC-Conformer_x_E>
              <PC-Conformer_x_E>-5.5979</PC-Conformer_x_E>
              <PC-Conformer_x_E>1.2897</PC-Conformer_x_E>
              <PC-Conformer_x_E>2.9482</PC-Conformer_x_E>
              <PC-Conformer_x_E>1.6775</PC-Conformer_x_E>
              <PC-Conformer_x_E>4.6712</PC-Conformer_x_E>
              <PC-Conformer_x_E>4.6518</PC-Conformer_x_E>
              <PC-Conformer_x_E>3.3272</PC-Conformer_x_E>
              <PC-Conformer_x_E>3.7327</PC-Conformer_x_E>
              <PC-Conformer_x_E>2.0137</PC-Conformer_x_E>
              <PC-Conformer_x_E>0.3499</PC-Conformer_x_E>
              <PC-Conformer_x_E>0.6873</PC-Conformer_x_E>
              <PC-Conformer_x_E>-3.5447</PC-Conformer_x_E>
              <PC-Conformer_x_E>-3.4318</PC-Conformer_x_E>
              <PC-Conformer_x_E>-1.9644</PC-Conformer_x_E>
              <PC-Conformer_x_E>-6.7151</PC-Conformer_x_E>
              <PC-Conformer_x_E>-6.61</PC-Conformer_x_E>
              <PC-Conformer_x_E>-6.7014</PC-Conformer_x_E>
              <PC-Conformer_x_E>-5.693</PC-Conformer_x_E>
              <PC-Conformer_x_E>-4.4411</PC-Conformer_x_E>
              <PC-Conformer_x_E>-7.0854</PC-Conformer_x_E>
              <PC-Conformer_x_E>-5.9398</PC-Conformer_x_E>
              <PC-Conformer_x_E>-4.9394</PC-Conformer_x_E>
              <PC-Conformer_x_E>-4.5621</PC-Conformer_x_E>
              <PC-Conformer_x_E>8.0834</PC-Conformer_x_E>
              <PC-Conformer_x_E>6.7157</PC-Conformer_x_E>
            </PC-Conformer_x>
            <PC-Conformer_y>
              <PC-Conformer_y_E>2.705</PC-Conformer_y_E>
              <PC-Conformer_y_E>-3.2503</PC-Conformer_y_E>
              <PC-Conformer_y_E>2.1599</PC-Conformer_y_E>
              <PC-Conformer_y_E>-3.4886</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.9272</PC-Conformer_y_E>
              <PC-Conformer_y_E>-1.118</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.517</PC-Conformer_y_E>
              <PC-Conformer_y_E>-1.3404</PC-Conformer_y_E>
              <PC-Conformer_y_E>2.3377</PC-Conformer_y_E>
              <PC-Conformer_y_E>-2.6167</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.2058</PC-Conformer_y_E>
              <PC-Conformer_y_E>3.3517</PC-Conformer_y_E>
              <PC-Conformer_y_E>-1.2639</PC-Conformer_y_E>
              <PC-Conformer_y_E>-3.502</PC-Conformer_y_E>
              <PC-Conformer_y_E>2.872</PC-Conformer_y_E>
              <PC-Conformer_y_E>-2.6087</PC-Conformer_y_E>
              <PC-Conformer_y_E>3.1577</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.6924</PC-Conformer_y_E>
              <PC-Conformer_y_E>-2.4592</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.7074</PC-Conformer_y_E>
              <PC-Conformer_y_E>2.2748</PC-Conformer_y_E>
              <PC-Conformer_y_E>-2.9072</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.1348</PC-Conformer_y_E>
              <PC-Conformer_y_E>3.753</PC-Conformer_y_E>
              <PC-Conformer_y_E>-1.9053</PC-Conformer_y_E>
              <PC-Conformer_y_E>2.8451</PC-Conformer_y_E>
              <PC-Conformer_y_E>-2.9601</PC-Conformer_y_E>
              <PC-Conformer_y_E>3.6329</PC-Conformer_y_E>
              <PC-Conformer_y_E>-3.2035</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.5263</PC-Conformer_y_E>
              <PC-Conformer_y_E>4.7807</PC-Conformer_y_E>
              <PC-Conformer_y_E>2.5394</PC-Conformer_y_E>
              <PC-Conformer_y_E>-2.9257</PC-Conformer_y_E>
              <PC-Conformer_y_E>-4.9791</PC-Conformer_y_E>
              <PC-Conformer_y_E>5.1012</PC-Conformer_y_E>
              <PC-Conformer_y_E>-1.8735</PC-Conformer_y_E>
              <PC-Conformer_y_E>3.0491</PC-Conformer_y_E>
              <PC-Conformer_y_E>-4.3097</PC-Conformer_y_E>
              <PC-Conformer_y_E>2.4348</PC-Conformer_y_E>
              <PC-Conformer_y_E>-3.2588</PC-Conformer_y_E>
              <PC-Conformer_y_E>2.1311</PC-Conformer_y_E>
              <PC-Conformer_y_E>-5.2115</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.3129</PC-Conformer_y_E>
              <PC-Conformer_y_E>3.0159</PC-Conformer_y_E>
              <PC-Conformer_y_E>-3.8863</PC-Conformer_y_E>
              <PC-Conformer_y_E>-2.2066</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.1671</PC-Conformer_y_E>
              <PC-Conformer_y_E>4.7057</PC-Conformer_y_E>
              <PC-Conformer_y_E>-4.2667</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.2921</PC-Conformer_y_E>
              <PC-Conformer_y_E>-0.5315</PC-Conformer_y_E>
              <PC-Conformer_y_E>0.6383</PC-Conformer_y_E>
              <PC-Conformer_y_E>5.1008</PC-Conformer_y_E>
              <PC-Conformer_y_E>4.9486</PC-Conformer_y_E>
              <PC-Conformer_y_E>5.4274</PC-Conformer_y_E>
              <PC-Conformer_y_E>3.5474</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.8113</PC-Conformer_y_E>
              <PC-Conformer_y_E>-3.6772</PC-Conformer_y_E>
              <PC-Conformer_y_E>-1.9441</PC-Conformer_y_E>
              <PC-Conformer_y_E>-5.3942</PC-Conformer_y_E>
              <PC-Conformer_y_E>-5.3061</PC-Conformer_y_E>
              <PC-Conformer_y_E>-5.4128</PC-Conformer_y_E>
              <PC-Conformer_y_E>5.8188</PC-Conformer_y_E>
              <PC-Conformer_y_E>5.0997</PC-Conformer_y_E>
              <PC-Conformer_y_E>5.4627</PC-Conformer_y_E>
              <PC-Conformer_y_E>-1.5506</PC-Conformer_y_E>
              <PC-Conformer_y_E>-1.1876</PC-Conformer_y_E>
              <PC-Conformer_y_E>-2.8571</PC-Conformer_y_E>
              <PC-Conformer_y_E>4.0826</PC-Conformer_y_E>
              <PC-Conformer_y_E>-4.5822</PC-Conformer_y_E>
              <PC-Conformer_y_E>2.4544</PC-Conformer_y_E>
              <PC-Conformer_y_E>1.0737</PC-Conformer_y_E>
              <PC-Conformer_y_E>-6.2155</PC-Conformer_y_E>
              <PC-Conformer_y_E>-4.9765</PC-Conformer_y_E>
              <PC-Conformer_y_E>2.6451</PC-Conformer_y_E>
              <PC-Conformer_y_E>-3.456</PC-Conformer_y_E>
            </PC-Conformer_y>
            <PC-Conformer_z>
              <PC-Conformer_z_E>-0.6711</PC-Conformer_z_E>
              <PC-Conformer_z_E>-2.9408</PC-Conformer_z_E>
              <PC-Conformer_z_E>1.493</PC-Conformer_z_E>
              <PC-Conformer_z_E>-0.7132</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.2862</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.2758</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.2379</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.4974</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.8711</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.1996</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.4657</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.8618</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.3342</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.2769</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.4652</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.4631</PC-Conformer_z_E>
              <PC-Conformer_z_E>-0.111</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.2747</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.54</PC-Conformer_z_E>
              <PC-Conformer_z_E>-0.2302</PC-Conformer_z_E>
              <PC-Conformer_z_E>1.2062</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.0057</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.3202</PC-Conformer_z_E>
              <PC-Conformer_z_E>-0.8571</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.5602</PC-Conformer_z_E>
              <PC-Conformer_z_E>-0.9341</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.7181</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.3107</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.6248</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.0526</PC-Conformer_z_E>
              <PC-Conformer_z_E>1.1965</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.0033</PC-Conformer_z_E>
              <PC-Conformer_z_E>-1.4638</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.1919</PC-Conformer_z_E>
              <PC-Conformer_z_E>-1.4661</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.6439</PC-Conformer_z_E>
              <PC-Conformer_z_E>-1.6044</PC-Conformer_z_E>
              <PC-Conformer_z_E>1.0073</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.3698</PC-Conformer_z_E>
              <PC-Conformer_z_E>-1.6419</PC-Conformer_z_E>
              <PC-Conformer_z_E>-2.1847</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.0645</PC-Conformer_z_E>
              <PC-Conformer_z_E>1.6711</PC-Conformer_z_E>
              <PC-Conformer_z_E>1.9856</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.4471</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.5729</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.1855</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.4708</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.8304</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.8961</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.0596</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.092</PC-Conformer_z_E>
              <PC-Conformer_z_E>2.0471</PC-Conformer_z_E>
              <PC-Conformer_z_E>1.4639</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.3414</PC-Conformer_z_E>
              <PC-Conformer_z_E>-0.3875</PC-Conformer_z_E>
              <PC-Conformer_z_E>-0.7907</PC-Conformer_z_E>
              <PC-Conformer_z_E>-2.0076</PC-Conformer_z_E>
              <PC-Conformer_z_E>-1.9173</PC-Conformer_z_E>
              <PC-Conformer_z_E>-0.029</PC-Conformer_z_E>
              <PC-Conformer_z_E>-0.6044</PC-Conformer_z_E>
              <PC-Conformer_z_E>1.1379</PC-Conformer_z_E>
              <PC-Conformer_z_E>-0.8503</PC-Conformer_z_E>
              <PC-Conformer_z_E>-2.4692</PC-Conformer_z_E>
              <PC-Conformer_z_E>-1.568</PC-Conformer_z_E>
              <PC-Conformer_z_E>-0.3082</PC-Conformer_z_E>
              <PC-Conformer_z_E>1.4317</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.8758</PC-Conformer_z_E>
              <PC-Conformer_z_E>-1.6921</PC-Conformer_z_E>
              <PC-Conformer_z_E>2.0553</PC-Conformer_z_E>
              <PC-Conformer_z_E>-2.6733</PC-Conformer_z_E>
              <PC-Conformer_z_E>-2.2183</PC-Conformer_z_E>
              <PC-Conformer_z_E>0.3391</PC-Conformer_z_E>
              <PC-Conformer_z_E>-0.9923</PC-Conformer_z_E>
              <PC-Conformer_z_E>-0.4143</PC-Conformer_z_E>
              <PC-Conformer_z_E>-3.0389</PC-Conformer_z_E>
            </PC-Conformer_z>
            <PC-Conformer_data>
              <PC-InfoData>
                <PC-InfoData_urn>
                  <PC-Urn>
                    <PC-Urn_label>Conformer</PC-Urn_label>
                    <PC-Urn_name>ID</PC-Urn_name>
                    <PC-Urn_datatype>
                      <PC-UrnDataType value="uint64">11</PC-UrnDataType>
                    </PC-Urn_datatype>
                    <PC-Urn_version>2.1</PC-Urn_version>
                    <PC-Urn_software>PubChem</PC-Urn_software>
                    <PC-Urn_source>ncbi.nlm.nih.gov</PC-Urn_source>
                    <PC-Urn_release>2009.12.11</PC-Urn_release>
                  </PC-Urn>
                </PC-InfoData_urn>
                <PC-InfoData_value>
                  <PC-InfoData_value_sval>0000136B00000001</PC-InfoData_value_sval>
                </PC-InfoData_value>
              </PC-InfoData>
              <PC-InfoData>
                <PC-InfoData_urn>
                  <PC-Urn>
                    <PC-Urn_label>Energy</PC-Urn_label>
                    <PC-Urn_name>MMFF94 NoEstat</PC-Urn_name>
                    <PC-Urn_datatype>
                      <PC-UrnDataType value="double">7</PC-UrnDataType>
                    </PC-Urn_datatype>
                    <PC-Urn_version>1.7.2</PC-Urn_version>
                    <PC-Urn_software>Szybki</PC-Urn_software>
                    <PC-Urn_source>openeye.com</PC-Urn_source>
                    <PC-Urn_release>2012.11.26</PC-Urn_release>
                  </PC-Urn>
                </PC-InfoData_urn>
                <PC-InfoData_value>
                  <PC-InfoData_value_fval>113.2274</PC-InfoData_value_fval>
                </PC-InfoData_value>
              </PC-InfoData>
              <PC-InfoData>
                <PC-InfoData_urn>
                  <PC-Urn>
                    <PC-Urn_label>Feature</PC-Urn_label>
                    <PC-Urn_name>Self Overlap</PC-Urn_name>
                    <PC-Urn_datatype>
                      <PC-UrnDataType value="double">7</PC-UrnDataType>
                    </PC-Urn_datatype>
                    <PC-Urn_version>2.1</PC-Urn_version>
                    <PC-Urn_software>PubChem</PC-Urn_software>
                    <PC-Urn_source>ncbi.nlm.nih.gov</PC-Urn_source>
                    <PC-Urn_release>2012.11.26</PC-Urn_release>
                  </PC-Urn>
                </PC-InfoData_urn>
                <PC-InfoData_value>
                  <PC-InfoData_value_fval>91.467</PC-InfoData_value_fval>
                </PC-InfoData_value>
              </PC-InfoData>
              <PC-InfoData>
                <PC-InfoData_urn>
                  <PC-Urn>
                    <PC-Urn_label>Fingerprint</PC-Urn_label>
                    <PC-Urn_name>Shape</PC-Urn_name>
                    <PC-Urn_datatype>
                      <PC-UrnDataType value="stringlist">2</PC-UrnDataType>
                    </PC-Urn_datatype>
                    <PC-Urn_version>2.1</PC-Urn_version>
                    <PC-Urn_software>PubChem</PC-Urn_software>
                    <PC-Urn_source>ncbi.nlm.nih.gov</PC-Urn_source>
                    <PC-Urn_release>2012.11.26</PC-Urn_release>
                  </PC-Urn>
                </PC-InfoData_urn>
                <PC-InfoData_value>
                  <PC-InfoData_value_slist>
                    <PC-InfoData_value_slist_E>10190206 1 17837227974003681670</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>11204353 107 18411981321871663070</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>11227688 84 18272077340465287277</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>11513181 2 18200582696201270198</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>12645989 146 17836087049689112414</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>14117953 113 18193272117098521597</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>14415360 78 17829314801318578837</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>14725015 67 17975403930735511203</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>14747282 125 18270417013720271431</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>15320467 1 18265329685113451249</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>15400415 2 18120079603191075997</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>15950262 2 15216139600569668141</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>15968369 26 18269254804497563256</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>16112460 7 18271817761242498769</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>20028762 73 17839462528964120378</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>20609170 92 18407757040677506604</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>20775438 99 18125412290218664175</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>21033648 144 18411981399492219519</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>21792965 2 18335686231985395930</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>22311459 1 18194965377705692746</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>25223398 141 18115581702694767268</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>4403749 210 18121193618807126224</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>50150288 127 16844182142828248609</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>5171179 24 18413392037791061314</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>5265222 85 17979079602809049044</PC-InfoData_value_slist_E>
                    <PC-InfoData_value_slist_E>5776283 40 18263933124382620565</PC-InfoData_value_slist_E>
                  </PC-InfoData_value_slist>
                </PC-InfoData_value>
              </PC-InfoData>
              <PC-InfoData>
                <PC-InfoData_urn>
                  <PC-Urn>
                    <PC-Urn_label>Shape</PC-Urn_label>
                    <PC-Urn_name>Multipoles</PC-Urn_name>
                    <PC-Urn_datatype>
                      <PC-UrnDataType value="doublevec">8</PC-UrnDataType>
                    </PC-Urn_datatype>
                    <PC-Urn_version>1.8.3</PC-Urn_version>
                    <PC-Urn_software>OEShape</PC-Urn_software>
                    <PC-Urn_source>openeye.com</PC-Urn_source>
                    <PC-Urn_release>2012.11.26</PC-Urn_release>
                  </PC-Urn>
                </PC-InfoData_urn>
                <PC-InfoData_value>
                  <PC-InfoData_value_fvec>
                    <PC-InfoData_value_fvec_E>820.94</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>15.1</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>9.26</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>1.44</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>10</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>1.8</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>0.92</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>0.13</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>4.37</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>-1.32</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>0.9</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>0.8</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>-0.04</PC-InfoData_value_fvec_E>
                    <PC-InfoData_value_fvec_E>7.12</PC-InfoData_value_fvec_E>
                  </PC-InfoData_value_fvec>
                </PC-InfoData_value>
              </PC-InfoData>
              <PC-InfoData>
                <PC-InfoData_urn>
                  <PC-Urn>
                    <PC-Urn_label>Shape</PC-Urn_label>
                    <PC-Urn_name>Self Overlap</PC-Urn_name>
                    <PC-Urn_datatype>
                      <PC-UrnDataType value="double">7</PC-UrnDataType>
                    </PC-Urn_datatype>
                    <PC-Urn_version>2.1</PC-Urn_version>
                    <PC-Urn_software>PubChem</PC-Urn_software>
                    <PC-Urn_source>ncbi.nlm.nih.gov</PC-Urn_source>
                    <PC-Urn_release>2012.11.26</PC-Urn_release>
                  </PC-Urn>
                </PC-InfoData_urn>
                <PC-InfoData_value>
                  <PC-InfoData_value_fval>1798.142</PC-InfoData_value_fval>
                </PC-InfoData_value>
              </PC-InfoData>
              <PC-InfoData>
                <PC-InfoData_urn>
                  <PC-Urn>
                    <PC-Urn_label>Shape</PC-Urn_label>
                    <PC-Urn_name>Volume</PC-Urn_name>
                    <PC-Urn_datatype>
                      <PC-UrnDataType value="double">7</PC-UrnDataType>
                    </PC-Urn_datatype>
                    <PC-Urn_version>1.8.3</PC-Urn_version>
                    <PC-Urn_software>OEShape</PC-Urn_software>
                    <PC-Urn_source>openeye.com</PC-Urn_source>
                    <PC-Urn_release>2012.11.26</PC-Urn_release>
                  </PC-Urn>
                </PC-InfoData_urn>
                <PC-InfoData_value>
                  <PC-InfoData_value_fval>447.4</PC-InfoData_value_fval>
                </PC-InfoData_value>
              </PC-InfoData>
            </PC-Conformer_data>
          </PC-Conformer>
        </PC-Coordinates_conformers>
        <PC-Coordinates_data>
          <PC-InfoData>
            <PC-InfoData_urn>
              <PC-Urn>
                <PC-Urn_label>Conformer</PC-Urn_label>
                <PC-Urn_name>RMSD</PC-Urn_name>
                <PC-Urn_datatype>
                  <PC-UrnDataType value="double">7</PC-UrnDataType>
                </PC-Urn_datatype>
                <PC-Urn_release>2009.12.11</PC-Urn_release>
              </PC-Urn>
            </PC-InfoData_urn>
            <PC-InfoData_value>
              <PC-InfoData_value_fval>1</PC-InfoData_value_fval>
            </PC-InfoData_value>
          </PC-InfoData>
          <PC-InfoData>
            <PC-InfoData_urn>
              <PC-Urn>
                <PC-Urn_label>Diverse Conformer</PC-Urn_label>
                <PC-Urn_name>ID List</PC-Urn_name>
                <PC-Urn_datatype>
                  <PC-UrnDataType value="uintvec">6</PC-UrnDataType>
                </PC-Urn_datatype>
                <PC-Urn_release>2010.05.05</PC-Urn_release>
              </PC-Urn>
            </PC-InfoData_urn>
            <PC-InfoData_value>
              <PC-InfoData_value_ivec>
                <PC-InfoData_value_ivec_E>1</PC-InfoData_value_ivec_E>
                <PC-InfoData_value_ivec_E>4</PC-InfoData_value_ivec_E>
                <PC-InfoData_value_ivec_E>9</PC-InfoData_value_ivec_E>
                <PC-InfoData_value_ivec_E>8</PC-InfoData_value_ivec_E>
                <PC-InfoData_value_ivec_E>6</PC-InfoData_value_ivec_E>
                <PC-InfoData_value_ivec_E>7</PC-InfoData_value_ivec_E>
                <PC-InfoData_value_ivec_E>2</PC-InfoData_value_ivec_E>
                <PC-InfoData_value_ivec_E>5</PC-InfoData_value_ivec_E>
                <PC-InfoData_value_ivec_E>3</PC-InfoData_value_ivec_E>
              </PC-InfoData_value_ivec>
            </PC-InfoData_value>
          </PC-InfoData>
        </PC-Coordinates_data>
      </PC-Coordinates>
    </PC-Compound_coords>
    <PC-Compound_props>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Charge</PC-Urn_label>
            <PC-Urn_name>MMFF94 Partial</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="stringlist">2</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>1.9.0</PC-Urn_version>
            <PC-Urn_software>OEChem</PC-Urn_software>
            <PC-Urn_source>openeye.com</PC-Urn_source>
            <PC-Urn_release>2012.11.26</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_slist>
            <PC-InfoData_value_slist_E>55</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>1 -0.65</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>10 -0.14</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>11 0.42</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>12 -0.14</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>13 0.17</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>14 -0.12</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>15 0.17</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>16 0.42</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>17 -0.2</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>18 0.1</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>19 0.1</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>2 -0.65</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>20 -0.2</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>21 0.14</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>22 0.14</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>23 -0.14</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>24 -0.18</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>25 -0.14</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>26 -0.05</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>28 -0.11</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>29 -0.14</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>3 -0.57</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>30 -0.11</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>31 0.14</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>32 0.06</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>33 0.06</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>34 0.14</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>35 0.18</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>36 0.14</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>37 -0.1</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>38 -0.15</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>39 0.66</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>4 -0.57</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>40 0.66</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>41 -0.3</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>42 -0.3</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>47 0.15</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>48 0.15</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>49 0.15</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>5 0.03</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>50 0.27</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>51 0.4</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>52 0.15</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>6 -0.6</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>69 0.15</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>7 -0.62</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>70 0.15</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>71 0.15</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>72 0.15</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>73 0.15</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>74 0.15</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>75 0.5</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>76 0.5</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>8 -0.62</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>9 -0.12</PC-InfoData_value_slist_E>
          </PC-InfoData_value_slist>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Count</PC-Urn_label>
            <PC-Urn_name>Effective Rotor</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="double">7</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_version>1.9.0</PC-Urn_version>
            <PC-Urn_software>OEChem</PC-Urn_software>
            <PC-Urn_source>ncbi.nlm.nih.gov</PC-Urn_source>
            <PC-Urn_release>2012.11.26</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_fval>8</PC-InfoData_value_fval>
        </PC-InfoData_value>
      </PC-InfoData>
      <PC-InfoData>
        <PC-InfoData_urn>
          <PC-Urn>
            <PC-Urn_label>Features</PC-Urn_label>
            <PC-Urn_name>Pharmacophore</PC-Urn_name>
            <PC-Urn_datatype>
              <PC-UrnDataType value="stringlist">2</PC-UrnDataType>
            </PC-Urn_datatype>
            <PC-Urn_parameters>ImplicitMillsDean merged</PC-Urn_parameters>
            <PC-Urn_version>1.8.3</PC-Urn_version>
            <PC-Urn_software>OEShape</PC-Urn_software>
            <PC-Urn_source>openeye.com</PC-Urn_source>
            <PC-Urn_release>2012.11.26</PC-Urn_release>
          </PC-Urn>
        </PC-InfoData_urn>
        <PC-InfoData_value>
          <PC-InfoData_value_slist>
            <PC-InfoData_value_slist_E>18</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>1 1 acceptor</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>1 2 acceptor</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>1 3 acceptor</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>1 4 acceptor</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>1 41 hydrophobe</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>1 42 hydrophobe</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>1 5 cation</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>1 5 donor</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>1 6 cation</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>1 6 donor</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>1 7 acceptor</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>1 8 acceptor</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>3 1 3 39 anion</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>3 2 4 40 anion</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>5 5 17 20 24 26 rings</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>5 6 18 19 25 27 rings</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>5 7 9 11 12 15 rings</PC-InfoData_value_slist_E>
            <PC-InfoData_value_slist_E>5 8 10 13 14 16 rings</PC-InfoData_value_slist_E>
          </PC-InfoData_value_slist>
        </PC-InfoData_value>
      </PC-InfoData>
    </PC-Compound_props>
    <PC-Compound_count>
      <PC-Count>
        <PC-Count_heavy-atom>42</PC-Count_heavy-atom>
        <PC-Count_atom-chiral>0</PC-Count_atom-chiral>
        <PC-Count_atom-chiral-def>0</PC-Count_atom-chiral-def>
        <PC-Count_atom-chiral-undef>0</PC-Count_atom-chiral-undef>
        <PC-Count_bond-chiral>0</PC-Count_bond-chiral>
        <PC-Count_bond-chiral-def>0</PC-Count_bond-chiral-def>
        <PC-Count_bond-chiral-undef>0</PC-Count_bond-chiral-undef>
        <PC-Count_isotope-atom>0</PC-Count_isotope-atom>
        <PC-Count_covalent-unit>1</PC-Count_covalent-unit>
        <PC-Count_tautomers>6</PC-Count_tautomers>
      </PC-Count>
    </PC-Compound_count>
  </PC-Compound>
</PC-Compounds>
"""

    @pytest.fixture
    def acetone_2d_molecule_data(self):
        return (
            {
                1: {"element": "O", "coords": np.array([3.732, 0.75, 0.0])},
                2: {"element": "C", "coords": np.array([2.866, 0.25, 0.0])},
                3: {"element": "C", "coords": np.array([2.0, 0.75, 0.0])},
                4: {"element": "C", "coords": np.array([2.866, -0.75, 0.0])},
                5: {"element": "H", "coords": np.array([2.31, 1.2869, 0.0])},
                6: {"element": "H", "coords": np.array([1.4631, 1.06, 0.0])},
                7: {"element": "H", "coords": np.array([1.69, 0.2131, 0.0])},
                8: {"element": "H", "coords": np.array([2.246, -0.75, 0.0])},
                9: {"element": "H", "coords": np.array([2.866, -1.37, 0.0])},
                10: {"element": "H", "coords": np.array([3.486, -0.75, 0.0])},
            },
            {
                0: {"from_atom_index": 1, "to_atom_index": 2, "bond_type": 2},
                1: {"from_atom_index": 2, "to_atom_index": 3, "bond_type": 1},
                2: {"from_atom_index": 2, "to_atom_index": 4, "bond_type": 1},
                3: {"from_atom_index": 3, "to_atom_index": 5, "bond_type": 1},
                4: {"from_atom_index": 3, "to_atom_index": 6, "bond_type": 1},
                5: {"from_atom_index": 3, "to_atom_index": 7, "bond_type": 1},
                6: {"from_atom_index": 4, "to_atom_index": 8, "bond_type": 1},
                7: {"from_atom_index": 4, "to_atom_index": 9, "bond_type": 1},
                8: {"from_atom_index": 4, "to_atom_index": 10, "bond_type": 1},
            },
        )

    @pytest.fixture
    def acetone_3d_molecule_data(self):
        return (
            {
                1: {
                    "element": "O",
                    "coords": np.array([3.0000e-04, -1.3171e00, -2.0000e-04]),
                },
                2: {"element": "C", "coords": np.array([0.0, -0.0872, 0.0006])},
                3: {
                    "element": "C",
                    "coords": np.array([1.281e00, 7.024e-01, -2.000e-04]),
                },
                4: {
                    "element": "C",
                    "coords": np.array([-1.2813e00, 7.0190e-01, -2.0000e-04]),
                },
                5: {"element": "H", "coords": np.array([1.3279, 1.3235, -0.898])},
                6: {"element": "H", "coords": np.array([1.326, 1.3282, 0.8945])},
                7: {"element": "H", "coords": np.array([2.1351, 0.0196, 0.0027])},
                8: {"element": "H", "coords": np.array([-2.1352, 0.0187, 0.0027])},
                9: {"element": "H", "coords": np.array([-1.3284, 1.323, -0.898])},
                10: {"element": "H", "coords": np.array([-1.3266, 1.3278, 0.8945])},
            },
            {
                0: {"from_atom_index": 1, "to_atom_index": 2, "bond_type": 2},
                1: {"from_atom_index": 2, "to_atom_index": 3, "bond_type": 1},
                2: {"from_atom_index": 2, "to_atom_index": 4, "bond_type": 1},
                3: {"from_atom_index": 3, "to_atom_index": 5, "bond_type": 1},
                4: {"from_atom_index": 3, "to_atom_index": 6, "bond_type": 1},
                5: {"from_atom_index": 3, "to_atom_index": 7, "bond_type": 1},
                6: {"from_atom_index": 4, "to_atom_index": 8, "bond_type": 1},
                7: {"from_atom_index": 4, "to_atom_index": 9, "bond_type": 1},
                8: {"from_atom_index": 4, "to_atom_index": 10, "bond_type": 1},
            },
        )

    @pytest.fixture
    def morphine_2d_molecule_data(self):
        return (
            {
                1: {"element": "O", "coords": np.array([2.2314, 0.0528, 0.0])},
                2: {"element": "O", "coords": np.array([2.0, -2.4021, 0.0])},
                3: {"element": "O", "coords": np.array([2.0, 2.4021, 0.0])},
                4: {"element": "N", "coords": np.array([6.1607, -0.9511, 0.0])},
                5: {"element": "C", "coords": np.array([3.6897, -0.4755, 0.0])},
                6: {"element": "C", "coords": np.array([4.5133, -0.9511, 0.0])},
                7: {"element": "C", "coords": np.array([5.337, -0.4755, 0.0])},
                8: {"element": "C", "coords": np.array([2.866, -0.9511, 0.0])},
                9: {"element": "C", "coords": np.array([4.2392, 0.2219, 0.0])},
                10: {"element": "C", "coords": np.array([3.6897, 0.4755, 0.0])},
                11: {"element": "C", "coords": np.array([5.337, 0.4755, 0.0])},
                12: {"element": "C", "coords": np.array([5.5918, 0.2219, 0.0])},
                13: {"element": "C", "coords": np.array([4.5133, 0.9511, 0.0])},
                14: {"element": "C", "coords": np.array([2.866, -1.9022, 0.0])},
                15: {"element": "C", "coords": np.array([4.5133, -1.9022, 0.0])},
                16: {"element": "C", "coords": np.array([2.866, 0.9511, 0.0])},
                17: {"element": "C", "coords": np.array([3.6897, -2.3777, 0.0])},
                18: {"element": "C", "coords": np.array([6.8418, -1.6832, 0.0])},
                19: {"element": "C", "coords": np.array([4.5133, 1.9022, 0.0])},
                20: {"element": "C", "coords": np.array([2.866, 1.9022, 0.0])},
                21: {"element": "C", "coords": np.array([3.6897, 2.3777, 0.0])},
                22: {"element": "H", "coords": np.array([5.0597, -1.6022, 0.0])},
                23: {"element": "H", "coords": np.array([5.6284, -1.274, 0.0])},
                24: {"element": "H", "coords": np.array([2.0496, -1.1875, 0.0])},
                25: {"element": "H", "coords": np.array([4.376, 0.8266, 0.0])},
                26: {"element": "H", "coords": np.array([3.6795, 0.4887, 0.0])},
                27: {"element": "H", "coords": np.array([5.9476, 0.3679, 0.0])},
                28: {"element": "H", "coords": np.array([5.549, 1.0581, 0.0])},
                29: {"element": "H", "coords": np.array([6.184, 0.4057, 0.0])},
                30: {"element": "H", "coords": np.array([5.4989, 0.8349, 0.0])},
                31: {"element": "H", "coords": np.array([2.866, -2.5222, 0.0])},
                32: {"element": "H", "coords": np.array([5.0503, -2.2122, 0.0])},
                33: {"element": "H", "coords": np.array([3.6897, -2.9977, 0.0])},
                34: {"element": "H", "coords": np.array([6.3879, -2.1055, 0.0])},
                35: {"element": "H", "coords": np.array([7.2641, -2.1371, 0.0])},
                36: {"element": "H", "coords": np.array([7.2957, -1.2609, 0.0])},
                37: {"element": "H", "coords": np.array([5.0503, 2.2122, 0.0])},
                38: {"element": "H", "coords": np.array([3.6897, 2.9977, 0.0])},
                39: {"element": "H", "coords": np.array([2.0, -3.0222, 0.0])},
                40: {"element": "H", "coords": np.array([2.0, 3.0222, 0.0])},
            },
            {
                0: {"from_atom_index": 1, "to_atom_index": 8, "bond_type": 1},
                1: {"from_atom_index": 1, "to_atom_index": 16, "bond_type": 1},
                2: {"from_atom_index": 2, "to_atom_index": 14, "bond_type": 1},
                3: {"from_atom_index": 2, "to_atom_index": 39, "bond_type": 1},
                4: {"from_atom_index": 3, "to_atom_index": 20, "bond_type": 1},
                5: {"from_atom_index": 3, "to_atom_index": 40, "bond_type": 1},
                6: {"from_atom_index": 4, "to_atom_index": 7, "bond_type": 1},
                7: {"from_atom_index": 4, "to_atom_index": 12, "bond_type": 1},
                8: {"from_atom_index": 4, "to_atom_index": 18, "bond_type": 1},
                9: {"from_atom_index": 5, "to_atom_index": 6, "bond_type": 1},
                10: {"from_atom_index": 5, "to_atom_index": 8, "bond_type": 1},
                11: {"from_atom_index": 5, "to_atom_index": 9, "bond_type": 1},
                12: {"from_atom_index": 5, "to_atom_index": 10, "bond_type": 1},
                13: {"from_atom_index": 6, "to_atom_index": 7, "bond_type": 1},
                14: {"from_atom_index": 6, "to_atom_index": 15, "bond_type": 1},
                15: {"from_atom_index": 6, "to_atom_index": 22, "bond_type": 1},
                16: {"from_atom_index": 7, "to_atom_index": 11, "bond_type": 1},
                17: {"from_atom_index": 7, "to_atom_index": 23, "bond_type": 1},
                18: {"from_atom_index": 8, "to_atom_index": 14, "bond_type": 1},
                19: {"from_atom_index": 8, "to_atom_index": 24, "bond_type": 1},
                20: {"from_atom_index": 9, "to_atom_index": 12, "bond_type": 1},
                21: {"from_atom_index": 9, "to_atom_index": 25, "bond_type": 1},
                22: {"from_atom_index": 9, "to_atom_index": 26, "bond_type": 1},
                23: {"from_atom_index": 10, "to_atom_index": 13, "bond_type": 2},
                24: {"from_atom_index": 10, "to_atom_index": 16, "bond_type": 1},
                25: {"from_atom_index": 11, "to_atom_index": 13, "bond_type": 1},
                26: {"from_atom_index": 11, "to_atom_index": 27, "bond_type": 1},
                27: {"from_atom_index": 11, "to_atom_index": 28, "bond_type": 1},
                28: {"from_atom_index": 12, "to_atom_index": 29, "bond_type": 1},
                29: {"from_atom_index": 12, "to_atom_index": 30, "bond_type": 1},
                30: {"from_atom_index": 13, "to_atom_index": 19, "bond_type": 1},
                31: {"from_atom_index": 14, "to_atom_index": 17, "bond_type": 1},
                32: {"from_atom_index": 14, "to_atom_index": 31, "bond_type": 1},
                33: {"from_atom_index": 15, "to_atom_index": 17, "bond_type": 2},
                34: {"from_atom_index": 15, "to_atom_index": 32, "bond_type": 1},
                35: {"from_atom_index": 16, "to_atom_index": 20, "bond_type": 2},
                36: {"from_atom_index": 17, "to_atom_index": 33, "bond_type": 1},
                37: {"from_atom_index": 18, "to_atom_index": 34, "bond_type": 1},
                38: {"from_atom_index": 18, "to_atom_index": 35, "bond_type": 1},
                39: {"from_atom_index": 18, "to_atom_index": 36, "bond_type": 1},
                40: {"from_atom_index": 19, "to_atom_index": 21, "bond_type": 2},
                41: {"from_atom_index": 19, "to_atom_index": 37, "bond_type": 1},
                42: {"from_atom_index": 20, "to_atom_index": 21, "bond_type": 1},
                43: {"from_atom_index": 21, "to_atom_index": 38, "bond_type": 1},
            },
        )

    @pytest.fixture
    def morphine_3d_molecule_data(self):
        return (
            {
                1: {"element": "O", "coords": np.array([-1.993, -0.474, 1.2005])},
                2: {"element": "O", "coords": np.array([-2.7826, -2.5168, -0.2218])},
                3: {"element": "O", "coords": np.array([-3.622, 1.8421, 0.5579])},
                4: {"element": "N", "coords": np.array([3.1777, -0.0101, 0.4474])},
                5: {"element": "C", "coords": np.array([0.3699, -0.7149, 0.6616])},
                6: {"element": "C", "coords": np.array([1.2913, -1.3046, -0.417])},
                7: {"element": "C", "coords": np.array([2.3441, -0.2023, -0.764])},
                8: {"element": "C", "coords": np.array([-0.9377, -1.475, 0.9848])},
                9: {"element": "C", "coords": np.array([1.1988, -0.3907, 1.9201])},
                10: {"element": "C", "coords": np.array([-0.2516, 0.5302, 0.1205])},
                11: {"element": "C", "coords": np.array([1.6887, 1.1052, -1.3279])},
                12: {"element": "C", "coords": np.array([2.4315, 0.4754, 1.6126])},
                13: {"element": "C", "coords": np.array([0.3384, 1.4306, -0.748])},
                14: {"element": "C", "coords": np.array([-1.3631, -2.5067, -0.0924])},
                15: {"element": "C", "coords": np.array([0.5066, -1.8183, -1.5971])},
                16: {"element": "C", "coords": np.array([-1.5672, 0.6306, 0.5136])},
                17: {"element": "C", "coords": np.array([-0.7155, -2.3492, -1.4425])},
                18: {"element": "C", "coords": np.array([4.3733, 0.7916, 0.2084])},
                19: {"element": "C", "coords": np.array([-0.4184, 2.5415, -1.1246])},
                20: {"element": "C", "coords": np.array([-2.331, 1.7217, 0.162])},
                21: {"element": "C", "coords": np.array([-1.7382, 2.6936, -0.6541])},
                22: {"element": "H", "coords": np.array([1.8278, -2.1759, -0.0118])},
                23: {"element": "H", "coords": np.array([3.0029, -0.6035, -1.5465])},
                24: {"element": "H", "coords": np.array([-0.8451, -2.0128, 1.9373])},
                25: {"element": "H", "coords": np.array([1.5366, -1.3335, 2.3712])},
                26: {"element": "H", "coords": np.array([0.5899, 0.1174, 2.679])},
                27: {"element": "H", "coords": np.array([1.5474, 0.9596, -2.4075])},
                28: {"element": "H", "coords": np.array([2.353, 1.968, -1.2194])},
                29: {"element": "H", "coords": np.array([2.1271, 1.5205, 1.476])},
                30: {"element": "H", "coords": np.array([3.0801, 0.4584, 2.4975])},
                31: {"element": "H", "coords": np.array([-1.0772, -3.5067, 0.2593])},
                32: {"element": "H", "coords": np.array([0.9601, -1.7947, -2.5831])},
                33: {"element": "H", "coords": np.array([-1.23, -2.7505, -2.3109])},
                34: {"element": "H", "coords": np.array([4.15, 1.8479, 0.0287])},
                35: {"element": "H", "coords": np.array([4.938, 0.4055, -0.6472])},
                36: {"element": "H", "coords": np.array([5.0444, 0.7352, 1.073])},
                37: {"element": "H", "coords": np.array([-0.0062, 3.2824, -1.8043])},
                38: {"element": "H", "coords": np.array([-2.3121, 3.5638, -0.9645])},
                39: {"element": "H", "coords": np.array([-3.1557, -2.6446, 0.6672])},
                40: {"element": "H", "coords": np.array([-3.8483, 1.0686, 1.1031])},
            },
            {
                0: {"from_atom_index": 1, "to_atom_index": 8, "bond_type": 1},
                1: {"from_atom_index": 1, "to_atom_index": 16, "bond_type": 1},
                2: {"from_atom_index": 2, "to_atom_index": 14, "bond_type": 1},
                3: {"from_atom_index": 2, "to_atom_index": 39, "bond_type": 1},
                4: {"from_atom_index": 3, "to_atom_index": 20, "bond_type": 1},
                5: {"from_atom_index": 3, "to_atom_index": 40, "bond_type": 1},
                6: {"from_atom_index": 4, "to_atom_index": 7, "bond_type": 1},
                7: {"from_atom_index": 4, "to_atom_index": 12, "bond_type": 1},
                8: {"from_atom_index": 4, "to_atom_index": 18, "bond_type": 1},
                9: {"from_atom_index": 5, "to_atom_index": 6, "bond_type": 1},
                10: {"from_atom_index": 5, "to_atom_index": 8, "bond_type": 1},
                11: {"from_atom_index": 5, "to_atom_index": 9, "bond_type": 1},
                12: {"from_atom_index": 5, "to_atom_index": 10, "bond_type": 1},
                13: {"from_atom_index": 6, "to_atom_index": 7, "bond_type": 1},
                14: {"from_atom_index": 6, "to_atom_index": 15, "bond_type": 1},
                15: {"from_atom_index": 6, "to_atom_index": 22, "bond_type": 1},
                16: {"from_atom_index": 7, "to_atom_index": 11, "bond_type": 1},
                17: {"from_atom_index": 7, "to_atom_index": 23, "bond_type": 1},
                18: {"from_atom_index": 8, "to_atom_index": 14, "bond_type": 1},
                19: {"from_atom_index": 8, "to_atom_index": 24, "bond_type": 1},
                20: {"from_atom_index": 9, "to_atom_index": 12, "bond_type": 1},
                21: {"from_atom_index": 9, "to_atom_index": 25, "bond_type": 1},
                22: {"from_atom_index": 9, "to_atom_index": 26, "bond_type": 1},
                23: {"from_atom_index": 10, "to_atom_index": 13, "bond_type": 2},
                24: {"from_atom_index": 10, "to_atom_index": 16, "bond_type": 1},
                25: {"from_atom_index": 11, "to_atom_index": 13, "bond_type": 1},
                26: {"from_atom_index": 11, "to_atom_index": 27, "bond_type": 1},
                27: {"from_atom_index": 11, "to_atom_index": 28, "bond_type": 1},
                28: {"from_atom_index": 12, "to_atom_index": 29, "bond_type": 1},
                29: {"from_atom_index": 12, "to_atom_index": 30, "bond_type": 1},
                30: {"from_atom_index": 13, "to_atom_index": 19, "bond_type": 1},
                31: {"from_atom_index": 14, "to_atom_index": 17, "bond_type": 1},
                32: {"from_atom_index": 14, "to_atom_index": 31, "bond_type": 1},
                33: {"from_atom_index": 15, "to_atom_index": 17, "bond_type": 2},
                34: {"from_atom_index": 15, "to_atom_index": 32, "bond_type": 1},
                35: {"from_atom_index": 16, "to_atom_index": 20, "bond_type": 2},
                36: {"from_atom_index": 17, "to_atom_index": 33, "bond_type": 1},
                37: {"from_atom_index": 18, "to_atom_index": 34, "bond_type": 1},
                38: {"from_atom_index": 18, "to_atom_index": 35, "bond_type": 1},
                39: {"from_atom_index": 18, "to_atom_index": 36, "bond_type": 1},
                40: {"from_atom_index": 19, "to_atom_index": 21, "bond_type": 2},
                41: {"from_atom_index": 19, "to_atom_index": 37, "bond_type": 1},
                42: {"from_atom_index": 20, "to_atom_index": 21, "bond_type": 1},
                43: {"from_atom_index": 21, "to_atom_index": 38, "bond_type": 1},
            },
        )

    @pytest.fixture
    def heme_2d_molecule_data(self):
        return (
            {
                1: {"element": "Fe", "coords": np.array([6.7437, 0.7222, 0.0])},
                2: {"element": "O", "coords": np.array([7.6407, -5.2892, 0.0])},
                3: {"element": "O", "coords": np.array([13.2337, 0.2017, 0.0])},
                4: {"element": "O", "coords": np.array([9.0357, -4.2626, 0.0])},
                5: {"element": "O", "coords": np.array([12.191, -1.1813, 0.0])},
                6: {"element": "N", "coords": np.array([6.7568, -0.2777, 0.0])},
                7: {"element": "N", "coords": np.array([8.2586, 1.0918, 0.0])},
                8: {"element": "N", "coords": np.array([5.2534, 1.0918, 0.0])},
                9: {"element": "N", "coords": np.array([6.7233, 2.4613, 0.0])},
                10: {"element": "C", "coords": np.array([7.2574, -1.8464, 0.0])},
                11: {"element": "C", "coords": np.array([9.7955, 0.6247, 0.0])},
                12: {"element": "C", "coords": np.array([7.5588, -0.8787, 0.0])},
                13: {"element": "C", "coords": np.array([8.8596, 0.3568, 0.0])},
                14: {"element": "C", "coords": np.array([6.2562, -1.8464, 0.0])},
                15: {"element": "C", "coords": np.array([9.7955, 1.6259, 0.0])},
                16: {"element": "C", "coords": np.array([7.8502, -2.6518, 0.0])},
                17: {"element": "C", "coords": np.array([10.594, 0.0227, 0.0])},
                18: {"element": "C", "coords": np.array([5.9549, -0.9122, 0.0])},
                19: {"element": "C", "coords": np.array([8.8261, 1.8938, 0.0])},
                20: {"element": "C", "coords": np.array([8.5599, -0.6109, 0.0])},
                21: {"element": "C", "coords": np.array([4.9872, -0.6109, 0.0])},
                22: {"element": "C", "coords": np.array([8.5265, 2.828, 0.0])},
                23: {"element": "C", "coords": np.array([7.4491, -3.5678, 0.0])},
                24: {"element": "C", "coords": np.array([11.5146, 0.4132, 0.0])},
                25: {"element": "C", "coords": np.array([4.6858, 0.3233, 0.0])},
                26: {"element": "C", "coords": np.array([7.5588, 3.1293, 0.0])},
                27: {"element": "C", "coords": np.array([5.5855, -2.5881, 0.0])},
                28: {"element": "C", "coords": np.array([10.5912, 2.2315, 0.0])},
                29: {"element": "C", "coords": np.array([3.7182, 0.5912, 0.0])},
                30: {"element": "C", "coords": np.array([7.2239, 4.0635, 0.0])},
                31: {"element": "C", "coords": np.array([5.9214, 3.0958, 0.0])},
                32: {"element": "C", "coords": np.array([6.2228, 4.0635, 0.0])},
                33: {"element": "C", "coords": np.array([4.6858, 1.8603, 0.0])},
                34: {"element": "C", "coords": np.array([3.7182, 1.5924, 0.0])},
                35: {"element": "C", "coords": np.array([4.9537, 2.828, 0.0])},
                36: {"element": "C", "coords": np.array([2.8521, 0.0912, 0.0])},
                37: {"element": "C", "coords": np.array([5.63, 4.8689, 0.0])},
                38: {"element": "C", "coords": np.array([8.0418, -4.3732, 0.0])},
                39: {"element": "C", "coords": np.array([12.3131, -0.1888, 0.0])},
                40: {"element": "C", "coords": np.array([7.7995, 4.8812, 0.0])},
                41: {"element": "C", "coords": np.array([2.9223, 2.1979, 0.0])},
                42: {"element": "C", "coords": np.array([7.3791, 5.7886, 0.0])},
                43: {"element": "C", "coords": np.array([2.0, 1.8114, 0.0])},
                44: {"element": "H", "coords": np.array([8.3663, -2.9953, 0.0])},
                45: {"element": "H", "coords": np.array([8.2781, -2.2032, 0.0])},
                46: {"element": "H", "coords": np.array([10.1405, -0.4, 0.0])},
                47: {"element": "H", "coords": np.array([10.9316, -0.4974, 0.0])},
                48: {"element": "H", "coords": np.array([8.9897, -1.0577, 0.0])},
                49: {"element": "H", "coords": np.array([4.551, -1.0515, 0.0])},
                50: {"element": "H", "coords": np.array([8.963, 3.2682, 0.0])},
                51: {"element": "H", "coords": np.array([6.9329, -3.2243, 0.0])},
                52: {"element": "H", "coords": np.array([7.0211, -4.0165, 0.0])},
                53: {"element": "H", "coords": np.array([11.9681, 0.8359, 0.0])},
                54: {"element": "H", "coords": np.array([11.177, 0.9333, 0.0])},
                55: {"element": "H", "coords": np.array([5.1257, -2.1723, 0.0])},
                56: {"element": "H", "coords": np.array([5.1697, -3.048, 0.0])},
                57: {"element": "H", "coords": np.array([6.0454, -3.004, 0.0])},
                58: {"element": "H", "coords": np.array([10.9667, 1.7382, 0.0])},
                59: {"element": "H", "coords": np.array([11.0846, 2.607, 0.0])},
                60: {"element": "H", "coords": np.array([10.2157, 2.7249, 0.0])},
                61: {"element": "H", "coords": np.array([4.5153, 3.2664, 0.0])},
                62: {"element": "H", "coords": np.array([2.5421, 0.6281, 0.0])},
                63: {"element": "H", "coords": np.array([2.3152, -0.2188, 0.0])},
                64: {"element": "H", "coords": np.array([3.1622, -0.4457, 0.0])},
                65: {"element": "H", "coords": np.array([6.1293, 5.2364, 0.0])},
                66: {"element": "H", "coords": np.array([5.2625, 5.3682, 0.0])},
                67: {"element": "H", "coords": np.array([5.1307, 4.5014, 0.0])},
                68: {"element": "H", "coords": np.array([8.417, 4.8257, 0.0])},
                69: {"element": "H", "coords": np.array([3.0007, 2.8129, 0.0])},
                70: {"element": "H", "coords": np.array([7.736, 6.2956, 0.0])},
                71: {"element": "H", "coords": np.array([6.7616, 5.8441, 0.0])},
                72: {"element": "H", "coords": np.array([1.5066, 2.1868, 0.0])},
                73: {"element": "H", "coords": np.array([1.9216, 1.1963, 0.0])},
                74: {"element": "H", "coords": np.array([8.0082, -5.7886, 0.0])},
                75: {"element": "H", "coords": np.array([13.7288, -0.1715, 0.0])},
            },
            {
                0: {"from_atom_index": 2, "to_atom_index": 38, "bond_type": 1},
                1: {"from_atom_index": 2, "to_atom_index": 74, "bond_type": 1},
                2: {"from_atom_index": 3, "to_atom_index": 39, "bond_type": 1},
                3: {"from_atom_index": 3, "to_atom_index": 75, "bond_type": 1},
                4: {"from_atom_index": 4, "to_atom_index": 38, "bond_type": 2},
                5: {"from_atom_index": 5, "to_atom_index": 39, "bond_type": 2},
                6: {"from_atom_index": 6, "to_atom_index": 12, "bond_type": 1},
                7: {"from_atom_index": 6, "to_atom_index": 18, "bond_type": 1},
                8: {"from_atom_index": 7, "to_atom_index": 13, "bond_type": 1},
                9: {"from_atom_index": 7, "to_atom_index": 19, "bond_type": 1},
                10: {"from_atom_index": 8, "to_atom_index": 25, "bond_type": 2},
                11: {"from_atom_index": 8, "to_atom_index": 33, "bond_type": 1},
                12: {"from_atom_index": 9, "to_atom_index": 26, "bond_type": 1},
                13: {"from_atom_index": 9, "to_atom_index": 31, "bond_type": 2},
                14: {"from_atom_index": 10, "to_atom_index": 12, "bond_type": 1},
                15: {"from_atom_index": 10, "to_atom_index": 14, "bond_type": 2},
                16: {"from_atom_index": 10, "to_atom_index": 16, "bond_type": 1},
                17: {"from_atom_index": 11, "to_atom_index": 13, "bond_type": 2},
                18: {"from_atom_index": 11, "to_atom_index": 15, "bond_type": 1},
                19: {"from_atom_index": 11, "to_atom_index": 17, "bond_type": 1},
                20: {"from_atom_index": 12, "to_atom_index": 20, "bond_type": 2},
                21: {"from_atom_index": 13, "to_atom_index": 20, "bond_type": 1},
                22: {"from_atom_index": 14, "to_atom_index": 18, "bond_type": 1},
                23: {"from_atom_index": 14, "to_atom_index": 27, "bond_type": 1},
                24: {"from_atom_index": 15, "to_atom_index": 19, "bond_type": 2},
                25: {"from_atom_index": 15, "to_atom_index": 28, "bond_type": 1},
                26: {"from_atom_index": 16, "to_atom_index": 23, "bond_type": 1},
                27: {"from_atom_index": 16, "to_atom_index": 44, "bond_type": 1},
                28: {"from_atom_index": 16, "to_atom_index": 45, "bond_type": 1},
                29: {"from_atom_index": 17, "to_atom_index": 24, "bond_type": 1},
                30: {"from_atom_index": 17, "to_atom_index": 46, "bond_type": 1},
                31: {"from_atom_index": 17, "to_atom_index": 47, "bond_type": 1},
                32: {"from_atom_index": 18, "to_atom_index": 21, "bond_type": 2},
                33: {"from_atom_index": 19, "to_atom_index": 22, "bond_type": 1},
                34: {"from_atom_index": 20, "to_atom_index": 48, "bond_type": 1},
                35: {"from_atom_index": 21, "to_atom_index": 25, "bond_type": 1},
                36: {"from_atom_index": 21, "to_atom_index": 49, "bond_type": 1},
                37: {"from_atom_index": 22, "to_atom_index": 26, "bond_type": 2},
                38: {"from_atom_index": 22, "to_atom_index": 50, "bond_type": 1},
                39: {"from_atom_index": 23, "to_atom_index": 38, "bond_type": 1},
                40: {"from_atom_index": 23, "to_atom_index": 51, "bond_type": 1},
                41: {"from_atom_index": 23, "to_atom_index": 52, "bond_type": 1},
                42: {"from_atom_index": 24, "to_atom_index": 39, "bond_type": 1},
                43: {"from_atom_index": 24, "to_atom_index": 53, "bond_type": 1},
                44: {"from_atom_index": 24, "to_atom_index": 54, "bond_type": 1},
                45: {"from_atom_index": 25, "to_atom_index": 29, "bond_type": 1},
                46: {"from_atom_index": 26, "to_atom_index": 30, "bond_type": 1},
                47: {"from_atom_index": 27, "to_atom_index": 55, "bond_type": 1},
                48: {"from_atom_index": 27, "to_atom_index": 56, "bond_type": 1},
                49: {"from_atom_index": 27, "to_atom_index": 57, "bond_type": 1},
                50: {"from_atom_index": 28, "to_atom_index": 58, "bond_type": 1},
                51: {"from_atom_index": 28, "to_atom_index": 59, "bond_type": 1},
                52: {"from_atom_index": 28, "to_atom_index": 60, "bond_type": 1},
                53: {"from_atom_index": 29, "to_atom_index": 34, "bond_type": 2},
                54: {"from_atom_index": 29, "to_atom_index": 36, "bond_type": 1},
                55: {"from_atom_index": 30, "to_atom_index": 32, "bond_type": 2},
                56: {"from_atom_index": 30, "to_atom_index": 40, "bond_type": 1},
                57: {"from_atom_index": 31, "to_atom_index": 32, "bond_type": 1},
                58: {"from_atom_index": 31, "to_atom_index": 35, "bond_type": 1},
                59: {"from_atom_index": 32, "to_atom_index": 37, "bond_type": 1},
                60: {"from_atom_index": 33, "to_atom_index": 34, "bond_type": 1},
                61: {"from_atom_index": 33, "to_atom_index": 35, "bond_type": 2},
                62: {"from_atom_index": 34, "to_atom_index": 41, "bond_type": 1},
                63: {"from_atom_index": 35, "to_atom_index": 61, "bond_type": 1},
                64: {"from_atom_index": 36, "to_atom_index": 62, "bond_type": 1},
                65: {"from_atom_index": 36, "to_atom_index": 63, "bond_type": 1},
                66: {"from_atom_index": 36, "to_atom_index": 64, "bond_type": 1},
                67: {"from_atom_index": 37, "to_atom_index": 65, "bond_type": 1},
                68: {"from_atom_index": 37, "to_atom_index": 66, "bond_type": 1},
                69: {"from_atom_index": 37, "to_atom_index": 67, "bond_type": 1},
                70: {"from_atom_index": 40, "to_atom_index": 42, "bond_type": 2},
                71: {"from_atom_index": 40, "to_atom_index": 68, "bond_type": 1},
                72: {"from_atom_index": 41, "to_atom_index": 43, "bond_type": 2},
                73: {"from_atom_index": 41, "to_atom_index": 69, "bond_type": 1},
                74: {"from_atom_index": 42, "to_atom_index": 70, "bond_type": 1},
                75: {"from_atom_index": 42, "to_atom_index": 71, "bond_type": 1},
                76: {"from_atom_index": 43, "to_atom_index": 72, "bond_type": 1},
                77: {"from_atom_index": 43, "to_atom_index": 73, "bond_type": 1},
            },
        )

    @pytest.fixture
    def heme_3d_molecule_data(self):
        return (
            {
                1: {"element": "O", "coords": np.array([7.1385, 2.705, -0.6711])},
                2: {"element": "O", "coords": np.array([5.7615, -3.2503, -2.9408])},
                3: {"element": "O", "coords": np.array([6.7154, 2.1599, 1.493])},
                4: {"element": "O", "coords": np.array([6.1372, -3.4886, -0.7132])},
                5: {"element": "N", "coords": np.array([-2.525, 1.9272, 0.2862])},
                6: {"element": "N", "coords": np.array([-2.6939, -1.118, 0.2758])},
                7: {"element": "N", "coords": np.array([0.4051, 1.517, 0.2379])},
                8: {"element": "N", "coords": np.array([0.1811, -1.3404, 0.4974])},
                9: {"element": "C", "coords": np.array([2.507, 2.3377, 0.8711])},
                10: {"element": "C", "coords": np.array([2.0591, -2.6167, 0.1996])},
                11: {"element": "C", "coords": np.array([1.6482, 1.2058, 0.4657])},
                12: {"element": "C", "coords": np.array([1.6304, 3.3517, 0.8618])},
                13: {"element": "C", "coords": np.array([1.5429, -1.2639, 0.3342])},
                14: {"element": "C", "coords": np.array([1.0549, -3.502, 0.2769])},
                15: {"element": "C", "coords": np.array([0.3143, 2.872, 0.4652])},
                16: {"element": "C", "coords": np.array([-0.1068, -2.6087, 0.4631])},
                17: {"element": "C", "coords": np.array([-2.0505, 3.1577, -0.111])},
                18: {"element": "C", "coords": np.array([-3.9963, -0.6924, 0.2747])},
                19: {"element": "C", "coords": np.array([-2.5688, -2.4592, 0.54])},
                20: {"element": "C", "coords": np.array([-3.7828, 1.7074, -0.2302])},
                21: {"element": "C", "coords": np.array([3.9475, 2.2748, 1.2062])},
                22: {"element": "C", "coords": np.array([3.5095, -2.9072, 0.0057])},
                23: {"element": "C", "coords": np.array([2.2658, -0.1348, 0.3202])},
                24: {"element": "C", "coords": np.array([-3.0486, 3.753, -0.8571])},
                25: {"element": "C", "coords": np.array([-4.7892, -1.9053, 0.5602])},
                26: {"element": "C", "coords": np.array([-4.1304, 2.8451, -0.9341])},
                27: {"element": "C", "coords": np.array([-3.9471, -2.9601, 0.7181])},
                28: {"element": "C", "coords": np.array([-0.7823, 3.6329, 0.3107])},
                29: {"element": "C", "coords": np.array([-1.4551, -3.2035, 0.6248])},
                30: {"element": "C", "coords": np.array([-4.5176, 0.5263, 0.0526])},
                31: {"element": "C", "coords": np.array([1.9005, 4.7807, 1.1965])},
                32: {
                    "element": "C",
                    "coords": np.array([4.8520e00, 2.5394e00, 3.3000e-03]),
                },
                33: {"element": "C", "coords": np.array([3.9112, -2.9257, -1.4638])},
                34: {"element": "C", "coords": np.array([1.0259, -4.9791, 0.1919])},
                35: {"element": "C", "coords": np.array([-2.9926, 5.1012, -1.4661])},
                36: {"element": "C", "coords": np.array([-6.2814, -1.8735, 0.6439])},
                37: {"element": "C", "coords": np.array([-5.36, 3.0491, -1.6044])},
                38: {"element": "C", "coords": np.array([-4.3596, -4.3097, 1.0073])},
                39: {"element": "C", "coords": np.array([6.3128, 2.4348, 0.3698])},
                40: {"element": "C", "coords": np.array([5.3729, -3.2588, -1.6419])},
                41: {"element": "C", "coords": np.array([-6.1715, 2.1311, -2.1847])},
                42: {"element": "C", "coords": np.array([-4.6339, -5.2115, 0.0645])},
                43: {"element": "H", "coords": np.array([4.1938, 1.3129, 1.6711])},
                44: {"element": "H", "coords": np.array([4.1687, 3.0159, 1.9856])},
                45: {"element": "H", "coords": np.array([3.7406, -3.8863, 0.4471])},
                46: {"element": "H", "coords": np.array([4.1341, -2.2066, 0.5729])},
                47: {"element": "H", "coords": np.array([3.3403, -0.1671, 0.1855])},
                48: {"element": "H", "coords": np.array([-0.7083, 4.7057, 0.4708])},
                49: {"element": "H", "coords": np.array([-1.5138, -4.2667, 0.8304])},
                50: {"element": "H", "coords": np.array([-2.0287, 1.2921, 0.8961])},
                51: {"element": "H", "coords": np.array([-1.9035, -0.5315, 0.0596])},
                52: {"element": "H", "coords": np.array([-5.5979, 0.6383, 0.092])},
                53: {"element": "H", "coords": np.array([1.2897, 5.1008, 2.0471])},
                54: {"element": "H", "coords": np.array([2.9482, 4.9486, 1.4639])},
                55: {"element": "H", "coords": np.array([1.6775, 5.4274, 0.3414])},
                56: {"element": "H", "coords": np.array([4.6712, 3.5474, -0.3875])},
                57: {"element": "H", "coords": np.array([4.6518, 1.8113, -0.7907])},
                58: {"element": "H", "coords": np.array([3.3272, -3.6772, -2.0076])},
                59: {"element": "H", "coords": np.array([3.7327, -1.9441, -1.9173])},
                60: {"element": "H", "coords": np.array([2.0137, -5.3942, -0.029])},
                61: {"element": "H", "coords": np.array([0.3499, -5.3061, -0.6044])},
                62: {"element": "H", "coords": np.array([0.6873, -5.4128, 1.1379])},
                63: {"element": "H", "coords": np.array([-3.5447, 5.8188, -0.8503])},
                64: {"element": "H", "coords": np.array([-3.4318, 5.0997, -2.4692])},
                65: {"element": "H", "coords": np.array([-1.9644, 5.4627, -1.568])},
                66: {"element": "H", "coords": np.array([-6.7151, -1.5506, -0.3082])},
                67: {"element": "H", "coords": np.array([-6.61, -1.1876, 1.4317])},
                68: {"element": "H", "coords": np.array([-6.7014, -2.8571, 0.8758])},
                69: {"element": "H", "coords": np.array([-5.693, 4.0826, -1.6921])},
                70: {"element": "H", "coords": np.array([-4.4411, -4.5822, 2.0553])},
                71: {"element": "H", "coords": np.array([-7.0854, 2.4544, -2.6733])},
                72: {"element": "H", "coords": np.array([-5.9398, 1.0737, -2.2183])},
                73: {"element": "H", "coords": np.array([-4.9394, -6.2155, 0.3391])},
                74: {"element": "H", "coords": np.array([-4.5621, -4.9765, -0.9923])},
                75: {"element": "H", "coords": np.array([8.0834, 2.6451, -0.4143])},
                76: {"element": "H", "coords": np.array([6.7157, -3.456, -3.0389])},
            },
            {
                0: {"from_atom_index": 1, "to_atom_index": 39, "bond_type": 1},
                1: {"from_atom_index": 1, "to_atom_index": 75, "bond_type": 1},
                2: {"from_atom_index": 2, "to_atom_index": 40, "bond_type": 1},
                3: {"from_atom_index": 2, "to_atom_index": 76, "bond_type": 1},
                4: {"from_atom_index": 3, "to_atom_index": 39, "bond_type": 2},
                5: {"from_atom_index": 4, "to_atom_index": 40, "bond_type": 2},
                6: {"from_atom_index": 5, "to_atom_index": 17, "bond_type": 1},
                7: {"from_atom_index": 5, "to_atom_index": 20, "bond_type": 1},
                8: {"from_atom_index": 5, "to_atom_index": 50, "bond_type": 1},
                9: {"from_atom_index": 6, "to_atom_index": 18, "bond_type": 1},
                10: {"from_atom_index": 6, "to_atom_index": 19, "bond_type": 1},
                11: {"from_atom_index": 6, "to_atom_index": 51, "bond_type": 1},
                12: {"from_atom_index": 7, "to_atom_index": 11, "bond_type": 2},
                13: {"from_atom_index": 7, "to_atom_index": 15, "bond_type": 1},
                14: {"from_atom_index": 8, "to_atom_index": 13, "bond_type": 1},
                15: {"from_atom_index": 8, "to_atom_index": 16, "bond_type": 2},
                16: {"from_atom_index": 9, "to_atom_index": 11, "bond_type": 1},
                17: {"from_atom_index": 9, "to_atom_index": 12, "bond_type": 2},
                18: {"from_atom_index": 9, "to_atom_index": 21, "bond_type": 1},
                19: {"from_atom_index": 10, "to_atom_index": 13, "bond_type": 1},
                20: {"from_atom_index": 10, "to_atom_index": 14, "bond_type": 2},
                21: {"from_atom_index": 10, "to_atom_index": 22, "bond_type": 1},
                22: {"from_atom_index": 11, "to_atom_index": 23, "bond_type": 1},
                23: {"from_atom_index": 12, "to_atom_index": 15, "bond_type": 1},
                24: {"from_atom_index": 12, "to_atom_index": 31, "bond_type": 1},
                25: {"from_atom_index": 13, "to_atom_index": 23, "bond_type": 2},
                26: {"from_atom_index": 14, "to_atom_index": 16, "bond_type": 1},
                27: {"from_atom_index": 14, "to_atom_index": 34, "bond_type": 1},
                28: {"from_atom_index": 15, "to_atom_index": 28, "bond_type": 2},
                29: {"from_atom_index": 16, "to_atom_index": 29, "bond_type": 1},
                30: {"from_atom_index": 17, "to_atom_index": 24, "bond_type": 2},
                31: {"from_atom_index": 17, "to_atom_index": 28, "bond_type": 1},
                32: {"from_atom_index": 18, "to_atom_index": 25, "bond_type": 1},
                33: {"from_atom_index": 18, "to_atom_index": 30, "bond_type": 2},
                34: {"from_atom_index": 19, "to_atom_index": 27, "bond_type": 1},
                35: {"from_atom_index": 19, "to_atom_index": 29, "bond_type": 2},
                36: {"from_atom_index": 20, "to_atom_index": 26, "bond_type": 2},
                37: {"from_atom_index": 20, "to_atom_index": 30, "bond_type": 1},
                38: {"from_atom_index": 21, "to_atom_index": 32, "bond_type": 1},
                39: {"from_atom_index": 21, "to_atom_index": 43, "bond_type": 1},
                40: {"from_atom_index": 21, "to_atom_index": 44, "bond_type": 1},
                41: {"from_atom_index": 22, "to_atom_index": 33, "bond_type": 1},
                42: {"from_atom_index": 22, "to_atom_index": 45, "bond_type": 1},
                43: {"from_atom_index": 22, "to_atom_index": 46, "bond_type": 1},
                44: {"from_atom_index": 23, "to_atom_index": 47, "bond_type": 1},
                45: {"from_atom_index": 24, "to_atom_index": 26, "bond_type": 1},
                46: {"from_atom_index": 24, "to_atom_index": 35, "bond_type": 1},
                47: {"from_atom_index": 25, "to_atom_index": 27, "bond_type": 2},
                48: {"from_atom_index": 25, "to_atom_index": 36, "bond_type": 1},
                49: {"from_atom_index": 26, "to_atom_index": 37, "bond_type": 1},
                50: {"from_atom_index": 27, "to_atom_index": 38, "bond_type": 1},
                51: {"from_atom_index": 28, "to_atom_index": 48, "bond_type": 1},
                52: {"from_atom_index": 29, "to_atom_index": 49, "bond_type": 1},
                53: {"from_atom_index": 30, "to_atom_index": 52, "bond_type": 1},
                54: {"from_atom_index": 31, "to_atom_index": 53, "bond_type": 1},
                55: {"from_atom_index": 31, "to_atom_index": 54, "bond_type": 1},
                56: {"from_atom_index": 31, "to_atom_index": 55, "bond_type": 1},
                57: {"from_atom_index": 32, "to_atom_index": 39, "bond_type": 1},
                58: {"from_atom_index": 32, "to_atom_index": 56, "bond_type": 1},
                59: {"from_atom_index": 32, "to_atom_index": 57, "bond_type": 1},
                60: {"from_atom_index": 33, "to_atom_index": 40, "bond_type": 1},
                61: {"from_atom_index": 33, "to_atom_index": 58, "bond_type": 1},
                62: {"from_atom_index": 33, "to_atom_index": 59, "bond_type": 1},
                63: {"from_atom_index": 34, "to_atom_index": 60, "bond_type": 1},
                64: {"from_atom_index": 34, "to_atom_index": 61, "bond_type": 1},
                65: {"from_atom_index": 34, "to_atom_index": 62, "bond_type": 1},
                66: {"from_atom_index": 35, "to_atom_index": 63, "bond_type": 1},
                67: {"from_atom_index": 35, "to_atom_index": 64, "bond_type": 1},
                68: {"from_atom_index": 35, "to_atom_index": 65, "bond_type": 1},
                69: {"from_atom_index": 36, "to_atom_index": 66, "bond_type": 1},
                70: {"from_atom_index": 36, "to_atom_index": 67, "bond_type": 1},
                71: {"from_atom_index": 36, "to_atom_index": 68, "bond_type": 1},
                72: {"from_atom_index": 37, "to_atom_index": 41, "bond_type": 2},
                73: {"from_atom_index": 37, "to_atom_index": 69, "bond_type": 1},
                74: {"from_atom_index": 38, "to_atom_index": 42, "bond_type": 2},
                75: {"from_atom_index": 38, "to_atom_index": 70, "bond_type": 1},
                76: {"from_atom_index": 41, "to_atom_index": 71, "bond_type": 1},
                77: {"from_atom_index": 41, "to_atom_index": 72, "bond_type": 1},
                78: {"from_atom_index": 42, "to_atom_index": 73, "bond_type": 1},
                79: {"from_atom_index": 42, "to_atom_index": 74, "bond_type": 1},
            },
        )

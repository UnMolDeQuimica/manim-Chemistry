# Changelog

## Unreleased

# Documentation
[Issue #79](https://github.com/UnMolDeQuimica/manim-Chemistry/issues/79): Updates the README.

# Fix
[Issue #69](https://github.com/UnMolDeQuimica/manim-Chemistry/issues/69): Fixes an error when calling the PubChem API and returns an error.

# New Features
[Issue #69](https://github.com/UnMolDeQuimica/manim-Chemistry/issues/69): Adds Molecule as a proxy to get multiple molecule types.
[Issue #80](https://github.com/UnMolDeQuimica/manim-Chemistry/issues/80): Adds a function to molecules to add the name.
[Issue #82](https://github.com/UnMolDeQuimica/manim-Chemistry/issues/82): Adds a cli utility to download molecules from PubChem to files.

## 0.5.0

### Bugfixes

### Fixes
* [Issue #48](https://github.com/UnMolDeQuimica/manim-Chemistry/issues/48): Fix test suite.
* [Issue #45](https://github.com/UnMolDeQuimica/manim-Chemistry/pull/63): Fixes issue with coloring on double and triple bonds in GraphMolecule

### New Features
* [Issue #56](https://github.com/UnMolDeQuimica/manim-Chemistry/pull/56): Adds `molecule_from_file` and `multiple_molecules_from_file` to MMolecule class. Now you just need to pass the file and Manim Chemistry will handle the parsing.
* [Issue #59](https://github.com/UnMolDeQuimica/manim-Chemistry/pull/59): Adds `molecule_from_file` and `multiple_molecules_from_file` to GraphMolecule class. Now you just need to pass the file and Manim Chemistry will handle the parsing.
* [Issue #60](https://github.com/UnMolDeQuimica/manim-Chemistry/pull/60): Adds `molecule_from_file` and `multiple_molecules_from_file` to ThreeDMolecule class. Now you just need to pass the file and Manim Chemistry will handle the parsing.
* [Issue #42](https://github.com/UnMolDeQuimica/manim-Chemistry/pull/61): Adds support for ASNT format.
* [Issue #43](https://github.com/UnMolDeQuimica/manim-Chemistry/pull/62): Adds support for JSON format.
* [Issue #44](https://github.com/UnMolDeQuimica/manim-Chemistry/pull/63): Adds support for XML format.
* [Issue #45](https://github.com/UnMolDeQuimica/manim-Chemistry/pull/63): Adds `molecule_from_string` and `multiple_molecules_from_string` to GraphMolecule, ThreeDMolecule and MMolecule.
* [Issue #45](https://github.com/UnMolDeQuimica/manim-Chemistry/pull/63): Adds support for Pub Chem API.
* [Issue #45](https://github.com/UnMolDeQuimica/manim-Chemistry/pull/63): Use of source csv is now optional on ThreeDMolecules.
* [Issue #68](https://github.com/UnMolDeQuimica/manim-Chemistry/pull/72): Added `ignore_hydrogens` and `ignore_all_hydrogens` parameter to MCMolecule molecule generation functions.
* [Issue #75](https://github.com/UnMolDeQuimica/manim-Chemistry/pull/76): Adds support for 3D structures on Pub Chem API.

### Improvements
* [Issue #46](https://github.com/UnMolDeQuimica/manim-Chemistry/pull/47): Modify automated tests to work only on pull requests.
* [Issue #41](https://github.com/UnMolDeQuimica/manim-Chemistry/pull/50): Adds FileHandler, BaseParser, MolParser and SDFParser classes. Adds tests for the MolParser.
* [Issue #51](https://github.com/UnMolDeQuimica/manim-Chemistry/pull/55): Adds MC Classes: MCElement, MCAtom, MCBond and MCMolecule
* [Issue #52](https://github.com/UnMolDeQuimica/manim-Chemistry/pull/56): Modifies GraphMolecule to use the new MC Classes and adds tests to be ran when modifications on GraphMolecule class are done.
* [Issue #60](https://github.com/UnMolDeQuimica/manim-Chemistry/pull/59): Modifies MMolecule to use the new MCClasses but keeps available old logic.
* [Issue #60](https://github.com/UnMolDeQuimica/manim-Chemistry/pull/60): Modifies ThreeDMolecule to use the new MCClasses but keeps available old logic.
* [Issue #58](https://github.com/UnMolDeQuimica/manim-Chemistry/pull/58): Adds contribute guide and PR template.
* [Issue #59](https://github.com/UnMolDeQuimica/manim-Chemistry/pull/59): Modifies MMolecule to use parsers.
* [Issue #70](https://github.com/UnMolDeQuimica/manim-Chemistry/pull/71): Implements AbstractMolecule across all molecule types.
* [Issue #66](https://github.com/UnMolDeQuimica/manim-Chemistry/pull/71): Adds tests for the new changes.
* [Issue #74](https://github.com/UnMolDeQuimica/manim-Chemistry/pull/77): Adds error message when trying to run ThreeDMolecules without OpenGL renderer

### Breaking changes
* [Issue #48 Fix](https://github.com/UnMolDeQuimica/manim-Chemistry/issues/48): Fix test suite. Removes support for python 3.8 and python 3.9 because configuring the tests on GitHub is trickier.

### Documentation
* [Issue #59](https://github.com/UnMolDeQuimica/manim-Chemistry/pull/59): Modifies the documentation to use the new functions (`molecule_from_file`) instead of the old ones (`from_mol`, `from_sdf` and `build_from_mol`)
* [Issue #67](https://github.com/UnMolDeQuimica/manim-Chemistry/pull/78): Adds decent documentation.

## 0.4.4


## 0.4.3
### Bugfix
* [Issue #36 Bugfix](https://github.com/UnMolDeQuimica/manim-Chemistry/pull/36): Fix error when creating triple bonds. It was cause by a call to a deprecated function. Big thanks to [@thinktraveler](https://github.com/thinktraveller) for opening a request!

## 0.4.2
### New Features
* [Issue #33 Improvement](https://github.com/UnMolDeQuimica/manim-Chemistry/pull/34): Adds functions to get the atoms and bonds positions. Big thanks to [@thinktraveler](https://github.com/thinktraveller) for opening a request!

## 0.4.1
### Bugfix
* Fixed GraphMolecule animations [36fbd7](https://github.com/UnMolDeQuimica/manim-Chemistry/commit/36fbd72bc76931a7f6fa1ab67c1bb48b573855e5)


## 0.4.0
### Fixes
* Fixed readme [a05ce8](https://github.com/UnMolDeQuimica/manim-Chemistry/commit/a05ce87bef3d855dbf3371bf4e5abadf17eccd06)

### Improvements
* Modified double and triple bond style in GraphMolecules [5f3aada](https://github.com/UnMolDeQuimica/manim-Chemistry/commit/5f3aada58fd3fe90ff1d3f6f5df3759366484b3d)
* Added ruff as linter [b9bee23](https://github.com/UnMolDeQuimica/manim-Chemistry/commit/b9bee231b70eac5b5decba1849d935b87e86342b)
* Added sheen direction to double bonds [a88edab](https://github.com/UnMolDeQuimica/manim-Chemistry/commit/a88edab87a3184328147c2bf3961b98817926fb1)
* Updated docs with new features [7ecb5d](https://github.com/UnMolDeQuimica/manim-Chemistry/commit/7ecb5d3dc34932d93b3cf71f65ed01e76e645dbd)

### New Features
* Added indexes to GraphMolecule labels [b8fc04b](https://github.com/UnMolDeQuimica/manim-Chemistry/commit/b8fc04b7adc9654a4529ddec01b6c2e6f67cd4cd)
* Added partial selection of atoms in GraphMolecule [80da008](https://github.com/UnMolDeQuimica/manim-Chemistry/commit/80da008f7ddcbaf944b813f8a6fd49eab5551183)
* Added GAAnimationBuilder [07097df](https://github.com/UnMolDeQuimica/manim-Chemistry/commit/07097dfe03671374b4f1e13a7a9eb7279c40775a)

## 0.3.2
### Fixes
* Fixed P Orbital example. Special thanks to [@Roseleaves](https://github.com/Roseleaves) for opening the [related issue #15](https://github.com/UnMolDeQuimica/manim-Chemistry/issues/15). [7ffdc5](https://github.com/UnMolDeQuimica/manim-Chemistry/pull/16/commits/7ffdc52f90bae0605c27a3f9d545d0538a51c04b).

## 0.3.1
### Bugfixes
* Fixed animation issue with SimpleLine and its subclasses.

## 0.3.0
### New Features
* Added GenericElement class that will be the base for future developments. [1668d67](https://github.com/UnMolDeQuimica/manim-Chemistry/commit/1668d670752c86b860ff20c2d9e58ba4286329e1)
* Added GraphMolecule. This class is based on Manim's Graph class and gives simple yet beautiful molecules based. [1668d67](https://github.com/UnMolDeQuimica/manim-Chemistry/commit/1668d670752c86b860ff20c2d9e58ba4286329e1)


## 0.2.0
### New Features
* Added basic support for chemical formulas. [fcc7110](https://github.com/UnMolDeQuimica/manim-Chemistry/commit/3948d73ff052ad3051b432dd17f9d4e5077e3892)

## 0.1.1
### New Features
* Created class NamedMolecule.  [3948d73](https://github.com/UnMolDeQuimica/manim-Chemistry/commit/3948d73ff052ad3051b432dd17f9d4e5077e3892)

### Bugfixes
* Fixed implicit hydrogen missing bonds. [a66062c](https://github.com/UnMolDeQuimica/manim-Chemistry/commit/a66062cb374b3c2dbb4e9abac11359e6a784db69)

### Code improvements
* Improved rotate bond function. [fa0ca46](https://github.com/UnMolDeQuimica/manim-Chemistry/commit/fa0ca46d28f1e505b0c40225912da2a6bc50383a)

### Auxiliary Files improvements

* Added English version of Elements.csv file. [da7438b](https://github.com/UnMolDeQuimica/manim-Chemistry/commit/da7438b724f4fc149a5be83f0f0dbdc3e64d42d8)


### Documentation improvement
* Fixed typo in add_bonds_numbering example.
* Added NamedMolecule example.

## 0.1.0
* Creation of the project

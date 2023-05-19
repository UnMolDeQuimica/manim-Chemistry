from .element import *
from .periodic_table import *
from .threeD import *
from .twoD import *
from .orbitals import *
from .bohr_atom import *
from .utils import *

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    # package is not installed
    __version__ = "unknown"

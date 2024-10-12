from .element import *  # noqa F841
from .periodic_table import *  # noqa F841
from .threeD import *  # noqa F841
from .twoD import *  # noqa F841
from .orbitals import *  # noqa F841
from .bohr_atom import *  # noqa F841
from .utils import *  # noqa F841

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    # package is not installed
    __version__ = "unknown"

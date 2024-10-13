import numpy as np

from .utils import OpenGLSphere
from ..element import Element


class ThreeDAtom(OpenGLSphere):
    """
    Used to draw a sphere which represents an atom.
    Uses an Element to get data.
    """

    def __init__(self, element: Element, coords=np.array([0, 0, 0]), **kwargs):
        self.center = coords
        self.coords = coords
        self.element = element

        super().__init__(center=self.center, color=element.color, **kwargs)
        self.scale(0.25)

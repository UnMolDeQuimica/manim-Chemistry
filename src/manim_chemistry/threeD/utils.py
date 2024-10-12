import numpy as np

from manim import ORIGIN, TAU, PI
from manim.mobject.opengl.opengl_surface import OpenGLSurface


class OpenGLSphere(OpenGLSurface):
    def __init__(
        self,
        center=ORIGIN,
        **kwargs,
    ):
        super().__init__(
            self.uv_func,
            u_range=(0, TAU),
            v_range=(0, PI),
            **kwargs,
        )

        self.shift(center)

    def uv_func(self, u, v):
        return np.array(
            [np.cos(u) * np.sin(v), np.sin(u) * np.sin(v), -np.cos(v)],
        )

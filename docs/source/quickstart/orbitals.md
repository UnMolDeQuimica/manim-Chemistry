# Orbitals
At this moment, Manim Chemistry can handle Atomic Orbitals only. Molecular orbitals are too complex to implement in such a basic system. See the [philosophy](/philosophy) section to know more about it.

Still, we can get atomic orbitals pretty easily just by selecting the *l* and *m* levels we want to plot. As they are 3D rendered, make sure you are using **opengl** as your renderer:

```python
from manim import *
from manim_chemistry import *

class DrawPOrbital(Scene):
    def construct(self):
        orbital = Orbital(l=1, m=-1)
        self.add(orbital)
```

![plot](../../../examples/examples_assets/orbitals_example.png)

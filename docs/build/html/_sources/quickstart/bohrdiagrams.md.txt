# BohrDiagrams

Bohr diagrams are very outdated, scientifically speaking, but drawing them might be usefull to communicate certain ideas. Here all you have to do is set the number of protons, electrons and neutrons and you will get a nice diagram:

```python
from manim import *
from manim_chemistry import *

class DrawBohrDiagram(Scene):
    def construct(self):
        diagram = BohrAtom(e=14, p=14,, n=10)
        self.add(diagram)
```
Here you have your nice diagram!

![plot](../../../examples/examples_assets/BohrDiagram_ManimCE_v0.17.3.png)

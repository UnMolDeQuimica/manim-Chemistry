# Creating a Periodic Table
Manim Chemistry uses `MElementObjects` to create the little boxes that contain element data. Then, you can put them together and make a periodic table. Let's see how can we do this!

## MElementObject
Again, you can use it a [csv data file](../../../assets/Elements_EN.csv) to automate the process and create a little MElementObject.

```
from manim import *
from manim_chemistry import *

class DrawCarbonElement(Scene):
    def construct(self):
        carbon = MElementObject.from_csv_file_data(filename="Elementos.csv", atomic_number=6)
        self.add(carbon)
```

And there you have it!

![plot](../../../examples/examples_assets/DrawCarbonElement_ManimCE_v0.17.3.png)

## PeriodicTable
To make the whole periodic table you need data for every element inside that data source file. The provided example file already has it, so you just have to copy it and adapt to your needs. Using the cpk coloring and the following code we get that beautiful periodic table:

```python
from manim import *
from manim_chemistry import *

class DrawPeriodicTable(Scene):
    def construct(self):
        self.add(PeriodicTable(data_file="Elementos.csv"))
```

![plot](../../../examples/examples_assets/DrawPeriodicTable_ManimCE_v0.17.3.png)

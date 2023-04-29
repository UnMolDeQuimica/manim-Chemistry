import pandas as pd


class Element:
    def __repr__(self) -> str:
        return f"Element {self.atomic_number}: {self.name} ({self.symbol})"

    def __init__(
        self,
        symbol: str = "H",
        name: str = "H",
        atomic_number: int = 1,
        mass: float = 1.008,
        color: str or None = "#FFFFFF",
    ):
        self.symbol = symbol
        self.name = name
        self.atomic_number = atomic_number
        self.mass = mass
        self.color = color or "#ff00ff"

    def from_csv_file(filename, element: str or int):
        use_valid_reference_string = f"What are you doing? Pass a valid atomic reference. {element} is NOT a valid reference"
        data = pd.read_csv(filename, index_col=False)

        if isinstance(element, str):
            search_column = "Symbol"

        elif isinstance(element, int) and element < 118:
            search_column = "AtomicNumber"

        else:
            raise Exception(use_valid_reference_string)

        subdata = data.loc[data[search_column] == element]

        if subdata.empty:
            raise Exception(use_valid_reference_string)

        element_data = subdata.squeeze().to_dict()

        return Element(
            symbol=element_data["Symbol"],
            name=element_data["Name"],
            atomic_number=element_data["AtomicNumber"],
            mass=element_data["AtomicMass"],
            color=element_data["Color"],
        )

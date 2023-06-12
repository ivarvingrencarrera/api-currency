class Currency:
    def __init__(self, id: int, alphabetic_code: str, numeric_code: int, name: str, symbol: str) -> None:
        self.id = id
        self.alphabetic_code = alphabetic_code
        self.numeric_code = numeric_code
        self.name = name
        self.symbol = symbol

    def __eq__(self, other: object) -> bool:
	    return self.alphabetic_code == other.alphabetic_code if isinstance(other, Currency) else False

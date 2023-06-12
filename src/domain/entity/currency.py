class Currency:
    def __init__(self, id: int, alphabetic_code: str, numeric_code: int, name: str, symbol: str) -> None:
        self.id = id
        self.alphabetic_code = alphabetic_code
        self.numeric_code = numeric_code
        self.name = name
        self.symbol = symbol

    def __eq__(self, other: object) -> bool:
        return self.alphabetic_code == other.alphabetic_code if isinstance(other, Currency) else False

    def __str__(self) -> str:
        return f'{self.alphabetic_code} - {self.name}'

    def __repr__(self) -> str:
        id_repr = f'id={self.id!r}'
        code_repr = f'alphabetic_code={self.alphabetic_code!r}'
        numeric_repr = f'numeric_code={self.numeric_code!r}'
        name_repr = f'name={self.name!r}'
        symbol_repr = f'symbol={self.symbol!r}'
        return f'Currency({id_repr}, {code_repr}, {numeric_repr}, {name_repr}, {symbol_repr})'

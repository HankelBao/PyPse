from enum import Enum, auto
from .values import Value, ValueType


class SymbolType(Enum):
    CONST = auto()
    VARIABLE = auto()
    FUNCTION = auto()
    PRECEDURE = auto()


class Symbol():
    def __init__(self, symbol_name: str, symbol_type: SymbolType):
        self.symbol_name = symbol_name
        self.symbol_type = symbol_type
        self.symbol_value = None

    def init_value(self, value_type):
        self.symbol_value = Value(value_type)

    def __repr__(self):
       return f"Symbol Name: {self.symbol_name}, Symbol Type: {self.symbol_type.name}"

    def match(self, symbol_name: str, symbol_type: SymbolType, block=None):
        if '[' in symbol_name and ']' in symbol_name:
            array_index_str = symbol_name[symbol_name.index('[')+1: symbol_name.index(']')]
            array_index = Expression(array_index_str, block).get_value().value_in_python
            symbol_name = symbol_name[:symbol_name.index('[')]

        if self.symbol_name == symbol_name and self.symbol_type == symbol_type:
            if 'array_index' in dir():
                symbol = Symbol("Array Item Symbol", SymbolType.VARIABLE)
                value = self.symbol_value.array_value(array_index)
                symbol.symbol_value = value
                return symbol
            return self
        return False


class Symbols():
    def __init__(self):
        self.symbols = []

    def add(self, symbol: Symbol):
        self.symbols.append(symbol)

    def get(self, symbol_type: SymbolType, symbol_name: str, block=None) -> Symbol:
        def find_symbol_in_symbols(symbol_type: SymbolType, symbol_name: str) -> Symbol:
            for symbol in self.symbols:
               if symbol.match(symbol_type, symbol_name, block):
                    return symbol.match(symbol_type, symbol_name, block)
            return None

        symbol = find_symbol_in_symbols(symbol_name, symbol_type)
        return symbol

from .expressions import Expression

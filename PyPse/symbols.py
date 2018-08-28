from enum import Enum, auto
from .values import Value


class SymbolType(Enum):
    CONST = auto()
    VARIABLE = auto()
    FUNCTION = auto()
    PRECEDURE = auto()


class Symbol():
    def __init__(self, symbol_name: str, symbol_type: SymbolType):
        self.sname = symbol_name
        self.svalue = Value(symbol_type)


class Symbols():
    def __init__(self):
        self.symbols = []

    def add(self, symbol: Symbol):
        self.symbols.append(symbol)

    def get(self, stype: SymbolType, sname: str):
        for symbol in self.symbols:
            if symbol.sname == sname and symbol.svalue.vtype == stype:
                return symbol

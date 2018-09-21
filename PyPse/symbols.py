from enum import Enum, auto
from .values import Value, ValueType, get_ValueType_by_name
from .precompiler import CodeLine


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


def create_symbol_variable(symbol_name_str: str, value_type_str: str) -> Symbol:
    symbol_type = SymbolType.VARIABLE
    value_type = get_ValueType_by_name(value_type_str)
    symbol = Symbol(symbol_name_str, symbol_type)
    symbol.init_value(value_type)

    if value_type == ValueType.ARRAY:
        array_range_exp = CodeLine("", 0, value_type_str).str_between('[', ']')
        range_left_exp_str, range_right_exp_str = array_range_exp.split("..")
        array_range_left_value = Expression(range_left_exp_str, None).get_value()
        array_range_right_value = Expression(range_right_exp_str, None).get_value()
        symbol.symbol_value.init_array(ValueType.INT, array_range_left_value.value_in_python, array_range_right_value.value_in_python)

    return symbol


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

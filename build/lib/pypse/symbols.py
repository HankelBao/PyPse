from enum import Enum, auto
from lark import Tree
from .debug import DebugOutput
from .values import Value, ValueType


class Symbol():
    def __init__(self, symbol_name: str, value_type: ValueType):
        self.name = symbol_name
        self.value = Value(value_type)

    def debug_output(self):
        DebugOutput.output(f"symbol name: {self.name}")
        DebugOutput.increase_depth()
        self.value.debug_output()
        DebugOutput.decrease_depth()


class Symbols():
    def __init__(self):
        self.symbol_list = []

    def append(self, symbol: Symbol):
        self.symbol_list.append(symbol)

    def search_by_name(self, symbol_name: str) -> Symbol:
        for symbol in self.symbol_list:
            if symbol.name == symbol_name:
                return symbol
        return None

    def debug_output(self):
        DebugOutput.output_block_attr("sumbols")
        DebugOutput.increase_depth()
        for symbol in self.symbol_list:
            symbol.debug_output()
        DebugOutput.decrease_depth()

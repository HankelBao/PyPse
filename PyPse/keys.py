from lark import Tree
from copy import deepcopy
from .symbols import convert_token_to_symbol_names
from .values import Value, ValueType
from .symbols import Symbol, Symbols
from .debug import DebugOutput


class Key():
    def __init__(self, token: Tree, current_block):
        self.variable_names = convert_token_to_symbol_names(token)
        self.current_block = current_block

    def get_value(self) -> Value:
        # Do one level only here
        symbol = self.__search_symbol_recursively(self.current_block)
        return deepcopy(symbol.value)

    def set_value(self, value: Value):
        symbol = self.__search_symbol_recursively(self.current_block)
        symbol.value.assign_value(value)

    def set_value_in_python(self, value_in_python):
        symbol = self.__search_symbol_recursively(self.current_block)
        symbol.value.assign_value_in_python(value_in_python)

    def __search_symbol_recursively(self, block) -> Symbol:
        symbol = None
        while not symbol:
            if not block:
                return None
            symbol = block.symbols.search_by_name(self.variable_names[0])
            block = block.parentblock
        return symbol

    def debug_output(self):
        DebugOutput.output_block_attr("key")
        DebugOutput.increase_depth()
        DebugOutput.output(self.variable_names)
        DebugOutput.decrease_depth()

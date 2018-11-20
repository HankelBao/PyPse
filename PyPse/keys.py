from lark import Tree
from copy import deepcopy
from .values import Value, ValueType
from .symbols import Symbol, Symbols
from .debug import DebugOutput
from .converters import convert_key_token_to_key_items
from . import blocks


class Key():
    def __init__(self, token: Tree, current_block):
        self.key_items = convert_key_token_to_key_items(token)
        self.current_block = current_block

    def get_value(self) -> Value:
        value = self.__search_recursively()
        return deepcopy(value)

    def set_value(self, value: Value):
        key_value = self.__search_recursively()
        key_value.assign_value(value)

    def set_value_in_python(self, value_in_python):
        symbol = self.__search_symbol_recursively(self.current_block)
        symbol.value.assign_value_in_python(value_in_python)

    def __search_recursively(self) -> Value:
        # Do one level only here
        # Fixme
        value = None
        block = self.current_block
        for key_item in self.key_items:
            symbol_name = key_item['symbol_name']
            array_index = key_item['array_index']

            symbol = block.search_symbol_by_name_recursively(symbol_name)

            if not symbol:
                return None

            if array_index:
                value = symbol.value.value_in_python[int(array_index)]
            else:
                value = symbol.value

            if not isinstance(value.value_type, blocks.TypeBlock):
                break
            else:
                block = value.value_in_python
        return value

    def debug_output(self):
        DebugOutput.output_block_attr("key")
        DebugOutput.increase_depth()
        DebugOutput.output(self.key_items)
        DebugOutput.decrease_depth()


from .symbols import Symbol, SymbolType
from .operations import OperationTypeStructureConjuncture


class Key():
    def __init__(self, key_exp: str, block) -> Symbol:
        self.symbol_names = key_exp.split(OperationTypeStructureConjuncture.identifier)
        for index, symbol_name in enumerate(self.symbol_names):
            self.symbol_names[index] = symbol_name.strip()
        self.root_symbol_name = self.symbol_names[0]
        self.block = block

    def get_symbol(self):
        # symbol_names = self.symbol_names
        root_symbol_name = self.root_symbol_name
        root_symbol = None
        block = self.block

        while True:
            root_symbol = block.symbols.get(SymbolType.VARIABLE, root_symbol_name, self.block)
            if root_symbol:
                break
            else:
                if block.parent:
                    block = block.parent
                else:
                    break

        return root_symbol
        # Not Dealing with Structures here yet

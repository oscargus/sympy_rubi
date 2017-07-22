from matchpy import Symbol, Wildcard
import matchpy

class VariableSymbol(Symbol):
    pass


class Integer(Symbol):
    def __init__(self, value, variable_name=None):
        super(self.__class__, self).__init__(name=str(value), variable_name=variable_name)

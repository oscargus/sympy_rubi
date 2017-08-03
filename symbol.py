from sympy.external import import_module
matchpy = import_module("matchpy")
from sympy.utilities.decorator import doctest_depends_on

if matchpy:
    from matchpy import Wildcard, Operation, CommutativeOperation, AssociativeOperation, OneIdentityOperation, register_operation_iterator
else:
    class Wildcard(object):
        pass

from sympy import cacheit, Symbol

@doctest_depends_on(modules=('matchpy',))
class WC(Wildcard, Symbol):
    def __init__(self, min_length, fixed_size, variable_name=None, optional=None, **assumptions):
        Wildcard.__init__(self, min_length, fixed_size, variable_name, optional)

    def __new__(cls, min_length, fixed_size, variable_name=None, optional=None, **assumptions):
        cls._sanitize(assumptions, cls)
        return WC.__xnew__(cls, min_length, fixed_size, variable_name, optional, **assumptions)

    def __getnewargs__(self):
        return (self.min_length, self.fixed_size, self.variable_name, self.optional)

    @staticmethod
    def __xnew__(cls, min_length, fixed_size, variable_name=None, optional=None, **assumptions):
        obj = Symbol.__xnew__(cls, variable_name, **assumptions)
        return obj

    def _hashable_content(self):
        if self.optional:
            return super()._hashable_content() + (self.min_count, self.fixed_size, self.variable_name, self.optional)
        else:
            return super()._hashable_content() + (self.min_count, self.fixed_size, self.variable_name)

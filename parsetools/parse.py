'''
Parser for FullForm[Downvalues[]] of Mathematica rules.

This parser is customised to parse the output in MatchPy rules format. Multiple
`Constraints` are divided into individual `Constraints` because it helps the
MatchPy's `ManyToOneReplacer` to backtrack earlier and improve the speed.

Parsed output is formatted into readable format by using `sympify` and print the
expression using `sstr`. This replaces `And`, `Mul`, 'Pow' by their respective
symbols.

Mathematica
===========

To get the full form from Wolfram Mathematica, type:
```
ShowSteps = False
Import["RubiLoader.m"]
Export["output.txt", ToString@FullForm@DownValues@Int]
```

The file ``output.txt`` will then contain the rules in parseable format.

References
==========
[1] http://reference.wolfram.com/language/ref/FullForm.html
[2] http://reference.wolfram.com/language/ref/DownValues.html
[3] https://gist.github.com/Upabjojr/bc07c49262944f9c1eb0
'''
import re
import os
import inspect
from sympy import sympify, Function, Set, Symbol
from sympy.printing import sstr, StrPrinter

class RubiStrPrinter(StrPrinter):
    def _print_Not(self, expr):
        return "Not(%s)" % self._print(expr.args[0])

def rubi_printer(expr, **settings):
    return RubiStrPrinter(settings).doprint(expr)

replacements = dict( # Mathematica equivalent functions in SymPy
        Times="Mul",
        Plus="Add",
        Power="Pow",
        Log='log',
        Sqrt='sqrt',
        Cos='cos',
        Sin='sin',
        Tan='tan',
        Cot='1/tan',
        cot='1/tan',
        Sec='1/cos',
        sec='1/cos',
        Csc='1/sin',
        csc='1/sin',
        ArcSin='asin',
        ArcCos='acos',
        # ArcTan='atan',
        ArcCot='acot',
        ArcSec='asec',
        ArcCsc='acsc',
        Sinh='sinh',
        Cosh='cosh',
        Tanh='tanh',
        Coth='1/tanh',
        coth='1/tanh',
        Sech='1/cosh',
        sech='1/cosh',
        Csch='1/sinh',
        csch='1/sinh',
        ArcSinh='asinh',
        ArcCosh='acosh',
        ArcTanh='atanh',
        ArcCoth='acoth',
        ArcSech='asech',
        ArcCsch='acsch',
        Expand='expand',
        Im='im',
        Re='re',
        Flatten='flatten',
        Polylog='polylog',
        Cancel='cancel',
        #Gamma='gamma',
        TrigExpand='expand_trig',
        Sign='sign',
        Simplify='simplify',
        Defer='UnevaluatedExpr',
        Identity = 'S',
        Sum = 'Sum_doit',
        Module = 'With',
        Block = 'With',
        Null = 'None'
)

temporary_variable_replacement = { # Temporarily rename because it can raise errors while sympifying
        'gcd' : "_gcd",
        'jn' : "_jn",

}

permanent_variable_replacement = { # Permamenely rename these variables
    r"\[ImaginaryI]" : 'ImaginaryI',
    "$UseGamma": '_UseGamma',
}

#these functions have different return type in different cases. So better to use a try and except in the constraints, when any of these appear
f_diff_return_type = ['BinomialParts', 'BinomialDegree', 'TrinomialParts', 'GeneralizedBinomialParts', 'GeneralizedTrinomialParts', 'PseudoBinomialParts', 'PerfectPowerTest',
    'SquareFreeFactorTest', 'SubstForFractionalPowerOfQuotientOfLinears', 'FractionalPowerOfQuotientOfLinears', 'InverseFunctionOfQuotientOfLinears',
    'FractionalPowerOfSquareQ', 'FunctionOfLinear', 'FunctionOfInverseLinear', 'FunctionOfTrig', 'FindTrigFactor', 'FunctionOfLog',
    'PowerVariableExpn', 'FunctionOfSquareRootOfQuadratic', 'SubstForFractionalPowerOfLinear', 'FractionalPowerOfLinear', 'InverseFunctionOfLinear',
    'Divides', 'DerivativeDivides', 'TrigSquare', 'SplitProduct', 'SubstForFractionalPowerOfQuotientOfLinears', 'InverseFunctionOfQuotientOfLinears',
    'FunctionOfHyperbolic', 'SplitSum']

def contains_diff_return_type(a):
    if isinstance(a, list):
        for i in a:
            if contains_diff_return_type(i):
                return True
    elif type(a) == Function('With') or type(a) == Function('Module'):
        for i in f_diff_return_type:
            if a.has(Function(i)):
                return True
    else:
        if a in f_diff_return_type:
            return True
    return False

def parse_full_form(wmexpr):
    '''
    Parses FullForm[Downvalues[]] generated by Mathematica
    '''
    out = []
    stack = [out]
    generator = re.finditer(r'[\[\],]', wmexpr)
    last_pos = 0
    for match in generator:
        if match is None:
            break
        position = match.start()
        last_expr = wmexpr[last_pos:position].replace(',', '').replace(']', '').replace('[', '').strip()

        if match.group() == ',':
            if last_expr != '':
                stack[-1].append(last_expr)
        elif match.group() == ']':
            if last_expr != '':
                stack[-1].append(last_expr)
            stack.pop()
            current_pos = stack[-1]
        elif match.group() == '[':
            stack[-1].append([last_expr])
            stack.append(stack[-1][-1])
        last_pos = match.end()
    return out[0]

def get_default_values(parsed, default_values={}):
    '''
    Returns Optional variables and their values in the pattern
    '''
    if not isinstance(parsed, list):
        return default_values

    if parsed[0] == "Times": # find Default arguments for "Times"
        for i in parsed[1:]:
            if i[0] == "Optional":
                default_values[(i[1][1])] = 1

    if parsed[0] == "Plus": # find Default arguments for "Plus"
        for i in parsed[1:]:
            if i[0] == "Optional":
                default_values[(i[1][1])] = 0

    if parsed[0] == "Power": # find Default arguments for "Power"
        for i in parsed[1:]:
            if i[0] == "Optional":
                default_values[(i[1][1])] = 1

    if len(parsed) == 1:
        return default_values

    for i in parsed:
        default_values = get_default_values(i, default_values)

    return default_values

def add_wildcards(string, optional={}):
    '''
    Replaces `Pattern(variable)` by `variable` in `string`.
    Returns the free symbols present in the string.
    '''
    symbols = [] # stores symbols present in the expression

    p = r'(Optional\(Pattern\((\w+), Blank\)\))'
    matches = re.findall(p, string)
    for i in matches:
        string = string.replace(i[0], "WC('{}', S({}))".format(i[1], optional[i[1]]))
        symbols.append(i[1])

    p = r'(Pattern\((\w+), Blank\))'
    matches = re.findall(p, string)
    for i in matches:
        string = string.replace(i[0], i[1] + '_')
        symbols.append(i[1])

    p = r'(Pattern\((\w+), Blank\(Symbol\)\))'
    matches = re.findall(p, string)
    for i in matches:
        string = string.replace(i[0], i[1] + '_')
        symbols.append(i[1])

    return string, symbols

def seperate_freeq(s, variables=[], x=None):
    '''
    Returns list of symbols in FreeQ.
    '''
    if s[0] == 'FreeQ':
        if len(s[1]) == 1:
            variables = [s[1]]
        else:
            variables = s[1][1:]
        x = s[2]
    else:
        for i in s[1:]:
            variables, x = seperate_freeq(i, variables, x)
            return variables, x
    return variables, x

def parse_freeq(l, x, cons_index, cons_dict, cons_import, symbols=None):
    '''
    Converts FreeQ constraints into MatchPy constraint
    '''
    res = []
    cons = ''
    for i in l:
        if isinstance(i, str):
            r = '    return FreeQ({}, {})'.format(i, x)
            if r not in cons_dict.values():
                cons_index += 1
                c = '\ndef cons_f{}({}, {}):\n'.format(cons_index, i, x)
                c += r
                c += '\n\ncons{} = CustomConstraint({})\n'.format(cons_index, 'cons_f{}'.format(cons_index))
                cons_name = 'cons{}'.format(cons_index)
                cons_dict[cons_name] = r
            else:
                c = ''
                cons_name = next(key for key, value in cons_dict.items() if value == r)

        elif isinstance(i, list):
            s = list(set(get_free_symbols(i, symbols)))
            s = ', '.join(s)
            r = '    return FreeQ({}, {})'.format(generate_sympy_from_parsed(i), x)
            if r not in cons_dict.values():
                cons_index += 1
                c = '\ndef cons_f{}({}):\n'.format(cons_index, s)
                c += r
                c += '\n\ncons{} = CustomConstraint({})\n'.format(cons_index, 'cons_f{}'.format(cons_index))
                cons_name = 'cons{}'.format(cons_index)
                cons_dict[cons_name] = r
            else:
                c = ''
                cons_name = next(key for key, value in cons_dict.items() if value == r)

        if cons_name not in cons_import:
            cons_import.append(cons_name)

        res.append(cons_name)
        cons += c

    if res != []:
        return ', ' + ', '.join(res), cons, cons_index
    return '', cons, cons_index

def generate_sympy_from_parsed(parsed, wild=False, symbols=[], replace_Int=False):
    '''
    Parses list into Python syntax.

    Parameters
    ==========
    wild : When set to True, the symbols are replaced as wild symbols.
    symbols : Symbols already present in the pattern.
    replace_Int: when set to True, `Int` is replaced by `Integral`(used to parse pattern).
    '''
    out = ""

    if not isinstance(parsed, list):
        try: #return S(number) if parsed is Number
            float(parsed)
            return "S({})".format(parsed)
        except:
            pass
        if parsed in symbols:
            if wild:
                return parsed + '_'
        return parsed

    if parsed[0] == 'Rational':
        return 'S({})/S({})'.format(generate_sympy_from_parsed(parsed[1], wild=wild, symbols=symbols, replace_Int=replace_Int), generate_sympy_from_parsed(parsed[2], wild=wild, symbols=symbols, replace_Int=replace_Int))

    if parsed[0] in replacements:
        out += replacements[parsed[0]]
    elif parsed[0] == 'Int' and replace_Int:
        out += 'Integral'
    else:
        out += parsed[0]

    if len(parsed) == 1:
        return out

    result = [generate_sympy_from_parsed(i, wild=wild, symbols=symbols, replace_Int=replace_Int) for i in parsed[1:]]
    if '' in result:
        result.remove('')

    out += "("
    out += ", ".join(result)
    out += ")"

    return out

def get_free_symbols(s, symbols, free_symbols=[]):
    '''
    Returns free_symbols present in `s`.
    '''
    if not isinstance(s, list):
        if s in symbols:
            free_symbols.append(s)
        return free_symbols

    for i in s:
        free_symbols = get_free_symbols(i, symbols, free_symbols)

    return free_symbols

def set_matchq_in_constraint(a, cons_index):
    '''
    Takes care of the case, when a pattern matching has to be done inside a constraint
    '''
    lst = []
    res = ''
    if(isinstance(a, list)):
        if a[0] == 'MatchQ':
            s = a
            optional = get_default_values(s, {})
            r = generate_sympy_from_parsed(s, replace_Int=True)
            r, free_symbols = add_wildcards(r, optional=optional)
            free_symbols = list(set(free_symbols)) #remove common symbols
            r = sympify(r, locals={"Or": Function("Or"), "And": Function("And"), "Not":Function("Not")})
            pattern = r.args[1].args[0]
            cons = r.args[1].args[1]
            pattern = rubi_printer(pattern, sympy_integers=True)
            pattern = setWC(pattern)
            res = '    def _cons_f_{}({}):\n        return {}\n'.format(cons_index, ', '.join(free_symbols), cons)
            res += '    _cons_{} = CustomConstraint(_cons_f_{})\n'.format(cons_index, cons_index)
            res += '    pat = Pattern(UtilityOperator({}, x), _cons_{})\n'.format(pattern, cons_index)
            res += '    result_matchq = is_match(UtilityOperator({}, x), pat)'.format(r.args[0])
            return "result_matchq", res

        else:
            for i in a:
                if isinstance(i, list):
                    r = set_matchq_in_constraint(i, cons_index)
                    lst.append(r[0])
                    res = r[1]
                else:
                    lst.append(i)
    return (lst, res)


def _divide_constriant(s, symbols, cons_index, cons_dict, cons_import):
    # Creates a CustomConstraint of the form `CustomConstraint(lambda a, x: FreeQ(a, x))`
    lambda_symbols = list(set(get_free_symbols(s, symbols, [])))
    r = generate_sympy_from_parsed(s)
    r = sympify(r, locals={"Or": Function("Or"), "And": Function("And"), "Not":Function("Not")})
    if r.has(Function('MatchQ')):
        match_res = set_matchq_in_constraint(s, cons_index)
        res = match_res[1]
        res += '\n    return {}'.format(rubi_printer(sympify(generate_sympy_from_parsed(match_res[0]), locals={"Or": Function("Or"), "And": Function("And"), "Not":Function("Not")}), sympy_integers = True))

    elif contains_diff_return_type(s):
        res = '    try:\n        return {}\n    except (TypeError, AttributeError):\n        return False'.format(rubi_printer(r, sympy_integers=True))
    else:
        res = '    return {}'.format(rubi_printer(r, sympy_integers=True))

    #res = '    return {}'.format(rubi_printer(sympify(generate_sympy_from_parsed(s),locals={"Or": Function("Or"), "And": Function("And"), "Not":Function("Not")}), sympy_integers=True))
    if not res in cons_dict.values():
        cons_index += 1
        cons = '\ndef cons_f{}({}):\n'.format(cons_index, ', '.join(lambda_symbols))
        if 'x' in lambda_symbols:
            cons += '    if isinstance(x, (int, Integer, float, Float)):\n        return False\n'
        cons += res
        cons += '\n\ncons{} = CustomConstraint({})\n'.format(cons_index, 'cons_f{}'.format(cons_index))
        cons_name = 'cons{}'.format(cons_index)
        cons_dict[cons_name] = res
    else:
        cons = ''
        cons_name = next(key for key, value in cons_dict.items() if value == res)

    if cons_name not in cons_import:
        cons_import.append(cons_name)
    return (cons_name, cons, cons_index)

def divide_constraint(s, symbols, cons_index, cons_dict, cons_import):
    '''
    Divides multiple constraints into smaller constraints.

    Parameters
    ==========
    s : constraint as list
    symbols : all the symbols present in the expression
    '''
    result =[]
    cons = ''
    if s[0] == 'And':
        for i in s[1:]:
            if i[0]!= 'FreeQ':
                a = _divide_constriant(i, symbols, cons_index, cons_dict, cons_import)
                result.append(a[0])
                cons += a[1]
                cons_index = a[2]
    else:
        a = _divide_constriant(s, symbols, cons_index, cons_dict, cons_import)
        result.append(a[0])
        cons += a[1]
        cons_index = a[2]


    r = ['']
    for i in result:
        if i != '':
            r.append(i)

    return ', '.join(r),cons, cons_index

def setWC(string):
    '''
    Replaces `WC(a, b)` by `WC('a', S(b))`
    '''
    p = r'(WC\((\w+), S\(([-+]?\d)\)\))'
    matches = re.findall(p, string)
    for i in matches:
        string = string.replace(i[0], "WC('{}', S({}))".format(i[1], i[2]))

    return string

def process_return_type(a1, L):
    a = sympify(a1[1])
    x  =''
    processed = False
    return_value = ''
    if type(a) == Function('With') or type(a) == Function('Module'):
        for i in a.args:
            for s in i.args:
                if isinstance(s, Set) and not s in L:
                    x += '\n        {} = {}'.format(s.args[0], rubi_printer(s.args[1], sympy_integers=True))

            if not type(i) in (Function('List'),  Function('CompoundExpression')) and not i.has(Function('CompoundExpression')):
                return_value = i
                processed = True

            elif type(i) ==Function('CompoundExpression'):
                return_value = i.args[-1]
                processed = True

            elif type(i.args[0]) == Function('CompoundExpression'):
                C = i.args[0]
                return_value = '{}({}, {})'.format(i.func, C.args[-1], i.args[1])
                processed = True
    return x, return_value, processed

def extract_set(s, L):
    '''
    this function extracts all `Set` functions
    '''
    lst = []
    if isinstance(s, Set) and not s in L:
        lst.append(s)
    else:
        try:
            for i in s.args:
                lst += extract_set(i, L)
        except: #when s has no attribute args (like `bool`)
            pass
    return lst

def replaceWith(s, symbols, index):
    '''
    Replaces `With` and `Module by python functions`
    '''
    return_type = None
    with_value = ''
    if type(s) == Function('With') or type(s) == Function('Module'):
        constraints = ' '
        result = '    def With{}({}):'.format(index, ', '.join(symbols))
        if type(s.args[0]) == Function('List'): # get all local variables of With and Module
            L = list(s.args[0].args)
        else:
            L = [s.args[0]]
        lst = []
        for i in s.args[1:]:
            lst+=extract_set(i, L)

        L+=lst
        for i in L: # define local variables
            if isinstance(i, Set):
                with_value += '\n        {} = {}'.format(i.args[0], rubi_printer(i.args[1], sympy_integers=True))

            elif isinstance(i, Symbol):
                with_value += "\n        {} = Symbol('{}')".format(i, i)
        #result += with_value
        if type(s.args[1]) == Function('CompoundExpression'): # Expand CompoundExpression
            C = s.args[1]
            result += with_value
            if isinstance(C.args[0], Set):
                result += '\n        {} = {}'.format(C.args[0].args[0], C.args[0].args[1])
            result += '\n        rubi.append({})\n        return {}'.format(index, rubi_printer(C.args[1], sympy_integers=True))
            return result, constraints, return_type

        elif type(s.args[1]) == Function('Condition'):
            C = s.args[1]
            if len(C.args) == 2:
                if all(j in symbols for j in [str(i) for i in C.free_symbols]):
                    result += with_value
                    #constraints += 'CustomConstraint(lambda {}: {})'.format(', '.join([str(i) for i in C.free_symbols]), sstr(C.args[1], sympy_integers=True))
                    result += '\n        rubi.append({})\n        return {}'.format(index, rubi_printer(C.args[0], sympy_integers=True))
                else:
                    if 'x' in symbols:
                        result += '\n        if isinstance(x, (int, Integer, float, Float)):\n            return False'

                    if contains_diff_return_type(s):
                        n_with_value = with_value.replace('\n', '\n    ')
                        result += '\n        try:{}\n            res = {}'.format(n_with_value, rubi_printer(C.args[1], sympy_integers=True))
                        result += '\n        except (TypeError, AttributeError):\n            return False'
                        result += '\n        if res:'

                    else:
                        result+=with_value
                        result += '\n        if {}:'.format(rubi_printer(C.args[1], sympy_integers=True))
                    return_type = (with_value, rubi_printer(C.args[0], sympy_integers=True))
                    return_type1 = process_return_type(return_type, L)
                    if return_type1[2]:
                        return_type = ( with_value+return_type1[0], rubi_printer(return_type1[1]))
                    result += '\n            return True'
                    result += '\n        return False'
            constraints = ', CustomConstraint(With{})'.format(index)
            return result, constraints, return_type

        elif type(s.args[1]) == Function('Module') or type(s.args[1]) == Function('With'):
            C = s.args[1]
            result += with_value
            return_type = (with_value, rubi_printer(C, sympy_integers=True))
            return_type1 = process_return_type(return_type, L)
            if return_type1[2]:
                return_type = ( with_value+return_type1[0], rubi_printer(return_type1[1]))
            result+=return_type1[0]
            result+='\n        rubi.append({})\n        return {}'.format(index, rubi_printer(return_type1[1]))
            return result, constraints, None

        elif s.args[1].has(Function("CompoundExpression")):
            C = s.args[1].args[0]
            result += with_value
            if isinstance(C.args[0], Set):
                result += '\n        {} = {}'.format(C.args[0].args[0], C.args[0].args[1])
            result += '\n        return {}({}, {})'.format(s.args[1].func, C.args[-1], s.args[1].args[1])
            return result, constraints, None

        result += with_value
        result += '\n        rubi.append({})\n        return {}'.format(index, rubi_printer(s.args[1], sympy_integers=True))
        return result, constraints, return_type
    else:
        return rubi_printer(s, sympy_integers=True), '', return_type

def downvalues_rules(r, header, cons_dict, cons_index, index):
    '''
    Function which generates parsed rules by substituting all possible
    combinations of default values.
    '''
    rules = '['
    parsed = '\n\n'
    cons = ''
    cons_import = []
    for i in r:
        # Parse Pattern
        if i[1][1][0] == 'Condition':
            p = i[1][1][1].copy()
        else:
            p = i[1][1].copy()

        optional = get_default_values(p, {})
        pattern = generate_sympy_from_parsed(p.copy(), replace_Int=True)
        pattern, free_symbols = add_wildcards(pattern, optional=optional)
        free_symbols = list(set(free_symbols)) #remove common symbols
        # Parse Transformed Expression and Constraints
        if i[2][0] == 'Condition': # parse rules without constraints separately
            constriant, constraint_def, cons_index = divide_constraint(i[2][2], free_symbols, cons_index, cons_dict, cons_import) # separate And constraints into individual constraints
            FreeQ_vars, FreeQ_x = seperate_freeq(i[2][2].copy()) # separate FreeQ into individual constraints
            transformed = generate_sympy_from_parsed(i[2][1].copy(), symbols=free_symbols)
        else:
            constriant = ''
            constraint_def = ''
            FreeQ_vars, FreeQ_x = [], []
            transformed = generate_sympy_from_parsed(i[2].copy(), symbols=free_symbols)
        FreeQ_constraint, free_cons_def, cons_index = parse_freeq(FreeQ_vars, FreeQ_x, cons_index, cons_dict, cons_import, free_symbols)
        pattern = sympify(pattern, locals={"Or": Function("Or"), "And": Function("And"), "Not":Function("Not") })
        pattern = rubi_printer(pattern, sympy_integers=True)

        pattern = setWC(pattern)
        transformed = sympify(transformed, locals={"Or": Function("Or"), "And": Function("And"), "Not":Function("Not") })
        constraint_def = constraint_def + free_cons_def
        cons+=constraint_def
        index += 1

        if type(transformed) == Function('With') or type(transformed) == Function('Module'): # define separate function when With appears
            transformed, With_constraints, return_type = replaceWith(transformed, free_symbols, index)
            if return_type is None:
                parsed += '{}'.format(transformed)
                parsed += '\n    pattern' + str(index) +' = Pattern(' + pattern + '' + FreeQ_constraint + '' + constriant + ')'
                parsed += '\n    ' + 'rule' + str(index) +' = ReplacementRule(' + 'pattern' + rubi_printer(index, sympy_integers=True) + ', With{}'.format(index) + ')\n'
            else:

                parsed += '{}'.format(transformed)
                parsed += '\n    pattern' + str(index) +' = Pattern(' + pattern + '' + FreeQ_constraint + '' + constriant + With_constraints + ')'
                parsed += '\n    def replacement{}({}):\n'.format(index, ', '.join(free_symbols)) + return_type[0] + '\n        rubi.append({})\n        return '.format(index) + return_type[1]
                parsed += '\n    ' + 'rule' + str(index) +' = ReplacementRule(' + 'pattern' + rubi_printer(index, sympy_integers=True) + ', replacement{}'.format(index) + ')\n'

        else:
            transformed = rubi_printer(transformed, sympy_integers=True)
            parsed += '    pattern' + str(index) +' = Pattern(' + pattern + '' + FreeQ_constraint + '' + constriant + ')'
            parsed += '\n    def replacement{}({}):\n        rubi.append({})\n        return '.format(index, ', '.join(free_symbols), index) + transformed
            parsed += '\n    ' + 'rule' + str(index) +' = ReplacementRule(' + 'pattern' + rubi_printer(index, sympy_integers=True) + ', replacement{}'.format(index) + ')\n'
        rules += 'rule{}, '.format(index)
        #parsed += 'rubi.add(rule{})\n\n'.format(index)
    rules += ']'
    parsed += '    return ' + rules +'\n'

    header += '    from sympy.integrals.rubi.constraints import ' + ', '.join(word for word in cons_import)
    parsed = header + parsed
    return parsed, cons_index, cons, index

def rubi_rule_parser(fullform, header=None, module_name='rubi_object', file = False):
    '''
    Parses rules in MatchPy format.

    Parameters
    ==========
    fullform : FullForm of the rule as string.
    header : Header imports for the file. Uses default imports if None.
    module_name : name of RUBI module

    References
    ==========
    [1] http://reference.wolfram.com/language/ref/FullForm.html
    [2] http://reference.wolfram.com/language/ref/DownValues.html
    [3] https://gist.github.com/Upabjojr/bc07c49262944f9c1eb0
    '''

    if header == None:  # use default header values
        path_header = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        header = open(os.path.join(path_header, "header.py.txt"), "r").read()
        header = header.format(module_name)

    # Temporarily rename these variables because it
    # can raise errors while sympifying
    cons_dict = {}
    cons_index =0
    index = 0
    cons = ''

    if not file:
        for i in temporary_variable_replacement:
            fullform = fullform.replace(i, temporary_variable_replacement[i])
        # Permanently rename these variables
        for i in permanent_variable_replacement:
            fullform = fullform.replace(i, permanent_variable_replacement[i])

        rules = []
        for i in parse_full_form(fullform): # separate all rules
            if i[0] == 'RuleDelayed':
                rules.append(i)
        parsed = downvalues_rules(rules, header, cons_dict, cons_index, index)
        result = parsed[0].strip() + '\n'
        cons_index = parsed[1]
        cons += parsed[2]
        index = parsed[3]
        # Replace temporary variables by actual values
        for i in temporary_variable_replacement:
            cons = cons.replace(temporary_variable_replacement[i], i)
            result = result.replace(temporary_variable_replacement[i], i)
        cons = "\n".join(header.split("\n")[:-2])+ '\n' + cons
        return result, cons

    input =['integrand_simplification.txt', 'linear_product.txt', 'quadratic_product.txt', 'binomial_product.txt', 'trinomial_product.txt', 'miscellaneous_algebra.txt', 'piecewise_linear.txt', 'exponential.txt', 'logarithms.txt', 'sine.txt', 'tangent.txt', 'secant.txt', 'miscellaneous_trig.txt', 'inverse_trig.txt', 'hyperbolic.txt', 'inverse_hyperbolic.txt', 'special_functions.txt', 'miscellanintegration.txt']
    output =['integrand_simplification.py', 'linear_products.py', 'quadratic_products.py', 'binomial_products.py', 'trinomial_products.py', 'miscellaneous_algebraic.py' ,'piecewise_linear.py', 'exponential.py', 'logarithms.py', 'sine.py', 'tangent.py', 'secant.py', 'miscellaneous_trig.py','inverse_trig.py', 'hyperbolic.py', 'inverse_hyperbolic.py', 'special_functions.py', 'miscellaneous_integration.py']
    for k in range(0, 18):
        module_name = output[k][0:-3]
        path_header = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        header = open(os.path.join(path_header, "header.py.txt"), "r").read()
        header = header.format(module_name)
        with open(input[k], 'r') as myfile:
            fullform =myfile.read().replace('\n', '')
        for i in temporary_variable_replacement:
            fullform = fullform.replace(i, temporary_variable_replacement[i])
        # Permanently rename these variables
        for i in permanent_variable_replacement:
            fullform = fullform.replace(i, permanent_variable_replacement[i])

        rules = []
        for i in parse_full_form(fullform): # separate all rules
            if i[0] == 'RuleDelayed':
                rules.append(i)
        parsed = downvalues_rules(rules, header, cons_dict, cons_index, index)
        result = parsed[0].strip() + '\n'
        cons_index = parsed[1]
        cons += parsed[2]
        index = parsed[3]
        # Replace temporary variables by actual values
        for i in temporary_variable_replacement:
            cons = cons.replace(temporary_variable_replacement[i], i)
            result = result.replace(temporary_variable_replacement[i], i)

        file = open(output[k],'w')
        file.write(str(result))
        file.close()

    cons = "\n".join(header.split("\n")[:-2])+ '\n' + cons
    constraints = open('constraints.py', 'w')
    constraints.write(str(cons))
    constraints.close()
    return None

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

replacements = dict( # Mathematica equivalent functions in SymPy
        Times="Mul",
        Plus="Add",
        Power="Pow",
        Log='log',
        Sqrt='sqrt',
        Cos='cos',
        Sin='sin',
        Tan='tan',
        Cot='cot',
        Sec='sec',
        Csc='csc',
        ArcSin='asin',
        ArcCos='acos',
        #ArcTan='atan',
        ArcCot='acot',
        ArcSec='asec',
        ArcCsc='acsc',
        Sinh='sinh',
        Tanh='tanh',
        Coth='coth',
        Sech='sech',
        Csch='csch',
        ArcSinh='asinh',
        ArcCosh='acosh',
        ArcTanh='atanh',
        ArcCoth='acoth',
        ArcSech='asech',
        ArcCsch='acsch',
        Expand='expand',
        Im='im',
        Re='re',
        Together='together',
        Flatten='flatten',
        Polylog='polylog',
        Cancel='cancel',
        #Gamma='gamma',
        TrigExpand='expand_trig',
        Sign='sign',
        Simplify='simplify',
        Defer='UnevaluatedExpr',
)

temporary_variable_replacement = { # Temporarily rename because it can raise errors while sympifying
        'Sum' : "_Sum",
        'gcd' : "_gcd",
        'jn' : "_jn",
}

permanent_variable_replacement = { # Permamenely rename these variables
    r"\[ImaginaryI]" : 'ImaginaryI',
    "$UseGamma": '_UseGamma',
}

class RubiStrPrinter(StrPrinter):
    def _print_Not(self, expr):
        return "Not(%s)" % self._print(expr.args[0])

def rubi_printer(expr, **settings):
    return RubiStrPrinter(settings).doprint(expr)

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

def parse_freeq(l, x, symbols=None):
    '''
    Converts FreeQ constraints into MatchPy constraint
    '''
    res = []
    for i in l:
        if isinstance(i, str):
            res.append(('CustomConstraint(lambda {}, {}: FreeQ({}, {}))').format(i, x, i, x))
        elif isinstance(i, list):
            s = list(set(get_free_symbols(i, symbols)))
            s = ', '.join(s)
            res.append(('CustomConstraint(lambda {}: FreeQ({}, {}))').format(s, generate_sympy_from_parsed(i), x))
    if res != []:
        return ', ' + ', '.join(res)
    return ''

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

def _divide_constriant(s, symbols):
    # Creates a CustomConstraint of the form `CustomConstraint(lambda a, x: FreeQ(a, x))`
    lambda_symbols = list(set(get_free_symbols(s, symbols, [])))
    return 'CustomConstraint(lambda {}: {})'.format(', '.join(lambda_symbols), rubi_printer(sympify(generate_sympy_from_parsed(s)), sympy_integers=True))

def divide_constraint(s, symbols):
    '''
    Divides multiple constraints into smaller constraints.

    Parameters
    ==========
    s : constraint as list
    symbols : all the symbols present in the expression
    '''
    if s[0] == 'And':
        result = [_divide_constriant(i, symbols) for i in s[1:] if i[0]!='FreeQ']
    else:
        result = [_divide_constriant(s, symbols)]

    r = ['']
    for i in result:
        if i != '':
            r.append(i)

    return ', '.join(r)

def setWC(string):
    '''
    Replaces `WC(a, b)` by `WC('a', S(b))`
    '''
    p = r'(WC\((\w+), S\(([-+]?\d)\)\))'
    matches = re.findall(p, string)
    for i in matches:
        string = string.replace(i[0], "WC('{}', S({}))".format(i[1], i[2]))

    return string

def replaceWith(s, symbols, i):
    '''
    Replaces `With` and `Module by python functions`
    '''
    if type(s) == Function('With') or type(s) == Function('Module'):
        constraints = ', '
        result = '    def With{}({}):'.format(i, ', '.join(symbols))
        if type(s.args[0]) == Function('List'): # get all local variables of With and Module
            L = list(s.args[0].args)
        else:
            L = [s.args[0]]

        for i in L: # define local variables
            if isinstance(i, Set):
                result += '\n        {} = {}'.format(i.args[0], rubi_printer(i.args[1], sympy_integers=True))
            elif isinstance(i, Symbol):
                result += "\n        {} = Symbol('{}')".format(i, i)

        if type(s.args[1]) == Function('CompoundExpression'): # Expand CompoundExpression
            C = s.args[1]
            if isinstance(C.args[0], Set):
                result += '\n        {} = {}'.format(C.args[0].args[0], C.args[0].args[1])
            result += '\n        return {}'.format(rubi_printer(C.args[1], sympy_integers=True))
            return result, constraints
        elif type(s.args[1]) == Function('Condition'):
            C = s.args[1]
            if len(C.args) == 2:
                if all(j in symbols for j in [str(i) for i in C.free_symbols]):
                    constraints += 'CustomConstraint(lambda {}: {})'.format(', '.join([str(i) for i in C.free_symbols]), rubi_printer(C.args[1], sympy_integers=True))
                    result += '\n        return {}'.format(rubi_printer(C.args[0], sympy_integers=True))
                else:
                    result += '\n        if {}:'.format(rubi_printer(C.args[1], sympy_integers=True))
                    result += '\n            return {}'.format(rubi_printer(C.args[0], sympy_integers=True))
                    result += '\n        print("Unable to Integrate")'
            return result, constraints

        result += '\n        return {}'.format(rubi_printer(s.args[1], sympy_integers=True))
        return result, constraints
    else:
        return rubi_printer(s, sympy_integers=True), ''

def downvalues_rules(r, parsed):
    '''
    Function which generates parsed rules by substituting all possible
    combinations of default values.
    '''
    res = []
    index = 0
    for i in r:
        print('parsing rule {}'.format(r.index(i) + 1))
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
            constriant = divide_constraint(i[2][2], free_symbols) # separate And constraints into individual constraints
            FreeQ_vars, FreeQ_x = seperate_freeq(i[2][2].copy()) # separate FreeQ into individual constraints
            transformed = generate_sympy_from_parsed(i[2][1].copy(), symbols=free_symbols)
        else:
            constriant = ''
            FreeQ_vars, FreeQ_x = [], []
            transformed = generate_sympy_from_parsed(i[2].copy(), symbols=free_symbols)

        FreeQ_constraint = parse_freeq(FreeQ_vars, FreeQ_x, free_symbols)
        pattern = sympify(pattern)
        pattern = rubi_printer(pattern, sympy_integers=True)
        pattern = setWC(pattern)
        transformed = sympify(transformed)

        index += 1
        if type(transformed) == Function('With') or type(transformed) == Function('Module'): # define separate function when With appears
            transformed, With_constraints = replaceWith(transformed, free_symbols, index)
            parsed += '    pattern' + str(index) +' = Pattern(' + pattern + '' + FreeQ_constraint + '' + constriant + With_constraints + ')'
            parsed += '\n{}'.format(transformed)
            parsed += '\n    ' + 'rule' + str(index) +' = ReplacementRule(' + 'pattern' + rubi_printer(index, sympy_integers=True) + ', lambda ' + ', '.join(free_symbols) + ' : ' + 'With{}({})'.format(index, ', '.join(free_symbols)) + ')\n    '
        else:
            transformed = rubi_printer(transformed, sympy_integers=True)
            parsed += '    pattern' + str(index) +' = Pattern(' + pattern + '' + FreeQ_constraint + '' + constriant + ')'
            parsed += '\n    ' + 'rule' + str(index) +' = ReplacementRule(' + 'pattern' + rubi_printer(index, sympy_integers=True) + ', lambda ' + ', '.join(free_symbols) + ' : ' + transformed + ')\n    '
        parsed += 'rubi.add(rule'+ str(index) +')\n\n'

    parsed += '    return rubi\n'

    return parsed

def rubi_rule_parser(fullform, header=None, module_name='rubi_object'):
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
    for i in temporary_variable_replacement:
        fullform = fullform.replace(i, temporary_variable_replacement[i])
    # Permanently rename these variables
    for i in permanent_variable_replacement:
        fullform = fullform.replace(i, permanent_variable_replacement[i])

    rules = []

    for i in parse_full_form(fullform): # separate all rules
        if i[0] == 'RuleDelayed':
            rules.append(i)

    result = downvalues_rules(rules, header).strip() + '\n'
    # Replace temporary variables by actual values
    for i in temporary_variable_replacement:
        result = result.replace(temporary_variable_replacement[i], i)

    return result

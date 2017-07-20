import sys
from sympy.external import import_module
matchpy = import_module("matchpy")

if not matchpy:
    #bin/test will not execute any tests now
    disabled = True

if sys.version_info[:2] < (3, 6):
    disabled = True

from sympy.core.symbol import symbols
from sympy.functions import log
from sympy import sqrt, simplify, S, atanh, hyper, I
from sympy.integrals.rubi.rubi import rubi_integrate

a, b, c, d, e, f, x, m, n, p = symbols('a b c d e f x m n p', real=True, imaginary=False)

def test_rubi_integrate():
    assert rubi_integrate(x, x) == x**2/2
    assert rubi_integrate(1/(x**2*(a + b*x)**2), x) == -b/(a**2*(a + b*x)) - 1/(a**2*x) - 2*b*log(x)/a**3 + 2*b*log(a + b*x)/a**3
    assert rubi_integrate(x**(S(5)/2)/(-a + b*x), x) == a*(a*(-2*sqrt(x)*hyper((1, 1/2), (3/2,), b*x/a)/b + 2*sqrt(x)/b)/b + 2*x**(3/2)/(3*b))/b + 2*x**(5/2)/(5*b)
    assert rubi_integrate((a*c - b*c*x)**2/(a + b*x)**2, x) == -4*a*b*c**2*(a/(b**2*(a + b*x)) + log(a + b*x)/b**2) + c**2*x
    assert rubi_integrate(x**6/(a + b*x)**2, x) == -a**6/(b**7*(a + b*x)) - 6*a**5*log(a + b*x)/b**7 + 5*a**4*x/b**6 - 2.0*a**3*x**2/b**5 + a**2*x**3/b**4 - a*x**4/(2*b**3) + x**5/(5*b**2)
    assert rubi_integrate(1/(x**2*(a + b*x)**2), x) == -b/(a**2*(a + b*x)) - 1/(a**2*x) - 2*b*log(x)/a**3 + 2*b*log(a + b*x)/a**3
    assert rubi_integrate((b*x)**m*(d*x + 2)**n, x) == 2**n*(b*x)**(m + 1)*hyper((-n, m + 1), (m + 2,), -d*x/2)/(b*(m + 1))
    assert rubi_integrate(x**a, x) == x**(a + S(1))/(a + S(1))
    assert rubi_integrate(x, x) == (S(1)/S(2))*x**S(2)
    assert rubi_integrate(S(1)/x, x) == log(x)
    assert rubi_integrate(a + S(1)/x, x) == a*x + log(x)
    assert rubi_integrate(a*x, x) == a*(S(1)/S(2))*x**S(2)
    assert rubi_integrate((a + b*x)**2/x**3, x) == -a**2/(2*x**2) - 2*a*b/x + b**2*log(x)
    assert rubi_integrate(a**3*x, x) == S(1)/S(2)*a**3*x**2
    assert rubi_integrate((a + b*x)**3/x**3, x) == -a**3/(2*x**2) - 3*a**2*b/x + 3*a*b**2*log(x) + b**3*x
    assert rubi_integrate(x**3*(a + b*x), x) == a*x**4/4 + b*x**5/5
    assert simplify(rubi_integrate(x**(S(4)/3)/(a + b*x)**2, x) - (-x**(S(4)/3)/(b*(a + b*x)) + S(4)*(-S(3)*x**(S(1)/3)*hyper((1, S(1)/3), (S(4)/3,), -b*x/a)/b + 3*x**(S(1)/3)/b)/(3*b))) == 0

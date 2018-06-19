from sympy.external import import_module
matchpy = import_module("matchpy")
from sympy.utilities.decorator import doctest_depends_on

if matchpy:
    from matchpy import Pattern, ReplacementRule, CustomConstraint
    from sympy.integrals.rubi.utility_function import (
        sympy_op_factory, Int, Sum, Set, With, Module, Scan, MapAnd, FalseQ,
        ZeroQ, NegativeQ, NonzeroQ, FreeQ, NFreeQ, List, Log, PositiveQ,
        PositiveIntegerQ, NegativeIntegerQ, IntegerQ, IntegersQ,
        ComplexNumberQ, PureComplexNumberQ, RealNumericQ, PositiveOrZeroQ,
        NegativeOrZeroQ, FractionOrNegativeQ, NegQ, Equal, Unequal, IntPart,
        FracPart, RationalQ, ProductQ, SumQ, NonsumQ, Subst, First, Rest,
        SqrtNumberQ, SqrtNumberSumQ, LinearQ, Sqrt, ArcCosh, Coefficient,
        Denominator, Hypergeometric2F1, Not, Simplify, FractionalPart,
        IntegerPart, AppellF1, EllipticPi, EllipticE, EllipticF, ArcTan,
        ArcCot, ArcCoth, ArcTanh, ArcSin, ArcSinh, ArcCos, ArcCsc, ArcSec,
        ArcCsch, ArcSech, Sinh, Tanh, Cosh, Sech, Csch, Coth, LessEqual, Less,
        Greater, GreaterEqual, FractionQ, IntLinearcQ, Expand, IndependentQ,
        PowerQ, IntegerPowerQ, PositiveIntegerPowerQ, FractionalPowerQ, AtomQ,
        ExpQ, LogQ, Head, MemberQ, TrigQ, SinQ, CosQ, TanQ, CotQ, SecQ, CscQ,
        Sin, Cos, Tan, Cot, Sec, Csc, HyperbolicQ, SinhQ, CoshQ, TanhQ, CothQ,
        SechQ, CschQ, InverseTrigQ, SinCosQ, SinhCoshQ, LeafCount, Numerator,
        NumberQ, NumericQ, Length, ListQ, Im, Re, InverseHyperbolicQ,
        InverseFunctionQ, TrigHyperbolicFreeQ, InverseFunctionFreeQ, RealQ,
        EqQ, FractionalPowerFreeQ, ComplexFreeQ, PolynomialQ, FactorSquareFree,
        PowerOfLinearQ, Exponent, QuadraticQ, LinearPairQ, BinomialParts,
        TrinomialParts, PolyQ, EvenQ, OddQ, PerfectSquareQ, NiceSqrtAuxQ,
        NiceSqrtQ, Together, PosAux, PosQ, CoefficientList, ReplaceAll,
        ExpandLinearProduct, GCD, ContentFactor, NumericFactor,
        NonnumericFactors, MakeAssocList, GensymSubst, KernelSubst,
        ExpandExpression, Apart, SmartApart, MatchQ,
        PolynomialQuotientRemainder, FreeFactors, NonfreeFactors,
        RemoveContentAux, RemoveContent, FreeTerms, NonfreeTerms,
        ExpandAlgebraicFunction, CollectReciprocals, ExpandCleanup,
        AlgebraicFunctionQ, Coeff, LeadTerm, RemainingTerms, LeadFactor,
        RemainingFactors, LeadBase, LeadDegree, Numer, Denom, hypergeom, Expon,
        MergeMonomials, PolynomialDivide, BinomialQ, TrinomialQ,
        GeneralizedBinomialQ, GeneralizedTrinomialQ, FactorSquareFreeList,
        PerfectPowerTest, SquareFreeFactorTest, RationalFunctionQ,
        RationalFunctionFactors, NonrationalFunctionFactors, Reverse,
        RationalFunctionExponents, RationalFunctionExpand, ExpandIntegrand,
        SimplerQ, SimplerSqrtQ, SumSimplerQ, BinomialDegree, TrinomialDegree,
        CancelCommonFactors, SimplerIntegrandQ, GeneralizedBinomialDegree,
        GeneralizedBinomialParts, GeneralizedTrinomialDegree,
        GeneralizedTrinomialParts, MonomialQ, MonomialSumQ,
        MinimumMonomialExponent, MonomialExponent, LinearMatchQ,
        PowerOfLinearMatchQ, QuadraticMatchQ, CubicMatchQ, BinomialMatchQ,
        TrinomialMatchQ, GeneralizedBinomialMatchQ, GeneralizedTrinomialMatchQ,
        QuotientOfLinearsMatchQ, PolynomialTermQ, PolynomialTerms,
        NonpolynomialTerms, PseudoBinomialParts, NormalizePseudoBinomial,
        PseudoBinomialPairQ, PseudoBinomialQ, PolynomialGCD, PolyGCD,
        AlgebraicFunctionFactors, NonalgebraicFunctionFactors,
        QuotientOfLinearsP, QuotientOfLinearsParts, QuotientOfLinearsQ,
        Flatten, Sort, AbsurdNumberQ, AbsurdNumberFactors,
        NonabsurdNumberFactors, SumSimplerAuxQ, Prepend, Drop,
        CombineExponents, FactorInteger, FactorAbsurdNumber,
        SubstForInverseFunction, SubstForFractionalPower,
        SubstForFractionalPowerOfQuotientOfLinears,
        FractionalPowerOfQuotientOfLinears, SubstForFractionalPowerQ,
        SubstForFractionalPowerAuxQ, FractionalPowerOfSquareQ,
        FractionalPowerSubexpressionQ, Apply, FactorNumericGcd,
        MergeableFactorQ, MergeFactor, MergeFactors, TrigSimplifyQ,
        TrigSimplify, TrigSimplifyRecur, Order, FactorOrder, Smallest,
        OrderedQ, MinimumDegree, PositiveFactors, Sign, NonpositiveFactors,
        PolynomialInAuxQ, PolynomialInQ, ExponentInAux, ExponentIn,
        PolynomialInSubstAux, PolynomialInSubst, Distrib, DistributeDegree,
        FunctionOfPower, DivideDegreesOfFactors, MonomialFactor, FullSimplify,
        FunctionOfLinearSubst, FunctionOfLinear, NormalizeIntegrand,
        NormalizeIntegrandAux, NormalizeIntegrandFactor,
        NormalizeIntegrandFactorBase, NormalizeTogether,
        NormalizeLeadTermSigns, AbsorbMinusSign, NormalizeSumFactors,
        SignOfFactor, NormalizePowerOfLinear, SimplifyIntegrand, SimplifyTerm,
        TogetherSimplify, SmartSimplify, SubstForExpn, ExpandToSum, UnifySum,
        UnifyTerms, UnifyTerm, CalculusQ, FunctionOfInverseLinear,
        PureFunctionOfSinhQ, PureFunctionOfTanhQ, PureFunctionOfCoshQ,
        IntegerQuotientQ, OddQuotientQ, EvenQuotientQ, FindTrigFactor,
        FunctionOfSinhQ, FunctionOfCoshQ, OddHyperbolicPowerQ, FunctionOfTanhQ,
        FunctionOfTanhWeight, FunctionOfHyperbolicQ, SmartNumerator,
        SmartDenominator, SubstForAux, ActivateTrig, ExpandTrig, TrigExpand,
        SubstForTrig, SubstForHyperbolic, InertTrigFreeQ, LCM,
        SubstForFractionalPowerOfLinear, FractionalPowerOfLinear,
        InverseFunctionOfLinear, InertTrigQ, InertReciprocalQ, DeactivateTrig,
        FixInertTrigFunction, DeactivateTrigAux, PowerOfInertTrigSumQ,
        PiecewiseLinearQ, KnownTrigIntegrandQ, KnownSineIntegrandQ,
        KnownTangentIntegrandQ, KnownCotangentIntegrandQ,
        KnownSecantIntegrandQ, TryPureTanSubst, TryTanhSubst, TryPureTanhSubst,
        AbsurdNumberGCD, AbsurdNumberGCDList, ExpandTrigExpand,
        ExpandTrigReduce, ExpandTrigReduceAux, NormalizeTrig, TrigToExp,
        ExpandTrigToExp, TrigReduce, FunctionOfTrig, AlgebraicTrigFunctionQ,
        FunctionOfHyperbolic, FunctionOfQ, FunctionOfExpnQ, PureFunctionOfSinQ,
        PureFunctionOfCosQ, PureFunctionOfTanQ, PureFunctionOfCotQ,
        FunctionOfCosQ, FunctionOfSinQ, OddTrigPowerQ, FunctionOfTanQ,
        FunctionOfTanWeight, FunctionOfTrigQ, FunctionOfDensePolynomialsQ,
        FunctionOfLog, PowerVariableExpn, PowerVariableDegree,
        PowerVariableSubst, EulerIntegrandQ, FunctionOfSquareRootOfQuadratic,
        SquareRootOfQuadraticSubst, Divides, EasyDQ, ProductOfLinearPowersQ,
        Rt, NthRoot, AtomBaseQ, SumBaseQ, NegSumBaseQ, AllNegTermQ,
        SomeNegTermQ, TrigSquareQ, RtAux, TrigSquare, IntSum, IntTerm, Map2,
        ConstantFactor, SameQ, ReplacePart, CommonFactors,
        MostMainFactorPosition, FunctionOfExponentialQ, FunctionOfExponential,
        FunctionOfExponentialFunction, FunctionOfExponentialFunctionAux,
        FunctionOfExponentialTest, FunctionOfExponentialTestAux, stdev,
        rubi_test, If, IntQuadraticQ, IntBinomialQ, RectifyTangent,
        RectifyCotangent, Inequality, Condition, Simp, SimpHelp, SplitProduct,
        SplitSum, SubstFor, SubstForAux, FresnelS, FresnelC, Erfc, Erfi, Gamma,
        FunctionOfTrigOfLinearQ, ElementaryFunctionQ, Complex, UnsameQ,
        _SimpFixFactor, SimpFixFactor, _FixSimplify, FixSimplify,
        _SimplifyAntiderivativeSum, SimplifyAntiderivativeSum,
        _SimplifyAntiderivative, SimplifyAntiderivative, _TrigSimplifyAux,
        TrigSimplifyAux, Cancel, Part, PolyLog, D, Dist, Sum_doit, PolynomialQuotient, Floor,
        PolynomialRemainder, Factor, UtilityOperator
    )
    from matchpy import is_match
    from sympy import Integral, S, sqrt, And, Or, Integer, Float, Mod
    from sympy.integrals.rubi.symbol import WC
    from sympy.core.symbol import symbols, Symbol
    from sympy.functions import (log, sin, cos, tan, cot, csc, sec, sqrt, erf, exp, log)
    from sympy.functions.elementary.hyperbolic import (acosh, asinh, atanh, acoth, acsch, asech, cosh, sinh, tanh, coth, sech, csch)
    from sympy.functions.elementary.trigonometric import (atan, acsc, asin, acot, acos, asec)
    from sympy import pi as Pi


    A_, B_, C_, F_, G_, H_, a_, b_, c_, d_, e_, f_, g_, h_, i_, j_, k_, l_, m_, n_, p_, q_, r_, t_, u_, v_, s_, w_, x_, y_, z_ = [WC(i) for i in 'ABCFGHabcdefghijklmnpqrtuvswxyz']
    a1_, a2_, b1_, b2_, c1_, c2_, d1_, d2_, n1_, n2_, e1_, e2_, f1_, f2_, g1_, g2_, n1_, n2_, n3_, Pq_, Pm_, Px_, Qm_, Qr_, Qx_, jn_, mn_, non2_, RFx_, RGx_ = [WC(i) for i in ['a1', 'a2', 'b1', 'b2', 'c1', 'c2', 'd1', 'd2', 'n1', 'n2', 'e1', 'e2', 'f1', 'f2', 'g1', 'g2', 'n1', 'n2', 'n3', 'Pq', 'Pm', 'Px', 'Qm', 'Qr', 'Qx', 'jn', 'mn', 'non2', 'RFx', 'RGx']]

    from sympy import Integral, S, sqrt, And, Or, Integer, Float, Mod, symbols
    C = symbols('C_1')


def cons_f1(a):
    return ZeroQ(a)

cons1 = CustomConstraint(cons_f1)

def cons_f2(a, x):
    return FreeQ(a, x)

cons2 = CustomConstraint(cons_f2)

def cons_f3(b, x):
    return FreeQ(b, x)

cons3 = CustomConstraint(cons_f3)

def cons_f4(n, x):
    return FreeQ(n, x)

cons4 = CustomConstraint(cons_f4)

def cons_f5(p, x):
    return FreeQ(p, x)

cons5 = CustomConstraint(cons_f5)

def cons_f6(j, n):
    return ZeroQ(j - S(2)*n)

cons6 = CustomConstraint(cons_f6)

def cons_f7(c, x):
    return FreeQ(c, x)

cons7 = CustomConstraint(cons_f7)

def cons_f8(b):
    return ZeroQ(b)

cons8 = CustomConstraint(cons_f8)

def cons_f9(c):
    return ZeroQ(c)

cons9 = CustomConstraint(cons_f9)

def cons_f10(x, v):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return NFreeQ(v, x)

cons10 = CustomConstraint(cons_f10)

def cons_f11(x, Pm):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return PolyQ(Pm, x)

cons11 = CustomConstraint(cons_f11)

def cons_f12(p):
    return Not(RationalQ(p))

cons12 = CustomConstraint(cons_f12)

def cons_f13(p):
    return RationalQ(p)

cons13 = CustomConstraint(cons_f13)

def cons_f14(a, x, c, b):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, b, c), x)

cons14 = CustomConstraint(cons_f14)

def cons_f15(a):
    return EqQ(a**S(2), S(1))

cons15 = CustomConstraint(cons_f15)

def cons_f16(u):
    return SumQ(u)

cons16 = CustomConstraint(cons_f16)

def cons_f17(m):
    return IntegerQ(m)

cons17 = CustomConstraint(cons_f17)

def cons_f18(m):
    return Not(IntegerQ(m))

cons18 = CustomConstraint(cons_f18)

def cons_f19(n):
    return PositiveIntegerQ(n + S(1)/2)

cons19 = CustomConstraint(cons_f19)

def cons_f20(n, m):
    return IntegerQ(m + n)

cons20 = CustomConstraint(cons_f20)

def cons_f21(m, x):
    return FreeQ(m, x)

cons21 = CustomConstraint(cons_f21)

def cons_f22(n):
    return NegativeIntegerQ(n + S(-1)/2)

cons22 = CustomConstraint(cons_f22)

def cons_f23(n):
    return Not(IntegerQ(n))

cons23 = CustomConstraint(cons_f23)

def cons_f24(n, m):
    return Not(IntegerQ(m + n))

cons24 = CustomConstraint(cons_f24)

def cons_f25(a, d, c, b):
    return ZeroQ(-a*d + b*c)

cons25 = CustomConstraint(cons_f25)

def cons_f26(a, n, b, x, d, c):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Or(Not(IntegerQ(n)), SimplerQ(c + d*x, a + b*x))

cons26 = CustomConstraint(cons_f26)

def cons_f27(d, x):
    return FreeQ(d, x)

cons27 = CustomConstraint(cons_f27)

def cons_f28(d, b):
    return PositiveQ(b/d)

cons28 = CustomConstraint(cons_f28)

def cons_f29(n, m):
    return Not(Or(IntegerQ(m), IntegerQ(n)))

cons29 = CustomConstraint(cons_f29)

def cons_f30(d, n, m, b):
    return Not(Or(IntegerQ(m), IntegerQ(n), PositiveQ(b/d)))

cons30 = CustomConstraint(cons_f30)

def cons_f31(m):
    return RationalQ(m)

cons31 = CustomConstraint(cons_f31)

def cons_f32(m):
    return LessEqual(m, S(-1))

cons32 = CustomConstraint(cons_f32)

def cons_f33(a, A, b, C, B):
    return ZeroQ(A*b**S(2) - B*a*b + C*a**S(2))

cons33 = CustomConstraint(cons_f33)

def cons_f34(A, x):
    return FreeQ(A, x)

cons34 = CustomConstraint(cons_f34)

def cons_f35(B, x):
    return FreeQ(B, x)

cons35 = CustomConstraint(cons_f35)

def cons_f36(C, x):
    return FreeQ(C, x)

cons36 = CustomConstraint(cons_f36)

def cons_f37(n, q):
    return ZeroQ(n + q)

cons37 = CustomConstraint(cons_f37)

def cons_f38(p):
    return IntegerQ(p)

cons38 = CustomConstraint(cons_f38)

def cons_f39(a, d, c, b):
    return ZeroQ(a*c - b*d)

cons39 = CustomConstraint(cons_f39)

def cons_f40(n, m):
    return Not(And(IntegerQ(m), NegQ(n)))

cons40 = CustomConstraint(cons_f40)

def cons_f41(p, m):
    return ZeroQ(m + p)

cons41 = CustomConstraint(cons_f41)

def cons_f42(a, d, c, b):
    return ZeroQ(a**S(2)*d + b**S(2)*c)

cons42 = CustomConstraint(cons_f42)

def cons_f43(a):
    return PositiveQ(a)

cons43 = CustomConstraint(cons_f43)

def cons_f44(d):
    return NegativeQ(d)

cons44 = CustomConstraint(cons_f44)

def cons_f45(a, c, b):
    return ZeroQ(-S(4)*a*c + b**S(2))

cons45 = CustomConstraint(cons_f45)

def cons_f46(n, n2):
    return ZeroQ(-S(2)*n + n2)

cons46 = CustomConstraint(cons_f46)

def cons_f47(d, e, c, b):
    return ZeroQ(-b*e + S(2)*c*d)

cons47 = CustomConstraint(cons_f47)

def cons_f48(e, x):
    return FreeQ(e, x)

cons48 = CustomConstraint(cons_f48)

def cons_f49(p, q):
    return PosQ(-p + q)

cons49 = CustomConstraint(cons_f49)

def cons_f50(q, x):
    return FreeQ(q, x)

cons50 = CustomConstraint(cons_f50)

def cons_f51(p, r):
    return PosQ(-p + r)

cons51 = CustomConstraint(cons_f51)

def cons_f52(r, x):
    return FreeQ(r, x)

cons52 = CustomConstraint(cons_f52)

def cons_f53(n, m):
    return ZeroQ(m - n + S(1))

cons53 = CustomConstraint(cons_f53)

def cons_f54(p):
    return NonzeroQ(p + S(1))

cons54 = CustomConstraint(cons_f54)

def cons_f55(a2, a1, b2, b1):
    return ZeroQ(a1*b2 + a2*b1)

cons55 = CustomConstraint(cons_f55)

def cons_f56(n, m):
    return ZeroQ(m - S(2)*n + S(1))

cons56 = CustomConstraint(cons_f56)

def cons_f57(a1, x):
    return FreeQ(a1, x)

cons57 = CustomConstraint(cons_f57)

def cons_f58(b1, x):
    return FreeQ(b1, x)

cons58 = CustomConstraint(cons_f58)

def cons_f59(a2, x):
    return FreeQ(a2, x)

cons59 = CustomConstraint(cons_f59)

def cons_f60(b2, x):
    return FreeQ(b2, x)

cons60 = CustomConstraint(cons_f60)

def cons_f61(x, Qm):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return PolyQ(Qm, x)

cons61 = CustomConstraint(cons_f61)

def cons_f62(m):
    return PositiveIntegerQ(m)

cons62 = CustomConstraint(cons_f62)

def cons_f63(p):
    return NegativeIntegerQ(p)

cons63 = CustomConstraint(cons_f63)

def cons_f64(x, Pq):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return PolyQ(Pq, x)

cons64 = CustomConstraint(cons_f64)

def cons_f65(Qr, x):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return PolyQ(Qr, x)

cons65 = CustomConstraint(cons_f65)

def cons_f66(m):
    return NonzeroQ(m + S(1))

cons66 = CustomConstraint(cons_f66)

def cons_f67(a, x, b):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, b), x)

cons67 = CustomConstraint(cons_f67)

def cons_f68(x, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return LinearQ(u, x)

cons68 = CustomConstraint(cons_f68)

def cons_f69(x, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return NonzeroQ(u - x)

cons69 = CustomConstraint(cons_f69)

def cons_f70(a, d, c, b):
    return ZeroQ(a*d + b*c)

cons70 = CustomConstraint(cons_f70)

def cons_f71(a, d, c, b):
    return NonzeroQ(-a*d + b*c)

cons71 = CustomConstraint(cons_f71)

def cons_f72(n, m):
    return ZeroQ(m + n + S(2))

cons72 = CustomConstraint(cons_f72)

def cons_f73(m):
    return PositiveIntegerQ(m + S(1)/2)

cons73 = CustomConstraint(cons_f73)

def cons_f74(m):
    return NegativeIntegerQ(m + S(3)/2)

cons74 = CustomConstraint(cons_f74)

def cons_f75(a, c, m):
    return Or(IntegerQ(m), And(PositiveQ(a), PositiveQ(c)))

cons75 = CustomConstraint(cons_f75)

def cons_f76(a, c):
    return ZeroQ(a + c)

cons76 = CustomConstraint(cons_f76)

def cons_f77(m):
    return Not(IntegerQ(S(2)*m))

cons77 = CustomConstraint(cons_f77)

def cons_f78(a, d, c, b):
    return PosQ(b*d/(a*c))

cons78 = CustomConstraint(cons_f78)

def cons_f79(m):
    return IntegerQ(m + S(1)/2)

cons79 = CustomConstraint(cons_f79)

def cons_f80(n):
    return IntegerQ(n + S(1)/2)

cons80 = CustomConstraint(cons_f80)

def cons_f81(n, m):
    return Less(S(0), m, n)

cons81 = CustomConstraint(cons_f81)

def cons_f82(n, m):
    return Less(m, n, S(0))

cons82 = CustomConstraint(cons_f82)

def cons_f83(m, n, c):
    return Or(Not(IntegerQ(n)), And(ZeroQ(c), LessEqual(S(7)*m + S(4)*n, S(0))), Less(S(9)*m + S(5)*n + S(5), S(0)), Greater(m + n + S(2), S(0)))

cons83 = CustomConstraint(cons_f83)

def cons_f84(m):
    return NegativeIntegerQ(m)

cons84 = CustomConstraint(cons_f84)

def cons_f85(n):
    return IntegerQ(n)

cons85 = CustomConstraint(cons_f85)

def cons_f86(n, m):
    return Not(And(PositiveIntegerQ(n), Less(m + n + S(2), S(0))))

cons86 = CustomConstraint(cons_f86)

def cons_f87(n):
    return RationalQ(n)

cons87 = CustomConstraint(cons_f87)

def cons_f88(n):
    return Greater(n, S(0))

cons88 = CustomConstraint(cons_f88)

def cons_f89(n):
    return Less(n, S(-1))

cons89 = CustomConstraint(cons_f89)

def cons_f90(a, d, c, b):
    return PosQ((-a*d + b*c)/b)

cons90 = CustomConstraint(cons_f90)

def cons_f91(a, d, c, b):
    return NegQ((-a*d + b*c)/b)

cons91 = CustomConstraint(cons_f91)

def cons_f92(n):
    return Less(S(-1), n, S(0))

cons92 = CustomConstraint(cons_f92)

def cons_f93(n, m):
    return RationalQ(m, n)

cons93 = CustomConstraint(cons_f93)

def cons_f94(m):
    return Less(m, S(-1))

cons94 = CustomConstraint(cons_f94)

def cons_f95(n, m):
    return Not(And(IntegerQ(n), Not(IntegerQ(m))))

cons95 = CustomConstraint(cons_f95)

def cons_f96(n, m):
    return Not(And(IntegerQ(m + n), LessEqual(m + n + S(2), S(0)), Or(FractionQ(m), GreaterEqual(m + S(2)*n + S(1), S(0)))))

cons96 = CustomConstraint(cons_f96)

def cons_f97(a, n, b, x, d, m, c):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return IntLinearcQ(a, b, c, d, m, n, x)

cons97 = CustomConstraint(cons_f97)

def cons_f98(a, m, n, c):
    return Not(And(Less(n, S(-1)), Or(ZeroQ(a), And(NonzeroQ(c), Less(m, n), IntegerQ(n)))))

cons98 = CustomConstraint(cons_f98)

def cons_f99(n, m):
    return Unequal(m + n + S(1), S(0))

cons99 = CustomConstraint(cons_f99)

def cons_f100(n, m):
    return Not(And(PositiveIntegerQ(m), Or(Not(IntegerQ(n)), Less(S(0), m, n))))

cons100 = CustomConstraint(cons_f100)

def cons_f101(n, m):
    return Not(And(IntegerQ(m + n), Less(m + n + S(2), S(0))))

cons101 = CustomConstraint(cons_f101)

def cons_f102(d, b):
    return ZeroQ(b + d)

cons102 = CustomConstraint(cons_f102)

def cons_f103(a, c):
    return PositiveQ(a + c)

cons103 = CustomConstraint(cons_f103)

def cons_f104(a, d, c, b):
    return PositiveQ(-a*d + b*c)

cons104 = CustomConstraint(cons_f104)

def cons_f105(b):
    return PositiveQ(b)

cons105 = CustomConstraint(cons_f105)

def cons_f106(d, b):
    return ZeroQ(b - d)

cons106 = CustomConstraint(cons_f106)

def cons_f107(m):
    return Less(S(-1), m, S(0))

cons107 = CustomConstraint(cons_f107)

def cons_f108(m):
    return LessEqual(S(3), Denominator(m), S(4))

cons108 = CustomConstraint(cons_f108)

def cons_f109(d, b):
    return PosQ(d/b)

cons109 = CustomConstraint(cons_f109)

def cons_f110(d, b):
    return NegQ(d/b)

cons110 = CustomConstraint(cons_f110)

def cons_f111(n, m):
    return Equal(m + n + S(1), S(0))

cons111 = CustomConstraint(cons_f111)

def cons_f112(n, m):
    return LessEqual(Denominator(n), Denominator(m))

cons112 = CustomConstraint(cons_f112)

def cons_f113(n, m):
    return NegativeIntegerQ(m + n + S(2))

cons113 = CustomConstraint(cons_f113)

def cons_f114(n, m):
    return Or(SumSimplerQ(m, S(1)), Not(SumSimplerQ(n, S(1))))

cons114 = CustomConstraint(cons_f114)

def cons_f115(d, n, c, b):
    return Or(IntegerQ(n), And(PositiveQ(c), Not(And(ZeroQ(n + S(1)/2), ZeroQ(c**S(2) - d**S(2)), PositiveQ(-d/(b*c))))))

cons115 = CustomConstraint(cons_f115)

def cons_f116(d, c, m, b):
    return Or(IntegerQ(m), PositiveQ(-d/(b*c)))

cons116 = CustomConstraint(cons_f116)

def cons_f117(c):
    return Not(PositiveQ(c))

cons117 = CustomConstraint(cons_f117)

def cons_f118(d, c, b):
    return Not(PositiveQ(-d/(b*c)))

cons118 = CustomConstraint(cons_f118)

def cons_f119(d, c, n, m):
    return Or(And(RationalQ(m), Not(And(ZeroQ(n + S(1)/2), ZeroQ(c**S(2) - d**S(2))))), Not(RationalQ(n)))

cons119 = CustomConstraint(cons_f119)

def cons_f120(a, d, c, b):
    return PositiveQ(b/(-a*d + b*c))

cons120 = CustomConstraint(cons_f120)

def cons_f121(a, n, b, d, c, m):
    return Or(RationalQ(m), Not(And(RationalQ(n), PositiveQ(-d/(-a*d + b*c)))))

cons121 = CustomConstraint(cons_f121)

def cons_f122(n, m):
    return Or(RationalQ(m), Not(SimplerQ(n + S(1), m + S(1))))

cons122 = CustomConstraint(cons_f122)

def cons_f123(x, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return NonzeroQ(Coefficient(u, x, S(0)))

cons123 = CustomConstraint(cons_f123)

def cons_f124(n, m):
    return ZeroQ(m - n)

cons124 = CustomConstraint(cons_f124)

def cons_f125(f, x):
    return FreeQ(f, x)

cons125 = CustomConstraint(cons_f125)

def cons_f126(p, n):
    return NonzeroQ(n + p + S(2))

cons126 = CustomConstraint(cons_f126)

def cons_f127(a, n, f, b, d, c, p, e):
    return ZeroQ(a*d*f*(n + p + S(2)) - b*(c*f*(p + S(1)) + d*e*(n + S(1))))

cons127 = CustomConstraint(cons_f127)

def cons_f128(p):
    return PositiveIntegerQ(p)

cons128 = CustomConstraint(cons_f128)

def cons_f129(a, f, e, b):
    return ZeroQ(a*f + b*e)

cons129 = CustomConstraint(cons_f129)

def cons_f130(p, n):
    return Not(And(NegativeIntegerQ(n + p + S(2)), Greater(n + S(2)*p, S(0))))

cons130 = CustomConstraint(cons_f130)

def cons_f131(p, n):
    return Or(NonzeroQ(n + S(1)), Equal(p, S(1)))

cons131 = CustomConstraint(cons_f131)

def cons_f132(a, f, e, b):
    return NonzeroQ(a*f + b*e)

cons132 = CustomConstraint(cons_f132)

def cons_f133(a, n, b, f, d, p, e):
    return Or(Not(IntegerQ(n)), Less(S(5)*n + S(9)*p, S(0)), GreaterEqual(n + p + S(1), S(0)), And(GreaterEqual(n + p + S(2), S(0)), RationalQ(a, b, d, e, f)))

cons133 = CustomConstraint(cons_f133)

def cons_f134(a, n, b, f, d, c, p, e):
    return Or(NegativeIntegerQ(n, p), ZeroQ(p + S(-1)), And(PositiveIntegerQ(p), Or(Not(IntegerQ(n)), LessEqual(S(5)*n + S(9)*p + S(10), S(0)), GreaterEqual(n + p + S(1), S(0)), And(GreaterEqual(n + p + S(2), S(0)), RationalQ(a, b, c, d, e, f)))))

cons134 = CustomConstraint(cons_f134)

def cons_f135(p, n):
    return ZeroQ(n + p + S(2))

cons135 = CustomConstraint(cons_f135)

def cons_f136(p, n):
    return Not(And(SumSimplerQ(n, S(1)), Not(SumSimplerQ(p, S(1)))))

cons136 = CustomConstraint(cons_f136)

def cons_f137(p):
    return Less(p, S(-1))

cons137 = CustomConstraint(cons_f137)

def cons_f138(p, n, e, c):
    return Or(Not(And(RationalQ(n), Less(n, S(-1)))), IntegerQ(p), Not(Or(IntegerQ(n), Not(Or(ZeroQ(e), Not(Or(ZeroQ(c), Less(p, n))))))))

cons138 = CustomConstraint(cons_f138)

def cons_f139(p):
    return SumSimplerQ(p, S(1))

cons139 = CustomConstraint(cons_f139)

def cons_f140(p, n):
    return NonzeroQ(n + p + S(3))

cons140 = CustomConstraint(cons_f140)

def cons_f141(a, n, f, b, d, c, p, e):
    return ZeroQ(-b*(c*f*(p + S(1)) + d*e*(n + S(1)))*(a*d*f*(n + p + S(4)) - b*(c*f*(p + S(2)) + d*e*(n + S(2)))) + d*f*(a**S(2)*d*f*(n + p + S(3)) - b*(a*(c*f*(p + S(1)) + d*e*(n + S(1))) + b*c*e))*(n + p + S(2)))

cons141 = CustomConstraint(cons_f141)

def cons_f142(n, m):
    return ZeroQ(m - n + S(-1))

cons142 = CustomConstraint(cons_f142)

def cons_f143(m):
    return Not(PositiveIntegerQ(m))

cons143 = CustomConstraint(cons_f143)

def cons_f144(p, n, m):
    return NonzeroQ(m + n + p + S(2))

cons144 = CustomConstraint(cons_f144)

def cons_f145(p):
    return Less(S(0), p, S(1))

cons145 = CustomConstraint(cons_f145)

def cons_f146(p):
    return Greater(p, S(1))

cons146 = CustomConstraint(cons_f146)

def cons_f147(p):
    return Not(IntegerQ(p))

cons147 = CustomConstraint(cons_f147)

def cons_f148(n):
    return PositiveIntegerQ(n)

cons148 = CustomConstraint(cons_f148)

def cons_f149(p):
    return FractionQ(p)

cons149 = CustomConstraint(cons_f149)

def cons_f150(n, m):
    return IntegersQ(m, n)

cons150 = CustomConstraint(cons_f150)

def cons_f151(p, n, m):
    return Or(IntegerQ(p), And(Greater(m, S(0)), GreaterEqual(n, S(-1))))

cons151 = CustomConstraint(cons_f151)

def cons_f152(p, n):
    return Or(And(RationalQ(n), Less(n, S(-1))), And(ZeroQ(n + p + S(3)), NonzeroQ(n + S(1)), Or(SumSimplerQ(n, S(1)), Not(SumSimplerQ(p, S(1))))))

cons152 = CustomConstraint(cons_f152)

def cons_f153(a, b, f, d, x, c, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, b, c, d, e, f), x)

cons153 = CustomConstraint(cons_f153)

def cons_f154(a, f, b, d, c, e):
    return ZeroQ(S(2)*b*d*e - f*(a*d + b*c))

cons154 = CustomConstraint(cons_f154)

def cons_f155(n, m):
    return ZeroQ(m + n + S(1))

cons155 = CustomConstraint(cons_f155)

def cons_f156(a, b, x, d, c):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return SimplerQ(a + b*x, c + d*x)

cons156 = CustomConstraint(cons_f156)

def cons_f157(p, n, m):
    return ZeroQ(m + n + p + S(2))

cons157 = CustomConstraint(cons_f157)

def cons_f158(p, m):
    return Not(And(SumSimplerQ(p, S(1)), Not(SumSimplerQ(m, S(1)))))

cons158 = CustomConstraint(cons_f158)

def cons_f159(p, n, m):
    return ZeroQ(m + n + p + S(3))

cons159 = CustomConstraint(cons_f159)

def cons_f160(a, n, b, f, d, m, c, p, e):
    return ZeroQ(a*d*f*(m + S(1)) + b*c*f*(n + S(1)) + b*d*e*(p + S(1)))

cons160 = CustomConstraint(cons_f160)

def cons_f161(m):
    return Or(And(RationalQ(m), Less(m, S(-1))), SumSimplerQ(m, S(1)))

cons161 = CustomConstraint(cons_f161)

def cons_f162(p, n, m):
    return RationalQ(m, n, p)

cons162 = CustomConstraint(cons_f162)

def cons_f163(p):
    return Greater(p, S(0))

cons163 = CustomConstraint(cons_f163)

def cons_f164(p, n, m):
    return Or(IntegersQ(S(2)*m, S(2)*n, S(2)*p), IntegersQ(m, n + p), IntegersQ(p, m + n))

cons164 = CustomConstraint(cons_f164)

def cons_f165(n):
    return Greater(n, S(1))

cons165 = CustomConstraint(cons_f165)

def cons_f166(m):
    return Greater(m, S(1))

cons166 = CustomConstraint(cons_f166)

def cons_f167(p, n, m):
    return NonzeroQ(m + n + p + S(1))

cons167 = CustomConstraint(cons_f167)

def cons_f168(m):
    return Greater(m, S(0))

cons168 = CustomConstraint(cons_f168)

def cons_f169(p, n, m):
    return Or(IntegersQ(S(2)*m, S(2)*n, S(2)*p), Or(IntegersQ(m, n + p), IntegersQ(p, m + n)))

cons169 = CustomConstraint(cons_f169)

def cons_f170(p, n, m):
    return IntegersQ(S(2)*m, S(2)*n, S(2)*p)

cons170 = CustomConstraint(cons_f170)

def cons_f171(p, n):
    return Or(IntegerQ(n), IntegersQ(S(2)*n, S(2)*p))

cons171 = CustomConstraint(cons_f171)

def cons_f172(n, m):
    return PositiveIntegerQ(m + n + S(1))

cons172 = CustomConstraint(cons_f172)

def cons_f173(n, m):
    return Or(And(RationalQ(m), Greater(m, S(0))), And(Not(RationalQ(m)), Or(SumSimplerQ(m, S(-1)), Not(SumSimplerQ(n, S(-1))))))

cons173 = CustomConstraint(cons_f173)

def cons_f174(d, e, c, f):
    return PositiveQ(-f/(-c*f + d*e))

cons174 = CustomConstraint(cons_f174)

def cons_f175(d, e, c, f):
    return Not(PositiveQ(-f/(-c*f + d*e)))

cons175 = CustomConstraint(cons_f175)

def cons_f176(d, e, c, f):
    return NonzeroQ(-c*f + d*e)

cons176 = CustomConstraint(cons_f176)

def cons_f177(c):
    return PositiveQ(c)

cons177 = CustomConstraint(cons_f177)

def cons_f178(e):
    return PositiveQ(e)

cons178 = CustomConstraint(cons_f178)

def cons_f179(d, b):
    return Not(NegativeQ(-b/d))

cons179 = CustomConstraint(cons_f179)

def cons_f180(d, b):
    return NegativeQ(-b/d)

cons180 = CustomConstraint(cons_f180)

def cons_f181(e, c):
    return Not(And(PositiveQ(c), PositiveQ(e)))

cons181 = CustomConstraint(cons_f181)

def cons_f182(a, f, e, b):
    return PositiveQ(b/(-a*f + b*e))

cons182 = CustomConstraint(cons_f182)

def cons_f183(a, d, c, b):
    return Not(NegativeQ(-(-a*d + b*c)/d))

cons183 = CustomConstraint(cons_f183)

def cons_f184(a, b, x, d, f, c, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(And(SimplerQ(c + d*x, a + b*x), PositiveQ(-d/(-a*d + b*c)), PositiveQ(d/(-c*f + d*e)), Not(NegativeQ((-a*d + b*c)/b))))

cons184 = CustomConstraint(cons_f184)

def cons_f185(a, b, f, d, c, e):
    return Not(And(PositiveQ(b/(-a*d + b*c)), PositiveQ(b/(-a*f + b*e))))

cons185 = CustomConstraint(cons_f185)

def cons_f186(d, f, b):
    return Or(PositiveQ(-b/d), NegativeQ(-b/f))

cons186 = CustomConstraint(cons_f186)

def cons_f187(d, f, b):
    return Or(PosQ(-b/d), NegQ(-b/f))

cons187 = CustomConstraint(cons_f187)

def cons_f188(a, f, x, b, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return SimplerQ(a + b*x, e + f*x)

cons188 = CustomConstraint(cons_f188)

def cons_f189(a, b, f, d, c, e):
    return Or(PositiveQ(-(-a*d + b*c)/d), NegativeQ(-(-a*f + b*e)/f))

cons189 = CustomConstraint(cons_f189)

def cons_f190(a, b, f, d, c, e):
    return Or(PosQ(-(-a*d + b*c)/d), NegQ(-(-a*f + b*e)/f))

cons190 = CustomConstraint(cons_f190)

def cons_f191(a, f, b, d, c, e):
    return ZeroQ(-a*d*f - b*c*f + S(2)*b*d*e)

cons191 = CustomConstraint(cons_f191)

def cons_f192(n, m):
    return PositiveIntegerQ(m - n)

cons192 = CustomConstraint(cons_f192)

def cons_f193(n, m):
    return Or(PositiveIntegerQ(m), NegativeIntegerQ(m, n))

cons193 = CustomConstraint(cons_f193)

def cons_f194(p, n, m):
    return NegativeIntegerQ(m + n + p + S(2))

cons194 = CustomConstraint(cons_f194)

def cons_f195(p, n, m):
    return Or(SumSimplerQ(m, S(1)), And(Not(And(NonzeroQ(n + S(1)), SumSimplerQ(n, S(1)))), Not(And(NonzeroQ(p + S(1)), SumSimplerQ(p, S(1))))))

cons195 = CustomConstraint(cons_f195)

def cons_f196(n):
    return NegativeIntegerQ(n)

cons196 = CustomConstraint(cons_f196)

def cons_f197(p, e):
    return Or(IntegerQ(p), PositiveQ(e))

cons197 = CustomConstraint(cons_f197)

def cons_f198(d, c, b):
    return PositiveQ(-d/(b*c))

cons198 = CustomConstraint(cons_f198)

def cons_f199(f, d, c, p, e):
    return Or(IntegerQ(p), PositiveQ(d/(-c*f + d*e)))

cons199 = CustomConstraint(cons_f199)

def cons_f200(a, b, x, d, c):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(And(PositiveQ(d/(a*d - b*c)), SimplerQ(c + d*x, a + b*x)))

cons200 = CustomConstraint(cons_f200)

def cons_f201(a, d, c, b):
    return Not(PositiveQ(b/(-a*d + b*c)))

cons201 = CustomConstraint(cons_f201)

def cons_f202(a, b, x, d, c):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(SimplerQ(c + d*x, a + b*x))

cons202 = CustomConstraint(cons_f202)

def cons_f203(a, b, f, d, x, c, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(And(PositiveQ(d/(a*d - b*c)), PositiveQ(d/(-c*f + d*e)), SimplerQ(c + d*x, a + b*x)))

cons203 = CustomConstraint(cons_f203)

def cons_f204(a, b, f, d, x, c, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(And(PositiveQ(f/(a*f - b*e)), PositiveQ(f/(c*f - d*e)), SimplerQ(e + f*x, a + b*x)))

cons204 = CustomConstraint(cons_f204)

def cons_f205(a, f, e, b):
    return Not(PositiveQ(b/(-a*f + b*e)))

cons205 = CustomConstraint(cons_f205)

def cons_f206(a, b, x, f, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(SimplerQ(e + f*x, a + b*x))

cons206 = CustomConstraint(cons_f206)

def cons_f207(n, m):
    return Or(PositiveIntegerQ(m), IntegersQ(m, n))

cons207 = CustomConstraint(cons_f207)

def cons_f208(g, x):
    return FreeQ(g, x)

cons208 = CustomConstraint(cons_f208)

def cons_f209(h, x):
    return FreeQ(h, x)

cons209 = CustomConstraint(cons_f209)

def cons_f210(n, m):
    return Not(And(SumSimplerQ(n, S(1)), Not(SumSimplerQ(m, S(1)))))

cons210 = CustomConstraint(cons_f210)

def cons_f211(n, m):
    return Or(And(RationalQ(m), Less(m, S(-2))), And(ZeroQ(m + n + S(3)), Not(And(RationalQ(n), Less(n, S(-2))))))

cons211 = CustomConstraint(cons_f211)

def cons_f212(m):
    return Or(And(RationalQ(m), Inequality(S(-2), LessEqual, m, Less, S(-1))), SumSimplerQ(m, S(1)))

cons212 = CustomConstraint(cons_f212)

def cons_f213(n, m):
    return NonzeroQ(m + n + S(3))

cons213 = CustomConstraint(cons_f213)

def cons_f214(n, m):
    return NonzeroQ(m + n + S(2))

cons214 = CustomConstraint(cons_f214)

def cons_f215(p, n, m):
    return Or(IntegersQ(m, n, p), PositiveIntegerQ(n, p))

cons215 = CustomConstraint(cons_f215)

def cons_f216(a, b, f, d, g, x, h, c, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, b, c, d, e, f, g, h), x)

cons216 = CustomConstraint(cons_f216)

def cons_f217(a, n, b, f, d, g, x, h, c, p, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, b, c, d, e, f, g, h, n, p), x)

cons217 = CustomConstraint(cons_f217)

def cons_f218(f, x, d, c, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return SimplerQ(c + d*x, e + f*x)

cons218 = CustomConstraint(cons_f218)

def cons_f219(p, n, m):
    return Or(SumSimplerQ(m, S(1)), And(Not(SumSimplerQ(n, S(1))), Not(SumSimplerQ(p, S(1)))))

cons219 = CustomConstraint(cons_f219)

def cons_f220(p, q):
    return IntegersQ(p, q)

cons220 = CustomConstraint(cons_f220)

def cons_f221(q):
    return PositiveIntegerQ(q)

cons221 = CustomConstraint(cons_f221)

def cons_f222(a, n, q, b, f, d, g, x, h, c, m, p, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, b, c, d, e, f, g, h, m, n, p, q), x)

cons222 = CustomConstraint(cons_f222)

def cons_f223(a, n, q, b, f, d, g, x, i, h, c, m, p, e, r):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, b, c, d, e, f, g, h, i, m, n, p, q, r), x)

cons223 = CustomConstraint(cons_f223)

def cons_f224(i, x):
    return FreeQ(i, x)

cons224 = CustomConstraint(cons_f224)

def cons_f225(p):
    return NonzeroQ(S(2)*p + S(1))

cons225 = CustomConstraint(cons_f225)

def cons_f226(a, c, b):
    return NonzeroQ(-S(4)*a*c + b**S(2))

cons226 = CustomConstraint(cons_f226)

def cons_f227(a, c, b):
    return PerfectSquareQ(-S(4)*a*c + b**S(2))

cons227 = CustomConstraint(cons_f227)

def cons_f228(a, c, b):
    return Not(PerfectSquareQ(-S(4)*a*c + b**S(2)))

cons228 = CustomConstraint(cons_f228)

def cons_f229(p):
    return IntegerQ(S(4)*p)

cons229 = CustomConstraint(cons_f229)

def cons_f230(p):
    return Unequal(p, S(-3)/2)

cons230 = CustomConstraint(cons_f230)

def cons_f231(a, c, b):
    return PosQ(-S(4)*a*c + b**S(2))

cons231 = CustomConstraint(cons_f231)

def cons_f232(a, c, b):
    return PositiveQ(S(4)*a - b**S(2)/c)

cons232 = CustomConstraint(cons_f232)

def cons_f233(x, c, b):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(b, c), x)

cons233 = CustomConstraint(cons_f233)

def cons_f234(p):
    return LessEqual(S(3), Denominator(p), S(4))

cons234 = CustomConstraint(cons_f234)

def cons_f235(p):
    return Not(IntegerQ(S(4)*p))

cons235 = CustomConstraint(cons_f235)

def cons_f236(m):
    return IntegerQ(m/S(2) + S(1)/2)

cons236 = CustomConstraint(cons_f236)

def cons_f237(p, m):
    return ZeroQ(m + S(2)*p + S(1))

cons237 = CustomConstraint(cons_f237)

def cons_f238(p, m):
    return NonzeroQ(m + S(2)*p + S(1))

cons238 = CustomConstraint(cons_f238)

def cons_f239(d, e, c, b):
    return NonzeroQ(-b*e + S(2)*c*d)

cons239 = CustomConstraint(cons_f239)

def cons_f240(p, m):
    return ZeroQ(m + S(2)*p + S(2))

cons240 = CustomConstraint(cons_f240)

def cons_f241(m):
    return NonzeroQ(m + S(2))

cons241 = CustomConstraint(cons_f241)

def cons_f242(p, m):
    return ZeroQ(m + S(2)*p + S(3))

cons242 = CustomConstraint(cons_f242)

def cons_f243(p):
    return NonzeroQ(p + S(3)/2)

cons243 = CustomConstraint(cons_f243)

def cons_f244(p, m):
    return RationalQ(m, p)

cons244 = CustomConstraint(cons_f244)

def cons_f245(m):
    return Inequality(S(-2), LessEqual, m, Less, S(-1))

cons245 = CustomConstraint(cons_f245)

def cons_f246(p):
    return IntegerQ(S(2)*p)

cons246 = CustomConstraint(cons_f246)

def cons_f247(m):
    return Less(m, S(-2))

cons247 = CustomConstraint(cons_f247)

def cons_f248(p, m):
    return Not(And(NegativeIntegerQ(m + S(2)*p + S(3)), Greater(m + S(3)*p + S(3), S(0))))

cons248 = CustomConstraint(cons_f248)

def cons_f249(p, m):
    return NonzeroQ(m + S(2)*p)

cons249 = CustomConstraint(cons_f249)

def cons_f250(m):
    return Not(And(RationalQ(m), Less(m, S(-2))))

cons250 = CustomConstraint(cons_f250)

def cons_f251(p, m):
    return Not(And(IntegerQ(m), Less(S(0), m, S(2)*p)))

cons251 = CustomConstraint(cons_f251)

def cons_f252(m):
    return Inequality(S(0), Less, m, LessEqual, S(1))

cons252 = CustomConstraint(cons_f252)

def cons_f253(p, m):
    return NonzeroQ(m + p + S(1))

cons253 = CustomConstraint(cons_f253)

def cons_f254(p, m):
    return Or(Not(RationalQ(p)), Inequality(S(-1), LessEqual, p, Less, S(0)), And(IntegerQ(m), Less(S(0), m, S(2)*p)), And(Equal(m, S(1)/2), Less(p, S(0))))

cons254 = CustomConstraint(cons_f254)

def cons_f255(p, m):
    return Or(IntegerQ(m), IntegerQ(S(2)*p))

cons255 = CustomConstraint(cons_f255)

def cons_f256(a, b, d, c, e):
    return ZeroQ(a*e**S(2) - b*d*e + c*d**S(2))

cons256 = CustomConstraint(cons_f256)

def cons_f257(a, d, e, c):
    return ZeroQ(a*e**S(2) + c*d**S(2))

cons257 = CustomConstraint(cons_f257)

def cons_f258(a, p, d, m):
    return Or(IntegerQ(p), And(PositiveQ(a), PositiveQ(d), IntegerQ(m + p)))

cons258 = CustomConstraint(cons_f258)

def cons_f259(p, m):
    return Or(Less(S(0), -m, p), Less(p, -m, S(0)))

cons259 = CustomConstraint(cons_f259)

def cons_f260(m):
    return Unequal(m, S(2))

cons260 = CustomConstraint(cons_f260)

def cons_f261(m):
    return Unequal(m, S(-1))

cons261 = CustomConstraint(cons_f261)

def cons_f262(p, m):
    return PositiveIntegerQ(m + p)

cons262 = CustomConstraint(cons_f262)

def cons_f263(p, m):
    return NegativeIntegerQ(m + S(2)*p + S(2))

cons263 = CustomConstraint(cons_f263)

def cons_f264(p, m):
    return Or(Less(m, S(-2)), ZeroQ(m + S(2)*p + S(1)))

cons264 = CustomConstraint(cons_f264)

def cons_f265(p, m):
    return Or(Inequality(S(-2), LessEqual, m, Less, S(0)), Equal(m + p + S(1), S(0)))

cons265 = CustomConstraint(cons_f265)

def cons_f266(m):
    return GreaterEqual(m, S(1))

cons266 = CustomConstraint(cons_f266)

def cons_f267(m):
    return Less(m, S(0))

cons267 = CustomConstraint(cons_f267)

def cons_f268(d):
    return PositiveQ(d)

cons268 = CustomConstraint(cons_f268)

def cons_f269(p, m):
    return Not(And(ZeroQ(m + S(-3)), Unequal(p, S(1))))

cons269 = CustomConstraint(cons_f269)

def cons_f270(p, m):
    return NonzeroQ(m + S(2)*p + S(3))

cons270 = CustomConstraint(cons_f270)

def cons_f271(p, m):
    return Not(And(EvenQ(m), Less(m + S(2)*p + S(3), S(0))))

cons271 = CustomConstraint(cons_f271)

def cons_f272(m):
    return Not(And(RationalQ(m), Less(m, S(-1))))

cons272 = CustomConstraint(cons_f272)

def cons_f273(p, m):
    return Not(And(PositiveIntegerQ(m/S(2) + S(-1)/2), Or(Not(IntegerQ(p)), Less(m, S(2)*p))))

cons273 = CustomConstraint(cons_f273)

def cons_f274(m):
    return Not(And(RationalQ(m), Greater(m, S(1))))

cons274 = CustomConstraint(cons_f274)

def cons_f275(a, c, b):
    return NegativeQ(c/(-S(4)*a*c + b**S(2)))

cons275 = CustomConstraint(cons_f275)

def cons_f276(m):
    return EqQ(m**S(2), S(1)/4)

cons276 = CustomConstraint(cons_f276)

def cons_f277(p, m):
    return Or(IntegerQ(S(2)*p), And(IntegerQ(m), RationalQ(p)), OddQ(m))

cons277 = CustomConstraint(cons_f277)

def cons_f278(p, m):
    return Or(IntegerQ(S(2)*p), And(IntegerQ(m), RationalQ(p)), IntegerQ(m/S(2) + p + S(3)/2))

cons278 = CustomConstraint(cons_f278)

def cons_f279(a, b, d, c, e):
    return NonzeroQ(a*e**S(2) - b*d*e + c*d**S(2))

cons279 = CustomConstraint(cons_f279)

def cons_f280(a, d, e, c):
    return NonzeroQ(a*e**S(2) + c*d**S(2))

cons280 = CustomConstraint(cons_f280)

def cons_f281(p, m):
    return Not(And(ZeroQ(m + S(-1)), Greater(p, S(1))))

cons281 = CustomConstraint(cons_f281)

def cons_f282(a, c, b):
    return NiceSqrtQ(-S(4)*a*c + b**S(2))

cons282 = CustomConstraint(cons_f282)

def cons_f283(a, c):
    return NiceSqrtQ(-a*c)

cons283 = CustomConstraint(cons_f283)

def cons_f284(a, c, b):
    return Not(NiceSqrtQ(-S(4)*a*c + b**S(2)))

cons284 = CustomConstraint(cons_f284)

def cons_f285(a, c):
    return Not(NiceSqrtQ(-a*c))

cons285 = CustomConstraint(cons_f285)

def cons_f286(d, m):
    return Or(NonzeroQ(d), Greater(m, S(2)))

cons286 = CustomConstraint(cons_f286)

def cons_f287(p):
    return Not(And(RationalQ(p), LessEqual(p, S(-1))))

cons287 = CustomConstraint(cons_f287)

def cons_f288(a, d, e, b):
    return ZeroQ(a*e + b*d)

cons288 = CustomConstraint(cons_f288)

def cons_f289(d, e, c, b):
    return ZeroQ(b*e + c*d)

cons289 = CustomConstraint(cons_f289)

def cons_f290(p, m):
    return PositiveIntegerQ(m - p + S(1))

cons290 = CustomConstraint(cons_f290)

def cons_f291(d, e, c, b):
    return NonzeroQ(-b*e + c*d)

cons291 = CustomConstraint(cons_f291)

def cons_f292(m):
    return Equal(m**S(2), S(1)/4)

cons292 = CustomConstraint(cons_f292)

def cons_f293(c):
    return NegativeQ(c)

cons293 = CustomConstraint(cons_f293)

def cons_f294(b):
    return RationalQ(b)

cons294 = CustomConstraint(cons_f294)

def cons_f295(m):
    return ZeroQ(m**S(2) + S(-1)/4)

cons295 = CustomConstraint(cons_f295)

def cons_f296(p, m):
    return Equal(m + S(2)*p + S(2), S(0))

cons296 = CustomConstraint(cons_f296)

def cons_f297(a, x, d, c, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, c, d, e), x)

cons297 = CustomConstraint(cons_f297)

def cons_f298(p, m):
    return Or(IntegerQ(p), And(RationalQ(m), Less(m, S(-1))))

cons298 = CustomConstraint(cons_f298)

def cons_f299(p, m):
    return Not(NegativeIntegerQ(m + S(2)*p + S(1)))

cons299 = CustomConstraint(cons_f299)

def cons_f300(a, b, x, d, c, m, p, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return IntQuadraticQ(a, b, c, d, e, m, p, x)

cons300 = CustomConstraint(cons_f300)

def cons_f301(a, x, d, c, m, p, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return IntQuadraticQ(a, S(0), c, d, e, m, p, x)

cons301 = CustomConstraint(cons_f301)

def cons_f302(m):
    return Or(Not(RationalQ(m)), Less(m, S(1)))

cons302 = CustomConstraint(cons_f302)

def cons_f303(p, m):
    return Not(NegativeIntegerQ(m + S(2)*p))

cons303 = CustomConstraint(cons_f303)

def cons_f304(p, m):
    return Or(Less(m, S(1)), And(NegativeIntegerQ(m + S(2)*p + S(3)), Unequal(m, S(2))))

cons304 = CustomConstraint(cons_f304)

def cons_f305(m):
    return If(RationalQ(m), Greater(m, S(1)), SumSimplerQ(m, S(-2)))

cons305 = CustomConstraint(cons_f305)

def cons_f306(a, b, x, d, c, m, p, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Or(And(RationalQ(m), Less(m, S(-1)), IntQuadraticQ(a, b, c, d, e, m, p, x)), And(SumSimplerQ(m, S(1)), IntegerQ(p), NonzeroQ(m + S(1))), And(NegativeIntegerQ(m + S(2)*p + S(3)), NonzeroQ(m + S(1))))

cons306 = CustomConstraint(cons_f306)

def cons_f307(a, x, d, c, m, p, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Or(And(RationalQ(m), Less(m, S(-1)), IntQuadraticQ(a, S(0), c, d, e, m, p, x)), And(SumSimplerQ(m, S(1)), IntegerQ(p), NonzeroQ(m + S(1))), And(NegativeIntegerQ(m + S(2)*p + S(3)), NonzeroQ(m + S(1))))

cons307 = CustomConstraint(cons_f307)

def cons_f308(a, b, d, c, e):
    return ZeroQ(-S(3)*a*c*e**S(2) + b**S(2)*e**S(2) - b*c*d*e + c**S(2)*d**S(2))

cons308 = CustomConstraint(cons_f308)

def cons_f309(d, e, c, b):
    return PosQ(c*e**S(2)*(-b*e + S(2)*c*d))

cons309 = CustomConstraint(cons_f309)

def cons_f310(a, d, e, c):
    return ZeroQ(-S(3)*a*e**S(2) + c*d**S(2))

cons310 = CustomConstraint(cons_f310)

def cons_f311(d, e, c, b):
    return NegQ(c*e**S(2)*(-b*e + S(2)*c*d))

cons311 = CustomConstraint(cons_f311)

def cons_f312(a, b, d, c, e):
    return ZeroQ(S(9)*a*c*e**S(2) - S(2)*b**S(2)*e**S(2) - b*c*d*e + c**S(2)*d**S(2))

cons312 = CustomConstraint(cons_f312)

def cons_f313(a, c, b):
    return Not(PositiveQ(S(4)*a - b**S(2)/c))

cons313 = CustomConstraint(cons_f313)

def cons_f314(p):
    return Not(IntegerQ(S(2)*p))

cons314 = CustomConstraint(cons_f314)

def cons_f315(d, g, e, f):
    return NonzeroQ(-d*g + e*f)

cons315 = CustomConstraint(cons_f315)

def cons_f316(b, g, c, f):
    return ZeroQ(-b*g + S(2)*c*f)

cons316 = CustomConstraint(cons_f316)

def cons_f317(m):
    return Not(And(RationalQ(m), Greater(m, S(0))))

cons317 = CustomConstraint(cons_f317)

def cons_f318(p, m):
    return Or(Not(RationalQ(p)), And(Greater(p, S(0)), Or(Not(IntegerQ(m)), GreaterEqual(m, -S(2)*p + S(-2)), Less(m, -S(4)*p + S(-4)))))

cons318 = CustomConstraint(cons_f318)

def cons_f319(p, m):
    return NonzeroQ(m + S(2)*p + S(2))

cons319 = CustomConstraint(cons_f319)

def cons_f320(p, m):
    return Or(Not(RationalQ(p)), Less(m, S(2)*p + S(2)))

cons320 = CustomConstraint(cons_f320)

def cons_f321(b, g, c, f):
    return NonzeroQ(-b*g + S(2)*c*f)

cons321 = CustomConstraint(cons_f321)

def cons_f322(p):
    return Less(p, S(0))

cons322 = CustomConstraint(cons_f322)

def cons_f323(b, d, c, m, p, e):
    return Or(And(ZeroQ(m + S(2)*p + S(2)), NonzeroQ(m + S(1))), And(ZeroQ(-b*e + S(2)*c*d), NonzeroQ(m + S(-1))))

cons323 = CustomConstraint(cons_f323)

def cons_f324(g, x, d, f, m, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(And(ZeroQ(m + S(-1)), SimplerQ(f + g*x, d + e*x)))

cons324 = CustomConstraint(cons_f324)

def cons_f325(a, p, d, m):
    return Or(IntegerQ(p), And(PositiveQ(a), PositiveQ(d), ZeroQ(m + p)))

cons325 = CustomConstraint(cons_f325)

def cons_f326(b, g, d, f, c, m, p, e):
    return ZeroQ(e*(p + S(1))*(-b*g + S(2)*c*f) + m*(c*e*f + g*(-b*e + c*d)))

cons326 = CustomConstraint(cons_f326)

def cons_f327(f, g, d, m, p, e):
    return ZeroQ(S(2)*e*f*(p + S(1)) + m*(d*g + e*f))

cons327 = CustomConstraint(cons_f327)

def cons_f328(m):
    return SumSimplerQ(m, S(-1))

cons328 = CustomConstraint(cons_f328)

def cons_f329(p, m):
    return Or(And(RationalQ(m), Less(m, S(-1)), Not(PositiveIntegerQ(m + p + S(1)))), And(RationalQ(m, p), Less(m, S(0)), Less(p, S(-1))), ZeroQ(m + S(2)*p + S(2)))

cons329 = CustomConstraint(cons_f329)

def cons_f330(a, f, c, g):
    return ZeroQ(a*g**S(2) + c*f**S(2))

cons330 = CustomConstraint(cons_f330)

def cons_f331(p):
    return Less(p, S(-2))

cons331 = CustomConstraint(cons_f331)

def cons_f332(p, m):
    return Or(Less(S(0), -m, p + S(1)), Less(p, -m, S(0)))

cons332 = CustomConstraint(cons_f332)

def cons_f333(p, n):
    return NegativeIntegerQ(n + S(2)*p)

cons333 = CustomConstraint(cons_f333)

def cons_f334(g, f, d, b, c, e):
    return ZeroQ(-b*e*g + c*d*g + c*e*f)

cons334 = CustomConstraint(cons_f334)

def cons_f335(n, m):
    return NonzeroQ(m - n + S(-1))

cons335 = CustomConstraint(cons_f335)

def cons_f336(d, g, e, f):
    return ZeroQ(d*g + e*f)

cons336 = CustomConstraint(cons_f336)

def cons_f337(n, m):
    return ZeroQ(m - n + S(-2))

cons337 = CustomConstraint(cons_f337)

def cons_f338(p, n):
    return RationalQ(n, p)

cons338 = CustomConstraint(cons_f338)

def cons_f339(p, n):
    return Not(And(IntegerQ(n + p), LessEqual(n + p + S(2), S(0))))

cons339 = CustomConstraint(cons_f339)

def cons_f340(n):
    return Not(PositiveIntegerQ(n))

cons340 = CustomConstraint(cons_f340)

def cons_f341(p, n):
    return Not(And(IntegerQ(n + p), Less(n + p + S(2), S(0))))

cons341 = CustomConstraint(cons_f341)

def cons_f342(p, n):
    return Or(IntegerQ(S(2)*p), IntegerQ(n))

cons342 = CustomConstraint(cons_f342)

def cons_f343(p, m):
    return ZeroQ(m + p + S(-1))

cons343 = CustomConstraint(cons_f343)

def cons_f344(n, g, b, f, d, c, p, e):
    return ZeroQ(b*e*g*(n + S(1)) - c*d*g*(S(2)*n + p + S(3)) + c*e*f*(p + S(1)))

cons344 = CustomConstraint(cons_f344)

def cons_f345(n, g, f, d, p, e):
    return ZeroQ(-d*g*(S(2)*n + p + S(3)) + e*f*(p + S(1)))

cons345 = CustomConstraint(cons_f345)

def cons_f346(n):
    return Not(And(RationalQ(n), Less(n, S(-1))))

cons346 = CustomConstraint(cons_f346)

def cons_f347(p):
    return IntegerQ(p + S(-1)/2)

cons347 = CustomConstraint(cons_f347)

def cons_f348(p, m):
    return Not(And(Less(m, S(0)), Less(p, S(0))))

cons348 = CustomConstraint(cons_f348)

def cons_f349(p):
    return Unequal(p, S(1)/2)

cons349 = CustomConstraint(cons_f349)

def cons_f350(a, f, g, d, b, c, e):
    return ZeroQ(-S(2)*a*e*g + b*(d*g + e*f) - S(2)*c*d*f)

cons350 = CustomConstraint(cons_f350)

def cons_f351(a, f, g, d, c, e):
    return ZeroQ(a*e*g + c*d*f)

cons351 = CustomConstraint(cons_f351)

def cons_f352(b, d, c, m, e):
    return Not(And(Equal(m, S(1)), Or(ZeroQ(d), ZeroQ(-b*e + S(2)*c*d))))

cons352 = CustomConstraint(cons_f352)

def cons_f353(d, m):
    return Not(And(Equal(m, S(1)), ZeroQ(d)))

cons353 = CustomConstraint(cons_f353)

def cons_f354(a, g, b, d, f, c, p, e):
    return ZeroQ(-S(2)*a*c*e*g + b**S(2)*e*g*(p + S(2)) + c*(S(2)*p + S(3))*(-b*(d*g + e*f) + S(2)*c*d*f))

cons354 = CustomConstraint(cons_f354)

def cons_f355(a, g, f, d, c, p, e):
    return ZeroQ(a*e*g - c*d*f*(S(2)*p + S(3)))

cons355 = CustomConstraint(cons_f355)

def cons_f356(m):
    return Not(RationalQ(m))

cons356 = CustomConstraint(cons_f356)

def cons_f357(p):
    return Not(PositiveIntegerQ(p))

cons357 = CustomConstraint(cons_f357)

def cons_f358(p, m):
    return ZeroQ(m - p)

cons358 = CustomConstraint(cons_f358)

def cons_f359(p, m):
    return Less(m + S(2)*p, S(0))

cons359 = CustomConstraint(cons_f359)

def cons_f360(p, m):
    return Not(NegativeIntegerQ(m + S(2)*p + S(3)))

cons360 = CustomConstraint(cons_f360)

def cons_f361(p, m):
    return Or(And(RationalQ(m), Less(m, S(-1))), Equal(p, S(1)), And(IntegerQ(p), Not(RationalQ(m))))

cons361 = CustomConstraint(cons_f361)

def cons_f362(p, m):
    return Or(IntegerQ(m), IntegerQ(p), IntegersQ(S(2)*m, S(2)*p))

cons362 = CustomConstraint(cons_f362)

def cons_f363(p, m):
    return Or(IntegerQ(p), Not(RationalQ(m)), Inequality(S(-1), LessEqual, m, Less, S(0)))

cons363 = CustomConstraint(cons_f363)

def cons_f364(a, b, f, d, g, c, m, p, e):
    return Or(And(Equal(m, S(2)), Equal(p, S(-3)), RationalQ(a, b, c, d, e, f, g)), Not(NegativeIntegerQ(m + S(2)*p + S(3))))

cons364 = CustomConstraint(cons_f364)

def cons_f365(a, f, g, d, c, m, p, e):
    return Or(And(Equal(m, S(2)), Equal(p, S(-3)), RationalQ(a, c, d, e, f, g)), Not(NegativeIntegerQ(m + S(2)*p + S(3))))

cons365 = CustomConstraint(cons_f365)

def cons_f366(f, x, d, g, m, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(And(Equal(m, S(1)), SimplerQ(d + e*x, f + g*x)))

cons366 = CustomConstraint(cons_f366)

def cons_f367(m):
    return FractionQ(m)

cons367 = CustomConstraint(cons_f367)

def cons_f368(g, x, d, f, m, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(And(Equal(m, S(1)), SimplerQ(f + g*x, d + e*x)))

cons368 = CustomConstraint(cons_f368)

def cons_f369(p, m):
    return NegativeIntegerQ(m + S(2)*p + S(3))

cons369 = CustomConstraint(cons_f369)

def cons_f370(a, b, d, c, e):
    return ZeroQ(S(4)*c*(a - d) - (b - e)**S(2))

cons370 = CustomConstraint(cons_f370)

def cons_f371(a, b, g, d, f, e):
    return ZeroQ(e*f*(b - e) - S(2)*g*(-a*e + b*d))

cons371 = CustomConstraint(cons_f371)

def cons_f372(a, d, e, b):
    return NonzeroQ(-a*e + b*d)

cons372 = CustomConstraint(cons_f372)

def cons_f373(a, g, x, f, c):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, c, f, g), x)

cons373 = CustomConstraint(cons_f373)

def cons_f374(a, g, f, x, c, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, c, e, f, g), x)

cons374 = CustomConstraint(cons_f374)

def cons_f375(p, n, m):
    return IntegersQ(m, n, p)

cons375 = CustomConstraint(cons_f375)

def cons_f376(p, n):
    return IntegersQ(n, p)

cons376 = CustomConstraint(cons_f376)

def cons_f377(d, m, f):
    return Or(IntegerQ(m), And(PositiveQ(d), PositiveQ(f)))

cons377 = CustomConstraint(cons_f377)

def cons_f378(p, n, m):
    return Or(IntegerQ(p), IntegersQ(m, n))

cons378 = CustomConstraint(cons_f378)

def cons_f379(a, g, f, x, c, m, p, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, c, e, f, g, m, p), x)

cons379 = CustomConstraint(cons_f379)

def cons_f380(a, n, b, f, d, g, x, c, m, p, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, b, c, d, e, f, g, m, n, p), x)

cons380 = CustomConstraint(cons_f380)

def cons_f381(a, n, f, g, d, x, c, m, p, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, c, d, e, f, g, m, n, p), x)

cons381 = CustomConstraint(cons_f381)

def cons_f382(a, d, c, f):
    return ZeroQ(-a*f + c*d)

cons382 = CustomConstraint(cons_f382)

def cons_f383(a, d, e, b):
    return ZeroQ(-a*e + b*d)

cons383 = CustomConstraint(cons_f383)

def cons_f384(p, c, f):
    return Or(IntegerQ(p), PositiveQ(c/f))

cons384 = CustomConstraint(cons_f384)

def cons_f385(a, q, f, x, d, b, c, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Or(Not(IntegerQ(q)), LessEqual(LeafCount(d + e*x + f*x**S(2)), LeafCount(a + b*x + c*x**S(2))))

cons385 = CustomConstraint(cons_f385)

def cons_f386(q):
    return Not(IntegerQ(q))

cons386 = CustomConstraint(cons_f386)

def cons_f387(c, f):
    return Not(PositiveQ(c/f))

cons387 = CustomConstraint(cons_f387)

def cons_f388(a, q, b, f, d, c, e):
    return ZeroQ(c*(-S(2)*d*f + e**S(2)*(q + S(2))) + f*(S(2)*q + S(3))*(S(2)*a*f - b*e))

cons388 = CustomConstraint(cons_f388)

def cons_f389(q):
    return NonzeroQ(q + S(1))

cons389 = CustomConstraint(cons_f389)

def cons_f390(q):
    return NonzeroQ(S(2)*q + S(3))

cons390 = CustomConstraint(cons_f390)

def cons_f391(a, q, f, d, c, e):
    return ZeroQ(S(2)*a*f**S(2)*(S(2)*q + S(3)) + c*(-S(2)*d*f + e**S(2)*(q + S(2))))

cons391 = CustomConstraint(cons_f391)

def cons_f392(a, q, f, d, c):
    return ZeroQ(S(2)*a*f*q + S(3)*a*f - c*d)

cons392 = CustomConstraint(cons_f392)

def cons_f393(q):
    return PositiveIntegerQ(q + S(2))

cons393 = CustomConstraint(cons_f393)

def cons_f394(d, e, f):
    return NonzeroQ(-S(4)*d*f + e**S(2))

cons394 = CustomConstraint(cons_f394)

def cons_f395(q):
    return RationalQ(q)

cons395 = CustomConstraint(cons_f395)

def cons_f396(q):
    return Less(q, S(-1))

cons396 = CustomConstraint(cons_f396)

def cons_f397(a, q, b, f, d, c, e):
    return NonzeroQ(c*(-S(2)*d*f + e**S(2)*(q + S(2))) + f*(S(2)*q + S(3))*(S(2)*a*f - b*e))

cons397 = CustomConstraint(cons_f397)

def cons_f398(a, q, f, d, c, e):
    return NonzeroQ(S(2)*a*f**S(2)*(S(2)*q + S(3)) + c*(-S(2)*d*f + e**S(2)*(q + S(2))))

cons398 = CustomConstraint(cons_f398)

def cons_f399(a, q, f, d, c):
    return NonzeroQ(S(2)*a*f*q + S(3)*a*f - c*d)

cons399 = CustomConstraint(cons_f399)

def cons_f400(q):
    return Not(PositiveIntegerQ(q))

cons400 = CustomConstraint(cons_f400)

def cons_f401(q):
    return Not(And(RationalQ(q), LessEqual(q, S(-1))))

cons401 = CustomConstraint(cons_f401)

def cons_f402(p, q):
    return RationalQ(p, q)

cons402 = CustomConstraint(cons_f402)

def cons_f403(q):
    return Greater(q, S(0))

cons403 = CustomConstraint(cons_f403)

def cons_f404(a, b, f, d, c, e):
    return NonzeroQ(-(-a*e + b*d)*(-b*f + c*e) + (-a*f + c*d)**S(2))

cons404 = CustomConstraint(cons_f404)

def cons_f405(p, q):
    return Not(And(Not(IntegerQ(p)), IntegerQ(q), Less(q, S(-1))))

cons405 = CustomConstraint(cons_f405)

def cons_f406(a, f, b, d, c):
    return NonzeroQ(b**S(2)*d*f + (-a*f + c*d)**S(2))

cons406 = CustomConstraint(cons_f406)

def cons_f407(a, f, d, c, e):
    return NonzeroQ(a*c*e**S(2) + (-a*f + c*d)**S(2))

cons407 = CustomConstraint(cons_f407)

def cons_f408(p, q):
    return NonzeroQ(p + q)

cons408 = CustomConstraint(cons_f408)

def cons_f409(p, q):
    return NonzeroQ(S(2)*p + S(2)*q + S(1))

cons409 = CustomConstraint(cons_f409)

def cons_f410(f, e, c, b):
    return ZeroQ(-b*f + c*e)

cons410 = CustomConstraint(cons_f410)

def cons_f411(f, e, c, b):
    return NonzeroQ(-b*f + c*e)

cons411 = CustomConstraint(cons_f411)

def cons_f412(a, c):
    return PosQ(-a*c)

cons412 = CustomConstraint(cons_f412)

def cons_f413(a, c, b):
    return NegQ(-S(4)*a*c + b**S(2))

cons413 = CustomConstraint(cons_f413)

def cons_f414(a, c):
    return NegQ(-a*c)

cons414 = CustomConstraint(cons_f414)

def cons_f415(a, q, b, f, d, x, c, p, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, b, c, d, e, f, p, q), x)

cons415 = CustomConstraint(cons_f415)

def cons_f416(a, q, f, x, d, c, p, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, c, d, e, f, p, q), x)

cons416 = CustomConstraint(cons_f416)

def cons_f417(a, b, g, h, c):
    return ZeroQ(a*h**S(2) - b*g*h + c*g**S(2))

cons417 = CustomConstraint(cons_f417)

def cons_f418(a, g, f, d, h, c, e):
    return ZeroQ(a**S(2)*f*h**S(2) - a*c*e*g*h + c**S(2)*d*g**S(2))

cons418 = CustomConstraint(cons_f418)

def cons_f419(a, h, c, g):
    return ZeroQ(a*h**S(2) + c*g**S(2))

cons419 = CustomConstraint(cons_f419)

def cons_f420(a, f, g, d, h, c):
    return ZeroQ(a**S(2)*f*h**S(2) + c**S(2)*d*g**S(2))

cons420 = CustomConstraint(cons_f420)

def cons_f421(a, f, b, c, e):
    return ZeroQ(a*f**S(2) - b*e*f + c*e**S(2))

cons421 = CustomConstraint(cons_f421)

def cons_f422(a, e, c, f):
    return ZeroQ(a*f**S(2) + c*e**S(2))

cons422 = CustomConstraint(cons_f422)

def cons_f423(f, b, g, h, m, c, p, e):
    return ZeroQ(b*f*h*(m + p + S(2)) + c*(-e*h*(m + S(2)*p + S(3)) + S(2)*f*g*(p + S(1))))

cons423 = CustomConstraint(cons_f423)

def cons_f424(a, f, g, b, d, h, m, c, p):
    return ZeroQ(b*f*g*(p + S(1)) + h*(a*f*(m + S(1)) - c*d*(m + S(2)*p + S(3))))

cons424 = CustomConstraint(cons_f424)

def cons_f425(g, f, h, c, m, p, e):
    return ZeroQ(c*(-e*h*(m + S(2)*p + S(3)) + S(2)*f*g*(p + S(1))))

cons425 = CustomConstraint(cons_f425)

def cons_f426(a, f, d, h, c, m, p):
    return ZeroQ(h*(a*f*(m + S(1)) - c*d*(m + S(2)*p + S(3))))

cons426 = CustomConstraint(cons_f426)

def cons_f427(f, b, g, h, m, c, p):
    return ZeroQ(b*f*h*(m + p + S(2)) + S(2)*c*f*g*(p + S(1)))

cons427 = CustomConstraint(cons_f427)

def cons_f428(p, m):
    return Or(IntegersQ(m, p), PositiveIntegerQ(p))

cons428 = CustomConstraint(cons_f428)

def cons_f429(a, b, g, h, c):
    return NonzeroQ(a*h**S(2) - b*g*h + c*g**S(2))

cons429 = CustomConstraint(cons_f429)

def cons_f430(a, h, c, g):
    return NonzeroQ(a*h**S(2) + c*g**S(2))

cons430 = CustomConstraint(cons_f430)

def cons_f431(a, b, g, h, c):
    return NonzeroQ(c*g**S(2) - h*(-a*h + b*g))

cons431 = CustomConstraint(cons_f431)

def cons_f432(p, q):
    return Or(Greater(p, S(0)), Greater(q, S(0)))

cons432 = CustomConstraint(cons_f432)

def cons_f433(p, q):
    return NonzeroQ(p + q + S(1))

cons433 = CustomConstraint(cons_f433)

def cons_f434(a, c):
    return PositiveQ(a*c)

cons434 = CustomConstraint(cons_f434)

def cons_f435(a, c):
    return Not(PositiveQ(a*c))

cons435 = CustomConstraint(cons_f435)

def cons_f436(f, e, h, g):
    return ZeroQ(e*h - S(2)*f*g)

cons436 = CustomConstraint(cons_f436)

def cons_f437(f, e, h, g):
    return NonzeroQ(e*h - S(2)*f*g)

cons437 = CustomConstraint(cons_f437)

def cons_f438(d, e, h, g):
    return ZeroQ(S(2)*d*h - e*g)

cons438 = CustomConstraint(cons_f438)

def cons_f439(d, e, h, g):
    return NonzeroQ(S(2)*d*h - e*g)

cons439 = CustomConstraint(cons_f439)

def cons_f440(a, b, g, d, f, h, c, e):
    return ZeroQ(g**S(2)*(-b*f + c*e) - S(2)*g*h*(-a*f + c*d) + h**S(2)*(-a*e + b*d))

cons440 = CustomConstraint(cons_f440)

def cons_f441(a, g, f, d, h, c, e):
    return ZeroQ(a*e*h**S(2) - c*e*g**S(2) + S(2)*g*h*(-a*f + c*d))

cons441 = CustomConstraint(cons_f441)

def cons_f442(a, g, b, d, f, h, c):
    return ZeroQ(b*d*h**S(2) - b*f*g**S(2) - S(2)*g*h*(-a*f + c*d))

cons442 = CustomConstraint(cons_f442)

def cons_f443(a, b, f, d, c):
    return ZeroQ(c**S(2)*d - f*(-S(3)*a*c + b**S(2)))

cons443 = CustomConstraint(cons_f443)

def cons_f444(a, b, g, h, c):
    return ZeroQ(S(9)*a*c*h**S(2) - S(2)*b**S(2)*h**S(2) - b*c*g*h + c**S(2)*g**S(2))

cons444 = CustomConstraint(cons_f444)

def cons_f445(b, h, c, g):
    return PositiveQ(-S(9)*c*h**S(2)/(-b*h + S(2)*c*g)**S(2))

cons445 = CustomConstraint(cons_f445)

def cons_f446(a, d, c, f):
    return ZeroQ(S(3)*a*f + c*d)

cons446 = CustomConstraint(cons_f446)

def cons_f447(a, h, c, g):
    return ZeroQ(S(9)*a*h**S(2) + c*g**S(2))

cons447 = CustomConstraint(cons_f447)

def cons_f448(a):
    return Not(PositiveQ(a))

cons448 = CustomConstraint(cons_f448)

def cons_f449(a, q, b, f, d, g, x, h, c, p, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, b, c, d, e, f, g, h, p, q), x)

cons449 = CustomConstraint(cons_f449)

def cons_f450(a, q, f, g, d, x, h, c, p, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, c, d, e, f, g, h, p, q), x)

cons450 = CustomConstraint(cons_f450)

def cons_f451(x, z):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return LinearQ(z, x)

cons451 = CustomConstraint(cons_f451)

def cons_f452(x, v, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return QuadraticQ(List(u, v), x)

cons452 = CustomConstraint(cons_f452)

def cons_f453(x, z, v, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(And(LinearMatchQ(z, x), QuadraticMatchQ(List(u, v), x)))

cons453 = CustomConstraint(cons_f453)

def cons_f454(p, q):
    return NonzeroQ(S(2)*p + S(2)*q + S(3))

cons454 = CustomConstraint(cons_f454)

def cons_f455(a, A, q, b, f, d, x, C, c, p, e, B):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, b, c, d, e, f, A, B, C, p, q), x)

cons455 = CustomConstraint(cons_f455)

def cons_f456(a, A, q, b, f, d, x, C, c, p, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, b, c, d, e, f, A, C, p, q), x)

cons456 = CustomConstraint(cons_f456)

def cons_f457(a, A, q, f, x, d, C, c, p, e, B):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, c, d, e, f, A, B, C, p, q), x)

cons457 = CustomConstraint(cons_f457)

def cons_f458(a, A, q, f, x, d, C, c, p, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, c, d, e, f, A, C, p, q), x)

cons458 = CustomConstraint(cons_f458)

def cons_f459(x, p, n, b):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(b, n, p), x)

cons459 = CustomConstraint(cons_f459)

def cons_f460(p, n):
    return ZeroQ(p + S(1) + S(1)/n)

cons460 = CustomConstraint(cons_f460)

def cons_f461(p, n):
    return NegativeIntegerQ(p + S(1) + S(1)/n)

cons461 = CustomConstraint(cons_f461)

def cons_f462(n):
    return NonzeroQ(S(3)*n + S(1))

cons462 = CustomConstraint(cons_f462)

def cons_f463(n):
    return Less(n, S(0))

cons463 = CustomConstraint(cons_f463)

def cons_f464(p, n):
    return PositiveIntegerQ(n, p)

cons464 = CustomConstraint(cons_f464)

def cons_f465(p, n):
    return Or(IntegerQ(S(2)*p), And(Equal(n, S(2)), IntegerQ(S(4)*p)), And(Equal(n, S(2)), IntegerQ(S(3)*p)), Less(Denominator(p + S(1)/n), Denominator(p)))

cons465 = CustomConstraint(cons_f465)

def cons_f466(a, b):
    return PosQ(b/a)

cons466 = CustomConstraint(cons_f466)

def cons_f467(n):
    return PositiveIntegerQ(n/S(2) + S(-3)/2)

cons467 = CustomConstraint(cons_f467)

def cons_f468(a, b):
    return PosQ(a/b)

cons468 = CustomConstraint(cons_f468)

def cons_f469(a, b):
    return NegQ(a/b)

cons469 = CustomConstraint(cons_f469)

def cons_f470(a, b):
    return Or(PositiveQ(a), PositiveQ(b))

cons470 = CustomConstraint(cons_f470)

def cons_f471(a, b):
    return Or(NegativeQ(a), NegativeQ(b))

cons471 = CustomConstraint(cons_f471)

def cons_f472(a, b):
    return Or(PositiveQ(a), NegativeQ(b))

cons472 = CustomConstraint(cons_f472)

def cons_f473(a, b):
    return Or(NegativeQ(a), PositiveQ(b))

cons473 = CustomConstraint(cons_f473)

def cons_f474(n):
    return PositiveIntegerQ(n/S(4) + S(-1)/2)

cons474 = CustomConstraint(cons_f474)

def cons_f475(a, b):
    return Or(PositiveQ(a/b), And(PosQ(a/b), AtomQ(SplitProduct(SumBaseQ, a)), AtomQ(SplitProduct(SumBaseQ, b))))

cons475 = CustomConstraint(cons_f475)

def cons_f476(a, b):
    return Not(PositiveQ(a/b))

cons476 = CustomConstraint(cons_f476)

def cons_f477(n):
    return PositiveIntegerQ(n/S(4) + S(-1))

cons477 = CustomConstraint(cons_f477)

def cons_f478(a, b):
    return PositiveQ(a/b)

cons478 = CustomConstraint(cons_f478)

def cons_f479(b):
    return PosQ(b)

cons479 = CustomConstraint(cons_f479)

def cons_f480(b):
    return NegQ(b)

cons480 = CustomConstraint(cons_f480)

def cons_f481(a):
    return PosQ(a)

cons481 = CustomConstraint(cons_f481)

def cons_f482(a):
    return NegQ(a)

cons482 = CustomConstraint(cons_f482)

def cons_f483(a, b):
    return NegQ(b/a)

cons483 = CustomConstraint(cons_f483)

def cons_f484(a):
    return NegativeQ(a)

cons484 = CustomConstraint(cons_f484)

def cons_f485(p):
    return Less(S(-1), p, S(0))

cons485 = CustomConstraint(cons_f485)

def cons_f486(p):
    return Unequal(p, S(-1)/2)

cons486 = CustomConstraint(cons_f486)

def cons_f487(p, n):
    return IntegerQ(p + S(1)/n)

cons487 = CustomConstraint(cons_f487)

def cons_f488(p, n):
    return Less(Denominator(p + S(1)/n), Denominator(p))

cons488 = CustomConstraint(cons_f488)

def cons_f489(n):
    return FractionQ(n)

cons489 = CustomConstraint(cons_f489)

def cons_f490(n):
    return Not(IntegerQ(S(1)/n))

cons490 = CustomConstraint(cons_f490)

def cons_f491(p, n):
    return Not(NegativeIntegerQ(p + S(1)/n))

cons491 = CustomConstraint(cons_f491)

def cons_f492(a, p):
    return Or(IntegerQ(p), PositiveQ(a))

cons492 = CustomConstraint(cons_f492)

def cons_f493(a, p):
    return Not(Or(IntegerQ(p), PositiveQ(a)))

cons493 = CustomConstraint(cons_f493)

def cons_f494(p, a2, a1):
    return Or(IntegerQ(p), And(PositiveQ(a1), PositiveQ(a2)))

cons494 = CustomConstraint(cons_f494)

def cons_f495(n):
    return PositiveIntegerQ(S(2)*n)

cons495 = CustomConstraint(cons_f495)

def cons_f496(p, n):
    return Or(IntegerQ(S(2)*p), Less(Denominator(p + S(1)/n), Denominator(p)))

cons496 = CustomConstraint(cons_f496)

def cons_f497(n):
    return NegativeIntegerQ(S(2)*n)

cons497 = CustomConstraint(cons_f497)

def cons_f498(n):
    return FractionQ(S(2)*n)

cons498 = CustomConstraint(cons_f498)

def cons_f499(c, m):
    return Or(IntegerQ(m), PositiveQ(c))

cons499 = CustomConstraint(cons_f499)

def cons_f500(n, m):
    return IntegerQ((m + S(1))/n)

cons500 = CustomConstraint(cons_f500)

def cons_f501(n, m):
    return Not(IntegerQ((m + S(1))/n))

cons501 = CustomConstraint(cons_f501)

def cons_f502(n):
    return NegQ(n)

cons502 = CustomConstraint(cons_f502)

def cons_f503(p, n, m):
    return ZeroQ(p + S(1) + (m + S(1))/n)

cons503 = CustomConstraint(cons_f503)

def cons_f504(p, n, m):
    return ZeroQ(p + S(1) + (m + S(1))/(S(2)*n))

cons504 = CustomConstraint(cons_f504)

def cons_f505(n, m):
    return IntegerQ((m + S(1))/(S(2)*n))

cons505 = CustomConstraint(cons_f505)

def cons_f506(p, n, m):
    return NegativeIntegerQ((m + n*(p + S(1)) + S(1))/n)

cons506 = CustomConstraint(cons_f506)

def cons_f507(p, n, m):
    return NegativeIntegerQ((m + S(2)*n*(p + S(1)) + S(1))/(S(2)*n))

cons507 = CustomConstraint(cons_f507)

def cons_f508(p, n, m):
    return Not(NegativeIntegerQ((m + n*p + n + S(1))/n))

cons508 = CustomConstraint(cons_f508)

def cons_f509(a, n, b, x, m, c, p):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return IntBinomialQ(a, b, c, n, m, p, x)

cons509 = CustomConstraint(cons_f509)

def cons_f510(p, n, m):
    return NonzeroQ(m + S(2)*n*p + S(1))

cons510 = CustomConstraint(cons_f510)

def cons_f511(n, b2, x, b1, a2, a1, c, m, p):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return IntBinomialQ(a1*a2, b1*b2, c, n, m, p, x)

cons511 = CustomConstraint(cons_f511)

def cons_f512(p, n, m):
    return NonzeroQ(m + n*p + S(1))

cons512 = CustomConstraint(cons_f512)

def cons_f513(m):
    return PositiveIntegerQ(m/S(4) + S(-1)/2)

cons513 = CustomConstraint(cons_f513)

def cons_f514(m):
    return NegativeIntegerQ(m/S(4) + S(-1)/2)

cons514 = CustomConstraint(cons_f514)

def cons_f515(m):
    return IntegerQ(S(2)*m)

cons515 = CustomConstraint(cons_f515)

def cons_f516(m):
    return Greater(m, S(3)/2)

cons516 = CustomConstraint(cons_f516)

def cons_f517(n, m):
    return Greater(m + S(1), n)

cons517 = CustomConstraint(cons_f517)

def cons_f518(p, n, m):
    return Not(NegativeIntegerQ((m + n*(p + S(1)) + S(1))/n))

cons518 = CustomConstraint(cons_f518)

def cons_f519(n, m):
    return Greater(m + S(1), S(2)*n)

cons519 = CustomConstraint(cons_f519)

def cons_f520(p, n, m):
    return Not(NegativeIntegerQ((m + S(2)*n*(p + S(1)) + S(1))/(S(2)*n)))

cons520 = CustomConstraint(cons_f520)

def cons_f521(n):
    return PositiveIntegerQ(n/S(2) + S(-1)/2)

cons521 = CustomConstraint(cons_f521)

def cons_f522(n, m):
    return Less(m, n + S(-1))

cons522 = CustomConstraint(cons_f522)

def cons_f523(n, m):
    return PositiveIntegerQ(m, n/S(2) + S(-1)/2)

cons523 = CustomConstraint(cons_f523)

def cons_f524(n, m):
    return PositiveIntegerQ(m, n/S(4) + S(-1)/2)

cons524 = CustomConstraint(cons_f524)

def cons_f525(n, m):
    return PositiveIntegerQ(m, n/S(4))

cons525 = CustomConstraint(cons_f525)

def cons_f526(n, m):
    return Less(m, n/S(2))

cons526 = CustomConstraint(cons_f526)

def cons_f527(n, m):
    return Inequality(n/S(2), LessEqual, m, Less, n)

cons527 = CustomConstraint(cons_f527)

def cons_f528(n, m):
    return PositiveIntegerQ(m, n)

cons528 = CustomConstraint(cons_f528)

def cons_f529(n, m):
    return Greater(m, S(2)*n + S(-1))

cons529 = CustomConstraint(cons_f529)

def cons_f530(n, m):
    return Greater(m, n + S(-1))

cons530 = CustomConstraint(cons_f530)

def cons_f531(n, m):
    return SumSimplerQ(m, -n)

cons531 = CustomConstraint(cons_f531)

def cons_f532(p, n, m):
    return NegativeIntegerQ((m + n*p + S(1))/n)

cons532 = CustomConstraint(cons_f532)

def cons_f533(n, m):
    return SumSimplerQ(m, -S(2)*n)

cons533 = CustomConstraint(cons_f533)

def cons_f534(p, n, m):
    return NegativeIntegerQ((m + S(2)*n*p + S(1))/(S(2)*n))

cons534 = CustomConstraint(cons_f534)

def cons_f535(n, m):
    return SumSimplerQ(m, n)

cons535 = CustomConstraint(cons_f535)

def cons_f536(n, m):
    return SumSimplerQ(m, S(2)*n)

cons536 = CustomConstraint(cons_f536)

def cons_f537(p, n, m):
    return IntegersQ(m, p + (m + S(1))/n)

cons537 = CustomConstraint(cons_f537)

def cons_f538(p, n, m):
    return IntegersQ(m, p + (m + S(1))/(S(2)*n))

cons538 = CustomConstraint(cons_f538)

def cons_f539(p, n, m):
    return Less(Denominator(p + (m + S(1))/n), Denominator(p))

cons539 = CustomConstraint(cons_f539)

def cons_f540(p, n, m):
    return Less(Denominator(p + (m + S(1))/(S(2)*n)), Denominator(p))

cons540 = CustomConstraint(cons_f540)

def cons_f541(n, m):
    return IntegerQ(n/(m + S(1)))

cons541 = CustomConstraint(cons_f541)

def cons_f542(n, m):
    return IntegerQ(S(2)*n/(m + S(1)))

cons542 = CustomConstraint(cons_f542)

def cons_f543(n):
    return Not(IntegerQ(S(2)*n))

cons543 = CustomConstraint(cons_f543)

def cons_f544(p, n, m):
    return ZeroQ(p + (m + S(1))/n)

cons544 = CustomConstraint(cons_f544)

def cons_f545(p, n, m):
    return ZeroQ(p + (m + S(1))/(S(2)*n))

cons545 = CustomConstraint(cons_f545)

def cons_f546(p, n, m):
    return IntegerQ(p + (m + S(1))/n)

cons546 = CustomConstraint(cons_f546)

def cons_f547(p, n, m):
    return IntegerQ(p + (m + S(1))/(S(2)*n))

cons547 = CustomConstraint(cons_f547)

def cons_f548(n, m):
    return FractionQ((m + S(1))/n)

cons548 = CustomConstraint(cons_f548)

def cons_f549(n, m):
    return Or(SumSimplerQ(m, n), SumSimplerQ(m, -n))

cons549 = CustomConstraint(cons_f549)

def cons_f550(a, p):
    return Or(NegativeIntegerQ(p), PositiveQ(a))

cons550 = CustomConstraint(cons_f550)

def cons_f551(a, p):
    return Not(Or(NegativeIntegerQ(p), PositiveQ(a)))

cons551 = CustomConstraint(cons_f551)

def cons_f552(x, v):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return LinearQ(v, x)

cons552 = CustomConstraint(cons_f552)

def cons_f553(x, v):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return NonzeroQ(v - x)

cons553 = CustomConstraint(cons_f553)

def cons_f554(x, v, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return LinearPairQ(u, v, x)

cons554 = CustomConstraint(cons_f554)

def cons_f555(p, q):
    return PositiveIntegerQ(p, q)

cons555 = CustomConstraint(cons_f555)

def cons_f556(p, n):
    return ZeroQ(n*p + S(1))

cons556 = CustomConstraint(cons_f556)

def cons_f557(p, n, q):
    return ZeroQ(n*(p + q + S(1)) + S(1))

cons557 = CustomConstraint(cons_f557)

def cons_f558(p, n, q):
    return ZeroQ(n*(p + q + S(2)) + S(1))

cons558 = CustomConstraint(cons_f558)

def cons_f559(a, q, b, d, c, p):
    return ZeroQ(a*d*(p + S(1)) + b*c*(q + S(1)))

cons559 = CustomConstraint(cons_f559)

def cons_f560(p, q):
    return Or(And(RationalQ(p), Less(p, S(-1))), Not(And(RationalQ(q), Less(q, S(-1)))))

cons560 = CustomConstraint(cons_f560)

def cons_f561(a, n, b, d, c, p):
    return ZeroQ(a*d - b*c*(n*(p + S(1)) + S(1)))

cons561 = CustomConstraint(cons_f561)

def cons_f562(p, n):
    return Or(And(RationalQ(p), Less(p, S(-1))), NegativeIntegerQ(p + S(1)/n))

cons562 = CustomConstraint(cons_f562)

def cons_f563(p, n):
    return NonzeroQ(n*(p + S(1)) + S(1))

cons563 = CustomConstraint(cons_f563)

def cons_f564(q):
    return NegativeIntegerQ(q)

cons564 = CustomConstraint(cons_f564)

def cons_f565(p, q):
    return GreaterEqual(p, -q)

cons565 = CustomConstraint(cons_f565)

def cons_f566(a, d, c, b):
    return ZeroQ(S(3)*a*d + b*c)

cons566 = CustomConstraint(cons_f566)

def cons_f567(p):
    return Or(Equal(p, S(1)/2), Equal(Denominator(p), S(4)))

cons567 = CustomConstraint(cons_f567)

def cons_f568(p):
    return Equal(Denominator(p), S(4))

cons568 = CustomConstraint(cons_f568)

def cons_f569(p):
    return Or(Equal(p, S(-5)/4), Equal(p, S(-7)/4))

cons569 = CustomConstraint(cons_f569)

def cons_f570(a, b):
    return PosQ(a*b)

cons570 = CustomConstraint(cons_f570)

def cons_f571(a, b):
    return NegQ(a*b)

cons571 = CustomConstraint(cons_f571)

def cons_f572(p):
    return Or(Equal(p, S(3)/4), Equal(p, S(5)/4))

cons572 = CustomConstraint(cons_f572)

def cons_f573(d, c):
    return PosQ(d/c)

cons573 = CustomConstraint(cons_f573)

def cons_f574(q):
    return Less(S(0), q, S(1))

cons574 = CustomConstraint(cons_f574)

def cons_f575(a, n, q, b, x, d, c, p):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return IntBinomialQ(a, b, c, d, n, p, q, x)

cons575 = CustomConstraint(cons_f575)

def cons_f576(q):
    return Greater(q, S(1))

cons576 = CustomConstraint(cons_f576)

def cons_f577(p, q):
    return Greater(p + q, S(0))

cons577 = CustomConstraint(cons_f577)

def cons_f578(p, n, q):
    return NonzeroQ(n*(p + q) + S(1))

cons578 = CustomConstraint(cons_f578)

def cons_f579(p):
    return Not(And(IntegerQ(p), Greater(p, S(1))))

cons579 = CustomConstraint(cons_f579)

def cons_f580(a, d, c, b):
    return Not(SimplerSqrtQ(b/a, d/c))

cons580 = CustomConstraint(cons_f580)

def cons_f581(d, c):
    return NegQ(d/c)

cons581 = CustomConstraint(cons_f581)

def cons_f582(a, d, c, b):
    return Not(And(NegQ(b/a), SimplerSqrtQ(-b/a, -d/c)))

cons582 = CustomConstraint(cons_f582)

def cons_f583(a, d, c, b):
    return PositiveQ(a - b*c/d)

cons583 = CustomConstraint(cons_f583)

def cons_f584(n):
    return NonzeroQ(n + S(1))

cons584 = CustomConstraint(cons_f584)

def cons_f585(mn, n):
    return EqQ(mn, -n)

cons585 = CustomConstraint(cons_f585)

def cons_f586(q):
    return IntegerQ(q)

cons586 = CustomConstraint(cons_f586)

def cons_f587(p, n):
    return Or(PosQ(n), Not(IntegerQ(p)))

cons587 = CustomConstraint(cons_f587)

def cons_f588(x, v, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return PseudoBinomialPairQ(u, v, x)

cons588 = CustomConstraint(cons_f588)

def cons_f589(p, m):
    return IntegersQ(p, m/p)

cons589 = CustomConstraint(cons_f589)

def cons_f590(v, x, u, m, p):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return PseudoBinomialPairQ(u*x**(m/p), v, x)

cons590 = CustomConstraint(cons_f590)

def cons_f591(e, m):
    return Or(IntegerQ(m), PositiveQ(e))

cons591 = CustomConstraint(cons_f591)

def cons_f592(a, n, b, d, c, m, p):
    return ZeroQ(a*d*(m + S(1)) - b*c*(m + n*(p + S(1)) + S(1)))

cons592 = CustomConstraint(cons_f592)

def cons_f593(non2, n):
    return ZeroQ(-n/S(2) + non2)

cons593 = CustomConstraint(cons_f593)

def cons_f594(n, b2, d, b1, a2, a1, m, c, p):
    return ZeroQ(a1*a2*d*(m + S(1)) - b1*b2*c*(m + n*(p + S(1)) + S(1)))

cons594 = CustomConstraint(cons_f594)

def cons_f595(p, n, m):
    return ZeroQ(m + n*(p + S(1)) + S(1))

cons595 = CustomConstraint(cons_f595)

def cons_f596(n, e):
    return Or(IntegerQ(n), PositiveQ(e))

cons596 = CustomConstraint(cons_f596)

def cons_f597(n, m):
    return Or(And(Greater(n, S(0)), Less(m, S(-1))), And(Less(n, S(0)), Greater(m + n, S(-1))))

cons597 = CustomConstraint(cons_f597)

def cons_f598(p):
    return Not(And(IntegerQ(p), Less(p, S(-1))))

cons598 = CustomConstraint(cons_f598)

def cons_f599(m):
    return PositiveIntegerQ(m/S(2))

cons599 = CustomConstraint(cons_f599)

def cons_f600(p, m):
    return Or(IntegerQ(p), Equal(m + S(2)*p + S(1), S(0)))

cons600 = CustomConstraint(cons_f600)

def cons_f601(m):
    return NegativeIntegerQ(m/S(2))

cons601 = CustomConstraint(cons_f601)

def cons_f602(p, n, m):
    return Or(IntegerQ(p), Not(RationalQ(m)), And(PositiveIntegerQ(n), NegativeIntegerQ(p + S(1)/2), LessEqual(S(-1), m, -n*(p + S(1)))))

cons602 = CustomConstraint(cons_f602)

def cons_f603(p, n, m):
    return NonzeroQ(m + n*(p + S(1)) + S(1))

cons603 = CustomConstraint(cons_f603)

def cons_f604(m):
    return Or(IntegerQ(m), PositiveIntegerQ(S(2)*m + S(2)), Not(RationalQ(m)))

cons604 = CustomConstraint(cons_f604)

def cons_f605(p, n, m):
    return NonzeroQ(m + n*(p + S(2)) + S(1))

cons605 = CustomConstraint(cons_f605)

def cons_f606(p, m, q):
    return RationalQ(m, p, q)

cons606 = CustomConstraint(cons_f606)

def cons_f607(n, m):
    return Greater(m - n + S(1), S(0))

cons607 = CustomConstraint(cons_f607)

def cons_f608(a, n, q, b, x, d, c, m, p, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return IntBinomialQ(a, b, c, d, e, m, n, p, q, x)

cons608 = CustomConstraint(cons_f608)

def cons_f609(n, m):
    return Greater(m - n + S(1), n)

cons609 = CustomConstraint(cons_f609)

def cons_f610(n, m):
    return Inequality(n, GreaterEqual, m - n + S(1), Greater, S(0))

cons610 = CustomConstraint(cons_f610)

def cons_f611(m, q):
    return RationalQ(m, q)

cons611 = CustomConstraint(cons_f611)

def cons_f612(n, m):
    return LessEqual(n, m, S(2)*n + S(-1))

cons612 = CustomConstraint(cons_f612)

def cons_f613(n, m):
    return IntegersQ(m/S(2), n/S(2))

cons613 = CustomConstraint(cons_f613)

def cons_f614(n, m):
    return Less(S(0), m - n + S(1), n)

cons614 = CustomConstraint(cons_f614)

def cons_f615(n):
    return LessEqual(n, S(4))

cons615 = CustomConstraint(cons_f615)

def cons_f616(a, d, c, b):
    return ZeroQ(-a*d + S(4)*b*c)

cons616 = CustomConstraint(cons_f616)

def cons_f617(m):
    return PositiveIntegerQ(m/S(3) + S(-1)/3)

cons617 = CustomConstraint(cons_f617)

def cons_f618(m):
    return NegativeIntegerQ(m/S(3) + S(-1)/3)

cons618 = CustomConstraint(cons_f618)

def cons_f619(m):
    return IntegerQ(m/S(3) + S(-1)/3)

cons619 = CustomConstraint(cons_f619)

def cons_f620(n):
    return Or(EqQ(n, S(2)), EqQ(n, S(4)))

cons620 = CustomConstraint(cons_f620)

def cons_f621(a, n, b, d, c):
    return Not(And(EqQ(n, S(2)), SimplerSqrtQ(-b/a, -d/c)))

cons621 = CustomConstraint(cons_f621)

def cons_f622(p, n, m, q):
    return IntegersQ(p + (m + S(1))/n, q)

cons622 = CustomConstraint(cons_f622)

def cons_f623(n, m):
    return Or(ZeroQ(m - n), ZeroQ(m - S(2)*n + S(1)))

cons623 = CustomConstraint(cons_f623)

def cons_f624(p, m, q):
    return IntegersQ(m, p, q)

cons624 = CustomConstraint(cons_f624)

def cons_f625(p):
    return GreaterEqual(p, S(-2))

cons625 = CustomConstraint(cons_f625)

def cons_f626(m, q):
    return Or(GreaterEqual(q, S(-2)), And(Equal(q, S(-3)), IntegerQ(m/S(2) + S(-1)/2)))

cons626 = CustomConstraint(cons_f626)

def cons_f627(n, m):
    return NonzeroQ(m - n + S(1))

cons627 = CustomConstraint(cons_f627)

def cons_f628(p, r, q):
    return PositiveIntegerQ(p, q, r)

cons628 = CustomConstraint(cons_f628)

def cons_f629(a, n, b, f, d, x, c, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, b, c, d, e, f, n), x)

cons629 = CustomConstraint(cons_f629)

def cons_f630(a, n, b, d, c):
    return Not(And(ZeroQ(n + S(-2)), Or(And(PosQ(b/a), PosQ(d/c)), And(NegQ(b/a), Or(PosQ(d/c), And(PositiveQ(a), Or(Not(PositiveQ(c)), SimplerSqrtQ(-b/a, -d/c))))))))

cons630 = CustomConstraint(cons_f630)

def cons_f631(p, n, q):
    return NonzeroQ(n*(p + q + S(1)) + S(1))

cons631 = CustomConstraint(cons_f631)

def cons_f632(a, n, b, f, d, x, c, p, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, b, c, d, e, f, p, n), x)

cons632 = CustomConstraint(cons_f632)

def cons_f633(a, n, q, b, f, d, x, c, p, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, b, c, d, e, f, n, p, q), x)

cons633 = CustomConstraint(cons_f633)

def cons_f634(d, c):
    return PositiveQ(d/c)

cons634 = CustomConstraint(cons_f634)

def cons_f635(e, f):
    return PositiveQ(f/e)

cons635 = CustomConstraint(cons_f635)

def cons_f636(d, e, c, f):
    return Not(SimplerSqrtQ(d/c, f/e))

cons636 = CustomConstraint(cons_f636)

def cons_f637(d, e, c, f):
    return Not(SimplerSqrtQ(-f/e, -d/c))

cons637 = CustomConstraint(cons_f637)

def cons_f638(e, f):
    return PosQ(f/e)

cons638 = CustomConstraint(cons_f638)

def cons_f639(d, e, c, f):
    return Not(And(NegQ(f/e), SimplerSqrtQ(-f/e, -d/c)))

cons639 = CustomConstraint(cons_f639)

def cons_f640(r, q):
    return RationalQ(q, r)

cons640 = CustomConstraint(cons_f640)

def cons_f641(r):
    return Greater(r, S(1))

cons641 = CustomConstraint(cons_f641)

def cons_f642(q):
    return LessEqual(q, S(-1))

cons642 = CustomConstraint(cons_f642)

def cons_f643(d, e, c, f):
    return PosQ((-c*f + d*e)/c)

cons643 = CustomConstraint(cons_f643)

def cons_f644(d, e, c, f):
    return NegQ((-c*f + d*e)/c)

cons644 = CustomConstraint(cons_f644)

def cons_f645(a, n, q, b, f, d, x, c, p, e, r):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, b, c, d, e, f, n, p, q, r), x)

cons645 = CustomConstraint(cons_f645)

def cons_f646(v, u):
    return ZeroQ(u - v)

cons646 = CustomConstraint(cons_f646)

def cons_f647(w, u):
    return ZeroQ(u - w)

cons647 = CustomConstraint(cons_f647)

def cons_f648(r):
    return IntegerQ(r)

cons648 = CustomConstraint(cons_f648)

def cons_f649(n, n2):
    return ZeroQ(-n/S(2) + n2)

cons649 = CustomConstraint(cons_f649)

def cons_f650(f2, e1, f1, e2):
    return ZeroQ(e1*f2 + e2*f1)

cons650 = CustomConstraint(cons_f650)

def cons_f651(e1, r, e2):
    return Or(IntegerQ(r), And(PositiveQ(e1), PositiveQ(e2)))

cons651 = CustomConstraint(cons_f651)

def cons_f652(e1, x):
    return FreeQ(e1, x)

cons652 = CustomConstraint(cons_f652)

def cons_f653(f1, x):
    return FreeQ(f1, x)

cons653 = CustomConstraint(cons_f653)

def cons_f654(e2, x):
    return FreeQ(e2, x)

cons654 = CustomConstraint(cons_f654)

def cons_f655(f2, x):
    return FreeQ(f2, x)

cons655 = CustomConstraint(cons_f655)

def cons_f656(m, g):
    return Or(IntegerQ(m), PositiveQ(g))

cons656 = CustomConstraint(cons_f656)

def cons_f657(p, r, q):
    return PositiveIntegerQ(p + S(2), q, r)

cons657 = CustomConstraint(cons_f657)

def cons_f658(p, r, q):
    return IntegersQ(p, q, r)

cons658 = CustomConstraint(cons_f658)

def cons_f659(a, q, b, f, d, c, e):
    return Not(And(Equal(q, S(1)), SimplerQ(-a*d + b*c, -a*f + b*e)))

cons659 = CustomConstraint(cons_f659)

def cons_f660(n, q, f, x, d, c, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(And(Equal(q, S(1)), SimplerQ(e + f*x**n, c + d*x**n)))

cons660 = CustomConstraint(cons_f660)

def cons_f661(r):
    return PositiveIntegerQ(r)

cons661 = CustomConstraint(cons_f661)

def cons_f662(a, n, q, b, f, d, g, x, c, m, p, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, b, c, d, e, f, g, m, n, p, q), x)

cons662 = CustomConstraint(cons_f662)

def cons_f663(a, n, q, b, f, d, g, x, c, m, p, e, r):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, b, c, d, e, f, g, m, n, p, q, r), x)

cons663 = CustomConstraint(cons_f663)

def cons_f664(p, n):
    return ZeroQ(n*(S(2)*p + S(1)) + S(1))

cons664 = CustomConstraint(cons_f664)

def cons_f665(p, n):
    return ZeroQ(S(2)*n*(p + S(1)) + S(1))

cons665 = CustomConstraint(cons_f665)

def cons_f666(p, n):
    return Or(ZeroQ(S(2)*n*p + S(1)), ZeroQ(n*(S(2)*p + S(-1)) + S(1)))

cons666 = CustomConstraint(cons_f666)

def cons_f667(p):
    return IntegerQ(p + S(1)/2)

cons667 = CustomConstraint(cons_f667)

def cons_f668(n):
    return NonzeroQ(S(2)*n + S(1))

cons668 = CustomConstraint(cons_f668)

def cons_f669(p, n):
    return NonzeroQ(S(2)*n*p + S(1))

cons669 = CustomConstraint(cons_f669)

def cons_f670(p, n):
    return NonzeroQ(n*(S(2)*p + S(-1)) + S(1))

cons670 = CustomConstraint(cons_f670)

def cons_f671(p, n):
    return NonzeroQ(n*(S(2)*p + S(1)) + S(1))

cons671 = CustomConstraint(cons_f671)

def cons_f672(p, n):
    return NonzeroQ(S(2)*n*(p + S(1)) + S(1))

cons672 = CustomConstraint(cons_f672)

def cons_f673(p, n):
    return Or(IntegerQ(p), ZeroQ(n + S(-2)))

cons673 = CustomConstraint(cons_f673)

def cons_f674(n):
    return PositiveIntegerQ(n/S(2))

cons674 = CustomConstraint(cons_f674)

def cons_f675(a, c, b):
    return PositiveQ(-S(4)*a*c + b**S(2))

cons675 = CustomConstraint(cons_f675)

def cons_f676(a, c):
    return PositiveQ(c/a)

cons676 = CustomConstraint(cons_f676)

def cons_f677(a, b):
    return NegativeQ(b/a)

cons677 = CustomConstraint(cons_f677)

def cons_f678(a, c):
    return PosQ(c/a)

cons678 = CustomConstraint(cons_f678)

def cons_f679(a, c):
    return NegQ(c/a)

cons679 = CustomConstraint(cons_f679)

def cons_f680(n, n2):
    return EqQ(n2, S(2)*n)

cons680 = CustomConstraint(cons_f680)

def cons_f681(n):
    return PosQ(n)

cons681 = CustomConstraint(cons_f681)

def cons_f682(p, n, m):
    return ZeroQ(m + n*(S(2)*p + S(1)) + S(1))

cons682 = CustomConstraint(cons_f682)

def cons_f683(n, m):
    return NonzeroQ(m + n + S(1))

cons683 = CustomConstraint(cons_f683)

def cons_f684(p, n, m):
    return ZeroQ(m + S(2)*n*(p + S(1)) + S(1))

cons684 = CustomConstraint(cons_f684)

def cons_f685(n, m):
    return Inequality(S(-1), LessEqual, m + n, Less, S(0))

cons685 = CustomConstraint(cons_f685)

def cons_f686(n, m):
    return Less(m + n, S(-1))

cons686 = CustomConstraint(cons_f686)

def cons_f687(p, n, m):
    return Not(And(NegativeIntegerQ((m + S(2)*n*(p + S(1)) + S(1))/n), Greater(p + (m + S(2)*n*(p + S(1)) + S(1))/n, S(0))))

cons687 = CustomConstraint(cons_f687)

def cons_f688(p, n, m):
    return NonzeroQ(m + n*(S(2)*p + S(-1)) + S(1))

cons688 = CustomConstraint(cons_f688)

def cons_f689(p, n, m):
    return Not(And(PositiveIntegerQ(m), IntegerQ((m + S(1))/n), Less(S(-1) + (m + S(1))/n, S(2)*p)))

cons689 = CustomConstraint(cons_f689)

def cons_f690(n, m):
    return Inequality(n + S(-1), Less, m, LessEqual, S(2)*n + S(-1))

cons690 = CustomConstraint(cons_f690)

def cons_f691(p, n, m):
    return Or(IntegerQ(S(2)*p), PositiveIntegerQ((m + S(1))/n))

cons691 = CustomConstraint(cons_f691)

def cons_f692(p, n, m):
    return Unequal(m + S(2)*n*p + S(1), S(0))

cons692 = CustomConstraint(cons_f692)

def cons_f693(p, n, m):
    return Unequal(m + n*(S(2)*p + S(-1)) + S(1), S(0))

cons693 = CustomConstraint(cons_f693)

def cons_f694(p, n, m):
    return Or(IntegerQ(p), And(IntegerQ(S(2)*p), IntegerQ(m), Equal(n, S(2))))

cons694 = CustomConstraint(cons_f694)

def cons_f695(n, m):
    return Greater(m, S(3)*n + S(-1))

cons695 = CustomConstraint(cons_f695)

def cons_f696(a, c, b):
    return NegativeQ(-S(4)*a*c + b**S(2))

cons696 = CustomConstraint(cons_f696)

def cons_f697(a, c):
    return PosQ(a*c)

cons697 = CustomConstraint(cons_f697)

def cons_f698(n, m):
    return PositiveIntegerQ(n/S(2), m)

cons698 = CustomConstraint(cons_f698)

def cons_f699(n, m):
    return Inequality(S(3)*n/S(2), LessEqual, m, Less, S(2)*n)

cons699 = CustomConstraint(cons_f699)

def cons_f700(n, m):
    return Inequality(n/S(2), LessEqual, m, Less, S(3)*n/S(2))

cons700 = CustomConstraint(cons_f700)

def cons_f701(n, m):
    return GreaterEqual(m, n)

cons701 = CustomConstraint(cons_f701)

def cons_f702(p):
    return NegativeIntegerQ(p + S(1))

cons702 = CustomConstraint(cons_f702)

def cons_f703(n, b, d, c, p, e):
    return ZeroQ(b*e*(n*p + S(1)) - c*d*(n*(S(2)*p + S(1)) + S(1)))

cons703 = CustomConstraint(cons_f703)

def cons_f704(n, b, d, c, p, e):
    return NonzeroQ(b*e*(n*p + S(1)) - c*d*(n*(S(2)*p + S(1)) + S(1)))

cons704 = CustomConstraint(cons_f704)

def cons_f705(a, d, e, c):
    return ZeroQ(-a*e**S(2) + c*d**S(2))

cons705 = CustomConstraint(cons_f705)

def cons_f706(d, e):
    return PosQ(d*e)

cons706 = CustomConstraint(cons_f706)

def cons_f707(d, e):
    return NegQ(d*e)

cons707 = CustomConstraint(cons_f707)

def cons_f708(a, d, e, c):
    return NonzeroQ(-a*e**S(2) + c*d**S(2))

cons708 = CustomConstraint(cons_f708)

def cons_f709(a, c):
    return NegQ(a*c)

cons709 = CustomConstraint(cons_f709)

def cons_f710(a, n, c):
    return Or(PosQ(a*c), Not(IntegerQ(n)))

cons710 = CustomConstraint(cons_f710)

def cons_f711(a, b, d, c, e):
    return Or(PositiveQ(-b/c + S(2)*d/e), And(Not(NegativeQ(-b/c + S(2)*d/e)), ZeroQ(d - e*Rt(a/c, S(2)))))

cons711 = CustomConstraint(cons_f711)

def cons_f712(a, c, b):
    return Not(PositiveQ(-S(4)*a*c + b**S(2)))

cons712 = CustomConstraint(cons_f712)

def cons_f713(a, n, c, b):
    return Or(PosQ(-S(4)*a*c + b**S(2)), Not(PositiveIntegerQ(n/S(2))))

cons713 = CustomConstraint(cons_f713)

def cons_f714(p, n):
    return NonzeroQ(S(2)*n*p + n + S(1))

cons714 = CustomConstraint(cons_f714)

def cons_f715(a, c):
    return PositiveQ(-a*c)

cons715 = CustomConstraint(cons_f715)

def cons_f716(p, n, q):
    return NonzeroQ(S(2)*n*p + n*q + S(1))

cons716 = CustomConstraint(cons_f716)

def cons_f717(p):
    return PositiveIntegerQ(p + S(-1)/2)

cons717 = CustomConstraint(cons_f717)

def cons_f718(c):
    return Not(NegativeQ(c))

cons718 = CustomConstraint(cons_f718)

def cons_f719(p):
    return NegativeIntegerQ(p + S(1)/2)

cons719 = CustomConstraint(cons_f719)

def cons_f720(d, e, c, b):
    return ZeroQ(-b*e + c*d)

cons720 = CustomConstraint(cons_f720)

def cons_f721(a, d):
    return Not(And(PositiveQ(a), PositiveQ(d)))

cons721 = CustomConstraint(cons_f721)

def cons_f722(p, n, q):
    return Or(And(IntegersQ(p, q), Not(IntegerQ(n))), PositiveIntegerQ(p), And(PositiveIntegerQ(q), Not(IntegerQ(n))))

cons722 = CustomConstraint(cons_f722)

def cons_f723(p, n):
    return Not(IntegersQ(n, S(2)*p))

cons723 = CustomConstraint(cons_f723)

def cons_f724(n, q):
    return Not(IntegersQ(n, q))

cons724 = CustomConstraint(cons_f724)

def cons_f725(mn, n2):
    return EqQ(n2, -S(2)*mn)

cons725 = CustomConstraint(cons_f725)

def cons_f726(mn, x):
    return FreeQ(mn, x)

cons726 = CustomConstraint(cons_f726)

def cons_f727(n2):
    return PosQ(n2)

cons727 = CustomConstraint(cons_f727)

def cons_f728(n2):
    return NegQ(n2)

cons728 = CustomConstraint(cons_f728)

def cons_f729(d2, e1, d1, e2):
    return ZeroQ(d1*e2 + d2*e1)

cons729 = CustomConstraint(cons_f729)

def cons_f730(d1, d2, q):
    return Or(IntegerQ(q), And(PositiveQ(d1), PositiveQ(d2)))

cons730 = CustomConstraint(cons_f730)

def cons_f731(d1, x):
    return FreeQ(d1, x)

cons731 = CustomConstraint(cons_f731)

def cons_f732(d2, x):
    return FreeQ(d2, x)

cons732 = CustomConstraint(cons_f732)

def cons_f733(m, f):
    return Or(IntegerQ(m), PositiveQ(f))

cons733 = CustomConstraint(cons_f733)

def cons_f734(n, m):
    return PositiveIntegerQ(m, n, (m + S(1))/n)

cons734 = CustomConstraint(cons_f734)

def cons_f735(m, q):
    return IntegersQ(m, q)

cons735 = CustomConstraint(cons_f735)

def cons_f736(p, n):
    return Greater(S(2)*n*p, n + S(-1))

cons736 = CustomConstraint(cons_f736)

def cons_f737(p, n, m, q):
    return NonzeroQ(m + S(2)*n*p + n*q + S(1))

cons737 = CustomConstraint(cons_f737)

def cons_f738(p, n, m):
    return Unequal(m + n*(S(2)*p + S(1)) + S(1), S(0))

cons738 = CustomConstraint(cons_f738)

def cons_f739(p, n, m):
    return NonzeroQ(m + n*(S(2)*p + S(1)) + S(1))

cons739 = CustomConstraint(cons_f739)

def cons_f740(n, m):
    return IntegersQ(m, n/S(2))

cons740 = CustomConstraint(cons_f740)

def cons_f741(d, e):
    return PositiveQ(d/e)

cons741 = CustomConstraint(cons_f741)

def cons_f742(d, e, c, b):
    return PosQ(c*(-b*e + S(2)*c*d)/e)

cons742 = CustomConstraint(cons_f742)

def cons_f743(n):
    return IntegerQ(n/S(2))

cons743 = CustomConstraint(cons_f743)

def cons_f744(n):
    return Greater(n, S(2))

cons744 = CustomConstraint(cons_f744)

def cons_f745(n, m):
    return Less(m, -n)

cons745 = CustomConstraint(cons_f745)

def cons_f746(n, m):
    return Greater(m, n)

cons746 = CustomConstraint(cons_f746)

def cons_f747(m, q):
    return Or(PositiveIntegerQ(q), IntegersQ(m, q))

cons747 = CustomConstraint(cons_f747)

def cons_f748(p, q):
    return Or(PositiveIntegerQ(p), PositiveIntegerQ(q))

cons748 = CustomConstraint(cons_f748)

def cons_f749(m, f):
    return Not(Or(IntegerQ(m), PositiveQ(f)))

cons749 = CustomConstraint(cons_f749)

def cons_f750(n, q):
    return ZeroQ(n - q)

cons750 = CustomConstraint(cons_f750)

def cons_f751(n, r):
    return ZeroQ(-n + r)

cons751 = CustomConstraint(cons_f751)

def cons_f752(n, q, r):
    return ZeroQ(-S(2)*n + q + r)

cons752 = CustomConstraint(cons_f752)

def cons_f753(n, q):
    return PosQ(n - q)

cons753 = CustomConstraint(cons_f753)

def cons_f754(p, n, q):
    return NonzeroQ(p*(S(2)*n - q) + S(1))

cons754 = CustomConstraint(cons_f754)

def cons_f755(n, q):
    return ZeroQ(-n + q)

cons755 = CustomConstraint(cons_f755)

def cons_f756(n, m, q):
    return Or(And(ZeroQ(m + S(-1)), ZeroQ(n + S(-3)), ZeroQ(q + S(-2))), And(Or(ZeroQ(m + S(1)/2), ZeroQ(m + S(-3)/2), ZeroQ(m + S(-1)/2), ZeroQ(m + S(-5)/2)), ZeroQ(n + S(-3)), ZeroQ(q + S(-1))))

cons756 = CustomConstraint(cons_f756)

def cons_f757(n, m):
    return ZeroQ(m - S(3)*n/S(2) + S(3)/2)

cons757 = CustomConstraint(cons_f757)

def cons_f758(n, q):
    return ZeroQ(-n + q + S(1))

cons758 = CustomConstraint(cons_f758)

def cons_f759(n, r):
    return ZeroQ(-n + r + S(-1))

cons759 = CustomConstraint(cons_f759)

def cons_f760(n, m):
    return ZeroQ(m - S(3)*n/S(2) + S(1)/2)

cons760 = CustomConstraint(cons_f760)

def cons_f761(p, n, m):
    return Equal(m + p*(n + S(-1)) + S(-1), S(0))

cons761 = CustomConstraint(cons_f761)

def cons_f762(p, n, m, q):
    return Equal(m + p*q + S(1), n - q)

cons762 = CustomConstraint(cons_f762)

def cons_f763(p, n, m, q):
    return Greater(m + p*q + S(1), n - q)

cons763 = CustomConstraint(cons_f763)

def cons_f764(p, n, m, q):
    return Unequal(m + p*(S(2)*n - q) + S(1), S(0))

cons764 = CustomConstraint(cons_f764)

def cons_f765(p, n, m, q):
    return Unequal(m + p*q + (n - q)*(S(2)*p + S(-1)) + S(1), S(0))

cons765 = CustomConstraint(cons_f765)

def cons_f766(p, n, m, q):
    return LessEqual(m + p*q + S(1), -n + q + S(1))

cons766 = CustomConstraint(cons_f766)

def cons_f767(p, m, q):
    return NonzeroQ(m + p*q + S(1))

cons767 = CustomConstraint(cons_f767)

def cons_f768(p, n, m, q):
    return Greater(m + p*q + S(1), -n + q)

cons768 = CustomConstraint(cons_f768)

def cons_f769(p, n, m, q):
    return Equal(m + p*q + S(1), -(n - q)*(S(2)*p + S(3)))

cons769 = CustomConstraint(cons_f769)

def cons_f770(p, n, m, q):
    return Greater(m + p*q + S(1), S(2)*n - S(2)*q)

cons770 = CustomConstraint(cons_f770)

def cons_f771(p, n, m, q):
    return Less(m + p*q + S(1), n - q)

cons771 = CustomConstraint(cons_f771)

def cons_f772(p, n, m, q):
    return Less(n - q, m + p*q + S(1), S(2)*n - S(2)*q)

cons772 = CustomConstraint(cons_f772)

def cons_f773(p):
    return Inequality(S(-1), LessEqual, p, Less, S(0))

cons773 = CustomConstraint(cons_f773)

def cons_f774(p, n, m, q):
    return Equal(m + p*q + S(1), S(2)*n - S(2)*q)

cons774 = CustomConstraint(cons_f774)

def cons_f775(p, n, m, q):
    return Equal(m + p*q + S(1), -S(2)*(n - q)*(p + S(1)))

cons775 = CustomConstraint(cons_f775)

def cons_f776(p, m, q):
    return Less(m + p*q + S(1), S(0))

cons776 = CustomConstraint(cons_f776)

def cons_f777(n, q, r):
    return ZeroQ(-n + q + r)

cons777 = CustomConstraint(cons_f777)

def cons_f778(j, n, q):
    return ZeroQ(j - S(2)*n + q)

cons778 = CustomConstraint(cons_f778)

def cons_f779(j, n, q):
    return ZeroQ(j - n + q)

cons779 = CustomConstraint(cons_f779)

def cons_f780(n):
    return ZeroQ(n + S(-3))

cons780 = CustomConstraint(cons_f780)

def cons_f781(q):
    return ZeroQ(q + S(-2))

cons781 = CustomConstraint(cons_f781)

def cons_f782(p, n, q):
    return NonzeroQ(p*q + (n - q)*(S(2)*p + S(1)) + S(1))

cons782 = CustomConstraint(cons_f782)

def cons_f783(p, n, m, q):
    return LessEqual(m + p*q, -n + q)

cons783 = CustomConstraint(cons_f783)

def cons_f784(p, m, q):
    return Unequal(m + p*q + S(1), S(0))

cons784 = CustomConstraint(cons_f784)

def cons_f785(p, n, m, q):
    return Unequal(m + p*q + (n - q)*(S(2)*p + S(1)) + S(1), S(0))

cons785 = CustomConstraint(cons_f785)

def cons_f786(p, n, m, q):
    return Greater(m + p*q, n - q + S(-1))

cons786 = CustomConstraint(cons_f786)

def cons_f787(p, n, m, q):
    return Greater(m + p*q, -n + q + S(-1))

cons787 = CustomConstraint(cons_f787)

def cons_f788(p, n, m, q):
    return Less(m + p*q, n - q + S(-1))

cons788 = CustomConstraint(cons_f788)

def cons_f789(p, n, m, q):
    return GreaterEqual(m + p*q, n - q + S(-1))

cons789 = CustomConstraint(cons_f789)

def cons_f790(p, n, m, q):
    return Or(Inequality(S(-1), LessEqual, p, Less, S(0)), Equal(m + p*q + (n - q)*(S(2)*p + S(1)) + S(1), S(0)))

cons790 = CustomConstraint(cons_f790)

def cons_f791(m):
    return Or(ZeroQ(m + S(-1)/2), ZeroQ(m + S(1)/2))

cons791 = CustomConstraint(cons_f791)

def cons_f792(q):
    return ZeroQ(q + S(-1))

cons792 = CustomConstraint(cons_f792)

def cons_f793(j, k, q):
    return ZeroQ(j - k + q)

cons793 = CustomConstraint(cons_f793)

def cons_f794(n, j, k):
    return ZeroQ(j - S(2)*k + n)

cons794 = CustomConstraint(cons_f794)

def cons_f795(j, k):
    return PosQ(-j + k)

cons795 = CustomConstraint(cons_f795)

def cons_f796(j, x):
    return FreeQ(j, x)

cons796 = CustomConstraint(cons_f796)

def cons_f797(k, x):
    return FreeQ(k, x)

cons797 = CustomConstraint(cons_f797)

def cons_f798(n, q):
    return IntegerQ(n*q)

cons798 = CustomConstraint(cons_f798)

def cons_f799(a, n, q, b, f, d, x, s, c, m, p, e, r):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, b, c, d, e, f, m, n, p, q, r, s), x)

cons799 = CustomConstraint(cons_f799)

def cons_f800(s, x):
    return FreeQ(s, x)

cons800 = CustomConstraint(cons_f800)

def cons_f801(d, e, b):
    return PositiveQ(b*d*e)

cons801 = CustomConstraint(cons_f801)

def cons_f802(a, d, c, b):
    return PositiveQ(-a*d/b + c)

cons802 = CustomConstraint(cons_f802)

def cons_f803(n):
    return IntegerQ(S(1)/n)

cons803 = CustomConstraint(cons_f803)

def cons_f804(x, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return PolynomialQ(u, x)

cons804 = CustomConstraint(cons_f804)

def cons_f805(m, r):
    return IntegersQ(m, r)

cons805 = CustomConstraint(cons_f805)

def cons_f806(a, n, b, x, c, p):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, b, c, n, p), x)

cons806 = CustomConstraint(cons_f806)

def cons_f807(n, n2):
    return ZeroQ(S(2)*n + n2)

cons807 = CustomConstraint(cons_f807)

def cons_f808(n):
    return IntegerQ(S(2)*n)

cons808 = CustomConstraint(cons_f808)

def cons_f809(x, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(LinearMatchQ(u, x))

cons809 = CustomConstraint(cons_f809)

def cons_f810(x, v, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return LinearQ(List(u, v), x)

cons810 = CustomConstraint(cons_f810)

def cons_f811(x, v, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(LinearMatchQ(List(u, v), x))

cons811 = CustomConstraint(cons_f811)

def cons_f812(w, v, u, x):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return LinearQ(List(u, v, w), x)

cons812 = CustomConstraint(cons_f812)

def cons_f813(w, v, u, x):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(LinearMatchQ(List(u, v, w), x))

cons813 = CustomConstraint(cons_f813)

def cons_f814(v, x, z, u, w):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return LinearQ(List(u, v, w, z), x)

cons814 = CustomConstraint(cons_f814)

def cons_f815(v, x, z, u, w):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(LinearMatchQ(List(u, v, w, z), x))

cons815 = CustomConstraint(cons_f815)

def cons_f816(x, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return QuadraticQ(u, x)

cons816 = CustomConstraint(cons_f816)

def cons_f817(x, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(QuadraticMatchQ(u, x))

cons817 = CustomConstraint(cons_f817)

def cons_f818(x, v):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return QuadraticQ(v, x)

cons818 = CustomConstraint(cons_f818)

def cons_f819(x, v, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(And(LinearMatchQ(u, x), QuadraticMatchQ(v, x)))

cons819 = CustomConstraint(cons_f819)

def cons_f820(w, x):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return QuadraticQ(w, x)

cons820 = CustomConstraint(cons_f820)

def cons_f821(x, v, w, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(And(LinearMatchQ(List(u, v), x), QuadraticMatchQ(w, x)))

cons821 = CustomConstraint(cons_f821)

def cons_f822(x, v, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(QuadraticMatchQ(List(u, v), x))

cons822 = CustomConstraint(cons_f822)

def cons_f823(x, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return BinomialQ(u, x)

cons823 = CustomConstraint(cons_f823)

def cons_f824(x, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(BinomialMatchQ(u, x))

cons824 = CustomConstraint(cons_f824)

def cons_f825(x, v, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return BinomialQ(List(u, v), x)

cons825 = CustomConstraint(cons_f825)

def cons_f826(x, v, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    try:
        return ZeroQ(BinomialDegree(u, x) - BinomialDegree(v, x))
    except TypeError:
        return False

cons826 = CustomConstraint(cons_f826)

def cons_f827(x, v, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(BinomialMatchQ(List(u, v), x))

cons827 = CustomConstraint(cons_f827)

def cons_f828(w, v, u, x):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return BinomialQ(List(u, v, w), x)

cons828 = CustomConstraint(cons_f828)

def cons_f829(x, w, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    try:
        return ZeroQ(BinomialDegree(u, x) - BinomialDegree(w, x))
    except TypeError:
        return False

cons829 = CustomConstraint(cons_f829)

def cons_f830(w, v, u, x):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(BinomialMatchQ(List(u, v, w), x))

cons830 = CustomConstraint(cons_f830)

def cons_f831(x, v, z, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return BinomialQ(List(u, v, z), x)

cons831 = CustomConstraint(cons_f831)

def cons_f832(x, z, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    try:
        return ZeroQ(BinomialDegree(u, x) - BinomialDegree(z, x))
    except TypeError:
        return False

cons832 = CustomConstraint(cons_f832)

def cons_f833(x, v, z, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(BinomialMatchQ(List(u, v, z), x))

cons833 = CustomConstraint(cons_f833)

def cons_f834(x, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return GeneralizedBinomialQ(u, x)

cons834 = CustomConstraint(cons_f834)

def cons_f835(x, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(GeneralizedBinomialMatchQ(u, x))

cons835 = CustomConstraint(cons_f835)

def cons_f836(x, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return TrinomialQ(u, x)

cons836 = CustomConstraint(cons_f836)

def cons_f837(x, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(TrinomialMatchQ(u, x))

cons837 = CustomConstraint(cons_f837)

def cons_f838(x, v):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return TrinomialQ(v, x)

cons838 = CustomConstraint(cons_f838)

def cons_f839(x, v, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(And(BinomialMatchQ(u, x), TrinomialMatchQ(v, x)))

cons839 = CustomConstraint(cons_f839)

def cons_f840(x, v):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return BinomialQ(v, x)

cons840 = CustomConstraint(cons_f840)

def cons_f841(x, v, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(And(BinomialMatchQ(u, x), BinomialMatchQ(v, x)))

cons841 = CustomConstraint(cons_f841)

def cons_f842(x, z):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return BinomialQ(z, x)

cons842 = CustomConstraint(cons_f842)

def cons_f843(x, z, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(And(BinomialMatchQ(z, x), TrinomialMatchQ(u, x)))

cons843 = CustomConstraint(cons_f843)

def cons_f844(x, z, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(And(BinomialMatchQ(z, x), BinomialMatchQ(u, x)))

cons844 = CustomConstraint(cons_f844)

def cons_f845(x, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return GeneralizedTrinomialQ(u, x)

cons845 = CustomConstraint(cons_f845)

def cons_f846(x, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(GeneralizedTrinomialMatchQ(u, x))

cons846 = CustomConstraint(cons_f846)

def cons_f847(x, z, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    try:
        return ZeroQ(BinomialDegree(z, x) - GeneralizedTrinomialDegree(u, x))
    except TypeError:
        return False

cons847 = CustomConstraint(cons_f847)

def cons_f848(x, z, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(And(BinomialMatchQ(z, x), GeneralizedTrinomialMatchQ(u, x)))

cons848 = CustomConstraint(cons_f848)

def cons_f849(n, q):
    return ZeroQ(-n/S(4) + q)

cons849 = CustomConstraint(cons_f849)

def cons_f850(n, r):
    return ZeroQ(-S(3)*n/S(4) + r)

cons850 = CustomConstraint(cons_f850)

def cons_f851(n, m):
    return ZeroQ(S(4)*m - n + S(4))

cons851 = CustomConstraint(cons_f851)

def cons_f852(a, e, h, c):
    return ZeroQ(a*h + c*e)

cons852 = CustomConstraint(cons_f852)

def cons_f853(m):
    return NegativeIntegerQ(m + S(1))

cons853 = CustomConstraint(cons_f853)

def cons_f854(n, m):
    return PositiveIntegerQ(n/(m + S(1)))

cons854 = CustomConstraint(cons_f854)

def cons_f855(x, m, Pq):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return PolyQ(Pq, x**(m + S(1)))

cons855 = CustomConstraint(cons_f855)

def cons_f856(x, n, Pq):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return NonzeroQ(Coeff(Pq, x, n + S(-1)))

cons856 = CustomConstraint(cons_f856)

def cons_f857(p, n):
    return Or(PositiveIntegerQ(p), ZeroQ(n + S(-1)))

cons857 = CustomConstraint(cons_f857)

def cons_f858(x, n, Pq):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return PolyQ(Pq, x**n)

cons858 = CustomConstraint(cons_f858)

def cons_f859(x, Pq):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return ZeroQ(Coeff(Pq, x, S(0)))

cons859 = CustomConstraint(cons_f859)

def cons_f860(Pq):
    return SumQ(Pq)

cons860 = CustomConstraint(cons_f860)

def cons_f861(x, m, Pq):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Less(m + Expon(Pq, x) + S(1), S(0))

cons861 = CustomConstraint(cons_f861)

def cons_f862(x, n, Pq):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Less(Expon(Pq, x), n + S(-1))

cons862 = CustomConstraint(cons_f862)

def cons_f863(a, d, g, b):
    return ZeroQ(a*g + b*d)

cons863 = CustomConstraint(cons_f863)

def cons_f864(a, e, h, b):
    return ZeroQ(-S(3)*a*h + b*e)

cons864 = CustomConstraint(cons_f864)

def cons_f865(a, A, B, b):
    return ZeroQ(-A**S(3)*b + B**S(3)*a)

cons865 = CustomConstraint(cons_f865)

def cons_f866(a, A, B, b):
    return NonzeroQ(-A**S(3)*b + B**S(3)*a)

cons866 = CustomConstraint(cons_f866)

def cons_f867(C, A, B):
    return ZeroQ(-A*C + B**S(2))

cons867 = CustomConstraint(cons_f867)

def cons_f868(a, C, B, b):
    return ZeroQ(B**S(3)*b + C**S(3)*a)

cons868 = CustomConstraint(cons_f868)

def cons_f869(a, A, b, C, B):
    return ZeroQ(A*b**(S(2)/3) - B*a**(S(1)/3)*b**(S(1)/3) - S(2)*C*a**(S(2)/3))

cons869 = CustomConstraint(cons_f869)

def cons_f870(a, C, B, b):
    return ZeroQ(B*a**(S(1)/3)*b**(S(1)/3) + S(2)*C*a**(S(2)/3))

cons870 = CustomConstraint(cons_f870)

def cons_f871(a, A, C, b):
    return ZeroQ(A*b**(S(2)/3) - S(2)*C*a**(S(2)/3))

cons871 = CustomConstraint(cons_f871)

def cons_f872(a, A, b, C, B):
    return ZeroQ(A*(-b)**(S(2)/3) - B*(-a)**(S(1)/3)*(-b)**(S(1)/3) - S(2)*C*(-a)**(S(2)/3))

cons872 = CustomConstraint(cons_f872)

def cons_f873(a, C, B, b):
    return ZeroQ(B*(-a)**(S(1)/3)*(-b)**(S(1)/3) + S(2)*C*(-a)**(S(2)/3))

cons873 = CustomConstraint(cons_f873)

def cons_f874(a, A, C, b):
    return ZeroQ(A*(-b)**(S(2)/3) - S(2)*C*(-a)**(S(2)/3))

cons874 = CustomConstraint(cons_f874)

def cons_f875(a, A, b, C, B):
    return ZeroQ(A*b**(S(2)/3) + B*b**(S(1)/3)*(-a)**(S(1)/3) - S(2)*C*(-a)**(S(2)/3))

cons875 = CustomConstraint(cons_f875)

def cons_f876(a, C, B, b):
    return ZeroQ(B*b**(S(1)/3)*(-a)**(S(1)/3) - S(2)*C*(-a)**(S(2)/3))

cons876 = CustomConstraint(cons_f876)

def cons_f877(a, A, C, b):
    return ZeroQ(A*b**(S(2)/3) - S(2)*C*(-a)**(S(2)/3))

cons877 = CustomConstraint(cons_f877)

def cons_f878(a, A, b, C, B):
    return ZeroQ(A*(-b)**(S(2)/3) + B*a**(S(1)/3)*(-b)**(S(1)/3) - S(2)*C*a**(S(2)/3))

cons878 = CustomConstraint(cons_f878)

def cons_f879(a, C, B, b):
    return ZeroQ(B*a**(S(1)/3)*(-b)**(S(1)/3) - S(2)*C*a**(S(2)/3))

cons879 = CustomConstraint(cons_f879)

def cons_f880(a, A, C, b):
    return ZeroQ(A*(-b)**(S(2)/3) - S(2)*C*a**(S(2)/3))

cons880 = CustomConstraint(cons_f880)

def cons_f881(a, A, b, C, B):
    return ZeroQ(A - B*(a/b)**(S(1)/3) - S(2)*C*(a/b)**(S(2)/3))

cons881 = CustomConstraint(cons_f881)

def cons_f882(a, C, B, b):
    return ZeroQ(B*(a/b)**(S(1)/3) + S(2)*C*(a/b)**(S(2)/3))

cons882 = CustomConstraint(cons_f882)

def cons_f883(a, A, C, b):
    return ZeroQ(A - S(2)*C*(a/b)**(S(2)/3))

cons883 = CustomConstraint(cons_f883)

def cons_f884(a, A, b, C, B):
    return ZeroQ(A - B*Rt(a/b, S(3)) - S(2)*C*Rt(a/b, S(3))**S(2))

cons884 = CustomConstraint(cons_f884)

def cons_f885(a, C, B, b):
    return ZeroQ(B*Rt(a/b, S(3)) + S(2)*C*Rt(a/b, S(3))**S(2))

cons885 = CustomConstraint(cons_f885)

def cons_f886(a, A, C, b):
    return ZeroQ(A - S(2)*C*Rt(a/b, S(3))**S(2))

cons886 = CustomConstraint(cons_f886)

def cons_f887(a, A, b, C, B):
    return ZeroQ(A + B*(-a/b)**(S(1)/3) - S(2)*C*(-a/b)**(S(2)/3))

cons887 = CustomConstraint(cons_f887)

def cons_f888(a, C, B, b):
    return ZeroQ(B*(-a/b)**(S(1)/3) - S(2)*C*(-a/b)**(S(2)/3))

cons888 = CustomConstraint(cons_f888)

def cons_f889(a, A, C, b):
    return ZeroQ(A - S(2)*C*(-a/b)**(S(2)/3))

cons889 = CustomConstraint(cons_f889)

def cons_f890(a, A, b, C, B):
    return ZeroQ(A + B*Rt(-a/b, S(3)) - S(2)*C*Rt(-a/b, S(3))**S(2))

cons890 = CustomConstraint(cons_f890)

def cons_f891(a, C, B, b):
    return ZeroQ(B*Rt(-a/b, S(3)) - S(2)*C*Rt(-a/b, S(3))**S(2))

cons891 = CustomConstraint(cons_f891)

def cons_f892(a, A, C, b):
    return ZeroQ(A - S(2)*C*Rt(-a/b, S(3))**S(2))

cons892 = CustomConstraint(cons_f892)

def cons_f893(a, A, B, b):
    return Or(ZeroQ(-A**S(3)*b + B**S(3)*a), Not(RationalQ(a/b)))

cons893 = CustomConstraint(cons_f893)

def cons_f894(a, b):
    return Not(RationalQ(a/b))

cons894 = CustomConstraint(cons_f894)

def cons_f895(a, A, C, b):
    return Not(RationalQ(a, b, A, C))

cons895 = CustomConstraint(cons_f895)

def cons_f896(a, A, b, C, B):
    return ZeroQ(A - B*(a/b)**(S(1)/3) + C*(a/b)**(S(2)/3))

cons896 = CustomConstraint(cons_f896)

def cons_f897(a, C, B, b):
    return ZeroQ(B*(a/b)**(S(1)/3) - C*(a/b)**(S(2)/3))

cons897 = CustomConstraint(cons_f897)

def cons_f898(a, A, C, b):
    return ZeroQ(A + C*(a/b)**(S(2)/3))

cons898 = CustomConstraint(cons_f898)

def cons_f899(a, A, b, C, B):
    return ZeroQ(A + B*(-a/b)**(S(1)/3) + C*(-a/b)**(S(2)/3))

cons899 = CustomConstraint(cons_f899)

def cons_f900(a, C, B, b):
    return ZeroQ(B*(-a/b)**(S(1)/3) + C*(-a/b)**(S(2)/3))

cons900 = CustomConstraint(cons_f900)

def cons_f901(a, A, C, b):
    return ZeroQ(A + C*(-a/b)**(S(2)/3))

cons901 = CustomConstraint(cons_f901)

def cons_f902(a, b):
    return RationalQ(a/b)

cons902 = CustomConstraint(cons_f902)

def cons_f903(a, b):
    return Greater(a/b, S(0))

cons903 = CustomConstraint(cons_f903)

def cons_f904(a, b):
    return Less(a/b, S(0))

cons904 = CustomConstraint(cons_f904)

def cons_f905(x, n, Pq):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Less(Expon(Pq, x), n)

cons905 = CustomConstraint(cons_f905)

def cons_f906(a, d, c, b):
    return ZeroQ(c*Rt(b/a, S(3)) - d*(-sqrt(S(3)) + S(1)))

cons906 = CustomConstraint(cons_f906)

def cons_f907(a, d, c, b):
    return NonzeroQ(c*Rt(b/a, S(3)) - d*(-sqrt(S(3)) + S(1)))

cons907 = CustomConstraint(cons_f907)

def cons_f908(a, d, c, b):
    return ZeroQ(c*Rt(b/a, S(3)) - d*(S(1) + sqrt(S(3))))

cons908 = CustomConstraint(cons_f908)

def cons_f909(a, d, c, b):
    return NonzeroQ(c*Rt(b/a, S(3)) - d*(S(1) + sqrt(S(3))))

cons909 = CustomConstraint(cons_f909)

def cons_f910(a, d, c, b):
    return ZeroQ(S(2)*c*Rt(b/a, S(3))**S(2) - d*(-sqrt(S(3)) + S(1)))

cons910 = CustomConstraint(cons_f910)

def cons_f911(a, d, c, b):
    return NonzeroQ(S(2)*c*Rt(b/a, S(3))**S(2) - d*(-sqrt(S(3)) + S(1)))

cons911 = CustomConstraint(cons_f911)

def cons_f912(a, d, c, b):
    return ZeroQ(-a*d**S(4) + b*c**S(4))

cons912 = CustomConstraint(cons_f912)

def cons_f913(a, d, c, b):
    return NonzeroQ(-a*d**S(4) + b*c**S(4))

cons913 = CustomConstraint(cons_f913)

def cons_f914(x, Pq):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return NonzeroQ(Coeff(Pq, x, S(0)))

cons914 = CustomConstraint(cons_f914)

def cons_f915(x, n, Pq):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(PolyQ(Pq, x**(n/S(2))))

cons915 = CustomConstraint(cons_f915)

def cons_f916(x, n, Pq):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Equal(Expon(Pq, x), n + S(-1))

cons916 = CustomConstraint(cons_f916)

def cons_f917(x, n, Pq):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return LessEqual(n + S(-1), Expon(Pq, x))

cons917 = CustomConstraint(cons_f917)

def cons_f918(x, n, Pq):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Or(PolyQ(Pq, x), PolyQ(Pq, x**n))

cons918 = CustomConstraint(cons_f918)

def cons_f919(n, v, Pq):
    return PolyQ(Pq, v**n)

cons919 = CustomConstraint(cons_f919)

def cons_f920(a, n, b, f, d, c, p, e):
    return ZeroQ(a*c*f - e*(a*d + b*c)*(n*(p + S(1)) + S(1)))

cons920 = CustomConstraint(cons_f920)

def cons_f921(a, n, b, g, d, c, p, e):
    return ZeroQ(a*c*g - b*d*e*(S(2)*n*(p + S(1)) + S(1)))

cons921 = CustomConstraint(cons_f921)

def cons_f922(p, n):
    return ZeroQ(n*(p + S(1)) + S(1))

cons922 = CustomConstraint(cons_f922)

def cons_f923(a, n, f, b, d, m, c, p, e):
    return ZeroQ(a*c*f*(m + S(1)) - e*(a*d + b*c)*(m + n*(p + S(1)) + S(1)))

cons923 = CustomConstraint(cons_f923)

def cons_f924(a, n, b, g, d, m, c, p, e):
    return ZeroQ(a*c*g*(m + S(1)) - b*d*e*(m + S(2)*n*(p + S(1)) + S(1)))

cons924 = CustomConstraint(cons_f924)

def cons_f925(x, Px):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return PolynomialQ(Px, x)

cons925 = CustomConstraint(cons_f925)

def cons_f926(a, n, b, d, p, e):
    return ZeroQ(a*e - b*d*(n*(p + S(1)) + S(1)))

cons926 = CustomConstraint(cons_f926)

def cons_f927(a, n, f, d, c, p):
    return ZeroQ(a*f - c*d*(S(2)*n*(p + S(1)) + S(1)))

cons927 = CustomConstraint(cons_f927)

def cons_f928(a, d, c, f):
    return ZeroQ(a*f + c*d)

cons928 = CustomConstraint(cons_f928)

def cons_f929(a, n, b, d, m, p, e):
    return ZeroQ(a*e*(m + S(1)) - b*d*(m + n*(p + S(1)) + S(1)))

cons929 = CustomConstraint(cons_f929)

def cons_f930(a, n, f, d, c, m, p):
    return ZeroQ(a*f*(m + S(1)) - c*d*(m + S(2)*n*(p + S(1)) + S(1)))

cons930 = CustomConstraint(cons_f930)

def cons_f931(n, n3):
    return ZeroQ(-S(3)*n + n3)

cons931 = CustomConstraint(cons_f931)

def cons_f932(a, n, g, b, d, c, p, e):
    return ZeroQ(a**S(2)*g*(n + S(1)) - c*(a*e - b*d*(n*(p + S(1)) + S(1)))*(n*(S(2)*p + S(3)) + S(1)))

cons932 = CustomConstraint(cons_f932)

def cons_f933(a, n, f, b, d, c, p, e):
    return ZeroQ(a**S(2)*f*(n + S(1)) - a*c*d*(n + S(1))*(S(2)*n*(p + S(1)) + S(1)) - b*(a*e - b*d*(n*(p + S(1)) + S(1)))*(n*(p + S(2)) + S(1)))

cons933 = CustomConstraint(cons_f933)

def cons_f934(a, n, b, g, d, c, p):
    return ZeroQ(a**S(2)*g*(n + S(1)) + b*c*d*(n*(p + S(1)) + S(1))*(n*(S(2)*p + S(3)) + S(1)))

cons934 = CustomConstraint(cons_f934)

def cons_f935(a, n, f, b, d, c, p):
    return ZeroQ(a**S(2)*f*(n + S(1)) - a*c*d*(n + S(1))*(S(2)*n*(p + S(1)) + S(1)) + b**S(2)*d*(n*(p + S(1)) + S(1))*(n*(p + S(2)) + S(1)))

cons935 = CustomConstraint(cons_f935)

def cons_f936(a, n, b, d, c, p, e):
    return ZeroQ(a*c*d*(n + S(1))*(S(2)*n*(p + S(1)) + S(1)) + b*(a*e - b*d*(n*(p + S(1)) + S(1)))*(n*(p + S(2)) + S(1)))

cons936 = CustomConstraint(cons_f936)

def cons_f937(a, n, b, d, c, p):
    return ZeroQ(a*c*d*(n + S(1))*(S(2)*n*(p + S(1)) + S(1)) - b**S(2)*d*(n*(p + S(1)) + S(1))*(n*(p + S(2)) + S(1)))

cons937 = CustomConstraint(cons_f937)

def cons_f938(n, q):
    return ZeroQ(-n/S(2) + q)

cons938 = CustomConstraint(cons_f938)

def cons_f939(n, r):
    return ZeroQ(-S(3)*n/S(2) + r)

cons939 = CustomConstraint(cons_f939)

def cons_f940(n, s):
    return ZeroQ(-S(2)*n + s)

cons940 = CustomConstraint(cons_f940)

def cons_f941(n, m):
    return ZeroQ(S(2)*m - n + S(2))

cons941 = CustomConstraint(cons_f941)

def cons_f942(a, d, c, g):
    return ZeroQ(a*g + c*d)

cons942 = CustomConstraint(cons_f942)

def cons_f943(a, e, h, c):
    return ZeroQ(-S(3)*a*h + c*e)

cons943 = CustomConstraint(cons_f943)

def cons_f944(b, h, c, g):
    return ZeroQ(-S(2)*b*h + c*g)

cons944 = CustomConstraint(cons_f944)

def cons_f945(a, b, g, d, c, e):
    return ZeroQ(S(3)*a*g - S(2)*b*e + S(3)*c*d)

cons945 = CustomConstraint(cons_f945)

def cons_f946(d, e, c, b):
    return ZeroQ(-S(2)*b*e + S(3)*c*d)

cons946 = CustomConstraint(cons_f946)

def cons_f947(a, n, Pq, x, b, c):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Or(NiceSqrtQ(-S(4)*a*c + b**S(2)), Less(Expon(Pq, x), n))

cons947 = CustomConstraint(cons_f947)

def cons_f948(c):
    return PosQ(c)

cons948 = CustomConstraint(cons_f948)

def cons_f949(c):
    return NegQ(c)

cons949 = CustomConstraint(cons_f949)

def cons_f950(x, n, Pq):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(PolyQ(Pq, x**n))

cons950 = CustomConstraint(cons_f950)

def cons_f951(m):
    return NegativeIntegerQ(m + S(-1)/2)

cons951 = CustomConstraint(cons_f951)

def cons_f952(n, j):
    return NonzeroQ(-j + n)

cons952 = CustomConstraint(cons_f952)

def cons_f953(p, j, n):
    return ZeroQ(j*p + j - n + S(1))

cons953 = CustomConstraint(cons_f953)

def cons_f954(p, n, j):
    return NegativeIntegerQ((j - n*p - n + S(-1))/(j - n))

cons954 = CustomConstraint(cons_f954)

def cons_f955(p, j):
    return NonzeroQ(j*p + S(1))

cons955 = CustomConstraint(cons_f955)

def cons_f956(p, j, n):
    return RationalQ(j, n, p)

cons956 = CustomConstraint(cons_f956)

def cons_f957(j, n):
    return Less(S(0), j, n)

cons957 = CustomConstraint(cons_f957)

def cons_f958(p, j):
    return Less(j*p + S(1), S(0))

cons958 = CustomConstraint(cons_f958)

def cons_f959(p, n):
    return NonzeroQ(n*p + S(1))

cons959 = CustomConstraint(cons_f959)

def cons_f960(p, j, n):
    return Greater(j*p + S(1), -j + n)

cons960 = CustomConstraint(cons_f960)

def cons_f961(p):
    return PositiveIntegerQ(p + S(1)/2)

cons961 = CustomConstraint(cons_f961)

def cons_f962(p, j):
    return ZeroQ(j*p + S(1))

cons962 = CustomConstraint(cons_f962)

def cons_f963(n):
    return NonzeroQ(n + S(-2))

cons963 = CustomConstraint(cons_f963)

def cons_f964(j, n):
    return RationalQ(j, n)

cons964 = CustomConstraint(cons_f964)

def cons_f965(n, j):
    return Less(S(2)*n + S(-2), j, n)

cons965 = CustomConstraint(cons_f965)

def cons_f966(n, j):
    return PosQ(-j + n)

cons966 = CustomConstraint(cons_f966)

def cons_f967(j, n):
    return IntegerQ(j/n)

cons967 = CustomConstraint(cons_f967)

def cons_f968(p, n, j, m):
    return ZeroQ(-j + m + n*p + n + S(1))

cons968 = CustomConstraint(cons_f968)

def cons_f969(j, c):
    return Or(IntegerQ(j), PositiveQ(c))

cons969 = CustomConstraint(cons_f969)

def cons_f970(p, n, j, m):
    return NegativeIntegerQ((j - m - n*p - n + S(-1))/(j - n))

cons970 = CustomConstraint(cons_f970)

def cons_f971(p, j, m):
    return NonzeroQ(j*p + m + S(1))

cons971 = CustomConstraint(cons_f971)

def cons_f972(c, j, n):
    return Or(IntegersQ(j, n), PositiveQ(c))

cons972 = CustomConstraint(cons_f972)

def cons_f973(n):
    return NonzeroQ(n**S(2) + S(-1))

cons973 = CustomConstraint(cons_f973)

def cons_f974(n, p, j, m):
    return RationalQ(j, m, n, p)

cons974 = CustomConstraint(cons_f974)

def cons_f975(p, j, m):
    return Less(j*p + m + S(1), S(0))

cons975 = CustomConstraint(cons_f975)

def cons_f976(p, j, m, n):
    return Greater(j*p + m + S(1), -j + n)

cons976 = CustomConstraint(cons_f976)

def cons_f977(p, j, m, n):
    return PositiveQ(j*p + j + m - n + S(1))

cons977 = CustomConstraint(cons_f977)

def cons_f978(p, j, m):
    return NegativeQ(j*p + m + S(1))

cons978 = CustomConstraint(cons_f978)

def cons_f979(p, j, m):
    return ZeroQ(j*p + m + S(1))

cons979 = CustomConstraint(cons_f979)

def cons_f980(j, m):
    return ZeroQ(-j/S(2) + m + S(1))

cons980 = CustomConstraint(cons_f980)

def cons_f981(j, k):
    return NonzeroQ(-j + k)

cons981 = CustomConstraint(cons_f981)

def cons_f982(n, k):
    return IntegerQ(k/n)

cons982 = CustomConstraint(cons_f982)

def cons_f983(jn, j, n):
    return ZeroQ(jn - j - n)

cons983 = CustomConstraint(cons_f983)

def cons_f984(a, n, b, d, j, m, c, p):
    return ZeroQ(a*d*(j*p + m + S(1)) - b*c*(m + n + p*(j + n) + S(1)))

cons984 = CustomConstraint(cons_f984)

def cons_f985(e, j):
    return Or(PositiveQ(e), IntegersQ(j))

cons985 = CustomConstraint(cons_f985)

def cons_f986(p, j, m):
    return RationalQ(j, m, p)

cons986 = CustomConstraint(cons_f986)

def cons_f987(j, m):
    return Inequality(S(0), Less, j, LessEqual, m)

cons987 = CustomConstraint(cons_f987)

def cons_f988(e, j):
    return Or(PositiveQ(e), IntegerQ(j))

cons988 = CustomConstraint(cons_f988)

def cons_f989(p, j, m, n):
    return Or(Less(j*p + m, S(-1)), And(IntegersQ(m + S(-1)/2, p + S(-1)/2), Less(p, S(0)), Less(m, -n*p + S(-1))))

cons989 = CustomConstraint(cons_f989)

def cons_f990(e, j, n):
    return Or(PositiveQ(e), IntegersQ(j, n))

cons990 = CustomConstraint(cons_f990)

def cons_f991(p, n, j, m):
    return NonzeroQ(j*p + m - n + S(1))

cons991 = CustomConstraint(cons_f991)

def cons_f992(p, n, j, m):
    return NonzeroQ(m + n + p*(j + n) + S(1))

cons992 = CustomConstraint(cons_f992)

def cons_f993(n, j):
    return Not(And(ZeroQ(n + S(-1)), ZeroQ(j + S(-1))))

cons993 = CustomConstraint(cons_f993)

def cons_f994(n):
    return Less(S(-1), n, S(1))

cons994 = CustomConstraint(cons_f994)

def cons_f995(m):
    return Greater(m**S(2), S(1))

cons995 = CustomConstraint(cons_f995)

def cons_f996(j, n):
    return PositiveIntegerQ(j, n, j/n)

cons996 = CustomConstraint(cons_f996)

def cons_f997(j, n):
    return PositiveIntegerQ(j, n)

cons997 = CustomConstraint(cons_f997)

def cons_f998(j, n):
    return Less(j, n)

cons998 = CustomConstraint(cons_f998)

def cons_f999(a, d, b):
    return ZeroQ(S(27)*a**S(2)*d + S(4)*b**S(3))

cons999 = CustomConstraint(cons_f999)

def cons_f1000(a, d, b):
    return NonzeroQ(S(27)*a**S(2)*d + S(4)*b**S(3))

cons1000 = CustomConstraint(cons_f1000)

def cons_f1001(a, d, c):
    return ZeroQ(S(27)*a*d**S(2) + S(4)*c**S(3))

cons1001 = CustomConstraint(cons_f1001)

def cons_f1002(a, d, c):
    return NonzeroQ(S(27)*a*d**S(2) + S(4)*c**S(3))

cons1002 = CustomConstraint(cons_f1002)

def cons_f1003(d, c, b):
    return ZeroQ(-S(3)*b*d + c**S(2))

cons1003 = CustomConstraint(cons_f1003)

def cons_f1004(a, c, b):
    return ZeroQ(-S(3)*a*c + b**S(2))

cons1004 = CustomConstraint(cons_f1004)

def cons_f1005(a, c, b):
    return NonzeroQ(-S(3)*a*c + b**S(2))

cons1005 = CustomConstraint(cons_f1005)

def cons_f1006(d, c, b):
    return NonzeroQ(-S(3)*b*d + c**S(2))

cons1006 = CustomConstraint(cons_f1006)

def cons_f1007(x, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return PolyQ(u, x, S(3))

cons1007 = CustomConstraint(cons_f1007)

def cons_f1008(x, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(CubicMatchQ(u, x))

cons1008 = CustomConstraint(cons_f1008)

def cons_f1009(x, v):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return PolyQ(v, x, S(3))

cons1009 = CustomConstraint(cons_f1009)

def cons_f1010(x, v, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(And(LinearMatchQ(u, x), CubicMatchQ(v, x)))

cons1010 = CustomConstraint(cons_f1010)

def cons_f1011(g, f):
    return ZeroQ(f + g)

cons1011 = CustomConstraint(cons_f1011)

def cons_f1012(a, c):
    return PosQ(a**S(2)*(S(2)*a - c))

cons1012 = CustomConstraint(cons_f1012)

def cons_f1013(a, c):
    return NegQ(a**S(2)*(S(2)*a - c))

cons1013 = CustomConstraint(cons_f1013)

def cons_f1014(d, e, c, b):
    return ZeroQ(S(8)*b*e**S(2) - S(4)*c*d*e + d**S(3))

cons1014 = CustomConstraint(cons_f1014)

def cons_f1015(p):
    return UnsameQ(p, S(2))

cons1015 = CustomConstraint(cons_f1015)

def cons_f1016(p):
    return UnsameQ(p, S(3))

cons1016 = CustomConstraint(cons_f1016)

def cons_f1017(x, v):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return PolynomialQ(v, x)

cons1017 = CustomConstraint(cons_f1017)

def cons_f1018(x, v):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Equal(Exponent(v, x), S(4))

cons1018 = CustomConstraint(cons_f1018)

def cons_f1019(a, d, c, b):
    return ZeroQ(S(8)*a**S(2)*d - S(4)*a*b*c + b**S(3))

cons1019 = CustomConstraint(cons_f1019)

def cons_f1020(d, b):
    return ZeroQ(-b + d)

cons1020 = CustomConstraint(cons_f1020)

def cons_f1021(a, e):
    return ZeroQ(-a + e)

cons1021 = CustomConstraint(cons_f1021)

def cons_f1022(a, x, c, b):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return SumQ(Factor(a*x**S(4) + a + b*x**S(3) + b*x + c*x**S(2)))

cons1022 = CustomConstraint(cons_f1022)

def cons_f1023(D, x):
    return FreeQ(D, x)

cons1023 = CustomConstraint(cons_f1023)

def cons_f1024(A, b, d, C, c, e, B):
    return ZeroQ(B**S(2)*d - S(2)*B*(S(2)*A*e + C*c) + S(2)*C*(A*d + C*b))

cons1024 = CustomConstraint(cons_f1024)

def cons_f1025(a, A, d, C, c, e, B):
    return ZeroQ(-S(4)*A*B*C*d + S(4)*A*e*(S(2)*A*C + B**S(2)) - B**S(3)*d + S(2)*B**S(2)*C*c - S(8)*C**S(3)*a)

cons1025 = CustomConstraint(cons_f1025)

def cons_f1026(A, d, C, c, e, B):
    return PosQ(C*(C*(-S(4)*c*e + d**S(2)) + S(2)*e*(-S(4)*A*e + B*d)))

cons1026 = CustomConstraint(cons_f1026)

def cons_f1027(d, A, C, b):
    return ZeroQ(A*d + C*b)

cons1027 = CustomConstraint(cons_f1027)

def cons_f1028(a, e, A, C):
    return ZeroQ(-A**S(2)*e + C**S(2)*a)

cons1028 = CustomConstraint(cons_f1028)

def cons_f1029(A, d, C, c, e):
    return PosQ(C*(-S(8)*A*e**S(2) + C*(-S(4)*c*e + d**S(2))))

cons1029 = CustomConstraint(cons_f1029)

def cons_f1030(A, d, C, c, e, B):
    return NegQ(C*(C*(-S(4)*c*e + d**S(2)) + S(2)*e*(-S(4)*A*e + B*d)))

cons1030 = CustomConstraint(cons_f1030)

def cons_f1031(A, d, C, c, e):
    return NegQ(C*(-S(8)*A*e**S(2) + C*(-S(4)*c*e + d**S(2))))

cons1031 = CustomConstraint(cons_f1031)

def cons_f1032(A, b, d, C, D, c, e, B):
    return ZeroQ(S(4)*d*(-S(2)*B*e + D*c)**S(2) - S(4)*(-S(2)*B*e + D*c)*(-S(8)*A*e**S(2) - S(4)*C*c*e + S(2)*D*b*e + S(3)*D*c*d) + S(8)*(-S(4)*C*e + S(3)*D*d)*(-A*d*e - C*b*e + D*b*d))

cons1032 = CustomConstraint(cons_f1032)

def cons_f1033(a, A, b, d, C, D, c, e, B):
    return ZeroQ(S(8)*a*(-S(4)*C*e + S(3)*D*d)**S(3) - S(8)*c*(-S(2)*B*e + D*c)**S(2)*(-S(4)*C*e + S(3)*D*d) + S(8)*d*(-S(4)*A*e + D*b)*(-S(2)*B*e + D*c)*(-S(4)*C*e + S(3)*D*d) + S(8)*d*(-S(2)*B*e + D*c)**S(3) - S(4)*e*(-S(4)*A*e + D*b)*(S(2)*(-S(4)*A*e + D*b)*(-S(4)*C*e + S(3)*D*d) + S(4)*(-S(2)*B*e + D*c)**S(2)))

cons1033 = CustomConstraint(cons_f1033)

def cons_f1034(A, b, d, D, c, e):
    return ZeroQ(D**S(2)*c**S(2)*d - D*c*(-S(8)*A*e**S(2) - S(4)*C*c*e + S(2)*D*b*e + S(3)*D*c*d) + S(2)*(-S(4)*C*e + S(3)*D*d)*(-A*d*e - C*b*e + D*b*d))

cons1034 = CustomConstraint(cons_f1034)

def cons_f1035(a, A, b, d, D, c, e, B):
    return ZeroQ(S(54)*D**S(3)*a*d**S(3) - S(6)*D*c*d*(-S(2)*B*e + D*c)**S(2) + S(6)*D*d**S(2)*(-S(4)*A*e + D*b)*(-S(2)*B*e + D*c) + S(2)*d*(-S(2)*B*e + D*c)**S(3) - e*(-S(4)*A*e + D*b)*(S(6)*D*d*(-S(4)*A*e + D*b) + S(4)*(-S(2)*B*e + D*c)**S(2)))

cons1035 = CustomConstraint(cons_f1035)

def cons_f1036(a, e, c, f):
    return ZeroQ(a*e**S(2) - c*f**S(2))

cons1036 = CustomConstraint(cons_f1036)

def cons_f1037(d, e, f, b):
    return ZeroQ(b*e**S(2) - d*f**S(2))

cons1037 = CustomConstraint(cons_f1037)

def cons_f1038(a, e, c, f):
    return NonzeroQ(a*e**S(2) - c*f**S(2))

cons1038 = CustomConstraint(cons_f1038)

def cons_f1039(d, e, f, b):
    return NonzeroQ(b*e**S(2) - d*f**S(2))

cons1039 = CustomConstraint(cons_f1039)

def cons_f1040(p, n):
    return ZeroQ(-S(2)*n + p)

cons1040 = CustomConstraint(cons_f1040)

def cons_f1041(d, c, b):
    return ZeroQ(b*c**S(2) - d**S(2))

cons1041 = CustomConstraint(cons_f1041)

def cons_f1042(d, c, b):
    return NonzeroQ(b*c**S(2) - d**S(2))

cons1042 = CustomConstraint(cons_f1042)

def cons_f1043(a, b, x, d, c, e):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, b, c, d, e), x)

cons1043 = CustomConstraint(cons_f1043)

def cons_f1044(a, b, d, c, e):
    return NonzeroQ(a*e**S(4) + b*d**S(2)*e**S(2) + c*d**S(4))

cons1044 = CustomConstraint(cons_f1044)

def cons_f1045(d, e, c, b):
    return ZeroQ(b*d*e**S(2) + S(2)*c*d**S(3))

cons1045 = CustomConstraint(cons_f1045)

def cons_f1046(d, e, c, b):
    return NonzeroQ(b*d*e**S(2) + S(2)*c*d**S(3))

cons1046 = CustomConstraint(cons_f1046)

def cons_f1047(a, d, e, c):
    return NonzeroQ(a*e**S(4) + c*d**S(4))

cons1047 = CustomConstraint(cons_f1047)

def cons_f1048(d, e, A, B):
    return ZeroQ(A*e + B*d)

cons1048 = CustomConstraint(cons_f1048)

def cons_f1049(a, c, A, B):
    return ZeroQ(A*c + B*a)

cons1049 = CustomConstraint(cons_f1049)

def cons_f1050(a, d, e, c):
    return ZeroQ(a*e + c*d)

cons1050 = CustomConstraint(cons_f1050)

def cons_f1051(a, f, g, d, b, h, c, e):
    return ZeroQ(-f**S(2)*(a*h**S(2) - b*g*h + c*g**S(2)) + (-d*h + e*g)**S(2))

cons1051 = CustomConstraint(cons_f1051)

def cons_f1052(f, g, d, b, h, c, e):
    return ZeroQ(-S(2)*d*e*h + S(2)*e**S(2)*g - f**S(2)*(-b*h + S(2)*c*g))

cons1052 = CustomConstraint(cons_f1052)

def cons_f1053(v, f, x, u, j):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(And(LinearMatchQ(u, x), QuadraticMatchQ(v, x), Or(ZeroQ(j), ZeroQ(f + S(-1)))))

cons1053 = CustomConstraint(cons_f1053)

def cons_f1054(v, f, x, g, u, k, j, h):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return ZeroQ(-f**S(2)*k**S(2)*(g**S(2)*Coefficient(v, x, S(2)) - g*h*Coefficient(v, x, S(1)) + h**S(2)*Coefficient(v, x, S(0))) + (g*Coefficient(u, x, S(1)) - h*(f*j + Coefficient(u, x, S(0))))**S(2))

cons1054 = CustomConstraint(cons_f1054)

def cons_f1055(e, c, f):
    return ZeroQ(-c*f**S(2) + e**S(2))

cons1055 = CustomConstraint(cons_f1055)

def cons_f1056(x, v, u, f):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return ZeroQ(-f**S(2)*Coefficient(v, x, S(2)) + Coefficient(u, x, S(1))**S(2))

cons1056 = CustomConstraint(cons_f1056)

def cons_f1057(a, i, c, g):
    return ZeroQ(-a*i + c*g)

cons1057 = CustomConstraint(cons_f1057)

def cons_f1058(p, m):
    return IntegersQ(p, S(2)*m)

cons1058 = CustomConstraint(cons_f1058)

def cons_f1059(i, c, m):
    return Or(IntegerQ(m), PositiveQ(i/c))

cons1059 = CustomConstraint(cons_f1059)

def cons_f1060(i, h, c, b):
    return ZeroQ(-b*i + c*h)

cons1060 = CustomConstraint(cons_f1060)

def cons_f1061(c, i):
    return Not(PositiveQ(i/c))

cons1061 = CustomConstraint(cons_f1061)

def cons_f1062(w, x, v):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return QuadraticQ(List(v, w), x)

cons1062 = CustomConstraint(cons_f1062)

def cons_f1063(v, f, x, u, w, j):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(And(LinearMatchQ(u, x), QuadraticMatchQ(List(v, w), x), Or(ZeroQ(j), ZeroQ(f + S(-1)))))

cons1063 = CustomConstraint(cons_f1063)

def cons_f1064(v, f, x, k, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return ZeroQ(-f**S(2)*k**S(2)*Coefficient(v, x, S(2)) + Coefficient(u, x, S(1))**S(2))

cons1064 = CustomConstraint(cons_f1064)

def cons_f1065(p, n):
    return ZeroQ(p - S(2)/n)

cons1065 = CustomConstraint(cons_f1065)

def cons_f1066(a, c, b):
    return ZeroQ(a**S(2) - b**S(2)*c)

cons1066 = CustomConstraint(cons_f1066)

def cons_f1067(a, d, b):
    return ZeroQ(a**S(2) - b**S(2)*d)

cons1067 = CustomConstraint(cons_f1067)

def cons_f1068(a, c, b):
    return ZeroQ(a + b**S(2)*c)

cons1068 = CustomConstraint(cons_f1068)

def cons_f1069(a, e, c, b):
    return ZeroQ(a + b**S(2)*c*e)

cons1069 = CustomConstraint(cons_f1069)

def cons_f1070(d, c, b):
    return ZeroQ(-b*d**S(2) + c**S(2))

cons1070 = CustomConstraint(cons_f1070)

def cons_f1071(e, b):
    return ZeroQ(-b**S(2) + e)

cons1071 = CustomConstraint(cons_f1071)

def cons_f1072(a, d, c, b):
    return ZeroQ(-a*d + b*c, S(0))

cons1072 = CustomConstraint(cons_f1072)

def cons_f1073(a, n, A, d, B):
    return ZeroQ(-A**S(2)*d*(n + S(-1))**S(2) + B**S(2)*a)

cons1073 = CustomConstraint(cons_f1073)

def cons_f1074(n, A, d, c, B):
    return ZeroQ(S(2)*A*d*(n + S(-1)) + B*c)

cons1074 = CustomConstraint(cons_f1074)

def cons_f1075(m, k):
    return ZeroQ(k - S(2)*m + S(-2))

cons1075 = CustomConstraint(cons_f1075)

def cons_f1076(a, n, A, d, m, B):
    return ZeroQ(-A**S(2)*d*(m - n + S(1))**S(2) + B**S(2)*a*(m + S(1))**S(2))

cons1076 = CustomConstraint(cons_f1076)

def cons_f1077(n, A, d, m, c, B):
    return ZeroQ(-S(2)*A*d*(m - n + S(1)) + B*c*(m + S(1)))

cons1077 = CustomConstraint(cons_f1077)

def cons_f1078(a, f, b, d, g, c):
    return ZeroQ(-S(12)*a**S(3)*g**S(2) + a**S(2)*c*f**S(2) + S(2)*a*b*g*(a*f + S(3)*c*d) + S(9)*c**S(3)*d**S(2) - c*d*f*(S(6)*a*c + b**S(2)))

cons1078 = CustomConstraint(cons_f1078)

def cons_f1079(a, f, g, d, b, c, e):
    return ZeroQ(a**S(3)*c*f**S(2)*g + S(2)*a**S(3)*g**S(2)*(-S(6)*a*g + b*f) - S(3)*a**S(2)*c**S(2)*d*f*g + S(3)*c**S(4)*d**S(2)*e - c**S(3)*d*(-S(12)*a*d*g + a*e*f + S(2)*b*d*f))

cons1079 = CustomConstraint(cons_f1079)

def cons_f1080(a, d, c, f):
    return NonzeroQ(-a*f + S(3)*c*d)

cons1080 = CustomConstraint(cons_f1080)

def cons_f1081(a, g, b, d, c):
    return NonzeroQ(-S(2)*a**S(2)*g + b*c*d)

cons1081 = CustomConstraint(cons_f1081)

def cons_f1082(a, f, b, d, g, c):
    return NonzeroQ(S(4)*a**S(2)*g - a*b*f + b*c*d)

cons1082 = CustomConstraint(cons_f1082)

def cons_f1083(a, g, f, d, b, c):
    return PosQ((S(12)*a**S(2)*g**S(2) - a*c*f**S(2) + f*(-S(2)*a*b*g + S(3)*c**S(2)*d))/(c*g*(-a*f + S(3)*c*d)))

cons1083 = CustomConstraint(cons_f1083)

def cons_f1084(a, g, f, d, c):
    return ZeroQ(-S(12)*a**S(3)*g**S(2) + a**S(2)*c*f**S(2) - S(6)*a*c**S(2)*d*f + S(9)*c**S(3)*d**S(2))

cons1084 = CustomConstraint(cons_f1084)

def cons_f1085(a, f, g, d, c, e):
    return ZeroQ(-S(12)*a**S(4)*g**S(3) + a**S(3)*c*f**S(2)*g - S(3)*a**S(2)*c**S(2)*d*f*g - a*c**S(3)*d*(-S(12)*d*g + e*f) + S(3)*c**S(4)*d**S(2)*e)

cons1085 = CustomConstraint(cons_f1085)

def cons_f1086(a, g, f, d, c):
    return PosQ((S(12)*a**S(2)*g**S(2) - a*c*f**S(2) + S(3)*c**S(2)*d*f)/(c*g*(-a*f + S(3)*c*d)))

cons1086 = CustomConstraint(cons_f1086)

def cons_f1087(v):
    return SumQ(v)

cons1087 = CustomConstraint(cons_f1087)

def cons_f1088(x, v, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(And(MonomialQ(u, x), BinomialQ(v, x)))

cons1088 = CustomConstraint(cons_f1088)

def cons_f1089(x, v, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(And(ZeroQ(Coefficient(u, x, S(0))), ZeroQ(Coefficient(v, x, S(0)))))

cons1089 = CustomConstraint(cons_f1089)

def cons_f1090(x, n, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    def _cons_f_u(n1, v):
        return ZeroQ(n - n1 - 1)
    cons_u = CustomConstraint(_cons_f_u)
    pat = Pattern(UtilityOperator(x**WC('n1', S(1))*WC('v', S(1)), x), cons_u)
    result_matchq = is_match(UtilityOperator(u, x), pat)
    return Not(result_matchq)

cons1090 = CustomConstraint(cons_f1090)

def cons_f1091(e, g):
    return ZeroQ(e + g)

cons1091 = CustomConstraint(cons_f1091)

def cons_f1092(d, f):
    return ZeroQ(d + f + S(-2))

cons1092 = CustomConstraint(cons_f1092)

def cons_f1093(A, f, d, C, e):
    return ZeroQ(A*e**S(2) + C*d*f)

cons1093 = CustomConstraint(cons_f1093)

def cons_f1094(d, e, B, C):
    return ZeroQ(-B*e + S(2)*C*(d + S(-1)))

cons1094 = CustomConstraint(cons_f1094)

def cons_f1095(F, x):
    return FreeQ(F, x)

cons1095 = CustomConstraint(cons_f1095)

def cons_f1096(e, A, C):
    return ZeroQ(A*e**S(2) + C)

cons1096 = CustomConstraint(cons_f1096)

def cons_f1097(n):
    return Not(PositiveQ(n))

cons1097 = CustomConstraint(cons_f1097)

def cons_f1098(y, v):
    return ZeroQ(-v + y)

cons1098 = CustomConstraint(cons_f1098)

def cons_f1099(y, w):
    return ZeroQ(-w + y)

cons1099 = CustomConstraint(cons_f1099)

def cons_f1100(y, z):
    return ZeroQ(y - z)

cons1100 = CustomConstraint(cons_f1100)

def cons_f1101(a, x, n, b):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, b, n), x)

cons1101 = CustomConstraint(cons_f1101)

def cons_f1102(a, n, b, x, p):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, b, n, p), x)

cons1102 = CustomConstraint(cons_f1102)

def cons_f1103(a, n, b, x, m, p):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, b, m, n, p), x)

cons1103 = CustomConstraint(cons_f1103)

def cons_f1104(w, v):
    return ZeroQ(-v + w)

cons1104 = CustomConstraint(cons_f1104)

def cons_f1105(p, r, q):
    return ZeroQ(p - q*(r + S(1)))

cons1105 = CustomConstraint(cons_f1105)

def cons_f1106(r):
    return NonzeroQ(r + S(1))

cons1106 = CustomConstraint(cons_f1106)

def cons_f1107(p, r):
    return IntegerQ(p/(r + S(1)))

cons1107 = CustomConstraint(cons_f1107)

def cons_f1108(p, r, q, s):
    return ZeroQ(p*(s + S(1)) - q*(r + S(1)))

cons1108 = CustomConstraint(cons_f1108)

def cons_f1109(p, m, q):
    return ZeroQ(p + q*(m*p + S(1)))

cons1109 = CustomConstraint(cons_f1109)

def cons_f1110(p, r, m, q):
    return ZeroQ(p + q*(m*p + r + S(1)))

cons1110 = CustomConstraint(cons_f1110)

def cons_f1111(p, q, m, s):
    return ZeroQ(p*(s + S(1)) + q*(m*p + S(1)))

cons1111 = CustomConstraint(cons_f1111)

def cons_f1112(s):
    return NonzeroQ(s + S(1))

cons1112 = CustomConstraint(cons_f1112)

def cons_f1113(s, q):
    return IntegerQ(q/(s + S(1)))

cons1113 = CustomConstraint(cons_f1113)

def cons_f1114(q, s, m, p, r):
    return ZeroQ(p*(s + S(1)) + q*(m*p + r + S(1)))

cons1114 = CustomConstraint(cons_f1114)

def cons_f1115(x, u, m):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FunctionOfQ(x**(m + S(1)), u, x)

cons1115 = CustomConstraint(cons_f1115)

def cons_f1116(w, x):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return NFreeQ(w, x)

cons1116 = CustomConstraint(cons_f1116)

def cons_f1117(x, z):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return NFreeQ(z, x)

cons1117 = CustomConstraint(cons_f1117)

def cons_f1118(a, m):
    return Not(And(EqQ(a, S(1)), EqQ(m, S(1))))

cons1118 = CustomConstraint(cons_f1118)

def cons_f1119(x, m, v):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(And(EqQ(v, x), EqQ(m, S(1))))

cons1119 = CustomConstraint(cons_f1119)

def cons_f1120(x, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(RationalFunctionQ(u, x))

cons1120 = CustomConstraint(cons_f1120)

def cons_f1121(x, v):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(LinearQ(v, x))

cons1121 = CustomConstraint(cons_f1121)

def cons_f1122(r, s):
    return PosQ(-r + s)

cons1122 = CustomConstraint(cons_f1122)

def cons_f1123(x, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Not(AlgebraicFunctionQ(u, x))

cons1123 = CustomConstraint(cons_f1123)

def cons_f1124(a, n, b, x, m, c):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return FreeQ(List(a, b, c, m, n), x)

cons1124 = CustomConstraint(cons_f1124)

def cons_f1125(u):
    return NonsumQ(u)

cons1125 = CustomConstraint(cons_f1125)

def cons_f1126(x, u, m):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return Or(Greater(m, S(0)), Not(AlgebraicFunctionQ(u, x)))

cons1126 = CustomConstraint(cons_f1126)

def cons_f1127(x, u):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return EulerIntegrandQ(u, x)

cons1127 = CustomConstraint(cons_f1127)

def cons_f1128(n):
    return EvenQ(n)

cons1128 = CustomConstraint(cons_f1128)

def cons_f1129(n):
    return OddQ(n)

cons1129 = CustomConstraint(cons_f1129)

def cons_f1130(x, u, v):
    if isinstance(x, (int, Integer, float, Float)):
        return False
    return PolynomialInQ(v, u, x)

cons1130 = CustomConstraint(cons_f1130)

def cons_f1131(a, d):
    return ZeroQ(a + d)

cons1131 = CustomConstraint(cons_f1131)

def cons_f1132(c, b):
    return ZeroQ(b + c)

cons1132 = CustomConstraint(cons_f1132)

def cons_f1133(n, m):
    return ZeroQ(m + n)

cons1133 = CustomConstraint(cons_f1133)

def cons_f1134(p, q):
    return ZeroQ(p + q)

cons1134 = CustomConstraint(cons_f1134)

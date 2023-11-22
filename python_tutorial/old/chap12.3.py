# CHAPITRE 12.3
# INTRODUCTION AU CALCUL SCIENTIFIQUE - sympy
import sympy

# Reference :
#   http://docs.sympy.org/latest/tutorial/index.html

# Ce module permet de faire des mathématiques symboliques, c'est-à-dire des mathématiques où
# l'on peut manipuler des expressions sous une forme symbolique plutôt que numérique.

# Le module sympy possède notamment les mêmes fonctionnalités que le module math,
# mais contrairement à ce dernier, la valeur des fonctions n'est pas évaluée sous une forme numérique par défaut :
print(sympy.sqrt(8))

# On remarque ici que sympy a su simplifier l'expression symbolique. Il sait aussi faire de la magie de « notebook » (Pour Jupyter notebook)
# et afficher ses expressions symboliques sous une forme de graphiques. Il suffit d'exécuter la fonction init_printing qui possède plusieurs options :
# sympy.init_printing()

# Avec sympy, on peut créer de nouveaux symboles de la façon suivante :
x, y = sympy.symbols('x y')
exp = x + 3*y**2
print(exp)
# Il importe ici de comprendre que les attributs Python x et y sont associés à des objets sympy qui sont des variables symboliques.

# À partir de là, on peut faire ce qu'on veut comme opération symbolique.
# Differentielle par rapport a y
print(sympy.diff(exp, y))

# Integrale par rapport a x
print(sympy.integrate(exp, x))

# Integrale sur un interval
print(sympy.integrate(exp, (x, 1, 5)))

# Resoudre pour x = 0
print(sympy.solve(x**2-3))

# Resolution symbolique d'une equation differentielle
# la deuxieme partie suit le signe d'egalite
from sympy import *
f = Function('f')
diffeq = Eq(f(x) + f(x).diff(x,x), sin(x))
print(diffeq)
print(dsolve(diffeq, f(x)))


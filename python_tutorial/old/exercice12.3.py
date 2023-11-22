# EXERCICE 12.3
# LE CALCUL SCIENTIFIQUE EN PYTHON
# 12.3 sympy
import sympy
import numpy
import matplotlib.pyplot as plt

# 12.3.1 DERIVE D'UNE FONCTION
# Trouver la deriver de sin(x)/x
# Valider graphiquement

# 12.3.1 REPONSE
x = sympy.symbols('x')
exp = sympy.sin(x)/x
print(exp)
derive = sympy.diff(exp, x)
print(derive)

#valider fonctions
def func(x):
    return numpy.sin(x)/x

def deri(x):
    return numpy.cos(x)/x - numpy.sin(x)/x**2

x = numpy.linspace(-10, 10, 200)
plt.plot(x, func(x), '-b', label="function")
plt.plot(x, deri(x), '-g', label="derive")
plt.title("Graphique de la fonction et sa derivee")
plt.legend()
plt.show()

# 12.3.2 INTEGRATION D'UNE FONCTION
# Trouver l'integrale de f
sympy.init_printing()
a, x = sympy.symbols('a x')
f = sympy.integrate(1/sympy.cos(a*x)**2, x)
print(f)
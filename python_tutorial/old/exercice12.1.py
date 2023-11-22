# EXERCICE 12.1
# LE CALCUL SCIENTIFIQUE EN PYTHON
# 12.1 numpy

# 12.1.1 CREATION D'UN TABLEAU NUMPY
# Définissez une fonction nommée créer_table qui accepte trois arguments :
#
# un nombre entier de lignes ;
# un nombre entier de colonnes ;
# et une valeur initiale en virgule flottante ;
# et qui retourne un tableau numpy à deux dimensions dont tous les éléments sont initialisés avec la valeur spécifiée.
import numpy

# 12.1.1 REPONSE
def creer_table(ligne, colonne, valeur):
    return numpy.array([valeur for _ in range(ligne*colonne)]).reshape(ligne, colonne)

print(creer_table(3,4,5))

# 12.1.2 DECOUPAGE D'UN TABLEAU NUMPY
# Soit un tableau numpy à deux dimensions nommé table, préexistant dans le contexte de cet exercice. Affichez le sous-tableau
# formé des  𝑚  dernières lignes et des  𝑛  premières colonnes de la table,  𝑚  et  𝑛  étant des variables également
# préexistantes dans le contexte de cet exercice.
table = numpy.random.random((20, 5)) #  matrice 20 par 5 de float aleatoire entre 0 et 1. Remarquez que l'argument est un tuple
m = 7
n = 2

# 12.1.2 REPONSE
sousTable = table[-m:, :n]
print(table, '\n\n')
print(sousTable, '\n\n')

# 12.1.3 RESOLUTION D'UN SYSTEME D'EQUATION LINEAIRE
# Soit un systeme d'equation lineaire a 3 inconnus, 3 equations
# On peut expremier ce system sous forme de matrice
# A les coefficients
# v les variables
# C les reponses
# Resoudre ce system Av = C

# 12.1.3 REPONSE
A = numpy.array([[1, 2, 3], [2, 3, 4], [3, 2, 3]])
C = numpy.array([3, 2, 1])
# v = (A-1)*C
Amoins = numpy.linalg.inv(A)
V = numpy.dot(Amoins, C)
print(V, '\n\n')

# 12.1.4 MOYENNE ET VARIANCE
# Soit la variable x, préexistante dans le contexte de cet exercice. Cette variable est associée à un tableau numpy à une dimension.
# Affectez respectivement aux variables moyenne et variance les moyenne et variance des éléments de ce tableau.
# Notez bien que pour résoudre cet exercice, il vous suffit de faire appel aux fonctions mean et var, préexistantes dans le module numpy.
# Inutile de programmer vos propres boucles pour faire ces calculs.
#
# Profitez de cet exercice pour survoler les nombreuses fonctionnalités disponibles dans le module numpy, dont notamment celles relatives :
#
# à la transformée de Fourrier ;
# aux fonctions financières ;
# à l'algèbre linéaire ;
# aux fonctions mathématiques ;
# aux polynômes ;
# aux tri et comptage ;
# et aux statistiques.
x = numpy.random.random(100)

# 12.1.4 REPONSE
moyenne = numpy.mean(x)
variance = numpy.var(x)

# 12.1.5 MATRICE 8X8
# En utilisant le module numpy, créez une matrice nommée échecs, de dimensions  8×8 , contenant des  0  et des  1  selon le patron d'un jeu d'échecs,
# c'est-à-dire où les cases noires sont des  0  et les cases blanches des  1 . Supposer que la case  (0,0)  est noire.

# 12.1.5 REPONSE
matrice = numpy.ones((8,8), dtype=numpy.int)
matrice[::2, 1::2] = 0
matrice[1::2, ::2] = 0
print(matrice)
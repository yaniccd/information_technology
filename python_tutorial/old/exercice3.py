# EXERCICES 3
#Notion de Fonctions
import math
import random

#3.1.1 PERIMETRE D'UN RECTANGLE
#definir une fonction qui retourne le perimetre d'un rectangle

#3.1.1 REPONSE
def perimetre_rectangle(longeur, hauteur):
    return 2*longeur+2*hauteur

#3.1.2 SURFACE D'UN RECTANGLE
#definir une fonction qui retourne l'aire d'un rectangle

#3.1.2 REPONSE
def aire_rectangle(longeur, hauteur):
    return longeur*hauteur

#3.1.3 PERIMETRE D'UN CERCLE
#definir une fonction calculant le perimetre d'un cercle en fonction de son rayon

#3.1.3 REPONSE
def perimetre_cercle(rayon):
    return 2*math.pi*rayon

#3.1.4 VOLUME D'UNE SPHERE
#definir une fonction qui retourne le volume d'une sphere en fonction de son rayon

#3.1.4 REPONSE
def volume_sphere(rayon):
    return 4/3*math.pi*rayon**3

#3.2.1 AFFECTATION SIMPLE D'UN BOOLEEN
#affecter vrai a vrai et faux a faux

#3.2.1 REPONSE
vrai = True
faux = False
print(vrai!=faux)

#3.2.2 EXPRESSION BOOLEENNE
#Affecter a test la valeur du test a-b > 0
a = random.randint(1, 99)
b = random.randint(1,99)

#3.2.2 REPONSE
test = a-b > 0
print(test)

# 3.2.3 AFFECTATION D'UNE EXPRESSION
# Affectez à la variable test la valeur de l'expression  (𝑎∧𝑏)∨ w ou w est la negation de(𝑐∧𝑑)
a = random.choice([True, False])
b = random.choice([True, False])
c = random.choice([True, False])
d = random.choice([True, False])

#3.2.3 REPONSE
test = (a and b) or not (c and d)
print(test)

# 3.3.1 UN CAS PARMIS QUATRE
# Soit la variable  𝑥  et les trois cas suivants :
# −327≤𝑥≤−299  ou  17≤𝑥≤23
# 123<𝑥≤213  ou  𝑥≥900  
# −77≤𝑥<3  ou  𝑥<−800
# Écrivez une fonction nommée cas qui reçoit l'argument  𝑥  et retourne le numéro du cas correspondant.
#  Si aucun des cas ne correspond à la valeur de  𝑥  retourner -1.

# 3.3.1 REPONSE
def cas(x):
    if (x >= -327 and x <= -299) or (x >= 17 and x <= 23):
        return 1
    elif (x > 123 and x < 213) or (x >= 900):
        return 2
    elif (x >= -77 and x < 3) or (x < -800):
        return 3
    else:
        return -1

# 3.3.2 MINIMUM DE TROIS VALEUR
# Definir une fonction, l'aide du if, qui retourne le minimum de trois entrees

# 3.3.2 REPONSE
def minimum(x,y,z):
    min = x
    if y < min :
        min = y
    if z < min :
        min = z
    return min

# 3.3.3 VALEUR ABSOLUE
#ecrire une fonction qui retourne la valeur absolu d'un nombre a l'aide d'un if

# 3.3.3 REPONSE
def absolu(x):
    if x < 0:
        return -x
    return x

# 3.3.4 MAXIMUM DES VALEURS ABSOLU
# definir une fonction qui retourne le max des valeurs absolus de trois variables

# 3.3.4 REPONSE
def max_absolu(x, y, z):
    return max(abs(x), abs(y), abs(z))

# QUIZ 1. CONVERSION EN RADIAN
# definir une fonction qui prend en entre un degre et retourne sa valeur en radian

# QUIZ 1. REPONSE
def convertir_radian(degre):
    return (degre % 360)*2*math.pi/360.0
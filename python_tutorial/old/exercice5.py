#EXERCICES 5
#Retour sur les Fonctions et Complexite Algorithmique
import math
from hypothesis import strategies
import random

# 5.1.1 POSITION SUR LA CIRCONFERENCE D'UN CERCLE
# Définissez une fonction nommée position_xy qui reçoit deux arguments  𝑟  et  𝜃  et retourne un tuple  (𝑥,𝑦)
# correspondant aux coordonnées cartésiennes d'une position à  𝜃  degrés sur la circonférence d'un cercle
# de rayon  𝑟  centré à l'origine.
# il faut egalement convertir l'angle en radian puisque la fonction fonctionne en degree, mais cos et sin
# fonctionnent en radian.

# 5.1.1 REPONSE
def position_xy(r, theta):
    x = r*math.cos(theta*math.pi/180)
    y = r*math.sin(theta*math.pi/180)
    return (x, y)

# 5.1.2 FONCTION MINMAX
# Définissez une fonction nommée minmax qui reçoit en entrée une liste de nombres
# et retourne en sortie un tuple des valeurs minimum et maximum de cette liste.
# Dans le cas où la liste d'entrée serait vide, votre fonction doit retourner un tuple d'objets None.
# Ne pas utiliser min et max

# 5.1.2 REPONSE
def minmax(liste):
    if not liste:
        return None, None
    else:
        min = max = liste[0]
        for valeur in liste[1:]:
            if valeur < min:
                min = valeur
            if valeur > max:
                max = valeur
        return min, max

# 5.1.3 CONVERSION D'ITERABLE EN TUPLE
# Créez un tuple à partir des éléments de la chaîne de caractères Bonjour le monde!, et affectez-le à la variable x.
# Faites de même avec la séquence des entiers allant de -15 à +37 (inclusivement), et affectez le résultat à la variable y.

# 5.1.3 REPONSE
x = tuple('Bonjour le monde!')
y = tuple(range(-15, 38))
print(x)
print(y)

# 5.1.4 DECOUPAGE D'UN TUPLE
# Soit la variable x associée à un tuple préexistant dans le contexte de cet algorithme.
# En débutant par la fin, découpez un élément sur deux de ce tuple et affectez le résultat à la variable y.
x = tuple(strategies.lists(strategies.integers(min_value=-100, max_value=100), min_size=15, max_size=15).example())
print(x)

# 5.1.4 REPONSE
y = x[::-2]
print(y)

# 5.2.1 FONCTION GENERATRICE SIMPLE
# Définissez une fonction génératrice nommée suite qui accepte en entrée un argument  𝑛
# et qui, lorsqu'on itère sur elle, produit la séquence suivante de valeurs :
# 1
# 1+2
# ...
# 1+2+..+n-1+n

#5.2.1 REPONSE
def suite(n):
    retour = 0
    for i in range(1, n+1):
        retour += i
        yield retour

for i in suite(4):
    print(i)

# 5.2.2 FONCTION AVEC ARGUMENT POSITIONEL
# Définissez une fonction nommée écho qui accepte en entrée trois arguments positionnels,
# dont le dernier avec valeur par défaut nulle (0), et qui retourne dans un tuple les valeurs des trois arguments reçus.

# 5.2.2 REPONSE
def echo(a, b, c=0):
    return a, b, c

# 5.2.3 FONCTION AVEC ARGUMENT ETOILE
# Définissez une fonction nommée écho qui accepte en entrée trois arguments positionnels
# en plus d'un argument étoilé, et qui retourne dans un tuple des quatre valeurs reçues en argument.
# Donnez des valeurs par défaut de respectivement -1, -2 et -3 aux trois arguments positionnels de cette fonction.

# 5.2.3 REPONSE
def echo(a=-1, b=-2, c=-3, *d):
    return a, b, c, d

print(echo(1,2,3,4,5))

# 5.2.4 FONCTION AVEC ARGUMENT ETOILE
# Définissez une fonction nommée afficher qui accepte en entrée un nombre arbitraire de valeurs nommées,
# et qui affiche à la console toutes les valeurs reçues en argument lors de l'appel de la fonction.
# Affichez ces valeurs sous la forme suivante&suivante

# 5.2.4 REPONSE
def afficher(**karg):
    for cle in sorted(karg):
        print('{} = {}'.format(cle, karg[cle]))

afficher(abc=123, a=10, toto=5, argument=-2)

# 5.3.1 AFFECTATION D'UNE VALEUR DE RETOUR
# Soit une fonction nommée fonc qui retourne un tuple des coordonnées d'un point en trois dimensions ;
# cette fonction étan préexistante dans le contexte de cet exercice (appelez-là pour voir son résultat).
# En utilisant une seule affectation multiple, affectez les éléments du tuple de retour de cette fonction
# à trois variables nommées x, y et z.
valeur = tuple(random.randint(-10,10) for i in range(3))
def fonc():
    return valeur

# 5.3.1 REPONSE
x,y,z = fonc()

# 5.3.2 AFFECTATION DES ELEMENTS D'UNE LISTE
# En utilisant un seul énoncé, affectez les éléments de cette liste à trois variables nommées a, b et c.
# Faites en sorte que le premier élément soit affecté à a, que le dernier soit affecté à c et que tous
# les autres éléments soient réunis dans une liste affectée à la variable b. Pour ce faire,
# utilisez une variable étoilée dans votre affectation.
liste = [random.randint(1, 5) for i in range(random.randint(2, 15))]

# 5.3.2 REPONSE
a, *b, c = liste
print(a)
print(b)
print(c)

# QUIZ 1. CHAINE FOLDINGO
# Définissez une fonction nommée foldingo qui reçoit en argument une chaîne de caractères et
# retourne cette chaîne, mais transformée de la façon suivante : les caractères d'indice pair
# (y compris 0) en majuscule et les caractères d'indice impair en minuscule.

# QUIZ 1. REPONSE
def foldingo(chaine):
    res = ''
    for position, lettre in enumerate(chaine):
        if position % 2 == 0:
            res += lettre.upper()
        else:
            res += lettre.lower()
    return res

print(foldingo('Ceci est une chaine'))

# QUIZ 2. DISTANCE PARCOURUE
# Définissez une fonction nommée calculer_distance_parcourue qui reçoit en argument une liste de coordonnées 2D
# et retourne la distance euclidienne parcourue. Les coordonnées 2D de cette liste sont des couples  (𝑥,𝑦)
# (tuples de deux valeurs) correspondants à des points dans le plan cartésien. Vous pouvez par exemple supposer
# que ces points ont été produits par le GPS de votre téléphone cellulaire. Votre fonction doit retourner la distance
# totale parcourue en calculant la somme des distances entre les points.

# QUIZ 2. REPONSE
def calculer_distance_parcourue(liste):
    distance = 0
    if len(liste) < 2:
        return distance
    actuel = liste[0]
    for tuple in liste[1:]:
        distance += math.sqrt((tuple[0] - actuel[0])**2 + (tuple[1] - actuel[1]))
        actuel = tuple
    return distance

print(calculer_distance_parcourue([(0, 0), (1, 1), (2, 2)]))

# QUIZ 3. VALEUR D'UNE LISTE DE CHAINES
# Définissez une fonction nommée valeur_liste qui reçoit en argument une liste de chaînes de caractères et retourne
# la valeur totale de cette liste en dollars. Dans le contexte de cet exercice, la valeur d'une chaîne de caractères est définie de la façon suivante :
# une chaîne constituée d'un nombre suivi du caractère $ possède la valeur du nombre en dollars ;
# toute autre chaîne n'a aucune valeur.
def isnumber(string):
    try:
        float(string)
    except:
        return False
    return True

liste = ['10$', 'chaussette', '12.55$', 'pizza', '0.57$', 'Rien', '7$', 'condom', '2$']

# QUIZ 3. REPONSE
def valeur_liste(liste):
    valeur = 0
    for chaine in liste:
        if chaine and isnumber(chaine[:-1]) and chaine[-1] == '$':
            valeur += float(chaine[:-1])
    return valeur

print(valeur_liste(liste))
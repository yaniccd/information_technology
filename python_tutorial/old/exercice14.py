# EXERCICE 14
# EXERCICES DE REVISION

import numpy as np

# QUIZ 1. CALCUL RECURSIF D'UNE PUISSANCE
# Écrivez le code Python d'une fonction nommée puissance (𝑥,𝑛) , qui élève un nombre  𝑥  à la puissance entière  𝑛 , en utilisant la formule de récurrence

# QUIZ 1. REPONSE
def puissance(x,n):
    if n < 0:
        raise ValueError('Exposant negatif')
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif x == 1:
        return 1
    elif n % 2 == 0:
        return puissance(x*x, n/2)
    return x*puissance()(x*x, n/2)

# QUIZ 2. SAPIN DE NOEL
# Définissez une fonction génératrice nommée sapin qui accepte en argument un nombre entier et qui retourne un itérable sur un nombre correspondant de chaînes
# de caractères. Chaque chaîne retournée représente une couche d'un sapin de Noël. Par exemple, en itérant sur les dix chaînes de sapin(10) et en les affichant
#  à la console, on produirait la sortie suivante :
#          x
#         x x
#        x - x
#       x - - x
#      x - - - x
#     x - - - - x
#    x - - - - - x
#   x - - - - - - x
#  x - - - - - - - x
# x - - - - - - - - x
# Notez bien que votre fonction génératrice ne doit rien afficher, elle doit se contenter de retourner les chaînes demandées dans la bonne séquence.
# Notez aussi que les x et les - ci-dessus sont séparés par des espaces.
#
# Si jamais l'argument de votre fonction est négatif, celle-ci devrait soulever une exception de type AssertionError.
#
# Prenez soin de bien tester votre solution dans votre notebook avant de la soumettre au serveur.

# QUIZ 2. REPONSE
def sapin(n):
    assert isinstance(n, int) and n >= 0
    if n > 0:
        yield ' '*(n-1) + 'x'
        for i in range(1, n):
            yield ' '*(n-1-i) + 'x' + ' -'*(i-1) + ' x'

for i in sapin(10):
    print(i)

# QUIZ 3. PALINDROME
#Définissez une fonction nommée palindrome qui accepte en argument une séquence (e.g. str, tuple ou list) et retourne si oui ou non celle-ci forme un palindrome

def palindrome(n):
    for a,b in zip(n, reversed(n)):
        if a != b :
            return False
    return True

print(palindrome("anana"))
print(palindrome("ananas"))

# QUIZ 4. SOMME RECURSIVE
#Définissez une fonction nommée somme capable de récursivement faire la somme des éléments d'un objet itérable, y compris les éléments qui sont eux-mêmes itérables.
#1 lorsqu'un élément est un nombre entier ou à virgule flottante, ajoutez simplement ce nombre à votre somme ;
#2 lorsqu'un élément est un tuple, une liste ou un ensemble, ajoutez à votre somme le résultat d'un appel récursif sur cet élément ;
#3 lorsqu'un élément est un dictionnaire, ajoutez à votre somme le résultat d'un appel récursif sur l'itérable des valeurs de cet élément (voir la méthode values) ;
#4 lorsqu'un élément est une chaîne de caractères, ignorez simplement cet élément ;
#5 lorsqu'un élément est un tableau numpy (numpy.ndarray), ajouter à votre somme la somme des éléments du tableau (voir la méthode sum) ;
#6 pour toute autre type d'élément, soulevez une exception de type TypeError.


def somme(iterable):
    res = 0
    for n in iterable:
        if isinstance(n, (int, float)):
            res += n
        elif isinstance(n, (tuple, list, set)):
            res += somme(n)
        elif isinstance(n, dict):
            res += somme(n.values())
        elif isinstance(n, str):
            continue
        elif isinstance(n, np.ndarray):
            res += n.sum()
        else:
            raise TypeError("Type Invalide")
    return res

test = [
  'cool',
  [1, {'a': {2, 3, 4, 5}, 'b':[{1: [6, 7], 2: 'nop'}]}, 3.14],
  np.array([1, 2, 3, 4]).reshape((2,2))
]

print(somme('cool'))
print(somme(test))

# QUIZ 5. FILTRE ANTI-MARQUES
# Définissez une classe nommé FiltreAntiMarques permettant de décorer n'importe quelle fonction recevant un nombre arbitraire d'arguments
# positionnels ou nommés. Votre décorateur doit analyser tous les arguments reçus et s'assurer qu'aucun d'entre eux n'est une chaîne de caractère appartenent à l'ensemble :
# {'coke', 'fanta', 'orangina', 'pepsi', 'sprite'}
# Rendez votre filtre invariant à la casse (majuscule vs minuscule) des chaînes de caractères. Si un argument de la fonction décorée correspond à l'une ou
# l'autre des chaînes de l'ensemble, votre fonction doit soulever une exception de type ValueError


class FiltreAntiMarque:
    def __init__(self, fonction):
        self.fonction = fonction
        self.marque = {'coke', 'fanta', 'orangina', 'pepsi', 'sprite'}

    def __call__(self, *args, **kargs):
        for val in args:
            if not isinstance(val, str):
                continue
            if val.lower() in self.marque:
                raise ValueError("l'argument {} est interdit".format(val))
        for key, val in kargs.items():
            if not isinstance(val, str):
                continue
            if val.lower() in self.marque:
                raise ValueError("l'argument {}={} est interdit".format(key, val))
        return self.fonction(*args, **kargs)

@FiltreAntiMarque
def fct(a, b, c):
    print(a, b, c)

fct("Bonjour", "le", c="monde")
#fct("Bonjour", "le", c="Fanta")

# QUIZ 6 HIERARCHIE DES FORMES
# Ecrire les classes formes et vec

class Vec2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        assert isinstance(other, Vec2D)
        return Vec2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        assert isinstance(other, Vec2D)
        return Vec2D(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        if isinstance(other, Vec2D):
            return self.x == other.x and self.y == other.y
        return False

    def __repr__(self):
        return("Ve2D({},{})".format(self.x, self.y))

    def norme(self):
        return (self.x**2 + self.y**2)**.5


class Forme:
    def __init__(self, org):
        self.org = org

    def perimetre(self):
        raise NotImplementedError("Class abstraite")


class Polygone(Forme):
    def __init__(self, org, pts):
        super().__init__(org)
        self.sommets = pts

    def perimetre(self):
        res = 0
        ptp = self.sommets[0]
        for ptc in self.sommets[1:]:
            res += (ptc - ptp).norme()
            ptp = ptc
        return res

class Rectangle(Polygone):
    def __init__(self, mil, larg, haut):
        pts = [ Vec2D(-larg/2, -haut/2), Vec2D(-larg/2, haut/2), Vec2D(larg/2, haut/2), Vec2D(larg/2, -haut/2)]
        super().__init__(mil, pts)


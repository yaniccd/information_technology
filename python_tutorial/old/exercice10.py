# EXERCICE 10
# RETOUR SUR LA PROGRAMMATION ORIENTEE OBJET

# 10.1.1 CLASSE FRACTION
# Soit la fonction nommée gcd (pour « greatest common divisor »), préexistante dans le contexte de cet exercice.
# Cette fonction accepte deux arguments de type entier et retourne le plus grand diviseur commun de ces deux arguments.
# Par exemple, gcd(14, 21) retourne la valeur 7, puisque 7 est la plus grande valeur qui divise à la fois 14 et 21.
#
# Utilisez cette fonction afin d'implanter une classe nommée Fraction qui encapsule des nombres fractionnaires,
# c'est-à-dire des nombres constitués d'un numérateur et d'un dénominateur.

from math import gcd

class Fraction:
    def __init__(self, num, denum):
        assert(isinstance(num, int) and isinstance(denum, int))
        if(denum == 0): raise ValueError
        self.__num = num
        self.__denum = denum
        self.reduire()

    def reduire(self):
        pgcd = gcd(self.__num, self.__denum)
        self.__num = int(self.__num/pgcd)
        self.__denum = int(self.__denum/pgcd)

    def getNumerator(self):
        return self.__num

    def getDenominator(self):
        return self.__denum

    def __str__(self):
        return '{}/{}'.format(self.__num, self.__denum)

    def __add__(self, other):
        return Fraction(self.__num*other.getDenominator() + other.getNumerator()*self.__denum, self.__denum*other.getDenominator())

    def __sub__(self, other):
        return self + (-other)

    def __neg__(self):
        return Fraction(-self.__num, self.__denum)

    def __mul__(self, other):
        return Fraction(self.__num*other.getNumerator(), self.__denum*other.getDenominator())


fr1 = Fraction(1,2)
print(fr1)

fr2 = Fraction(5,7)
print(fr2)

print(fr1+fr2)
print(fr1*fr2)

fr3 = Fraction(4,8)
print(fr3)

print(fr1+fr3)

# 10.1.2 LE LIEVRE ET LA TORTUE
# Définissez deux classes nommées Lievre et Tortue, toutes deux dérivées de la classe Coureur.
# Cette dernière est ce qu'on appelle une classe abstraite, dans le sens qu'on ne peut définir d'instance pour cette classe,
# car une de ses méthodes est incomplète. On peut cependant procéder par héritage, afin de compléter les interfaces et
# en faire des classes concrètes pour lesquelles ont pourra construire des instances.
# our vos deux classes Lievre et Tortue, vous devez définir un constructeur qui initialisera les variables d'instance
# min et max utilisées par la méthode courir de la classe Coureur. Pour la classe Lievre, vous devez fixer la valeur de
# min à 0 et la valeur de max à 5. Pour la classe Tortue, vous devez fixer la valeur de min à 2 et max à 3. Notez que
# ces valeurs, qui correspondent à des vitesses moyennes de 2.5 unités de distance par unité de temps, autant pour le lièvre
# que la tortue, ont été choisies afin de rendre la course intéressante. Le lièvre peut bien sûr courir plus rapidement
# que la tortue, mais également plus lentement. Comme le dit si bien la fable de La Fontaine, rien ne sert de courir  il faut partir à point...
#
# Finalement, vous devez implanter une fonction nommée course acceptant les trois arguments suivants :
#
# une instance de lièvre ;
# une instance de tortue ;
# une distance totale à parcourir pour compléter la course.
# Votre fonction doit simuler une course entre le lièvre et la tortue. À chaque itération de la course (une unité de temps),
#  votre fonction doit appeler la méthode courir du lièvre et de la tortue, afin de déterminer la distance parcourue durant
# cette itération. Cette méthode retourne un nombre aléatoire d'unités de distance parcourue, qui dépend des variables min et
# max (0-5 pour le lièvre et 2-3 pour la tortue). Votre fonction doit retourner un tuple contenant le vainqueur de la course ainsi
# que le nombre d'itérations qui a été nécessaire pour parcourir la distance demandée. Pour désigner le vainqueur, utilisez l'une des
# trois chaînes de caractères suivantes : 'lievre', 'tortue' ou 'match nul'.
#
# Votre fonction ne doit rien afficher, mais simplement retourner le tuple demandé.
import random

class Coureur(object):
    def __init__(self):
        raise NotImplementedError(
            'Vous ne devez pas implementer cette classe'
            'Vous pouvez l"utiliser pour de l"heritage'
        )
    def courir(self):
        return random.randint(self.min, self.max)

# 10.1.2 REPONSE
class Lievre(Coureur):
    def __init__(self):
        self.min = 0
        self.max = 5

class Tortue(Coureur):
    def __init__(self):
        self.min = 2
        self.max = 3

def course(lievre, tortue, distance):
    distTortue = 0
    distLievre = 0
    for i in range(1, distance // 2 + 2):    # plus longueur course possible
        distTortue += tortue.courir()
        distLievre += lievre.courir()
        if distLievre >= distance or distTortue >= distance:
            if distLievre == distTortue:
                return 'match nul', i
            elif distLievre > distTortue:
                return 'Lievre', i
            return 'Tortue', i

lievre = Lievre()
tortue = Tortue()
print(course(lievre, tortue, 30))

# 10.2.1 DIAGRAMME DE CLASSE
# Voir l'enonce dans le doc word

# 10.2.1 REPONSE
class A:
    def __init__(self, x, y):
        pass

class B(A):
    def fct1(self, a):
        pass

class C(B):
    def fct2(self, a, b):
        pass

    def fct3(self, a, b, c):
        pass

class D(B):
    def fct4(self, w, z):
        pass

# 10.2.2 CLASSE FORME, POLYGONE, RECTANGLE
# Voir l'enonce dans le doc word
class Vec2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Additionner avec un autre vecteur
        assert isinstance(other, Vec2D)
        return Vec2D(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        # Tester l'equivalence
        assert isinstance(other, Vec2D)
        return self.x == other.x and self.y == other.y

    def __sub__(self, other):
        # Substraction
        assert isinstance(other, Vec2D)
        return Vec2D(self.x - other.x, self.y - other.y)

    def __repr__(self):
        # Convertir en chaine de caractere
        return 'Vec2D : ({},{})'.format(self.x, self.y)

    def norme(self):
        # Calcul de la norme du vecteur
        return (self.x**2 + self.y**2)**0.5

# 10.2.2 REPONSE
class Forme:
    def __init__(self, org):
        assert isinstance(org, Vec2D)
        self.org = org

    def perimetre(self):
        raise NotImplementedError


class Polygone(Forme):
    def __init__(self, org, pts):
        super().__init__(org)
        self.sommets = pts

    def perimetre(self):
        res = 0
        ptp = self.sommets[0]
        for pts in self.sommets[1:]:
            res += (pts - ptp).norme()
            ptp = pts
        return res


class Rectangle(Polygone):
    def __init__(self, mil, larg, haut):
        pts = [Vec2D(-larg/2, -haut/2),
               Vec2D(-larg/2, haut/2),
               Vec2D(larg/2, haut/2),
               Vec2D(larg/2, -haut/2),
               Vec2D(-larg/2, -haut/2)
               ]
        super().__init__(mil, pts)


rect = Rectangle(Vec2D(0, 0), 2, 2)
print(rect.perimetre())

rect2 = Rectangle(Vec2D(-1, -1), 4, 2)
print(rect2.perimetre())
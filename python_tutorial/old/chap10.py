# CHAPITRE 10
# RETOUR SUR LA PROGRAMMATION ORIENTEE OBJET

# Ce document est un retour sur les notions sous-jacentes à la programmation orientée objet :
#
# Notion de classe et d'encapsulation ;
# Notion d'héritage ;
# Notion de polymorphisme ;
# Langage UML et diagrammes de classe ;
# Notion de composition ;
# Notion d'agrégation.

# Une classe définit deux types d'attribut :
#
# des variables ;
# des méthodes.

# En programmation procédurale, on parle de procédures organisées autour de fonctions auquelles on passe des variables (arguments).
# En programmation orientée objet, on parle plutôt d'objets et de méthodes auxquels on passe des messages.

# Durant l'exécution d'une méthode A1 d'un objet A, un message est envoyé à la méthode B1 d'un objet B.
# En pratique, ce passage de messages prend la forme d'un appel de fonction membre d'une classe
class A:
    def a1(self):
        b = B()
        message = 'Bonjour'
        b.b1(message)

class B:
    def b1(self, message):
        pass

a = A()
a.a1()

# Notion d'encapsulation
# En python, pour protéger un membre d'une classe, on doit mettre deux caractères de soulignement (__) devant son nom.
# Alors, Python refusera à l'utilisateur l'accès à cet attribut. Cependant, l'accès sera permis à l'intérieur des méthodes de la classe.
# Les méthodes qui servent à accéder aux données de la classe s'appellent des accesseurs (en anglais des « getters » et « setters »).
# Dans une certaine mesure, ces méthodes d'interface protègent l'utilisateur des changements d'implantation qui pourraient éventuellement survenir dans la classe.
class Fraction:
    def __init__(self, num, denum):
        assert denum != 0
        self.__num = num
        self.__denum = denum
        self.reduce()

    def getNumerator(self):
        return self.__num

    def getDenumerator(self):
        return self.__denum

    def setNumerator(self, num):
        self.__num = num

    def setDenumerator(self, denum):
        if denum == 0:
            raise ValueError
        self.__denum == denum

    def reduce(self):
        #a faire
        return self

    def __repr__(self):
        return '{}/{}'.format(self.__num, self.__denum)

    def __neg__(self):
        return Fraction(-self.__num, self.__denum)

    def __add__(self, other):
        num = self.__num*other.getDenumerator() + other.getNumerator()*self.__denum
        denum = self.__denum*other.getDenumerator()
        return Fraction(num, denum)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return Fraction(self.__num*other.getNumerator(), self.__denum*other.getDenumerator())

    def __eq__(self, other):
        return self.__num == other.getNumerator() and self.__denum == other.getDenumerator()

    def __neq__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.__num/self.__denum < other.getNumerator()/other.getDenumerator()

    def __le__(self, other):
        return self.__num/self.__denum <= other.getNumerator()/other.getDenumerator()

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

a = Fraction(2,3)
b = Fraction(3,4)
print(a, b)
print (a<b)
print(a>=b)
print(a == b)
print(a-b)
print(a*b)

# Notion d'heritage
# Voir document word

# Notion de polymorphisme
# Voir document word
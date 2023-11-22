# CHAPITRE 6
# Notion de Classes et d'Objets

# Vise a favoriser la reutilisation du code.

# Encapsulation : Une classe reunit des donnes et des fonctions s'appliquant a cette classe
# Heritage : On peut construire une classe a partir d'une autre classe. La classe est alors derivee de son ancetre
# Composition : Au lieu de l'heritage, on peut parfois inclure dans une classe, une instance d'une autre classe
# Polymorphise : La fonction d'une methode varie selon la nature des arguments qu'elle recoit.

# Un objet est une instance d'une classe
# Les attributs d'une classe vont etre accede avec : objet.attribut

# La classe python:
# class <nom>(<classe de base>):
#   var = valeur #variable de classe partagee par toutes les instances
#   def fonc1(self, ...):
#       self.membre = valeur #variable d'instance
#       ...
#   def fonc2( self, ...):
#       ...

# Une classe est une usine a fabriquer des objets

# Exemple de classe


class FirstClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


x = FirstClass()
y = FirstClass()

x.setdata('Le roi')
y.setdata(3.1416)

x.display()
y.display()

# Heritage Python
# Le classe d'heritage peut redefinir une methode

class SecondClass(FirstClass):
    def display(self):
        print('Valeur actuelle = "%s"' % self.data)

z=SecondClass()
z.setdata(42)
z.display()

# Operateur Python
# Un operateur dans une classe est de la forme __x__

# Constructeur
# Le constructeur est une fonction qui initialise l'objet
# le constructeur est toujours __init__

class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

a = ThirdClass('abc')
a.display()
a.setdata('def')
a.display()

class ThirdClass(SecondClass):
    def __init__(self, value):
        self.setdata(value)

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return '[ThirdClass : {}]'.format(self.data)

a = ThirdClass('abc')
a.display()
print(a)
b = a + 'xyz'
b.display()
print(b)

#Fonctions Speciales
# __add__ operateur +
# __sub__ operateur -
# __mul__ operateur *
# __truediv__ operateur /
# __lt__ operateur <
# __gt__ opearteur >
# __le__ operateur <=
# __ge__ operateur >=
# __eq__ operateur ==
# __ne__ opearteur !=
# __init__ constructeur
# __getitem_ operateur [] en lecture
# __setitem__ operateur [] en ecriture
# __str__ pour convertir en string (pour la fonction print())
# __len__ pour determiner la longueur (avec fonction len())
# __bool__ pour convertir en booleen

# super()
# La fonction super() retourne la classe de base

class Toto:
    def fonc(self): pass

class Tata(Toto):
    def fonc(self):
        Toto.fonc(self) #ces deux enonces
        super().fonc() #sont equivalent

# Variable de classe
# Variable partage entre toutes les instances d'une classe

class Toto:
    x = 44

a = Toto()
b = Toto()
print('a.x = ', a.x)
print('b.x = ', b.x)

# Variable d'instance
# Variable propre a chaque instance (objet) de la classe

class Toto:
    x= 'Toto'
    def __init__(self, x):
        self.x = x
    def afficher(self):
        print(self.x, Toto.x)

a = Toto(25)
b = Toto('spam')
a.afficher()
b.afficher()

# Appel d'une methode
# Cas particulier : instance.methode(arg,...)
# Comment attribut de classe : class.methode(instance, arg,...)

# Iterateur
# __iter__ et __next__ doivent etre implemente

class SeqCarre:
    def __init__(self, deb, fin):
        self.val = deb-1
        self.fin = fin

    def __iter__(self):
        return self

    def __next__(self):
        if self.val == self.fin:
            raise StopIteration
        self.val += 1
        return self.val**2

for i in SeqCarre(1,5):
    print(i, end=' ')
print()

iterateur = iter(SeqCarre(1,5))
print(next(iterateur))
print(next(iterateur))

# La meme chose aurait pu etre accompli plus simplement avec une fonction generatrice
def gSeqCarre(deb, fin):
    for i in range(deb, fin+1):
        yield i**2

for i in gSeqCarre(1, 5):
    print(i, end=' ')
print()

# Objet fonction
# Un class qui implement __call__ peut etre utilisee comme une fonction

class Toto:
    def __call__(self, *args, **kargs):
        print('Toto ; ', args, kargs)

a= Toto()
a(1,2,3, x=4, y=5)

# Exemple d'heritage avec une classe employe

class Employe:
    def __init__(self, nom, salaire=0):
        self.nom = nom
        self.salaire = salaire

    def donnerAugmentation(self, pourcent):
        self.salaire *= 1+pourcent

    def travailler(self):
        print(self.nom, ' fait des choses.')

    def __str__(self):
        return ('<Employe : nom=%s, salaire=%s>' % (self.nom, self.salaire))


class Chef(Employe):
    def __init__(self, nom):
        super().__init__(nom, 50000)

    def travailler(self):
        print(self.nom, ' prepare a manger.')


class Serveur(Employe):
    def __init__(self, nom):
        super().__init__(nom, 40000)

    def travailler(self):
        print(self.nom, ' sert les clients')


class RobotPizza(Chef):
    def __init__(self, nom):
        super().__init__(nom)

    def travailler(self):
        print(self.nom, ' prepare la pizza.')


if __name__ == '__main__':
    bob = RobotPizza('bob')
    print(bob)
    bob.travailler()
    bob.donnerAugmentation(0.2)
    print(bob)
    print()

for employe in (Employe, Chef, Serveur, RobotPizza):
    obj = employe(employe.__name__)
    obj.travailler()


# Composition
# La composition est une relation de 'contient un...'
# Exemple la pizzeria n'herite pas de la classe client, mais la pizzaria contient un client
# La pizzeria contient aussi un four

class Client:
    def __init__(self, nom):
        self.nom = nom

    def passerCommande(self, serveur):
        print(self.nom, 'passe une comande a' , serveur)

    def payer(self, serveur):
        print(self.nom, 'paye', serveur)

class Four:
    def cuire(self):
        print('Le four cuit.')

class Pizzeria:
    def __init__(self):
        self.serveur = Serveur('Edouard')
        self.chef = RobotPizza('Bob')
        self.four = Four()

    def commander(self, nom):
        client = Client(nom)
        client.passerCommande(self.serveur)
        self.chef.travailler()
        self.four.cuire()
        client.payer(self.serveur)

if __name__ == '__main__':
    restaurant = Pizzeria()
    restaurant.commander('Gerard')
    print('...')
    restaurant.commander('John')

# CHAPITRE 11
# Retour sur la programmation fonctionnelle
from functools import partial, reduce
from operator import add, concat

# Sommairement, la programmation fonctionnelle se caractérise par les principaux éléments suivants :
#
# le flux des données passe par l'exécution de fonctions ;
# les fonctions ne possèdent aucun état interne, les sorties ne dépendent que des entrées ;
# l'usage de variables globales est donc proscrit.

# Les avantages principaux de ce style de programmation sont :
#
# on peut plus facilement démontrer le bon fonctionnement des programmes ;
# on peut plus facilement les rendre modulaires ;
# on peut aisément composer de nouvelles fonctions en chaînant les sorties d'une fonction dans les entrées d'une autre fonction ;
# on peut plus facilement déboguer et tester les programmes.

# Plan
# Les itérables et les itérateurs ;
# Les expressions génératrices et les listes « en compréhension » ;
# Les fonctions génératrices ;
# Le module itertools ;
# Le module functools ;
# Les fonctions anonymes (lambda) ;
# Les décorateurs (sujet traité dans une leçon distincte).

# ITERABLES ET ITERATEURS
# Un itérable est une classe d'objets qui agrège une séquence d'éléments et sur laquelle on peut itérer,
# c'est-à-dire accéder un par un aux éléments de la séquence. Par exemple, la liste et le tuple sont des itérables.
# Un itérateur est quant à lui l'objet qui permet d'itérer sur un itérable.

# Pour qu'une classe devienne itérable, celle-ci doit simplement définir une méthode nommée __iter__
# qui n'accepte aucun argument, et qui retourne un objet itérateur. Normalement, on ne fait jamais
# directement appel à cette méthode, car on utilise plutôt la fonction standard iter qui effectue cet appel à notre place
# L'objet itérateur doit quant à lui définir une méthode nommée __next__, qui n'accepte aucun argument et retourne
# le prochain élément de la séquence de l'itérable. Lorsqu'il n'y a plus d'élément dans la séquence, la méthode __next__
# doit soulever une exception de type StopIteration pour mettre fin au processus itératif.

# Par exemple, la classe standard list définit la méthode __iter__ :
liste = [2, 4, 6]
print('__iter__' in dir(liste))

# Et l'objet retourné par cette méthode est un objet de la classe list_iterator :
i = iter(liste)
print(i)

# Cette classe spécifique pour itérer sur les listes définit une méthode __next__ :
print('__next__' in dir(i))

# En appelant de façon répétitive la fonction standard next avec l'itérateur en argument, on obtient toutes les valeurs de la séquence :
print(next(i))
print(next(i))
print(next(i))

# Le prochain appel à next va soulever une exception, car la fin de la séquence est atteinte 

# Les étapes précédentes sont exactement ce que fait l'énoncé for suivant :
for i in liste:
    print(i)

# Et cette boucle for est équivalente aux énoncés suivants :
try:
    i = iter(liste)
    while(True):
        print(next(i))
except StopIteration:
    pass

# De nombreuses fonctions standards en Python acceptent des objets itérables :
print(min(liste))
print(max(liste))
print(sum(liste))

# Tout comme les listes et les tuples, les chaînes de caractères sont aussi des itérables,
# de même que les dictionnaires, les fichiers et même les tableaux numpy que nous étudierons plus tard.
#
# Lorsqu'on itère sur un dictionnaire, on itère en fait sur les clés de celui-ci :
dico = {'a':1, 'b':2, 'c':3}
for i in dico:
    print(i)

# Mais on peut faire appel à la méthode items qui permet d'itérer sur des tuples qui associent une clé avec une valeur :
for i in dico.items():
    print(i)

# C'est que la méthode items du dictionnaire retourne un itérable sur les tuples en question.

# De la même façon, la méthode values du dictionnaire retourne un itérable sur les valeurs du dictionnaire :
for i in dico.values():
    print(i)

# En Python 3, la plupart des fonctions standards retournent des objets itérables. Par exemple, la fonction range :
for i in range(3):
    print(i+1)

# Il est important de retenir qu'un itérateur ne peut parcourir un itérable que dans une seule direction,
# du début de la séquence jusqu'à la fin de la séquence.
# On ne peut jamais revenir en arrière.

# EXPRESSION GENERATRICE
# Les expressions génératrices sont des expressions qui utilisent la boucle for et qui retournent un itérable.
# Par exemple
exp = (i**2 for i in range(5,8))
print(next(exp))
# est une expression dont la valeur est un objet de la classe generator, et les objets de cette classe sont itérables
print('__iter__' in dir(exp))
# On peut donc utiliser le résultat d'une expression génératrice partout où l'on peut utiliser un itérable.

for x in exp:
    print('exp =', x)

# On peut utliser les expression generatrice pour construire des listes et des tuples
tup = (2*i for i in range(4))
liste = [2*i for i in range(4)]

# La forme générale de l'expression génératrice peut inclure plusieurs boucles for.
exp = ((x, y) for x in range(3) for y in range(4))
for i in exp:
    print(i)

#  On peut même ajouter une condition après chaque boucle
exp = ((x, y) for x in range(3) for y in range(4) if x != y)
for i in exp:
    print(i)

# Pour créer des itérables, on peut aussi créer ce qu'on appele des fonctions génératrices.
# Celles-ci sont des fonctions en bon et due forme, mais elles retournent systématiquement un itérable.
# Une fonction devient génératrice au moment où l'on utilise l'énoncé yield au lieu de return pour retourner un résultat :
def suiteDesCarres(n):
    i = 0
    while i < n:
        yield i**2
        i+=1

gen = suiteDesCarres(10)
print(gen)

# Ce resultat peut etre utiliser partout ou un iterable est accepte
print(list(gen))

# Il importe de noter, cependant, qu'un objet générateur ne peut servir qu'à
# parcourir une seule fois une séquence. Lorsque la séquence d'éléments est épuisée,
# une exception sera systématiquement soulevée, car un générateur n'est pas un itérable, mais bien un itérateur 
print(tuple(gen))
# Il engendrera donc une séquence vide. Bref, la fonction génératrice est un itérable et, lorsqu'appelée, retourne un itérateur
print(tuple(suiteDesCarres(10)))

# FONCTION STANDARDS
# On a déjà étudié plusieurs des fonctions standards map, filter et zip qui s'inspirent des languages fonctionnels et retournent des itérables :
def majuscule(x):
    return x.upper()

# map permet d'affecter une fonction a tous les elements d'un iterable et retourne le tout sous forme de map
maMap = map(majuscule, ['bonjour', 'le', 'monde'])
liste = list(maMap)
print(liste)

def pair(x):
    return x % 2 == 0

# filter concerve uniquement les elements dont le retour de la fonction est vrai
monFiltre = filter(pair, range(10))
liste = list(monFiltre)
print(liste)

# zip permet de jumelle des iterateurs. Les elements de l'iterateur renvoye sont des tuples
itr1 = [1, 2, 3]
itr2 = (i**2 for i in itr1)
monZip = zip(itr1, itr2)
liste = list(monZip)
print(liste)

# Il y a aussi les fonctions any et all. La fonction any retourne True si au moins un élément de l'itérable
# reçu en argument est vrai, et False s'ils sont tous faux. Similairement, la fonction all retourne True si
# tous les éléments sont vrais, et False si au moins un d'entre eux est faux.

# MODULE itertools
# Ce module contient toute une série de fonctions qui créent des itérateurs ou qui combinent des itérateurs :
#
# itertools.count(n=0): permet de générer une séquence infinie d'entiers croissants ;
# itertools.cycle(iter): permet de générer une séquence infinie qui boucle sur les éléments d'un itérable iter ;
# itertools.repeat(valeur): permet de générer une séquence qui répète sans cesse la même valeur, ou encore un nombre déterminé de fois ;
# itertools.chain(iter1, iter2, ...): retourne un itérateur qui itère en séquence sur tous les itérateurs reçus en argument ;
# itertools.islice(iter, [start], stop, [step]): retourne un itérateur qui effectue un découpage sur l'itérateur reçu en argument ;
# itertools.combinations(iter, r): retourne un itérable sur toutes les combinaisons de r éléments choisis parmi ceux de l'itérable iter ;
# itertools.permutations(iter, r=None): retourne un itérable sur tous les arrangements de r éléments choisis parmi ceux de l'itérable iter ;
# etc.

# MODULE functools
# Ce module contient plusieurs fonctions qui reçoivent en argument une ou plusieurs fonctions, et qui retourne une nouvelle fonction.
# La plus utile d'entre elles se nomme partial. À partir d'une fonction f, elle permet de créer une nouvelle fonction g correspondant à f,
# mais où les valeurs de certains de ses arguments sont fixés. Par exemple :
def f(a, b, c):
    print(a, b, c)

g = partial(f, -1)

f(1,2,3)
g(2,3)

# Une autre fonction intéressante de ce module se nomme reduce. Elle permet d'appliquer un opérateur (une fonction) sur les éléments consécutifs
# d'un itérable et d'accummuler le résultat de cet opérateur. On appelle ça une réduction, car on transforme (réduit) une séquence en une seule valeur.
# Par exemple, en utilisant l'opérateur add, on peut s'en servir pour calculer une somme de nombres :
# Le premier argument est la fonction de réduction, le second est un iterable et le dernier est une valeur initiale optionnelle qui est ajoutée
# devant le premier élément de l'itérable.
print(reduce(add, [1, 2, 3, 4], 10))

# On peut réduire n'importe quelle sorte d'objet, à condition de posséder un opérateur adéquat. Par exemple, la concaténation de
# chaînes de caractères est une opération de réduction :
print(reduce(concat, ['Bonjour ', 'le ', 'monde!'], 'reduce = '))

# FONCTIONS ANONYMES / FONCTIONS LAMBDAS
# n lambda n'est rien d'autre qu'une petite fonction anonyme, c'est-à-dire une fonction qui ne possède pas de nom,
# et qui prend la forme d'une expression 
f = lambda x: x**2
print(f)
print(f(2))

# Par ailleurs, une fonction n'est rien d'autre qu'un objet de la classe function. Également, une fonction est un
# type « callable », c'est-à-dire un objet d'une classe qui possède une méthode nommée __call__ :
print('__call__' in dir(f))

# NOTION DE DECORATEUR
# Les décorateurs sont des fonctions (plus généralement des objets que l'on peut appeler) qui permettent de modifier le comportement d'autres fonctions.

# De façon générale, on sait qu'une fonction n'est rien d'autre qu'un objet qui produit un résultat à partir d'un ensemble d'arguments. On sait aussi qu'une fonction est un objet comme les autres et, qu'à ce titre, elle peut être passée en tant qu'argument à une autre fonction ou retournée par une fonction en tant que résultat de celle-ci. Finalement, on sait qu'une fonction peut définir en son sein d'autres fonctions.
#
# Toutes ces notions sont importantes afin de saisir ce qu'est un décorateur et comment on utilise les décorateurs dans la pratique.
#
# Par exemple, la fonction toto suivante retourne une fonction tata qui ne fait rien :
def toto(fct):
    def tata():
        pass
    return tata

# Cet exemple peu utile jette néanmoins les bases de ce qu'est un décorateur. Notez bien que la fonction toto reçoit un argument fct,
# mais ne fait rien avec celui-ci. Dans un décorateur, l'argument fct correspond à la fonction que l'on désire décorer.
#
# Décorer une fonction consiste à modifier son comportement. Considérons l'exemple suivant :
def verbose(fct):
    def nouvelle_fct(*args, **kargs):
        print('Debut de',fct.__name__ ,'appele avec', args, 'et', kargs)
        resultat = fct(*args, **kargs)
        print('Fin de', fct.__name__)
        return resultat
    return nouvelle_fct

# La fonction verbose est un décorateur de fonction qui permet d'afficher un message avant et après l'exécution d'une fonction quelconque. Par exemple :
def add(a,b):
    print('a+b = ', a+b)

verbose_add = verbose(add)
verbose_add(2, b=3)

# On constate qu'un décorateur est donc utilisé afin d'ajouter un traitement additionnel au traitement habituel d'une fonction existante.
# Le langage Python inclut une notation @ qui simplifie l'application d'un décorateur sur une fonction.
# Ainsi, on obtient le même résultat que précédemment avec les énoncés suivants :
@verbose
def add(a, b):
    print('a+b = ', a+b)

add(3, b=4)

# Un décorateur peut être une fonction, mais également n'importe quel objet que l'on peut appeler.
# Autrement dit, un décorateur peut aussi être une classe pour laquelle on a défini une méthode __call__.
# Par exemple, on peut recoder le décorateur verbose sous la forme de la classe suivante :
class Verbose:
    def __init__(self, fct):
        self.fct = fct

    def __call__(self, *args, **kwargs):
        print('debut de ', self.fct.__name__, 'appeler avec', args, 'et', kwargs)
        result = self.fct(*args, **kwargs)
        print('fin de la fonction')
        return result

@Verbose
def add(a, b):
    print('a+b = ', a+b)

add(3, b=4)

# Ci-dessous un second exemple d'un décorateur qui permet de compter le nombre d'appels effectués à une fonction quelconque :
class Count:
    def __init__(self, fct):
        self.fct = fct
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.fct(*args, **kwargs)

@Count
def add(a, b):
    return a+b

somme = 0
for i in range(20):
    somme += add(1, i+1)

print('somme = ', somme)
print('conteur = ', add.count)

# Mentionnons finalement que les décorateurs peuvent être chaînés, c'est-à-dire qu'un décorateur peut servir à décorer le résultat d'un autre décorateur. Par exemple :
@Count
@Verbose
def add(a, b):
    return a+b

somme = 0
for i in range(20):
    somme += add(i, i+1)
print('somme =', somme)
print('nombre appels a add =', add.count)

# RECURSION ET FONCTION DE RECURSIVE
# Une fonction récursive est une fonction qui s'appelle elle-même, soit directement, soit indirectement.
# souvent, ce n'est pas pas une solution optimale, mais une solution assez simple
# exemple factoriel non recursif
def factorielleNR(n):
    valeur = 1
    for i in range(2, n+1):
        valeur *= i
    return valeur

#exemple factoriel recursif
def factorielleR(n):
    assert n > 0
    if n == 1: return 1
    return n*factorielleR(n-1)

print(factorielleNR(5))
print(factorielleR(5))

# ATTENTION :
#
# la récursion n'est pas une panacée ; si l'on peut aisément la remplacer par une boucle, il vaut mieux le faire ;
# par exemple, l'implantation récursive de la factorielle est inefficace par rapport à l'implantation qui utilise une boucle ;
# mais la récursion permet de traiter des structures arbitraires, ce qui est impossible avec des boucles imbriquées,
# car on ne peut prédire combien de boucles seront nécessaires.

# Par exemple, supposons que l'on veut récursivement sommer les éléments d'une liste de listes de listes, etc.,
# de complexité arbitraire. La solution récursive suivante résoud simplement le problème :
# somme d'une liste de listes
def somme(sequence):
    resultat = 0
    for x in sequence:
        if isinstance(x, list):
            resultat += somme(x)
        else:
            resultat += x
    return resultat

print(somme([1, [2, [3, 4], 5], 6, [7, 8]]))
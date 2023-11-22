# CHAPITRE 8
# Exceptions et traitement des erreurs

# try/except/finally
# raise
# assert

# le bloc try permet de tester du code en prenant en consideration
# la possibilite de soulever une erreur ou un exception
def getItem(obj, indice):
    return obj[indice]

x = 'spam'

i = input("Entrez l'indice de l'element desire : ")
try:
    element = getItem(x, int(i))
    print(element)
except IndexError:
    print('Une exception de type IndexError est survenue.')

# On peut traiter nous meme l'erreur ou laisser python s'en charger
# Dans le second cas, le programme s'arrete

# On peut intentionnellement soulever une erreur
# raise IndexError('Mon message a moi.')

# le bloc else est executer si aucune exception. Permet de verifier si un exception est survenue.
# le bloc finally est toujours exectuer a la fin, meme losrqu'un exception survient

try:
    element = getItem(x, int(i))
    print(element)
except IndexError:
    print('Une exception de type IndexError est survenue.')
else:
    print('aucune erreur survenue')
finally:
    print('le programme peut poursuivre.')

# clause except avec option as
# À la clause except ZeroDivisionError, nous avons ici associé le nom de variable err à l'exception soulevée.
# À partir de là, on peut à l'intérieur de cette clause manipuler l'objet correspondant, récupérer son contexte et
# s'en servir afin de traiter l'exception. Dans cet exemple simple, on ne fait que récupérer le message standard
# associé à l'exception et l'afficher à la console. On aurait tout aussi bien pu décider d'effectuer des traitements
# plus sophistiqués, y compris soulever de nouveau l'exception err afin qu'elle puisse être traitée ailleurs, ou encore
# soulever un autre type d'exception. En fait, on peut placer dans le bloc indenté de la clause n'importe quel énoncé
# Python valide, y compris l'énoncé try.

try:
    element = getItem(x, int(i))
    print(element)
except IndexError as err:
    print(err)

# Exepctions:
# BaseException : classe de base pour toutes les exceptions
# Exception : classe de base pour les exceptions non liées au système
# ArithmeticError
#   OverflowError : lorsque le nombre est trop grand pour être représenté
#   ZeroDivisionError : lors d'une division par zéro
# LookupError
#   IndexError : lorsqu'un indice est invalide (e.g. liste)
#   KeyError : lorsqu'une clé est invalide (e.g. dictionnaire)
# AssertionError : lors de l'échec d'un énoncé assert
# EOFError : lorsque la fonction input atteint la condition de fin de fichier
# ImportError : lorsque l'importation échoue (module introuvable)
# StopIteration : lorsqu'il n'y a plus d'autres valeurs pour un itérateur (ou une fonction génératrice)

# L'expression IndexError('indice invalide') produit une instance de la classe IndexError, et c'est cet objet qui est soulevé.
# err = IndexError("Erreur d'indexe")
# raise err

# On peut creer une objet d'erreur par heritage
class MonErreur(Exception):
    pass

# On peut alors soulever cette erreur
try:
    raise MonErreur('Erreur tres special')
except MonErreur as err:
    print(err)

# Autre exemple de classe d'erreur
class MonErreur(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return str(self.message)

# Les constructeurs des classes d'erreur appellent un nombre arbitraire d'arguments
def action(test):
    if test:
        raise Exception('ceci est mon erreur')
    return 'action normale'

try:
    action(True)
except Exception as err:
    print('monErreur :', err)

def action():
    raise Exception('erreur', 'tres', 'special', 1234)
    return 'action normale'

try:
    action()
except Exception as err:
    print('MonErreur :', err)

# Enonce assert
# Permet de tester une expression
# assert <expression>[, <objet>]

def factorielle(x):
    assert x >= 0, 'x doit etre positif ou nul'
    res = 1
    for i in range(2, x+1):
        res *= i
    return res

# factorielle(-2)

# MODULE ET ORGANISATION DU CODE
# Un module est un fichier de code source.
# Exemple, chap1.py, chap2.py, etc, sont des modules du present projet
# Le main.py est appelle le top level

# Forme 1
# import module as nom
# importe le module au complet et le nomme nom
# la partie as nom est facultative
# pas besoin de la partie .py de module.py
# cet enonce cree un nouvel espace de nom
# on doit utiliser module.nomObjet

# Forme 2
# from module import attribut1, attribut2, ...
# importe tous les attributs enumeres du module
# les attribues sont copies dans l'espace de nom actuel
# On peut utiliser nomObjet directement

# Forme 3
# from module import *
# importe tous les attributs de module
# les attributs sont copies dans l'espace de nom actuel
# Il ne faut cependant pas abuser de ce mécanisme potentiellement dangeureux,
# car à moins d'être sûr qu'aucun attribut du module importé n'entrera en conflit
# avec les attributs du module courant, on s'expose à de mauvaises surprises, et
# à des bogues parfois difficiles à identifier.

# Librairie standard

# Processus d'importation
# 1. Trouver le fichier du module : la recherche s'effectue à plusieurs endroits ;
# 2. Traduire le code Python dans un format intermédiaire (s'il y a lieu) : cette
# étape produit un fichier .pyc pour tous les modules importés ;
# 3. Exécuter le code pour créer les objets et les associer aux attributs.

# Recherche d'un module
# La recherche d'un module s'effectue selon les chemins suivants :
# 1. le répertoire courant du programme ;
# 2. les chemins définis par la variable d'environnement nommée PYTHONPATH ;
# 3. les répertoires de la librairie standard.

# attention de ne pas cacher les modules standards avec vos propres modules!
# Par exemple, si dans votre programme vous créez un fichier nommé math.py, celui-ci remplacera effectivement le module standard math.

# Espace de nom (name space)
# à la suite de l'importation d'un module toto, tous les attributs x, y, z, etc.,
# du fichier toto.py correspondant s'appeleront dorénavant toto.x, toto.y, toto.z, etc.
# Les espaces de noms permettent d'isoler les identifieurs afin d'éviter les conflits :
# deux identifieurs qui portent le même nom peuvent coexister, mais à condition d'appartenir à des espaces de noms différents.

# Fonction reload
# Un module déjà importé ne sera jamais réimporté par l'interpréteur Python :
# l'interpréteur se souvient des importations.
# On peut forcer la réimportation d'un module à l'aide de la fonction reload du module imp :
# permet de modifier le code d'un module sans redémarrer le programme.
# import module
# from imp import reload
# reload(module)

# Groupe de modules
# En mettant plusieurs fichiers dans un même répertoire, on crée un groupe de modules :
# en anglais, on dit un « package ».
# En python, on spécifie un chemin pour se rendre à un fichier en séparant les noms de dossier par des .
# Par exemple :
# import dir.mod
# Pour que Python reconnaisse un répertoire en tant que « package », celui-ci doit contenir un fichier nommé __init__.py :
# généralement, ce fichier contient des énoncés d'initialisation pour le groupe de modules ;
# le fichier peut être vide, mais il doit néanmoins être présent ;
# son contenu sera exécuté avant l'importation du premier module contenu dans le groupe ;
# le groupe possède son propre espace de noms.
# Les groupes de modules permettent de regrouper des modules qui travaillent ensembles et, aussi, d'éviter les conflits de noms de fichier :
# deux modules de même nom peuvent coexister à condition d'appartenir à des groupes différents.

# Variable __name__
# Cette variable __name__ est automatiquement définie pour chaque module (fichier).
# Si le module est exécuté directement par l'interpréteur, alors cette variable prend la valeur __main__.
# Au contraire, si le module est importé, alors la variable prend comme valeur le nom du module.
# Ceci permet à chaque module de déterminer s'il est exécuté en tant que programme ou en tant que module :
# en tant que programme, il a le loisir de pouvoir accomplir une tâche particulière; par exemple se tester lui-même;
# en tant que module, en général, il ne fait rien ; il attend qu'on lui dise quoi faire.
# Par exemple :
if __name__ == '__main__':
    """Test des fonctionnalite du module."""
    pass
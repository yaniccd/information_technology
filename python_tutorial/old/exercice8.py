# EXERCICE 8
# Exceptions et traitement des erreurs

# 8.1.1 SOULEVEMENT D'UNE EXCEPTION
# Définissez une fonction nommée valider_valeur qui accepte trois arguments :
# un nombre ;
# une borne inférieure ;
# une borne supérieure.
# Votre fonction doit retourner le nombre reçu à condition que celui-ci soit
# supérieur ou égal à la borne inférieure et inférieur ou égal à la borne supérieure.
# Sinon, votre fonction doit soulever une exception de type ValueError.

# 8.1.1 REPONSE
def valider_valeur(n, a, b):
    if n < a or n > b:
        raise ValueError("votre valeur {} n'est pas incluse dans [{}, {}]".format(n, a, b))
    return n

# 8.1.2 EXCEPTION MYSTERIEUSE
# On vous demande de définir une fonction nommée fonction qui accepte en argument une valeur entière et qui
# fait appel à la fonction mystérieuse en lui passant cette valeur. Faites en sorte que votre fonction puisse
# traiter n'importe quel type d'exception soulevée par la fonction mystérieuse ; vous pouvez cependant supposer
# qu'elles sont toutes dérivées de la classe Exception.
# Pour traiter l'exception, on vous demande simplement d'afficher le nom de la classe, suivi d'un :, suivi
# du message contenu dans l'exception. Par exemple UneClasse: message où UneClasse est le nom de la
# classe et message le message de l'exception.
# Pour récupérer le nom de la classe, il vous suffit de passer l'exception à la fonction standard type et
# de récupérer son attribut __name__. Ainsi, par exemple, si l'objet associé à l'exception se nomme err,
# alors le nom de sa classe sera type(err).__name__.
# Dans le cas où la fonction mystérieuse retournerait un résultat au lieu de soulever une exception,
# alors afficher simplement ce résultat en utilisant print.
def mystere(n):
    exceptions = [RuntimeError, AssertionError, KeyError, ValueError, IndexError, NameError]
    n = n % len(exceptions)
    if n == 0: return 'Ceci est un resultat mysterieux!'
    raise exceptions[n % len(exceptions)]('Ceci est une exception mysterieuse!')

# 8.1.2 REPONSE
def fonction(entier):
    try:
        res = mystere(entier)
        print(res)
    except Exception as err:
        print('{} : {}'.format(type(err).__name__, err))

fonction(4)
fonction(11)

# 8.2.1 IMPORTATION SIMPLE
# Pour cet exercice, on vous demande simplement d'importer le module standard math,
# mais de faire en sorte qu'il porte le nom mathématique au lieu de math.
# On vous demande également d'afficher à la console (avec print) la liste de tous
# les attributs contenus dans ce module. Pour ce faire, utilisez la fonction standard dir.

# 8.2.1 REPONSE
import math as mathematique
print(dir(mathematique))

# 8.2.2 IMPORTATTION D'ATTRIBUTS PARTICULIERS
# Pour cet exercice, vous devez importer dans le module courant uniquement les attributs
# pi, cos et sin du module math. Ne pas importer le module en entier, mais seulement
# les attributs demandés. Pour ce faire, utilisez la forme from de l'énoncé import.
# Faites cette importation multiple en un seul énoncé (en séparant les trois attributs par des virgules).
# Affichez la valeur de  𝜋  à la console.

# 8.2.2 REPONSE
from math import pi, cos, sin
print(pi)
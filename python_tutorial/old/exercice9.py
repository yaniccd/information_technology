# EXERCICE 9
# Appercu de la librairie standard
import datetime
import random
import re

# 9.1.1 JOUR DE LA SEMAINE
# Définissez une fonction nommée jour_de_la_semaine qui retourne sous forme d'une chaîne de caractères le jour de la semaine ('lundi', 'mardi', etc.)

# 9.1.1 REPONSE
def jourDeLaSemaine(uneDate):
    jour = {
        0: 'Lundi',
        1: 'Mardi',
        2: 'Mercredi',
        3: 'Jeudi',
        4: 'Vendredi',
        5: 'Samedi',
        6: 'Dimanche'
    }
    return jour[datetime.date.weekday(uneDate)]


print(jourDeLaSemaine(datetime.date(2017,1, 5)))

# 9.1.2 NOMBRE DE JOURS, D'HEURES, DE MINUTES ET DE SECONDES
# Définissez une fonction nommée durée qui accepte en argument deux dates
# arbitraires et retourne sous forme d'un tuple les nombres entiers de jours, d'heures, de minutes
# et de secondes entre ces deux dates. Par exemple, si la différence entre les deux dates (le timedelta)
# est d'une journée et 3661 secondes, alors vous devez retourner (1, 1, 1, 1).

# 9.1.2 REPONSE
dt1 = datetime.datetime(2017, 1, 11, 15, 50, 4)
dt2 = datetime.datetime(2030, 3, 4, 22, 44, 2)

def duree(date1, date2):
    delta = date2 - date1
    jour = delta.days
    heure = delta.seconds//3600
    minute = delta.seconds % 3600 // 60
    second = delta.seconds % 60
    return jour, heure, minute, second

# 9.1.3 LOTO 6/49
# Définissez une fonction sans argument nommée combinaison649 permettant de générer aléatoirement une combinaison
# valide pour la loterie 6/49. Pour être valide, une combinaison doit respecter les deux conditions suivantes :
#
# comporter six nombres entiers distincts ;
# chaque nombre ayant une valeur dans l'intervalle  [1,49] .

# 9.1.3 REPONSE
def loto():
    combinaison = [i for i in range(1, 50)]
    random.shuffle(combinaison)
    return sorted(combinaison[:6])

print(loto())

# 9.1.4 EXPRESSION REGULIERE
# Dans une chaîne de caractères, créez une expression régulière qui permet de décrire toutes les chaines de
# caractères comportant exactement un caractère parmi les lettres de a à z, en minuscules ou en majuscules, suivi de
# deux chiffres, suivi d'un ou de deux caractères _. Affectez votre chaîne à la variable rexp.

# 9.1.4 REPONSE
rexp = re.compile('[a-z,A-Z]\d{2}_{1,2}')   #\d est equivalent a [0,9] dans ce module
print(re.findall(rexp, 'a12 a34_ _B27__'))
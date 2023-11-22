# EXERCICE 13
# EXERCICES DE REVISION

# QUIZ 1. DECOUPAGE D'UNE CHAINE
# Soit la chaine de caractères chaine et les entiers i et n. Toutes ces variables sont préexistantes (ne pas changer leur valeur).
#
# En utilisant l'opérateur [], découper une sous-chaîne de n caractères dans chaine à partir de l'indice i.
# Affichez le résultat à l'aide de la fonction print.
chaine = 'Bonjour le monde'
i = 3
n = 7

# QUIZ 1. REPONSE
print(chaine[i:n+i])

# QUIZ 2. FONCTION AVEC ARGUMENT OBLIGATOIREMENT NOMME
# Définissez une fonction nommée écho qui accepte en entrée deux arguments positionnels et trois arguments obligatoirement nommés.
# Les noms de vos arguments obligatoirement nommés doivent être karg1, karg2, et karg3. Donnez respectivement
# à ces trois arguments les valeurs par défaut 1, 2 et 3.
#
# Votre fonction doit par ailleurs retourner le tuple des valeurs reçues pour ses cinq arguments, avec notamment dans
# l'ordre les valeurs des trois arguments nommés karg1, karg2, et karg3.

# QUIZ 2. REPONSE
def echo(arg1, arg2, *, karg1=1, karg2=2, karg3=3):
    return arg1, arg2, karg1, karg2, karg3

# QUIZ 3. PATRON +--+
# Définissez une fonction nommée patron qui accepte en argument deux entiers  𝑚≥0  et  𝑛≥0 , et qui retourne une chaîne
# de caractères formée d'un + initial suivi de  𝑛  fois le patron constitué d'une séquence de  𝑚  caractères - suivis d'un seul +.
# Par exemple, l'appel de patron(9, 3) doit produire la chaîne de caractères suivante :
# +---------+---------+---------+
# Notez bien que votre fonction ne doit rien afficher, mais simplement retourner la chaîne de caractères demandée.
#
# Dans le cas où l'un des arguments  𝑚  et  𝑛  de votre fonction recevrait une valeur plus petite que zéro,
# vous devez soulever une exception de type ValueError.
#
# Prenez soin de bien tester votre solution dans votre notebook avant de la soumettre au serveur. Pour chaque exercice,
# vous n'avez droit qu'à un maximum de trois soumissions avec rétroaction. Après ces trois premiers essais, vous pourrez continuer
# à soumettre de nouvelles solutions, mais vous ne recevrez plus aucune rétroaction. N'oubliez pas que c'est la dernière soumission qui compte,
# peu importe que celle-ci soit meilleure ou pire que la précédente.

# QUIZ 3. REPONSE
def patron(m, n):
    if m < 0 or n < 0:
        raise ValueError
    return '+' + n*(m*'-' + '+')

print(patron(9,3))
print(patron(9,3) == '+---------+---------+---------+')

# QUIZ 4. 0-10-20
# Définissez une fonction nommée patron10 qui accepte en argument deux entiers  𝑚≥0  et  𝑛≥0 , et qui retourne une chaîne de
# caractères formée d'un premier groupe de  𝑚  espaces suivis d'un zéro, suivi d'une séquence croissante de multiples de 10 séparés
# par des espaces. La dernière valeur de la séquence est le plus petit multiple de 10 supérieur ou égal à  𝑛 . De plus, notez que vos valeurs
# doivent être séparées les unes des autres par un nombre d'espaces qui fait en sorte que le dernier chiffre de chaque valeur (un 0) soit
# toujours exactement à 10 caractères de ses voisins. Par exemple, patron10(5, 23) doit produire la chaîne suivante où les espaces ont été
# substitués par des points afin de vous permettre de mieux les distinguer :
# .....0........10........20........30
# Notez bien que le nombre d'espaces qui séparent les valeurs adjacentes dépend de leur ordre de grandeur. Dans l'exemple ci-dessus, il y
# en a toujours 8 puisqu'il n'y a que des dizaines, mais le nombre d'espaces doit être réduit à 7 pour les centaines, à 6 pour les milliers, etc.
#
# Notez aussi que votre fonction ne doit rien afficher, mais simplement retourner la chaîne de caractères demandée.
#
# Dans le cas où l'un des arguments  𝑚  et  𝑛  de votre fonction recevrait une valeur plus petite que zéro, vous devez soulever une exception de type ValueError.
#
# Prenez soin de bien tester votre solution dans votre notebook avant de la soumettre au serveur. Pour chaque exercice, vous n'avez droit
# u'à un maximum de trois soumissions avec rétroaction. Après ces trois premiers essais, vous pourrez continuer à soumettre de nouvelles solutions,
#  mais vous ne recevrez plus aucune rétroaction. N'oubliez pas que c'est la dernière soumission qui compte, peu importe que celle-ci soit
# meilleure ou pire que la précédente.

# QUIZ 4. REPONSE
def patron10(m, n):
    if m < 0 or n < 0:
        raise ValueError
    res = ' '*m + '0'
    for i in range((n+1)//10+1):
        res += '{:10}'.format((i+1)*10) # pour avoir exactement 10 caracteres dans format {:10}
    return res

print(patron10(5, 23))

# QUIZ 5. AFFICHAGE D'UN HISTOGRAMME
# Soit un dictionnaire qui associe des étiquettes à des valeurs. Les étiquettes sont des chaînes de caractères d'une longueur arbitraire;
# les valeurs sont des entiers positifs ou nuls.
#
# Définissez une fonction nommée histogramme, qui accepte un tel dictionnaire en argument et affiche un histogramme des valeurs de celui-ci selon le modèle ci-dessous.

# QUIZ 5. REPONSE
def patron10(m, n):
    res = ' '*m + '0'
    for i in range(int(round(n)-1)//10+1):
        res += '{:10}'.format((i+1)*10)
    return res

def axe(m, n):
    return '+' + ('-'*m + '+')*((n-1)//10+1)

def batonnet(etiq, val, maxetiq, maxval):
    res = '{{:>{}}}:{}'.format(maxetiq, '-'*min(val, maxval)).format(etiq[:maxetiq])
    return res if val <= maxval else res[:-1]+'*'

def histogramme(dico, *, maxetiq=None, maxval=None):
    # trouver la plus longue étiquette et la valeur max
    if not maxetiq:
        maxetiq = 0
        for key in dico:
            if len(key) > maxetiq:
                maxetiq = len(key)
    if not maxval:
        maxval = 0
        for key, value in dico.items():
            if value > maxval:
                maxval = value
    print(patron10(maxetiq, maxval))
    print(' '*maxetiq + axe(9, maxval))
    for key in sorted(dico.keys()):
        print(batonnet(key, dico[key], maxetiq, maxval))
    print(' '*maxetiq + axe(9, maxval))
    print(patron10(maxetiq, maxval))


dico = {'chats': 10, 'poissons rouges': 3, 'chiens': 25, 'tortues': 7}
histogramme(dico, maxetiq=8, maxval=18)
histogramme(dico, maxetiq=8, maxval=31)

# QUIZ 6. CREATION D'UNE CLASSE D'EXCEPTION
# Définissez une classe nommée MonErreur qui désigne un type d'erreur particulier à votre application. Faites en sorte qu'en affichant
# une instance de cette classe le message de l'exception soit formatté de la façon suivante : MonErreur: «message» où message est le
# message avec lequel l'exception a été constuite. Dans le cas particulier où l'exception serait soulevée avec aucun message, ou avec
# une chaîne vide, on veut que l'affichage soit simplement MonErreur au lieu de MonErreur: «».
#
# Définissez aussi une fonction nommée soulever_mon_erreur qui accepte en argument un message sous la forme d'une chaîne de caractères
# et qui soulève une exception de type MonErreur en lui passant la chaîne reçue.
#
# Finalement, faites un appel à votre fonction soulever_mon_erreur à l'intérieur d'un bloc try, en lui passant le message
# "mon type d'erreur particulier" et en en affichant l'exception soulevée à la console.

# QUIZ 6. REPONSE
class MonErreur(Exception):
    def __str__(self):
        if self.args and self.args[0]:
            return 'MonErreur: "{}"'.format(self.args[0])
        return 'MonErreur'


def soulever_mon_erreur(message):
    raise MonErreur(message)

try:
    soulever_mon_erreur("mon type d'erreur particulier")
except MonErreur as err:
    print(err)


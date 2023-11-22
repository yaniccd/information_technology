# EXERCICE 6
# Notion de Classes et d'Objets

# 6.1.1 CLASSE POINT
# Définissez une classe nommée Point qui encapsule les coordonnées  (𝑥,𝑦)  d'un point dans le plan cartésien.
# Le constructeur de votre classe (méthode __init__) doit accepter en argument deux nombres arbitraires
# et les affecter respectivement à des variables d'instance (variables stockées dans self) nommées x et y.

# 6.1.1 REPONSE
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({},{})'.format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def norme(self):
        return (self.x**2 + self.y**2)**0.5

Point1 = Point(1, 2)
print(Point1)
Point2 = Point(3, 3)
Point3 = Point1 + Point2
print(Point3)
print(Point3.norme())

# 6.1.2 CLASSE ET OPERATEUR []
# Définissez une classe nommée Vecteur qui encapsule une séquence de nombres réels.
# Le constructeur de votre classe (méthode __init__) doit accepter en argument un nombre arbitraire de valeurs,
# faire une liste avec ces valeurs et affecter cette liste à une variable d'instance nommée data.
# Ajoutez à votre classe les méthodes __getitem__et __setitem__ permettant d'implanter l'opérateur [] pour
# les instances de votre classe. Outre l'argument self, la méthode __getitem__ doit accepter l'indice de la
# composante désirée et retourner la valeur de cette composante. De même, la méthode __setitem__ doit accepter
# l'indice de la composante désirée ainsi que la valeur que l'on veut donner à cette composante et effectuer
# l'affectation de cette valeur à cette composante. Notez que la fonction __setitem__ ne doit rien retourner.

# 6.1.2 REPONSE
class Vecteur():
    def __init__(self, *args):
        self.data = list(args)

    def __getitem__(self, item):
        if item < 0 or item >= len(self.data):
            raise IndexError('Indice invalide')
        return self.data[item]

    def __setitem__(self, key, value):
        if key < 0 or key >= len(self.data):
            raise IndexError('Indice invalide')
        self.data[key] = value

V = Vecteur(5, 6, 7)
print(V[0], V[1], V[2])
V[0] = 23
V[1] = 37
V[2] = 15
print(V[0], V[1], V[2])

# 6.1.3 HERITAGE SIMPLE
# Définissez une classe nommée B qui hérite de la classe A et qui lui ajoute
# une méthode de conversion en chaîne de caractères. Faites en sorte que les énoncés :
# a = B(27)
# print(a)
# produisent la sortie valeur = 27.
class A:
    def __init__(self, x):
        self.val = x

    def getValue(self):
        return self.val

    def setValue(self, x):
        self.val = x

# 6.1.3 REPONSE
class B(A):
    def __str__(self):
        return 'valeur  = {}'.format(self.val)

a = B(27)
print(a)

# QUIZ 1. PATRON -+-+-+-
# Définissez une fonction nommée make_sep_line qui reçoit en argument un entier  𝑛  et retourne
# une chaîne de caractères constituée de  𝑛  caractères - intercalés de  𝑛−1  caractères +.
# Par exemple, l'appel de make_sep_line(4) doit produire :
# `-+-+-+-`.
# Dans le cas où  𝑛≤0 , votre fonction doit soulèver une exception de type AssertionError.

# QUIZ 1. REPONSE
def make_sep_line(n):
    if n <= 0:
        raise AssertionError('Assertion error')
    return '-+'*(n-1) + '-'

print(make_sep_line(4))

# QUIZ 2. Patron x | y | z
# Définissez une fonction nommée make_data_line qui reçoit en argument une liste de  𝑛  valeurs
# [𝑥1,𝑥2,…,𝑥𝑛] , où les  𝑥𝑖 ,  𝑖=1,…,𝑛 , sont des chaînes d'un seul caractère, et retourne la chaîne «  𝑥1|𝑥2|⋯|𝑥𝑛  ».
# Par exemple, l'appel de makeDataLine(['a', 'b', 'c', 'd']) doit produire a|b|c|d.

# QUIZ 2. REPONSE
def make_data_line(liste):
    if not liste:
        return ''
    res = ''
    for valeur in liste:
        if not isinstance(valeur, str):
            raise TypeError()
        if len(valeur) != 1:
            raise ValueError("une valeur n'est pas un caractere unique")
        res += valeur + '|'
    return res[:-1]

print(make_data_line(['a', 'b', 'c', 'd']))

# QUIZ 3. CLASSE TABLE
# Définissez une classe nommée Table afin d'encapsuler un tableau de
# 𝑚  lignes par  𝑛  colonnes. Votre classe doit posséder l'interface suivante :
# Un **constructeur** qui **accepte** les arguments  𝑚  et  𝑛  et qui **initialise** le tableau avec des
# valeurs `None`. Dans le cas où  𝑚≤0  ou  𝑛≤0 , le constructeur doit soulever une **exception** de type AssertionError.
# Un **opérateur** `[]` qui **accepte** un **couple** d'indices  [𝑖,𝑗]  afin de pouvoir spécifier, autant
# en **lecture** qu'en **écriture**, l'élément du tableau qui correspond à la ligne  𝑖  et à la colonne  𝑗 .
# Dans le cas d'un indice **invalide**, c'est-à-dire lorsque  𝑖<0  ou  𝑖≥𝑚  ou  𝑗<0  ou  𝑗≥𝑛 , la méthode doit
# soulever une **exception** de type IndexError.
# Une **méthode** nommée `set_values` qui **accepte** en argument un **itérable*** de  𝑚×𝑛  valeurs et qui affecte
# ces valeurs aux éléments du tableau dans l'ordre des lignes (i.e. les  𝑛  premières valeurs sont affectées de la 1ère ligne,
# les  𝑛  suivantes à la 2ème ligne, *etc*.). Dans le cas où le nombre de valeurs dans l'*itérable* ne serait
# pas égal à  𝑚×𝑛  (soit plus petit, soit plus grand), la méthode doit soulever une exception de type ValueError.
# Cette méthode doit aussi retourner une référence sur le tableau.
# Une **méthode** nommée `get_line` qui **accepte** en argument un **indice** de ligne, et **retourne** la **liste**
# des valeurs associées à cette ligne dans le tableau. Dans le cas d'un indice de ligne **invalide**, la méthode doit soulever
# une **exception** de type IndexError.
# Une **méthode** nommée `get_size` qui **retourne** la **taille** du tableau sous la forme d'un **tuple**  (𝑚,𝑛) .

# QUIZ 3. REPONSE

class Table:
    def __init__(self, m, n):
        assert m > 0 and n > 0
        self.m = m
        self.n = n
        self.data = []
        self.set_values(None for _ in range(m*n))

    def __getitem__(self, index):
        i, j = index
        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            raise IndexError
        return self.data[i*self.n + j]

    def __setitem__(self, index, x):
        i, j = index
        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            raise IndexError
        self.data[i*self.n + j] = x

    def set_values(self, iterable):
        data = list(iterable)
        if len(data) != self.n*self.m:
            raise ValueError()
        self.data = data
        return self

    def get_line(self, i):
        if i < 0 or i >= self.m:
            raise IndexError
        return self.data[i*self.n: (i+1)*self.n]

    def get_size(self):
        return self.m, self.n

# QUIZ 4. CREATION D'UNE GRILLE
# Définissez une fonction nommée make_grid qui accepte en argument une table (quiz précédent),
# et retourne une chaîne de caractères représentant les éléments de cette table à l'intérieur d'une grille.
# Par exemple, pour le tableau x = Table(m=3, n=4), initialisé par x.set_values('X' for _ in range(12)),
# l'appel de make_grid(x) doit retourner la chaîne :
# X|X|X|X\n-+-+-+-\nX|X|X|X\n-+-+-+-\nX|X|X|X\n
# et l'énoncé print(make_grid(x)) produira :
# X|X|X|X
# -+-+-+-
# X|X|X|X
# -+-+-+-
# X|X|X|X

# QUIZ 4. REPONSE
def make_grid(table):
    m, n = table.get_size()
    valeur = ''
    for i in range(m-1):
        valeur += make_data_line(table.get_line(i)) + '\n'
        valeur += make_sep_line(n) + '\n'
    valeur += make_data_line(table.get_line(m-1))
    return valeur

x = Table(m=3,n=4)
x.set_values(['O', 'X', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'X', 'X'])
print(make_grid(x))

# QUIZ 5. CLASS TICTACTOE
# Définissez une classe nommée TicTacToe permettant d'encapsuler le jeu de Tic-tac-toe.
# Le jeu Tic-tac-toe se joue sur une grille carrée de  3×3  cases. Deux joueurs s'affrontent.
# Ils doivent remplir chacun leur tour une case de la grille avec le symbole qui leur est attribué : O ou X.
# Le gagnant est celui qui arrive à aligner trois symboles identiques, horizontalement, verticalement ou en diagonale.
#
# Dérivez votre classe de la classe Table définie dans le contexte de cet exercice, et donnez-lui l'interface suivante :
# Un **constructeur** qui **initialise** une grille de  3×3  cases avec des espaces.
# Une **méthode** qui **convertit** cette grille en chaîne de caractères, en faisant appel à la fonction `make_grid` définie dans le **contexte** de cet exercice.
# Une **méthode** nommée `reset` qui **réinitialise** le jeu en remplissant la grille par des espaces.
# Une **méthode** nommée `choose` qui reçoit en argument le **symbole** à jouer ainsi que deux arguments correspondant aux indices de **ligne** et de **colonne** de la case où le symbole doit être inscrit. Cette méthode ne retourne **rien**, mais soulève une exception de type ValueError si le symbole reçu est autre chose que `X` ou `O` (comme dans « O Canada ») ou si la case spécifiée n'est **pas** libre. Elle doit également soulever une exception de type IndexError, si les **indices** de ligne et de colonne sont **invalides**.
# Une **méthode** nommée `check_win` qui **détermine** si l'état actuel du jeu correspond à une situation **gagnante**. Dans le cas d'une situation gagnante, cette méthode **retourne** le symbole du joueur qui a gagné ; autrement la méthode ne retourne **rien**. Une situation est **gagnante** dans l'un ou l'autre des cas suivants :
# trois symboles **identiques** sont alignés sur une même **ligne** ;
# trois symboles **identiques** sont alignés sur une même **colonne** ;
# trois symboles **identiques** sont alignés sur une **diagonale**.

# QUIZ 5. REPONSE
class Tictactoe(Table):
    def __init__(self):
        super().__init__(3, 3)
        self.reset()

    def reset(self):
        self.set_values(' ' for _ in range(9))

    def __str__(self):
        return make_grid(self)

    def choose(self, i, j, valeur):
        if valeur != 'X' and valeur != 'O':
            raise ValueError()
        if self[i, j] != ' ':
            raise ValueError()
        if i >=3 or i < 0 or j >= 3 or j < 0:
            raise IndexError()
        self[i, j] = valeur

    def check_win(self):
        for i in range(3):
            if self[i, 0] == self[i, 1] == self[i, 2] != ' ':
                return self[i, 0]
            if self[0, i] == self[1, i] == self[2, i] != ' ':
                return self[0, i]
        if self[0, 0] == self [1, 1] == self[2, 2] != ' ':
            return self[0, 0]
        if self[2, 0] == self[1, 1] == self[2, 0] != ' ':
            return self[1, 1]
        return None
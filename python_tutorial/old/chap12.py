# CHAPITRE 12.1
# INTRODUCTION AU CALCUL SCIENTIFIQUE - numpy
import numpy as np

# References
#   http://numpy.scipy.org/
#   http://www.scipy.org/Tentative_NumPy_Tutorial

# MODULE numpy
# Ce module est à la base du calcul scientifique en Python.
# Il inclus notamment :
#
# un type de données capable de gérer des tableaux à  𝑛  dimensions ;
# des outils d'intégration pour du code en C/C+ et Fortran ;
# des fonctionnalités de base en mathématiques et en statistiques ;
# des fonctions spécialisées pour générer des tableaux de nombres pseudo-aléatoires.
# Il est à la base du module scipy qui offre des fonctionnalités plus évoluées.

# Le module numpy définit une classe nommée ndarray, pour gérer des tableaux multidimensionnels dont les éléments (habituellement des nombres) sont homogènes :
#
# tous les éléments du tableau sont de même type ;
# le type est fixé au moment de la création du tableau ;
# le nombre de dimensions est également fixé au moment de sa création.

# La fonction arange est l'équivalent du range standard ; elle produit une séquence de nombres, mais sous la forme d'un tableau d'éléments homogènes :
a = np.arange(12)
print(a)
print('')
#La méthode reshape permet de modifier la forme du tableau :
b = a.reshape(3, 4)
print(b)
print('')
# Elle retourne un nouveau tableau ; il faut que la nouvelle forme possède le même nombre d'éléments que la forme d'origine. Par exemple :
print(a.reshape(3, 2, 2))
print('')

# Les tableaux numpy possèdent des attributs standards :
print(a.shape, b.shape)
print(a.ndim, b.ndim)
print(a.size, b.size)
print(a.dtype.name, b.dtype.name) #int sur 32 bits

# On peut aussi créer un tableau à partir d'un itérable d'itérables (p.ex. une liste de listes) ; on obtient alors un tableau à deux dimensions :
d = np.array([(1.5, 2, 3), (4, 5, 6)])
print(d)
print(type(d))
print(d.dtype.name) #float sur 64 bits

# D'autres fonctions sont aussi disponibles pour créer des tableaux numpy particuliers, notamment les
# fonctions zeros et ones qui initialisent les tableaux avec des zéros et des uns, respectivement :
e = np.zeros((3,4))
print(e)

# Par défaut, les tableaux sont constitués de nombres à virgule flottante codés sur 64 bits.
# On peut cependant spécifier le type désiré lors de la création du tableau. Par exemple :
f = np.ones((3,4), dtype=np.int16)
print(f)

# Les types d'éléments disponibles sont :
#
# booléens: bool ;
# nombres entiers non signés: uint8, uint16, uint32, uint64 ;
# nombres entiers signés: int8, int16, int32, int64 ;
# nombres à virgules flottantes : float32, float64 ;
# nombres complexes : complex64, complex128.

# Les opérations sur les tableaux numpy s'effectuent toujours élément par élément :
x = np.array([20, 20, 40, 30])
y = np.array([2, 4, 5, 1])
print(x - y)
print(x/y)
print(y**2)
print(x*y)
print('')

# Pour le produit matriciel, il faut utiliser la fonction dot :
A = np.array([[1,1],
             [0,0]])
B = np.array([[2,0],
             [3,4]])
C = np.dot(A, B)
print(C)
print('')

# On peut aussi faire des opérations sans créer de nouveaux tableaux :
A = np.ones((2,3), dtype=np.int)
A *= 3
print(A)
print('')

# On peut facilement construire des matrices de nombres pseudo-aléatoires (l'interface est similaire à celle du module random standard) :
B = np.random.random((2,3))
print(B)
B += (A)
print(B)
print('')
# On remarque que numpy effectue des conversions automatiques de type, puisque le type des éléments d'un tableau ne peut pas changer après sa création.
# Lorsqu'on combine des éléments de types différents, le résultat s'exprime dans le type le plus général.
print(A+B)

# Différentes fonctions permettent de traiter l'ensemble des éléments d'un tableau, sans tenir compte de sa forme :
C = np.arange(12).reshape((3,4))
print(C.sum(), C.min(), C.max())
print('')
# on peut restreindre l'operation a un axe
# Dans le cas d'un tableau à deux dimensions, l'axe 0 correspond (par convention) aux lignes, et l'axe 1 au colonnes.
C[2,0] = 1
print(C, end='\n\n')
print("axe 1 = ", C.max(axis = 1), end='\n\n')
print("axe 0 = ", C.max(axis = 0), end='\n\n')

# On peut aussi découper les tableaux numpy de la même façon que l'on découpe les listes.
a = np.arange(9)**3
print(a[2])
print(a[2:5])
a[:6:2] = -10
print(a)
print(a[::-1], end='\n\n')

# dans le cas de deux dimensions
b = np.arange(12).reshape((3,4))
print(b[0,2])

# On doit préciser un découpage sur les indices des deux dimensions, en séparant ces découpages par une virgule.
# Par exemple, nous avons ci-dessus découpé l'élément qui est à la croisée de la ligne d'indice 2 et de la colonne d'indice 3.
# Les découpages dans chaque dimension fonctionnent comme ceux de la liste ou de la chaîne de caractères. Il s'agit simplement de les séparer par une virgule.
print(b, end='\n\n')
print(b[:,1], end='\n\n')
print(b[1:3,:], end='\n\n')
print(b[::-1,:], end='\n\n')
print(b[:-1,:], end='\n\n')

# Lorsqu'on itère sur un tableau multidimensionnel, on itère en fait sur les éléments du premier axe :
for row in b:
    print(row)

# On peut aussi aplatir un tableau multidimensionnel avec la méthode ravel :
print('')
print(b.ravel())

# On peut aussi changer sa forme
print('')
print(b.reshape(2,6), end='\n\n')

# On peut changer la taille du tableau avec resize (des 0 sont ajoutee)
b = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(b, end='\n\n')
b.resize((3,5))
print(b, end='\n\n')
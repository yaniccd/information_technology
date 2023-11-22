# CHAPITRE 13.2
# INTRODUCTION AU MODULE turtle
import turtle

# plan
# Comment créer un fenêtre graphique;
# Comment dessiner dans la fenêtre;
# Comment définir une forme;
# Comment interagir avec le clavier et la souris.

# Le module turtle permet d'aisément créer une fenêtre graphique et de tracer des dessins dans cette fenêtre. Il contient notamment les deux classes suivantes:
#
# Screen: la fenêtre d'affichage;
# Turtle: l'outil (le crayon) qui permet de dessiner à l'intérieur de la fenêtre.
fen = turtle.Screen()
fen.title('Ma tortue')
fen.setup(width=1200, height=1000)
yanic = turtle.Turtle()

yanic.forward(50)   # avancer de 50 pixels
yanic.left(90)  # tourner de 90 en sens anti-horaire
yanic.forward(30)   # avancer de 30 pixels
# turtle.done()   # Pour ne pas que la fenetre ferme lorsque le programme se termine
# turtle.Screen().exitonclick()   # Pour fermer sur un click

# La fonction Screen construit une fenêtre, title permet de lui définir un titre, setup permet de
# lui fixer sa taille en pixels, Turtle construit une tortue, c'est-à-dire un instrument de dessin
# qui peut tracer un trait en avançant (forward) et qui peut changer d'orientation, par exemple vers la gauche (left).
# Par défaut, la tortue est positionnée au centre de la fenêtre et pointe vers la droite.

# En se déplaçant, la tortue laisse une trace sur la fenêtre. La largeur de cette trace peut
# être changée à l'aide de la méthode pensize et sa couleur à l'aide de pencolor. Par exemple:

yanic.pensize(10)
yanic.pencolor('red')
yanic.left(30)
yanic.forward(100)

# La méthode penup permet quant à elle de lever le crayon de la tortue:
yanic.penup()
yanic.forward(30)
yanic.pendown()
yanic.left(60)
yanic.pensize(5)
yanic.pencolor('blue')
yanic.forward(100)

# On peut remplir un tracé à l'aide des méthodes fillcolor, begin_fill et end_fill:
yanic.fillcolor('green')
yanic.begin_fill()
yanic.left(30)
yanic.forward(100)
yanic.left(90)
yanic.forward(100)
yanic.end_fill()
# L'appel à end_fill ferme le polygone et le remplit avec la couleur spécifiée.

# Definition d'une forme
# Il existe une forme nommée «turtle» que l'on peut choisir avec la méthode shape:
print(yanic.shape())
# On peut estamper la forme actuelle à la position actuelle en utilisant la méthode stamp:
yanic.stamp()
yanic.forward(100)
yanic.stamp()

# On peut créer de nouvelles tortues:
joe = turtle.Turtle()
joe.forward(200)
# Chaque tortue est independante

# On peut creer une nouvelle forme pour une tortue
poly = ((-20,-20), (0,50), (60,-20), (-20,-20))
turtle.addshape('maforme', poly)
joe.shape('maforme')
joe.pencolor('blue')
joe.fillcolor('red')
# Les coordonnées du polygone sont relatives à la position et à l'orientation de la tortue.
# La première coordonnée pointe à 90 degrés vers la droite; la deuxième est dans la direction de la tortue:

# Par défaut, une tortue se déplace vers l'avant (ou l'arrière), selon sa position et son orientation courante,
# et les changements de directions sont en degrés par rapport à cette orientation. Pour effectuer le tracé
# d'un polygone exprimés comme une séquence de points de coordonnées absolues, on peut faire appel à la méthode goto:
# a l'aide de la tortue 'toto', tracer un polygone
def tracerPolygone(toto, poly):
    toto.penup()
    toto.goto(poly[0])
    toto.pendown()
    for pos in poly[1:]:
        toto.goto(pos)

tracerPolygone(joe, ((200, 0),(200, 200),(150, 250),
                     (210, 280), (270, 250), (220, 200),
                     (220, 0), (200, 0)))


# pour effacer le tableau
fen.clearscreen()

# Gestion du clavier
# Pour gérer les événements en provenance du clavier, il faut appeler la fonction onkeypress,
# afin de spécifier l'action à exécuter lorsque l'utilisateur pressera une touche spécifique.
# Par exemple, à chaque fois que la barre d'espacement est pressée, le programme ci-dessous fait
# avancer la tortue de 10 unités vers l'avant, puis la tourne de 5 degrés vers la gauche:
alex = turtle.Turtle()


def tourner():
    fen.onkeypress(None, 'space') #unaibable function while processing
    alex.forward(10)
    alex.left(5)
    fen.onkeypress(tourner, 'space')


def tracerClic(x, y):
    fen.onclick(None, btn=1)
    alex.setheading(alex.towards(x,y))
    alex.goto(x, y)
    fen.onclick(tracerClic, btn=1)


def changerModeEcriture():
    fen.onkeypress(None, 'Up')
    if alex.isdown():
        alex.penup()
        alex.fillcolor('white')
    else:
        alex.pendown()
        alex.fillcolor('black')
    fen.onkeypress(changerModeEcriture, 'Up')


fen = turtle.Screen() # Ferme la premiere fenetre
fen.setup(width=500, height=500)
fen.onkeypress(tourner, 'space')
fen.onclick(tracerClic, btn=1)
fen.onkeypress(changerModeEcriture, 'Up')
fen.listen()
alex = turtle.Turtle()
fen.mainloop() #permet egalement de ne pas fermer la fenetre a la fin de l'execution

# Notez bien que le code ci-dessus effectue deux actions essentielles:
#
# il fait appel à la méthode listen qui redirige tous les événements en provennance du clavier vers la fenêtre turtle;
# il fait appel à la méthode mainloop qui transfère le contrôle du programme au module turtle afin que celui-ci
# gère les événements rapportés par l'environnement graphique de la machine.
# C'est le paradigme dit de la programmation événementielle où l'environnement graphique prend le contrôle
# du programme et fait appel à votre code seulement lorsqu'un événement se produit.
#
# Notez également que le onkeypress est annulé à l'entrée de la fonction tourner et rétabli juste avant la sortie,
# afin d'interdir tout autre événement du même type pendant que la tortue est en déplacement. Autrement, si les
# événements se produise trop rapidement, ils risquent d'interagir entre eux.
#
# De nouveau, il importe de remarquer que nous avons annulé les événements à l'entrée des fonctions qui les
# traitent et nous les avons rétabli juste avant la sortie, afin d'éviter les interactions potentielles.

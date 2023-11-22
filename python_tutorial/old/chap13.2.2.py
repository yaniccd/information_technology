# CHAPITRE 13.2
# INTRODUCTION AU MODULE turtle
import turtle

# Boucle evenementielle
# Dans le cas où l'on veut prendre périodiquement le contrôle de la boucle événementielle, on peut enregistrer
# une fonction auprès de l'événement ontimer. Celle-ci sera appelée après le délai spécifié lors de l'enregistrement.
# Par exemple, le programme suivant fait avancer la tortue en ligne droite et à vitesse constante, même en l'absence
# de clic de souris. Lors d'un clic, la position de celui-ci change l'orientation de la tortue. Et comme précédemment,
# une pression de la barre d'espacement lève ou baisse le crayon selon son état:

class App:
    def __init__(self, largeur, longueur):
        self.fen = turtle.Screen()
        self.fen.setup(largeur, longueur)
        self.fen.onclick(self.changeOrientation, btn=1)
        self.fen.onkeypress(self.changerModeEcriture, 'space')
        self.fen.listen()
        self.alex = turtle.Turtle()
        self.alex.speed('fastest')
        self.clic = None

    def changeOrientation(self, x, y):
        self.clic = turtle.Vec2D(x, y)

    def changerModeEcriture(self):
        self.fen.onkeypress(None, 'space')
        if self.alex.isdown():
            self.alex.penup()
            self.alex.fillcolor('white')
        else:
            self.alex.pendown()
            self.alex.fillcolor('black')
        self.fen.onkeypress(self.changerModeEcriture, 'space')

    def go(self):
        if self.clic:
            self.alex.setheading(self.alex.towards(self.clic))
            self.clic = None
        self.alex.forward(100)
        turtle.ontimer(x.go, 0)

x = App(800, 600)
turtle.ontimer(x.go, 0)
turtle.mainloop()



# Le programme principal fait ses initialisations en appelant notamment la méthode ontimer qui spécifie à turtle d'appler
# go dès que possible. Ensuite, on donne le contrôle du programme à turtle en appelant sa mainloop. Celle-ci entre dans
# une boucle de traitement des événements et réalise notamment que le délai d'un chronomètre est terminé. Notre fonction
# go est donc appelée aussitôt. La mission de notre fonction go est d'effectuer une itération de notre propre boucle de traitement.
# Mais au lieu de boucler sur nos itérations, on collabore avec la boucle de turtle en lui rendant le contrôle du fil
# d'exécution après chacune de nos itérations, après lui avoir spécifié de nous rappeler après un certain délai déterminé lors
# de l'appel de la méthode ontimer. Ainsi, turtle peut s'occuper de traiter les événements au fur et à mesure qu'ils se produisent.

# Ce qu'il importe de noter est que turtle effectue des animations lorsqu'on lui demande de déplacer une tortue.
# Or, pendant ces animations qui demandent d'attendre périodiquement, au lieu de ne rien faire, turtle en profite pour gérer
# les événements qui ont pu survenir pendant ce temps. C'est pour cette raison qu'il faut désactiver le traitement d'un événement
# lorsque ce dernier est déjà en cours de traitement. Sinon, un traitement récursif surviendra avec sans doute un comportement inattendu.

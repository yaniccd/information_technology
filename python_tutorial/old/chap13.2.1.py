# CHAPITRE 13.2
# INTRODUCTION AU MODULE turtle
import turtle

# Encapsulation dans une classe
class App:
    def __init__(self, largeur, longueur):
        self.fen = turtle.Screen()
        self.fen.setup(largeur, longueur)
        self.fen.onclick(self.tracerClic, btn=1)
        self.fen.onkeypress(self.changerModeEcriture, 'space')
        self.fen.listen()
        self.alex = turtle.Turtle()

    def tracerClic(self, x, y):
        self.fen.onclick(None, btn=1)
        self.alex.setheading(self.alex.towards(x, y))
        self.alex.goto(x, y)
        self.fen.onclick(self.tracerClic, btn=1)

    def changerModeEcriture(self):
        self.fen.onkeypress(None, 'space')
        if self.alex.isdown():
            self.alex.penup()
            self.alex.fillcolor('white')
        else:
            self.alex.pendown()
            self.alex.fillcolor('black')
        self.fen.onkeypress(self.changerModeEcriture, 'space')

test = App(800, 600)
turtle.mainloop()
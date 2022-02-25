from turtle import *
import turtle

'''
i denne oppgaven lager jeg kuben ved hjelp av en funksjon fordi jeg vil at det skal være mer oversiktlig,
fordi du kan lese navnet på funskjonen og forstår med en gang hva den gjør, siden selve filen heter "oppgave1_A"
og forteller ingenting om hva programmet gjør.
'''
def kube():
    # lager et område for turtle å rendere #
    # lager tittel til vinduet
    # setter bakgrunnsfarge til grønn
    vindu = turtle.Screen()
    vindu.bgcolor("green")
    vindu.title("3D KUBE")

    # setter pennfarge til svart
    # lager variabler "turt" for å kalle turtle med kortere navn
    turt = turtle.Turtle()
    turt.color("black")

    # lager første firkant
    for i in range(4):
        turt.forward(100)
        turt.left(90)

    # lager linje i nederst venstre hjørne som kobler de to firkantene sammmen
    turt.goto(50, 50)

    # lager firkant 2
    for i in range(4):
        turt.forward(100)
        turt.left(90)

    # lager linje i nederst høyre hjørne som kobler de to firkantene sammen
    turt.goto(150, 50)
    turt.goto(100, 0)

    # lager linje i øverst høyre hjørne som kobler de to firkantene sammen
    turt.goto(100, 100)
    turt.goto(150, 150)

    # lager linje i øverst ventre hjørne som kobler de to firkantene sammen
    turt.goto(50, 150)
    turt.goto(0, 100)

    # starter eventloop
    # gjør akkurat det samme som tkinter.mainloop()
    turtle.done()

# starter programmet om funsksjonen ikke er importert
if __name__ == "__main__":
    kube()

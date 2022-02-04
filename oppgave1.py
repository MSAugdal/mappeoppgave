
from turtle import *
 
import turtle 
  
def kube():
    # lager et område for turtle å rendere #
    # lager tittel til vinduet
    # setter bakgrunnsfarge til svart og penn farge til blå
    # lager variabler "turt" for å kalle turtle med kortere navn
    vindu = turtle.Screen()
    vindu.bgcolor("black")
    vindu.title("3D KUBE")
    turt = turtle.Turtle()
    turt.color("blue")           

    #lager første firkant
    for i in range(4):
        turt.forward(100)
        turt.left(90)

    #lager første linje som kobler første firkant med firkant 2
    turt.goto(50,50)
    
    # for i in range(4):
    #     turt.forward(100)
    #     turt.left(90)

    # turt.goto(150,50)
    # turt.goto(100,0)
    
    # turt.goto(100,100)
    # turt.goto(150,150)
    
    # turt.goto(50,150)
    # turt.goto(0,100)

    turtle.done()

kube()

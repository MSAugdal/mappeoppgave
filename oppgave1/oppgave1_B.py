from turtle import *
import turtle

''' 
i denne oppgaven bruker jeg class og def fordi jeg vil at den skal kunne være mer funksjonell.
det gjør det også da mulig å gjøre selve bokstavmodulene "usynlig" så du ikke med et uhell caller
en bokstav til å bli tegnet. dette gjør jeg ikke i denne oppgaven fordi jeg mener det gjør det unødvendig komplisert.
med denne metoden kan du også lage en __init__ def som laget variabler du skal bruke i resten av classen,
men det er ikke mulig å kalle den utenfor, og du slepper å lage globale variabler (som er dårlig programmeringsskikk).
du kan også da ha en def/modul som caller alle bokstavene i den rekkefølgen du vil ha dem. ergo: mer funksjonell.
om du vil skrive "amthias", eller "aaaaa" istedenfor "mathias" er dette mulig ve å omrokkere i "run" modulen.
'''
class NavnTegner():
    def __init__(self):
        # lager vinduet for å tegne i
        # endrer bakgrunsfarge til svart
        # endrer tittel på vinduet til MATHIAS
        # setter vindu størrelse til 99% av skjerm
        vindu = turtle.Screen()
        vindu.setup(height=.88, width=.99, startx=0, starty=0)
        vindu.bgcolor("black")
        vindu.title("MATHIAS")

        # lager nytt variabel navn for turtle
        # endrer pennfargen til hvit
        # endrer pensize til 5
        self.turt = turtle.Turtle()
        self.turt.pensize(5)
        self.turt.color("white")

    # funksjon som tegner en M
    def m(self):
        # lager variabler for å lagre posisjon og x posisjon til pennen
        posisjon = self.turt.pos()
        posisjonX = int(posisjon[0])

        # setter x posisjonen litt frem så den ikke tegnes i tidligere tegnet bokstaver
        posisjonX += 10

        # setter y posisjonen til 0 så den ikke begynner å tegne på feil y koordinat om pennen har annen posisjon
        self.turt.penup()
        self.turt.goto(posisjonX, 0)
        self.turt.pendown()

        # disse blokkene tegner selve M'en
        posisjonX += 25
        self.turt.goto(posisjonX, 100)

        posisjonX += 25
        self.turt.goto(posisjonX, 0)

        posisjonX += 25
        self.turt.goto(posisjonX, 100)

        posisjonX += 25
        self.turt.goto(posisjonX, 0)

        # setter y posisjonen til 0 så den er på rett plass når neste bokstav skal tegnes
        self.turt.penup()
        self.turt.goto(posisjonX, 0)
        self.turt.pendown()

    # lager bokstaven A
    def a(self):
        # lager variabler for å lagre posisjon og x posisjon til pennen
        posisjon = self.turt.pos()
        posisjonX = int(posisjon[0])

        # setter x posisjonen litt frem så den ikke tegnes i tidligere tegnet bokstaver
        posisjonX += 10

        # setter y posisjonen til 0 så den ikke begynner å tegne på feil y koordinat om pennen har annen posisjon
        self.turt.penup()
        self.turt.goto(posisjonX, 0)
        self.turt.pendown()

        posisjonX += 25
        self.turt.goto(posisjonX, 100)

        posisjonX += 25
        self.turt.goto(posisjonX, 0)

        self.turt.penup()
        self.turt.goto(posisjonX, 50)
        self.turt.pendown()

        # disse to linjene lager streken i A'en
        # lager posisjonX2 så jeg slepper å endre på posisjonX for så å flytte pennen til rett plass og så lagre posisjon igjen
        posisjonX2 = posisjonX-50
        self.turt.goto(posisjonX2, 50)

        # setter y posisjonen til 0 så den er på rett plass når neste bokstav skal tegnes
        self.turt.penup()
        self.turt.goto(posisjonX, 0)
        self.turt.pendown()

    def t(self):
        # lager variabler for å lagre posisjon og x posisjon til pennen
        posisjon = self.turt.pos()
        posisjonX = int(posisjon[0])

        # setter x posisjonen litt frem så den ikke tegnes i tidligere tegnet bokstaver
        posisjonX += 25

        # setter y posisjonen til 0 så den ikke begynner å tegne på feil y koordinat om pennen har annen posisjon
        self.turt.penup()
        self.turt.goto(posisjonX, 0)
        self.turt.pendown()

        # disse linjene tegner T'en
        self.turt.goto(posisjonX, 100)

        posisjonX -= 25
        self.turt.goto(posisjonX, 100)
        posisjonX += 50
        self.turt.goto(posisjonX, 100)

        # setter y posisjonen til 0 så den er på rett plass når neste bokstav skal tegnes
        self.turt.penup()
        self.turt.goto(posisjonX, 0)
        self.turt.pendown()

    def h(self):
        # lager variabler for å lagre posisjon og x posisjon til pennen
        posisjon = self.turt.pos()
        posisjonX = int(posisjon[0])

        # setter x posisjonen litt frem så den ikke tegnes i tidligere tegnet bokstaver
        posisjonX += 10

        # setter y posisjonen til 0 så den ikke begynner å tegne på feil y koordinat om pennen har annen posisjon
        self.turt.penup()
        self.turt.goto(posisjonX, 0)
        self.turt.pendown()

        # disse linjene tegner H'en
        self.turt.goto(posisjonX, 100)
        self.turt.goto(posisjonX, 50)

        posisjonX += 25
        self.turt.goto(posisjonX, 50)

        self.turt.goto(posisjonX, 100)
        self.turt.goto(posisjonX, 0)

    def i(self):
        # lager variabler for å lagre posisjon og x posisjon til pennen
        posisjon = self.turt.pos()
        posisjonX = int(posisjon[0])

        # setter x posisjonen litt frem så den ikke tegnes i tidligere tegnet bokstaver
        posisjonX += 25

        # setter y posisjonen til 0 så den ikke begynner å tegne på feil y koordinat om pennen har annen posisjon
        self.turt.penup()
        self.turt.goto(posisjonX, 0)
        self.turt.pendown()

        # disse linjene tegner I'en
        self.turt.goto(posisjonX, 100)

        # setter y posisjonen til 0 så den er på rett plass når neste bokstav skal tegnes
        self.turt.penup()
        self.turt.goto(posisjonX, 0)
        self.turt.pendown()

    def s(self):
        # lager variabler for å lagre posisjon og x posisjon til pennen
        posisjon = self.turt.pos()
        posisjonX = int(posisjon[0])

        # setter x posisjonen litt frem så den ikke tegnes i tidligere tegnet bokstaver
        posisjonX += 10

        # setter y posisjonen til 0 så den ikke begynner å tegne på feil y koordinat om pennen har annen posisjon
        self.turt.penup()
        self.turt.goto(posisjonX, 0)
        self.turt.pendown()

        # disse linjene tegner S'en
        self.turt.circle(25, 180)
        posisjonX += 15

        self.turt.penup()
        self.turt.goto(posisjonX, 96)
        self.turt.setheading(180)
        self.turt.pendown()

        self.turt.circle(25, 180)

        # setter y posisjonen til 0 så den er på rett plass når neste bokstav skal tegnes
        posisjonX += 10
        self.turt.penup()
        self.turt.goto(posisjonX, 0)
        self.turt.pendown()

    # caller alle bokstav-tegne-funksjonene og starter eventloopen
    # det er denne modulen du caller for å tegne "MATHIAS"
    # du kan endre på rekkefølgen slik som du selv ønsker (det burde ihvertfall fungere)
    def run(self):
        self.m()
        self.a()
        self.t()
        self.h()
        self.i()
        self.a()
        self.s()
        turtle.done()

# starter programmet om den ikke er importert
if __name__ == "__main__":
    navn = NavnTegner()
    navn.run()

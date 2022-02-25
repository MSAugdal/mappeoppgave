from random import sample
from time import sleep

'''
i denne oppgaven bruker jeg også class og def (moduler) for samme grunn som i oppgave1_A.
programmet er ikke så stort men det gjør det mer oversiktlig når du skal lese igjennom koden.
'''
class DeTiStørste():
    # her lages variabler for å lagre antall gjett,
    # hvor langt inn i listen spilleren er kommet,
    # en liste over de ti største landene fra størst til minst
    # og en shufflet versjon av listen som vises til spilleren
    def __init__(self):
        self.gjett = 0
        self.nummerIlista = 0
        self.deTiStørste = ["RUSSLAND", "CANADA", "USA", "KINA", "BRASIL",
                            "AUSTRALIA", "INDIA", "ARGENTINA", "KAZAKHSTAN", "ALGERIA"]
        self.shufflet = sample(self.deTiStørste, len(self.deTiStørste))

    # i guess modulen lagres gjettet til spilleren og antall gjett går opp med 1
    def guess(self):
        self.answer = input("gjett et land: ").upper()
        self.gjett += 1

    # sjekkGuess modulen sjekker gjettet til spilleren
    def sjekkGuess(self):
        # try sjekker om landet faktisk er i listen
        try:
            self.deTiStørste.index(self.answer)

        # om landet i gjettet til spilleren ikke er i listen printer except: en beskjed og spilleren må gjette på nytt
        except:
            print(f"\n{self.answer} er ikke i lista over de ti største landene\n")

        # else skjer om landet er i lista og ingen error forekom
        else:
            # if legger til 1 på nummerIlista så beskjedene spilleren får har rett tall i seg
            if self.nummerIlista == 0:
                self.nummerIlista += 1

            # printer gratulerer om du har gjettet alle 10 landene og avslutter programmet
            if self.nummerIlista == 10:
                print(
                    f"du gjettet alle landene i rett rekkefølge med {self.gjett} gjett!\nGratulerer!!\n")
                quit()

            # printer en beskjed om landet du gjettet er i listen, men ikke i rett rekkefølge
            elif self.deTiStørste.index(self.answer) != self.nummerIlista - 1:
                print(f"{self.answer} er ikke land nr {self.nummerIlista} i lista\n")

            # printer en beskjer om landet er i listen og er i rett rekkefølge
            elif self.deTiStørste.index(self.answer) == self.nummerIlista - 1:
                print(
                    f"{self.answer} er nr {self.nummerIlista} i listen over de ti største landene!")
                print(f"{10 - self.nummerIlista} land igjen\n")
                self.nummerIlista += 1
                sleep(1)

    # run er den modulen du caller for å starte programmet
    def run(self):
        # printer først en beskjed som forklarer hvordan du spiller spillet
        print(
            "\nI dette spillet får du en liste over de 10 største landene i verden")
        sleep(2)

        print("Du skal gjette land fra størst til minst")
        sleep(2)

        print("\nher er listen over landene:")
        sleep(1)
        # priner en shufflet versjon av listen av land så det blir litt lettere for spilleren
        print(self.shufflet)
        sleep(2)

        print("\nLykke til!\n")
        sleep(2)

        # er på en måte en "game-loop" som gjør seg ferdig når du har gjettet alle landene
        while True:
            self.guess()
            print("\n...\n")
            sleep(1)
            self.sjekkGuess()


# starter programmet kun om den blir excecutet i sin fil og ikke er importert til en annen
if __name__ == "__main__":
    tistore = DeTiStørste()
    tistore.run()

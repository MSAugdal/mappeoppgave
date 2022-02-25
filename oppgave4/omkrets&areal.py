from time import sleep

'''
i denne oppgaven bruker jeg også class og def (moduler) for samme grunn som i oppgave1_A.
programmet er ikke så stort men det gjør det mer oversiktlig når du skal lese igjennom koden.
'''
class OmkretsOgAreal:
    # printer en velkomstbeskjed og hvordan man bruker programmet
    # lager en variabel for verdien av Pi
    def __init__(self):
        print("\nVelkommen til utregningsprogrammet!")
        sleep(2)
        print("I dette programmet kan du regne ut:\n")
        sleep(2)
        print("Areal og omkrets av sirkel\nVolum og Overflate av kule\nVolum og overflate av sylinder")
        sleep(5)
        print("\nStart programmet ved å velge av alternativene under:")
        sleep(2)

        self.PI = 3.14

    # lar bruker velge geometrisk objekt å regne ut enten volum, areal eller overflate
    # caller modulene til geomtetrisk objekt utifra hvilket nummer som ble skrevet av bruker
    # printer error om bruker-svar ikke er gyldig
    def velgObjekt(self):
        print('''
	1: Sirkel (areal, omkrets)
	
	2: Kule (overflateareal, volum)
	
	3: Sylinder (overflateareal, volum)
        ''')
        sleep(2)
        objekt = input(
            "skriv 1, 2 eller 3 for å velge en figur å regne med\n>>")

        if objekt == "1":
            print("\nDu valgte: SIRKEL")
            sleep(2)
            self.sirkel()

        elif objekt == "2":
            print("\nDu valgte: KULE")
            sleep(2)
            self.kule()

        elif objekt == "3":
            print("\nDu valgte: SYLINDER")
            sleep(2)
            self.sylinder()

        else:
            print("du må skrive enten 1, 2 eller 3...\n")
            self.velgObjekt()

    # modul for å regne ut areal og omkrets av sirkel
    def sirkel(self):
        # lagrer radius i r
        try:
            r = float(input('\nSkriv inn radius av sirkelen: '))

        # printer error om svar ikke er gyldig
        except Exception as ex:
            print(ex)
            print("du må skrive et tall...\n")
            self.sirkel()

        # regner ut og printer areal og omkrets om svar er gyldig
        else:
            sleep(2)
            areal = round(self.PI * r * r, 2)
            omkrets = round(2 * self.PI * r, 2)
            print(f"\nRadius av sirkel = {r}")
            print(f"Areal av sirkel = {areal}")
            print(f"Omkrets av sirkel = {omkrets}\n")
            sleep(2)

    # regner ut overflate og volum av kule
    def kule(self):
        # lagrer radius i r
        try:
            r = float(input('\nSkriv inn radius av kulen: '))

        # printer error om svar ikke er gyldig
        except Exception as ex:
            print(ex)
            print("du må skrive et tall...\n")
            self.kule()

        # regner ut og printer volum  og overflate om svar er gyldig
        else:
            sleep(2)
            overflate = round(4 * self.PI * r * r, 2)
            volum = round((4/3) * self.PI * r ** 3, 2)
            print(f"\nRadius av kule: {r}")
            print(f"Overflate av kule: {overflate}")
            print(f"Volum av kule: {volum}\n")
            sleep(2)

    # regner ut volum og overflate av sylinder
    def sylinder(self):
        # lagrer radius i r og hødye i h
        try:
            r = float(input('\nSkriv inn radius av sylinderet: '))
            h = float(input("skriv inn høyde av sylinderet: "))

        # printer error om svar ikke er gyldig
        except Exception as ex:
            print(ex)
            print("du må skrive et tall...\n")
            self.sylinder()

        # regner ut og printer overflate og volum om svar er gyldig
        else:
            sleep(2)
            overflate = round(2*self.PI * r**2 + (2*self.PI * r * h))
            volum = round(self.PI * r**2 * h)
            print(f"\nRadius av sylinder: {r}")
            print(f"Overflate av sylinder: {overflate}")
            print(f"Volum av sylinder: {volum}\n")
            sleep(2)

    # starter ny utregning om bruker svarer Y
    # avslutter program om bruker svarer N
    # printer error om svar er noe annet
    def startPåNytt(self):
        svar = input("\nVil du gjøre en ny utregning? [Y][N]\n>>").upper()

        if svar == "Y":
            sleep(1)
            pass

        elif svar == "N":
            sleep(1)
            print("\nSees neste gang!\n")
            sleep(2)
            quit()

        else:
            print("\ndu må skrive enten Y eller N...\n")
            self.startPåNytt()

    # starter programmet i en loop som fortsetter til bruker svarer N i startPåNytt
    def run(self):
        while True:
            self.velgObjekt()
            self.startPåNytt()


# starter programmet om det ikke er importert
if __name__ == "__main__":
    prog = OmkretsOgAreal()
    prog.run()

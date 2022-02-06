import csv


class Grunderen():
    def __init__(self):
        print('''
Velkommen til Schjølberg Fisk AS, 
vi selger Fisk til 100kr stykket + 79kr frakt per bestilling (minimum 5 stykker per kjøp). 
Om du kjøper mer enn 15 stykker vil du få en rabatt på 10%, og om du kjøper mer enn 20 pakker gir vi deg 15% Rabatt. 
Om prisen på bestillingen(uten frakt og rabatter) overstiger 1000kr koster det ingenting for frakt.
        ''')

        self.prisPrVare = 100
        self.frakt = 79
        self.rabatt10 = 0.9
        self.rabatt15 = 0.85

        with open("kunder.csv", "a") as register:
            register.close()

        self.innlogging()
        self.antallVarer = input(
            "hvor mange stykker fisk ønsker du å bestille?\n>>")

    def registrering(self):
        brukernavn = input("\nskriv inn ett brukernavn: ")

        with open("kunder.csv", "r") as register:
            iRegister = False

            reader = csv.reader(register)
            for kunde in reader:
                if kunde == [brukernavn]:
                    iRegister = True

            if iRegister == False:
                with open("kunder.csv", "a") as register:
                    writer = csv.writer(register)
                    writer.writerow([brukernavn])
                    register.close()
                    print(
                        f"Du er nå registrer i vårt kunderegister!\nVelkommen {brukernavn}!\n")

            else:
                print("det brukernavnet eksisterer allerede. velg et annet")
                self.registrering()

    def innlogging(self):
        brukernavn = input(
            "skriv inn brukernavnet ditt for å logge deg inn\nom du ikke har registrert deg før, skriv 'registrer' for å registrere deg\n>>").lower()

        if brukernavn == "registrer":
            self.registrering()

        else:
            iRegister = False

            with open("kunder.csv", "r") as register:
                reader = csv.reader(register)
                for kunde in reader:
                    if kunde == [brukernavn]:
                        iRegister = True

                if iRegister == True:
                    print(f"Velkommen tilbake {brukernavn}!\n")

                else:
                    print(
                        "du er ikke registrert i vårt kunderegister.\nregistrer deg hær")
                    self.registrering()

    def handel(self):
        try:
            antallVarer = int(self.antallVarer)

        except Exception as ex:
            print("Du må skrive inn tall, ikke bokstaver eller symboler...\n")
            self.antallVarer = input(
                "hvor mange stykker fisk ønsker du å bestille: ")
            self.handel()

        else:
            if antallVarer < 5:
                print("Du kan bestille minimun 5 varer..\n")
                self.antallVarer = input(
                    "hvor mange stykker fisk ønsker du å bestille?\n>>")
                self.handel()

            elif antallVarer < 10 and antallVarer >= 5:
                totalPris = antallVarer * self.prisPrVare + self.frakt
                trukketFra = 0
                frakt = 79

            elif antallVarer * self.prisPrVare >= 1000 and antallVarer < 15:
                totalPris = antallVarer * self.prisPrVare
                trukketFra = antallVarer*self.prisPrVare - totalPris
                frakt = 0

            elif antallVarer >= 15 and antallVarer < 20:
                totalPris = self.prisPrVare * antallVarer
                totalPris = totalPris * self.rabatt10
                trukketFra = antallVarer*self.prisPrVare - totalPris
                frakt = 0

            elif antallVarer >= 20:
                totalPris = self.prisPrVare * antallVarer
                totalPris = totalPris * self.rabatt15
                trukketFra = antallVarer*self.prisPrVare - totalPris
                frakt = 0

            print(f"\nPrisen blir {int(totalPris)} kroner")
            print(f"{int(trukketFra)} kroner er trukket fra i rabatt")
            print(f"{int(frakt)} kroner i frakt")

    def nyPrisutregning(self):
        nyPrisutregning = input(
            "\nønsker du å gjøre en ny prisutregning?\nskriv [Y] for ja, eller [N] for nei\n>>").upper()
        if nyPrisutregning == "Y":
            self.__init__()
            self.run()

        elif nyPrisutregning == "N":
            print(
                "Ta kontakt på telefon 555 44 555 for å gjennomføre handelen. Takk for nå")

        else:
            print("du må skrive enten 'Y' eller 'N'...\n")
            self.nyPrisutregning()

    def run(self):
        self.handel()
        self.nyPrisutregning()


if __name__ == "__main__":
    grunderen = Grunderen()
    grunderen.run()

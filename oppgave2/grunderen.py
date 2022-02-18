import csv


class Grunderen():
    def __init__(self):
        # printer en beskjed som forklarer regler for kjøp, rabatter og prisen på vare
        print('''
Velkommen til Schjølberg Fisk AS, 
vi selger Fisk til 100kr stykket + 79kr frakt per bestilling (minimum 5 stykker per kjøp). 
Om du kjøper mer enn 15 stykker vil du få en rabatt på 10%, og om du kjøper mer enn 20 pakker gir vi deg 15% Rabatt. 
Om prisen på bestillingen(uten frakt og rabatter) overstiger 1000kr koster det ingenting for frakt.
        ''')

        # variabler for å lagre pris på varen, frakt og 10% og 15% rabatt til senere bruk i utregning
        self.prisPrVare = 100
        self.frakt = 79
        self.rabatt10 = 0.9
        self.rabatt15 = 0.85

        # lager en fil som heter kunder som det blir skrevet i senere
        with open("kunder.csv", "a") as register:
            register.close()

        # kaller modulen for innlogging
        self.innlogging()

        # lagrer antall varer du vil bestille i en variabel
        self.antallVarer = input(
            "hvor mange stykker fisk ønsker du å bestille?\n>>")

    # regististrerer en bruker om navnet ikke allerede eksisterer i brukere filen
    def registrering(self):
        brukernavn = input("\nskriv inn ett brukernavn: ")

        # åpner filen kunder i les-modus og lager et variabel med verdi False
        with open("kunder.csv", "r") as register:
            iRegister = False

            # leser filen og sjekker om brukernavnet som ble skrevet inn eksisterer i filen
            # setter iRegister til True om brukernavnet er i filen
            reader = csv.reader(register)
            for kunde in reader:
                if kunde == [brukernavn]:
                    iRegister = True

            # om brukernavnet ikke er i filen, skriver programmet brukernavnet brukeren valgre inn i filen og sier velkommen
            if iRegister == False:
                with open("kunder.csv", "a") as register:
                    writer = csv.writer(register)
                    writer.writerow([brukernavn])
                    register.close()
                    print(
                        f"Du er nå registrer i vårt kunderegister!\nVelkommen {brukernavn}!\n")
            # om brukernavnet eksisterer i filen (iRegister = True) printer den en beskjed og får bruker til å velge et annet navn
            else:
                print("det brukernavnet eksisterer allerede. velg et annet")
                self.registrering()

    # spørr om du skal registrere deg eller logge deg inn
    def innlogging(self):
        brukernavn = input(
            "skriv inn brukernavnet ditt for å logge deg inn\nom du ikke har registrert deg før, skriv 'registrer' for å registrere deg\n>>").lower()

        #  om bruker skriver inn registrer, caller programmet registrering modulen
        if brukernavn == "registrer":
            self.registrering()

        # om bruker ikke skriver registrer så settes iRegister til False
        else:
            iRegister = False

            # kunder filen åpnes i read og sjekker om brukernavnet er i filen
            # setter iRegister til True om brukernavn er i fil
            with open("kunder.csv", "r") as register:
                reader = csv.reader(register)
                for kunde in reader:
                    if kunde == [brukernavn]:
                        iRegister = True

                # om brukernavn er i register sier programmet velkommen
                if iRegister == True:
                    print(f"Velkommen tilbake {brukernavn}!\n")

                # om brukernavn ikke er i registeret blir brukeren sendt til registrering
                else:
                    print(
                        "du er ikke registrert i vårt kunderegister.\nregistrer deg hær")
                    self.registrering()

    # prosesserer selve handelen
    def handel(self):
        # prøver å gjøre "antallVarer" om til integer
        try:
            antallVarer = int(self.antallVarer)

        # om "antallVarer" ikke er mulig å gjøre om til integer printes en error og handelen startes på nytt
        except Exception as ex:
            print("Du må skrive inn tall, ikke bokstaver eller symboler...\n")
            self.antallVarer = input(
                "hvor mange stykker fisk ønsker du å bestille: ")
            self.handel()

        # printer beskjed om du prøver å bestille mindre en 5 varer og starter handelen på nyttt
        else:
            if antallVarer < 5:
                print("Du kan bestille minimun 5 varer..\n")
                self.antallVarer = input(
                    "hvor mange stykker fisk ønsker du å bestille?\n>>")
                self.handel()

            # regner ut pris for vare + frakt
            elif antallVarer < 10 and antallVarer >= 5:
                totalPris = antallVarer * self.prisPrVare + self.frakt
                trukketFra = 0
                frakt = 79

            # regner ut pris for vare uten frakt
            elif antallVarer * self.prisPrVare >= 1000 and antallVarer < 15:
                totalPris = antallVarer * self.prisPrVare
                trukketFra = antallVarer*self.prisPrVare - totalPris
                frakt = 0

            # regner ut pris for vare med 10% rabatt og uten frakt
            elif antallVarer >= 15 and antallVarer < 20:
                totalPris = self.prisPrVare * antallVarer
                totalPris = totalPris * self.rabatt10
                trukketFra = antallVarer*self.prisPrVare - totalPris
                frakt = 0

            # regner ut pris for vare med 15% rabatt og uten frakt
            elif antallVarer >= 20:
                totalPris = self.prisPrVare * antallVarer
                totalPris = totalPris * self.rabatt15
                trukketFra = antallVarer*self.prisPrVare - totalPris
                frakt = 0

            # printer prisen for bestillingen, hvor mye som er trukket fra i rabatt og hvor mye det kostet for frakt
            print(f"\nPrisen blir {int(totalPris)} kroner")
            print(f"{int(trukketFra)} kroner er trukket fra i rabatt")
            print(f"{int(frakt)} kroner i frakt")

    # starter en ny prisutregning om bruker skrivet "Y" og avsluttet programmet med kontaktinformasjon om bruker skriver "N"
    # starter nyPrisUtregning på nytt om svar ikke er Y eller N
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

    # starter programmet
    # er den modulen du caller for å starte programmet
    def run(self):
        self.handel()
        self.nyPrisutregning()


# starter programmet om den ikke er importert
if __name__ == "__main__":
    grunderen = Grunderen()
    grunderen.run()

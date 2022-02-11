	# 	○ Finn ut hva som er de ti største landene per areal.
	# 	○ Lag et spill der man kan gjette seg til de ti største landene ved å skrive inn et og et land.
	# 	○ Spillet skal stoppe når du har gjettet alle ti landene.
	# 	○ UTFORDRING:
	# 		§ Spilleren må gjette fra størst til minst.
	# Til denne oppgaven må du bruke lister, input, variabler, funksjoner og betingelser. 
	
	# Eksempel på kjøring:
	# Hva er de ti største landene per areal i verden? Gjett: Russland
	
	# Ja! Russland er et av de ti største landene i verden. 9 land igjen. Gjett: 
	
	# ….
	
	# Ja! Kina er et av de største landene i verden. 0 land igjen.
	# Du klarte det.
	# Slutt. 

class DeTiStørste:
    def __init__(self):
        self.tiStørste = sorted({
            "Russland": 17098242,
            "Canada": 9984670,
            "USA": 933517,
            "Kina": 9596960,
            "Brasil": 8515770,
            "Australi": 7741220,
            "India": 287263,
            "Argentina": 2780400,
            "Kasakhstan": 2724900,
            "Algerie": 2381740
        }.items(), key=lambda x: x[1], reverse=True)
    
    def gjett(self):
        gjett = input("gjett: ")
        return(gjett)
    
    def sjekkSvar(self):
        for item in self.tiStørste:
            print(item[0], item[1])
    
    def run(self):
        self.sjekkSvar()

run = DeTiStørste()
run.run()

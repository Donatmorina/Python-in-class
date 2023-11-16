
#Oppgave 1, 2 og 6

class Bil:
    def __init__(self, merke, modell, år, eier=None):    
        self.merke = merke
        self.modell = modell
        self.år = år
        self.eier = eier

    def skriv_ut_info(self):
        if self.eier == None:
            print(f"Merke: {self.merke}, Modell: {self.modell}, År: {self.år}")
        else:
            print(f"Merke: {self.merke}, Modell: {self.modell}, År: {self.år} eier: {self.eier.navn}")

#Oppgave 3
        
    def alder(self, nåverende_år = 2023):
        return (int(nåverende_år) - int(self.år))

#Oppgave 4

bil1 = Bil("Volkswagen", "Golf", 2019)
bil2 = Bil("Tesla", "Model 3", 2021)
    
bilpark = [bil1, bil2]

def bilpark_info(bilpark):
    
    for bil in bilpark:
        bil.skriv_ut_info()

#Oppgave 5 

class Eier:
    def __init__(self, navn, adresse):
        self.navn = navn
        self.adresse = adresse

    def skriv_ut_info(self):
        print(f"Navn: {self.navn}, Adresse: {self.adresse}")

eier1 = Eier("Ola Nordmann", "Solheimslien")
bil2.eier = eier1
bilpark_info(bilpark)

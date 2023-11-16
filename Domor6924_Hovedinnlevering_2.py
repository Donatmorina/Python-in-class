
class Tekstanalyse:

    tekst = ''  # teksten som analyseres
    avsnittliste = []  # liste over normaliserte avsnitt i teksten
    ordlister = []  # liste av lister over ord som forekommer i hvert avsnitt
    ordtellinger = []  # liste av lister med ordtellinger for hvert avsnitt

    def __init__(self, tekst):
        self.tekst = tekst

    def normaliser_tekst(self, spesialtegn='.,:;!?'):
        "Fjerner spesialtegn fra self.tekst og konverterer til små bokstaver."

        for tegn in spesialtegn:
            self.tekst = self.tekst.replace(tegn, "")
        self.tekst = self.tekst.lower()
        return self.tekst
    
    def til_avsnitt(self, avsnittskille='\n\n'):
        "Deler self.tekst opp i en liste av avsnitt som lagres i self.avsnitt ."
        
        self.avsnittliste = self.tekst.split(avsnittskille)

    def lag_ordliste(self, avsnittekst):
        "Lager en liste av ord som forekommer i avsnittet."

        ordliste = []
        for ordet in avsnittekst.split():
            ordliste.append(ordet)
        return ordliste
        
    def tell_ordforekomster(self, ordliste, avsnittekst):
        "Lager en liste over antall forekomster av ordene i ordliste i avsnittet."

        ordtelling = []
        alle_ord = avsnittekst.split()
        for ordet in ordliste:
            antall = alle_ord.count(ordet)
            ordtelling.append(antall)
        return ordtelling        

    def analyser_tekst(self):
        "Lager en ordliste og teller ordforekomster for hvert avsnitt i teksten."
        ordlister = []
        ordtellinger = []
        for avsnittekst in self.avsnittliste:
            ordliste = self.lag_ordliste(avsnittekst)
            ordtelling = self.tell_ordforekomster(ordliste, avsnittekst)
            ordlister.append(ordliste)
            ordtellinger.append(ordtelling)
        self.ordlister = ordlister
        self.ordtellinger = ordtellinger

    def skriv_ut(self):
        "Skriver ut analyseresultatene for hvert avsnitt på skjermen."

        x = 0
        for avsnitt in self.avsnittliste:
            print(f"Avsnitt {x+1}: \n{avsnitt} \n{self.ordlister[x]} \n{self.ordtellinger[x]}")
            x = x + 1
    
    def lagre_til_fil(self, filnavn):
        "Lagrer analyseresultatene for hvert avsnitt i en fil."
        
        with open(filnavn, 'w') as fil:
            x = 0
            for avsnitt in self.avsnittliste: 
                fil.write(f"Avsnitt {x+1}: \n{avsnitt} \n{self.ordlister[x]} \n{self.ordtellinger[x]}")
                x = x + 1
                

# testkjøring
filnavn = 'eksempeltekst.txt'
eksempeltekst = open(filnavn).read()
tekstanalyse = Tekstanalyse(eksempeltekst)
tekstanalyse.normaliser_tekst()
tekstanalyse.til_avsnitt()
tekstanalyse.analyser_tekst()
tekstanalyse.skriv_ut()
tekstanalyse.lagre_til_fil('testresultat.txt')

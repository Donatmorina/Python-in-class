

#Temaoppgave 5
#1a)
def telle_bokstaver(ditt_ord, lengde_bokstaver):
    return ditt_ord.count(lengde_bokstaver)
#1b)
def telle_ord(ditt_ord):
    
    for lengde in ditt_ord:
        return (len(ditt_ord.split()))
#Oppgave 2
def erstatte_bokstav(ditt_ord, x, y):
    return ditt_ord.replace(x,y)
#Oppgave 3
#3a og 3b)
def formater_navn(fornavn, etternavn, mellomnavn=None):
    if mellomnavn != None:
        return f"{etternavn}, {fornavn} {mellomnavn}"
    else:
        return f"{etternavn}, {fornavn}"
#Oppgave 4
def finn_mest_brukte_ord(setning):
    ordliste = setning.split()
    teller = 0
    for ordet in ordliste:
        antall_ord = ordliste.count(ordet)
        if antall_ord > teller:
            mest_brukt = ordet
            teller = antall_ord
    return mest_brukt
print(finn_mest_brukte_ord("Dette er en test som er enkel og grei"))

#for i in range(n+1, 9)
##
###
####
#####
######
#######

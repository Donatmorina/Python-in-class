#oppgave 1

import math

def pi_function(d=2):
    if d > 15:
          print("For mange desimaler")
          return(pi)
    else:
        print(round(pi,d ))


#oppgave 2


def temp_konv(grader, skala):
    if skala == "C":
        print((grader)*(9/5)+32)

    elif skala == "F":
        print((grader-32)*(5/9))

    else:
       print("prøv på nytt")
        

#oppgave 3a)


saldo = 500
rentesats = 0.01

def innskudd(ditt_innskudd):
    global saldo
    saldo = saldo + ditt_innskudd
    endring("+" + str (ditt_innskudd))

def uttak(ditt_uttak):
    global saldo
    saldo = saldo - ditt_uttak
    endring("-" + str(ditt_uttak))
    
def beregn_rente():
    global rentesats
    if saldo >= 1000000:
        rentesats = 0.02
    else:
        rentesats = 0.01
    return (saldo * rentesats)

def renteoppgjør():
    global saldo
    saldo = saldo + beregn_rente()


#oppgave 3b)


def velg():
    print("--------------------")
    print("1 - vis saldo")
    print("2 - innskudd")
    print("3 - uttak")
    print("4 - renteoppgjør")
    print("5 - siste endring")
    print("--------------------\n")
    
    valg = int(input("Velg handling: "))
    
    global saldo
    
    if valg == 1:
        print(saldo)
        
    elif valg == 2:
        penger_inn = int(input("Beløp: "))
        innskudd(penger_inn)
        if valg == 2 and int(penger_inn) >= 100000:
            print("Gratulerer, du får bonusrente")
    
    elif valg == 3:
        penger_ut = int(input("Beløp: "))
        uttak(penger_ut)
        if valg == 3 and int (saldo) < 1000000:
            print("Du har nå ordinær rente. ")
    elif valg == 4:
        return renteoppgjør()

    elif valg == 5: 
        print(endring1)
        print(endring2)
        print(endring3)
        

#Oppgave 3c)


endring1 = None
endring2 = None 
endring3 = None

def endring(siste_endring):
    global endring1
    global endring2
    global endring3

    endring1 = endring2
    endring2 = endring3
    endring3 = siste_endring


#Oppgave 4

import random

def tre_tilfeldige():
    tall_1 = random.randint(1,9) 
    tall_2 = random.randint(1,9) 
    tall_3 = random.randint(1,9)

    minste = min(tall_1, tall_2, tall_3)
    største = max(tall_1, tall_2, tall_3)
    midt = (største + tall_2 + minste - minste - største)

    tall = str(minste)+ str(midt) + str(største)
    return int(tall)







    
    
    








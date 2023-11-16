
#Oppgave 1

#1a og 1b)

def multiplikasjonstabell(n):
    max_num = n * n
    num_bredde = len(str(max_num))
    
    print(" * |", end=" ")
    for x in range(1, n + 1):
        print(f"{x:>{num_bredde}}", end=" ")
    print("\n" + "---+" + "----" * n)
    
    for tall in range(1, n + 1):
        print(f"{tall:>{num_bredde}} |", end=" ")
        for x in range(1, n + 1):
            resultat = tall * x
            print(f"{resultat:>{num_bredde}}", end=" ")
        print()
#Oppgave 2
def fakultet(z):
    resultat = 1 
    if type(z) == int:
        if z < 0:
            print("tallet må være større enn 0. ")
    elif type(z) == float:
        print("tallet kan ikke ha desimaler. ")
        return 
        
    for i in range(1, z + 1):
        resultat *= i
    return resultat
def fakultet_2(y):
    if type(y) == int:
        if y < 0:
            print("tallet må være større enn 0. ")
    elif type(y) == float:
        print("tallet kan ikke ha desimaler. ")
        return
    resultat = 1
    i = 1
    while i <= y:
        resultat *= i
        i += 1
    return resultat


        


    



#Oppgave 1

personer = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

def lag_fortegnelse(personer):
    
    x = dict(personer)
    return x

#Oppgave 2

personer_2 = {'Alice': 25, 'Charlie': 35, 'Bob': 30}
def sorter_personer_etter_navn(personer_2):

        
    #x = tuple(personer_dict)
    #x = sorted(x)

    tuppel_liste = []
    for key, value in personer_2.items():
        tuppel_liste.append((key, value))
        tuppel_sortert_liste = sorted (tuppel_liste)
        
        
    return(tuppel_sortert_liste)

#Oppgave 3

vennefortegnelse = {'Alice': ['Bob', 'Charlie', 'Devin'], 'Bob': ['Charlie'], 'Charlie': ['Alice'], 'Devin': ['Alice', 'Bob'], 'Eva': ['Charlie', 'Bob']}
def finn_gjensidige_venner(venneliste, navn):

    gjensidige_venner = []
    

    if navn in venneliste:
        for venner in venneliste[navn]:
            if navn in venneliste[venner]:
                gjensidige_venner.append(venner)
                
    return gjensidige_venner


#Oppgave 4

def finn_venners_venner(venneliste, navn):

    venners_venner = []
    if navn not in venneliste:    
        for venn in vennefortegnelse[navn]:
            for venners_venn in venneliste[venn]:
                if venners_venn not in vennefortegnelse[navn] and venners_venn != navn:
                    venners_venner.append(navn)
    return venners_venner



    
            
            
            
        
    

    

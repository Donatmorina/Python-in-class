
import tkinter as tk


#Oppgave 1


root = tk.Tk()

def lukk_vindu():
    print("Du har trykket på lukkeknappen :) ")
    root.destroy()

Farvell_knapp = tk.Button(root, text = 'Farvel', command = lukk_vindu)
Farvell_knapp.grid(row = 1, column = 0)



#Oppgave 2


antall_klikk = 0

def tell_knapp():
    global antall_klikk
    antall_klikk = antall_klikk + 1
    print(antall_klikk)
    telleknapp.configure(text = f"Labelled {antall_klikk}")
    
telleknapp = tk.Button(root, text = f"Labelled 0", command = tell_knapp)
telleknapp.grid(row = 3, column = 0)

root.mainloop()

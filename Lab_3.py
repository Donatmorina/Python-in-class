
#Oppgave 1

def selection_sort_one_pass(array):

    size = len(array)
    for pass_num in range(size):
        minimum_index = pass_num
    
        for elem in range(pass_num + 1, size):
            if array[elem] < array[minimum_index]:
                minimum_index = elem
        
        temp = array[pass_num]
        array[pass_num] = array[minimum_index]
        array[minimum_index] = temp

        #break

test_liste = [5, 2, 3, 4, 0, 1]
selection_sort_one_pass(test_liste)
#print(test_liste)


#Oppgave 2
from large_list import liste

print(len(liste))


def forLoop(para):
    for i in range(11):
        print("I er ", i + para)


forLoop(5)

print("Hello World!")
        
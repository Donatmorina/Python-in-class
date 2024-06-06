

#Assignment 2 INFO135 Domor6924 

 

#1.  

def selection_sort(your_list):
    size = len(your_list)
    for elem in range(3):
        min_index = elem
    
        for i in range(elem + 1, size):
            if your_list[i] < your_list[min_index]:
                min_index = i
        
        temp = your_list[elem]
        your_list[elem] = your_list[min_index]
        your_list[min_index] = temp
    
    print(your_list)

your_list = [1502, 1560, 1600, 1540, 100, 1660, 1700, 2024] 
selection_sort(your_list)



#2

def bubble_sort(liste):
    size = len(liste)
    for i in range(3):
        for j in range(0, size - i - 1):
            if liste[j] > liste[j + 1]:
                temp = liste[j]
                liste[j] = liste[j + 1]
                liste[j + 1] = temp
    
    print(liste)

liste =  [400, 10, 210, 160, 70, 220, 280, 380, 180, 260, 540]
bubble_sort(liste)


#3

def sort_and_rem_dup(arr):
    
    ny_liste = []

    for elem in arr:
        if elem not in ny_liste:
            ny_liste.append(elem)

    size = len(ny_liste)
    for i in range(size):
        for j in range(0, size - i - 1):
            if ny_liste[j] > ny_liste[j + 1]:
                temp = ny_liste[j]
                ny_liste[j] = ny_liste[j + 1]
                ny_liste[j + 1] = temp
                
    

    print(ny_liste)

new_list = [5, 4, 3, 2, 1, 2, 3, 4, 5]
sort_and_rem_dup(new_list)


#4

class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()


class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def size(self):
        return len(self.items)

def check_palindrome(ditt_ord):
    stack = Stack()
    queue = Queue()

    for word in ditt_ord:
        stack.push(word)
        queue.enqueue(word)

    while not stack.is_empty():
        if stack.pop() != queue.dequeue():
            return "Not Palindrome"

    return "Palindrome"

result = check_palindrome("hello")
print(result) 

result = check_palindrome("civic")
print(result)  




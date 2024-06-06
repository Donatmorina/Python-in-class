#Assignment 1

#1.

#a) If we are looking for a specific word in the Italian dictionary with 102400 words,
#   with binary search it would take us 17 guesses in the worst case. This is because we half the number every guess

#b) If we are looking for a specific word in the French dictionary with 480000 words,
#   with binary search it would take us 19 guesses in the worst case. This is because we half the number every guess



#2.

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self, head):
        self.head = head
    
    def print_list(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.next
        
node1 = Node("banan") 
node2 = Node("eple") 
node3 = Node("pære") 

node1.next = node2
node2.next = node3

my_linked_list = LinkedList(node1)
my_linked_list.print_list()

#3.

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

def reverse_list(liste):
    ny_liste = Stack()
    for item in liste:
        ny_liste.push(item)

    reversed_liste = []
    while not ny_liste.is_empty():
        reversed_liste.append(ny_liste.pop())
    return reversed_liste


my_list = [1,2,3,4,5]
print(reverse_list(my_list))
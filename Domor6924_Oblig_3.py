
#Oppgave 1

#key = 27 % 13 = 1
#key = 130 % 13 = 0

# I think the answer is b) 1,0


#Oppgave 2

#Q1 I think the load factor is 9/11 because 9 of 11 nodes have a number stored in them

#Q2 I think its answer D because after taking the hash function h(key) = key % m, we get the following numbers
#   presented as indexes of where they should map to


#Oppgave 3


import hashlib as hl
import random

class HashClass:
    def __init__(self, id_num):
        self.id_num = str(id_num)
        self.salt = random.randint(1, 1000)
        self.id_num_with_salt = self.id_num + str(self.salt)

    def hash_it(self):
        hash_string = hl.sha1(self.id_num_with_salt.encode()).hexdigest()
        return hash_string

    def print_it(self):
        hashed_value = self.hash_it()
        print(hashed_value)

my_hash = HashClass(11011999)
my_hash.print_it()


#Oppgave 4

def most_frequent_integer(my_list):

    hash_list = {}

    for num in my_list:
        if num not in hash_list:
            hash_list[num] = 1
        else:
            hash_list[num] += 1

    max_value = max(hash_list.values())

    resultat = [key for key, value in hash_list.items() if value == max_value]
    print(resultat)

my_list = [10, 2, 5, 2, 0, 5, 6, 8, 5, 10]
result = most_frequent_integer(my_list)
print(result)




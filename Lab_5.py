
#Oppgave 1

class MiniBankSystem:

    def __init__(self):

        self.balance = 0
        self.bills = [("electric", 5000), ("water", 2200), ("wolfram alpha", 150)]

    def add_money(self, amount):

        self.balance += amount
        return f"You added {amount} to your account, your new balance is {self.balance}"

    def pay_bill(self, bill_name):

        for bill in self.bills:
            if bill[0] == bill_name:
                if self.balance >= bill[1]:
                    self.balance -= bill[1]
                    return f"You paid {bill_name}"
    
    def get_sorted_bills(self):
        sorted_bills = sorted(self.bills, key=lambda x: x[1], reverse=True)
        return sorted_bills

bank = MiniBankSystem()
print(bank.add_money(10000))
print(bank.get_sorted_bills())


#Oppgave 2

#liste = list(range(100))

#def fibonacci(n):
#    first_num = 0
#    second_num = 1

#    for i in range(n):
#        print(first_num)
#        next_num = first_num + second_num
#        first_num, second_num = second_num, next_num   

#fibonacci(11)


def while_fibonacci(n):

    first_num = 0
    second_num = 1
    while first_num >= n:
        print(first_num)
        next_num = first_num + second_num
        first_num, second_num = second_num, next_num   

while_fibonacci(10)
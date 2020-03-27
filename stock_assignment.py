from lichcode import LinkedListTail


# Queue just list popping from head pushing from the end!
class Queue:
    def __init__(self):
        self.myList = []

# Represent the data through specific memory
    def __repr__(self):
        return repr(self.myList)

# Pushing to the list
    def push(self, data):
        self.myList.append(data)

# Getting the list
    def get(self):
        return self.myList

# Popping from first index
    def pop(self):
        self.myList.pop(0)

# access_pop popping from every index in the list
    def access_pop(self, i):
        print(self.myList[i])
        self.myList.pop(i)

# access function to pick from every index
    def access(self, a):
        return int(self.myList[a])


# Creating banks to store information
bank_of_stock = Queue()           # Main Bank
number = int(input("What is you option? 1)Adding the stocks 2)Look at the bank of the stocks : "))  # Give an option
if number == 1:  # number 1 is for adding stocks as blocks
    while True:   # Looping till pressing 0
        amount = int(input('How many stocks do u wanna buy: '))     # amount is how many stocks in EACH block
        print("To stop buying press 0")            # Giving an instruction to stop pressing 0
        print(f'Adding...{amount}')              # Printing how many blocks is added
        bank_of_stock.push(amount)     # Pushing to the head!
        if amount == 0:                       # if user pressing 0 breaks
            break                                        # Breaking function
    number = int(input("What is you option?:Press 2 to sell the stocks")) # Giving an option for selling the stock and make profit!
    if number == 2:                                      # 2 for printing bank
        print(bank_of_stock)                                 # Bank
        option = int(input("Which stock to sell: "))           # Option which stock to sell
        if option == 1:                                         # if option 1 selling first stock in the list
            print(f"The stock which u want to sell {bank_of_stock.access(0)}")   # Printing this index
            bank_of_stock.pop()          # Popping from head
            bank_of_stock.access_pop(-1)                # Popping the last number because it is 0
            print(f"Your current bank of the stocks {bank_of_stock}")    # Current bank
            prev_price_stock = int(input("What was the previous price of this stock $$$?: "))  # TO give price for pre_s
            curr_price_stock = int(input("What is current price of this stock EACH $$$?: "))   # To give price for cur_s
            print(f"Your profit from this stock is ${curr_price_stock * bank_of_stock.access(0) - prev_price_stock * bank_of_stock.access(0)}")
        else:
            option -= 1     # Option -1 because user's option will decrease by one to point the list
            print(f"The stock which u want to sell {bank_of_stock.access(option)}")    # Printing Bank without first
            bank_of_stock.access_pop(option)                       # Popping from user's preference
            bank_of_stock.access_pop(-1)                         # Popping the last because it is 0
            print(f"Your current bank of the stocks {bank_of_stock}")                    # Printing the current bank
            prev_price_stock = int(input("What was the previous price of this stock $$$?: "))  # TO give price for pre_s
            curr_price_stock = int(input("What is current price of this stock EACH $$$?: "))   # To give price for cur_s
            print(f"Your profit from this stock is ${curr_price_stock * bank_of_stock.access(option) - prev_price_stock * bank_of_stock.access(option)}")
else:
    print(bank_of_stock)  # Printing empty bank because there is nothing in the first time!

                    















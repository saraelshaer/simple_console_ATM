class CardHolder:
    def __init__(self, card_num, pin,first_name, second_name, balance=0) :
        self.card_num = card_num
        self.pin = pin
        self.first_name = first_name
        self.second_name = second_name
        self.balance = balance

class ATM:
    def check_balance(self, current_user):
        print(f"Current balance : ${current_user.balance}")
    
    def deposit_money(self, current_user):
        amount= float(input("How much would you like to deposite ? "))
        if amount > 0:
            current_user.balance += amount
            print(f"Deposited ${amount} . Current balance : ${current_user.balance} ")
        else:
            print("Invalid input")

    def withdraw_money(self, current_user):
        amount= float(input("How much would you like to withdraw ? "))
        if amount > 0:
            if amount <= current_user.balance:
                current_user.balance -= amount
                print(f"Withdrawn ${amount} . Current balance: ${current_user.balance}")
            else:
                print("Insufficient funds")
        else:
            print("Invalid input")

    def authenticate(self, card_holders):
        card_number = input("Please insert your debit card : ")
        current_user = None
        for obj in card_holders:
            if(obj.card_num == card_number):
                current_user = obj
                break
        if current_user == None:
            print("Card not recognized. Please try again")
        else:
            while(True):
                PIN = int(input("Please enter your PIN : "))
                if(obj.pin == PIN):
                    print("--------------------------------------------")
                    print(f"Welcome {current_user.first_name} {current_user.second_name} ")
                    return current_user
                
                else:
                    print("Incorrect PIN. Please try again")

#-----------------------------------------------------------    
card_holders=[]
card_holders.append(CardHolder("123456789",1234, "Sara","Elshaer",880))
card_holders.append(CardHolder("123000000",4444, "Kareem","Shabaan",500))
card_holders.append(CardHolder("100000000",0000, "Ali","Ahamed",60))
card_holders.append(CardHolder("000000000",5555, "Renad","Mohammed",1000))
#---------------------------------------------------------------
def main():
    print("Welcome to simple ATM")
    print("-----------------------\n")
    atm = ATM()
    current_user = None
    while( current_user == None):
        current_user = atm.authenticate(card_holders)
    while(True):
        print("---------------------------")
        print("Please enter an option : ")
        print("1) Check balance.")
        print("2) Deposit money.")
        print("3) Withdraw money.")
        print("4) Exit.")
        print("---------------------------")
        option= input()
        if option == "1":
            atm.check_balance(current_user)
        elif option == "2":
            atm.deposit_money(current_user)
        elif option == "3":
            atm.withdraw_money(current_user)
        elif option == "4":
            print("Thank You!. Have a nice day :)")
            break
        else:
            print("Invalid input. Try again")

main()



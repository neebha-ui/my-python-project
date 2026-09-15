balance = 1500
def credit():
    global balance
    amount = int(input("Enter amount: "))
    balance = balance + amount
    print("Amount credited.")

def debit():
    global balance
    amount = int(input("Enter amount:"))
    if amount <= balance:
        balance = balance - amount 
        print("Amount debited.")  
    else:
        print("Insufficient balance.")
def balance_check():
    print("Balance =",balance)
while True:
      print("\nATM MENU") 
      print("1. Credit")  
      print("3.Balance")  
      print("4.Exit")
    
      choice = input("Enter your choice: ") 
      if choice == "1" :
          credit()
      elif choice == "2" :
          debit()
      elif choice == "3" :
        balance_check()
      elif choice == "4" : 
        print("Thank You!")
      else:
          print("Invalid choice")  
        

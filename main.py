import mysql.connector

print("Hello and welcome to BigBucks Bank.")
print("-----------------------------------")

def welcome_menu():
  print("1. Sign in to bank account\n")
  print("2. Create account\n")

print("\nBefore we begin, please sign in to your account. If you don't have an account, please select option 2. \n")
def user_selection():
  user_selection = int(input("\nSelect an option by typing a number:"))
  return user_selection

def sign_in():
  acc_num = input("Enter account number:")
  acc_pin = input("Enter account pin:")
  
def create_acc(): 
  conn = mysql.connector(database="bankapp", user="root", password="0saeAnnett3")
  cursor = conn.cursor()
  cursor.execute("INSERT INTO accounts (username, email, acc_pin) VALUES (%s, %s, %s)", (username, email, acc_pin))
  conn.commit()
  conn.close()
  #  print("After making your account, you will be sent to the welcome menue. Then you will select sign in.")

  


#if user_selection == "1":
 # sign_in()
#elif user_selection == "2":
 # create_acc()

#welcome_menu()
#while program_loop:
#  option = user_selection()

#if option in range:
# if option == 1:
    #sign_in()
#elif option == 2:
 #   create_acc()




print("welcome. What would you like to do?")
#range = (1, 2, 3, 4, 5)

def bank_menu():
  print("1. Check Balance")
  print("2. Withdraw Money")
  print("3. Deposit Money")
  print("4. Modify Account")
  print("5. Delete Account")

def user_choice():
  user_choice = int(input("\nSelect an option by typing a number:"))
  return user_choice


def check_balance(acc_num):
  conn = mysql.connector(database="bankapp", user="root", password="0saeAnnett3")
  cursor = conn.cursor()
  cursor.execute("SELECT balance FROM accounts WHERE acc_num = %s", (acc_num,))
  balance = cursor.fetchone()[0]
  conn.close()
  return balance

def withdraw(acc_num, amount):
  conn = mysql.connector(database="bankapp", user="root", password="0saeAnnett3")
  cursor = conn.cursor()
  cursor.execute("UPDATE accounts SET balance = balance - %s WHERE acc_num = %s", (amount, acc_num))
  cursor.execute("INSERT INTO transactions (acc_num, amount, transc_type) VALUES (%s, %s, 'withdrawal')", (acc_num, amount))
  conn.commit()
  conn.close()

def deposit(acc_num, amount):
  conn = mysql.connector(database="bankapp", user="root", password="0saeAnnett3")
  cursor = conn.cursor()
  cursor.execute("UPDATE accounts SET balance = balance + %s WHERE acc_num = %s", (amount, acc_num))
  cursor.execute("INSERT INTO transactions (acc_num, amount, transaction_type) VALUES (%s, %s, 'deposit')", (acc_num, amount))
  conn.commit()
  conn.close()

def modify(acc_num, new_email, new_password):
  conn = mysql.connector(database="bankapp", user="root", password="0saeAnnett3")
  cursor = conn.cursor()
  cursor.execute("UPDATE accounts SET email = %s, password = %s WHERE acc_num = %s", (new_email, new_password, acc_numd))
  conn.commit()
  conn.close()

def delete(acc_num):
  conn = mysql.connector(database="bankapp", user="root", password="0saeAnnett3")
  cursor = conn.cursor()
  cursor.execute("DELETE FROM accounts WHERE acc_num = %s", (acc_num,))
  conn.commit()
  conn.close()

welcome_menu()
while True:
    option = user_selection()
    if option == 1:
      sign_in()

      bank_menu()
      choice = user_choice()
      if choice == 1:
        acc_num = input("Enter your account number: ")
        balance = check_balance(acc_num)
        print("Your balance is:", balance)         
        pass
      elif choice == 2:
        withdraw()
        pass
      elif choice == 3:
        deposit()
        pass
      elif choice == 4:
        modify()
        pass
      elif choice == 5:
        delete()
        pass   
    
    elif option == 2:
        create_acc()
        bank_menu()
        choice = user_choice()

#bank_menu()1
#if user_choice == "1":
 # check_balance()
#elif user_choice == "2":
 # withdraw()
#elif user_choice == "3":
 # deposit()
#elif user_choice == "4":
 # modify()
#elif user_choice == "5":
 # delete()
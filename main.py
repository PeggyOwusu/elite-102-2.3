import mysql.connector

program_loop = True

print("Hello and welcome to BigBucks Bank.")
print("-----------------------------------")

def welcome_menu():
  print("1. Sign in to bank account\n")
  print("2. Create account\n")

range = (1, 2)

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


if user_selection == "1":
  sign_in()
elif user_selection == "2":
  create_acc()

welcome_menu()
while program_loop:
  option = user_selection()

if option in range:
  if option == 1:
    sign_in()
  elif option == 2:
    create_acc()




print("welcome. What would you like to do?")
#range = (1, 2, 3, 4, 5)

def bank_menu():
  print ("1. Check Balance\n2. Withdraw Money\n3. Deposit Money\n4.Modify Account\n5. Delete Account")

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


bank_menu()
if user_choice == "1":
  check_balance()
elif user_choice == "2":
  withdraw()
elif user_choice == "3":
  deposit()
elif user_choice == "4":
  modify()
elif user_choice == "5":
  delet()
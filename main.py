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
  print("c")



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

#after user enters acc num and pin, the program will take the user's name from the SQL and use it
bank_menu()

print("welcome {name}. What would you like to do?")
def bank_menu():
  print ("1. Check Balance\n2. Withdraw Money\n3. Deposit Money")

def user_choice():
  user_choice = int(input("\nSelect an option by typing a number:"))
  return user_choice

if user_choice == "1":
  check_balance()
elif user_choice == "2":
  withdraw()

def check_balance(acc_num):
    conn = mysql.connector(database="bankapp", user="root", password="0saeAnnett3")
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM users WHERE acc_num = %s", (acc_num,))
    balance = cursor.fetchone()[0]
    conn.close()
    return balance

def withdraw(acc_num, amount):
    conn = mysql.connector(database="bankapp", user="root", password="0saeAnnett3")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET balance = balance - %s WHERE user_id = %s", (amount, acc_num))
    cursor.execute("INSERT INTO transactions (acc_num, amount, transc_type) VALUES (%s, %s, 'withdrawal')", (acc_num, amount))
    conn.commit()
    conn.close()

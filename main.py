import mysql.connector

import tkinter as tk

print("Hello and welcome to BigBucks Bank.")
print("-----------------------------------")

def welcome_menu():
  print("1. Sign in to bank account")
  print("2. Create account")

print("\nBefore we begin, please sign in to your account. If you don't have an account, please select option 2. \n")
def user_selection():
  user_selection = int(input("\nSelect an option by typing a number:"))
  return user_selection

def sign_in():
  acc_num = input("Enter account number:")
  acc_pin = input("Enter account pin:")
  
  conn = mysql.connector.connect(database="bankapp", user="root", password="0saeAnnett3")
  cursor = conn.cursor()
  cursor.execute("SELECT acc_num, acc_pin FROM accounts WHERE acc_num = %s", (acc_num))
  account = cursor.fetchone()

  if account:
    if account[1] == acc_pin:
      print("Sign-in successful.")

    else:
      print("Incorrect PIN. Please try again.")
  else:
    print("Account number not found. Please try again.")

  conn.close()

  
def create_acc(): 
  username = input("Enter username: ")
  email = input("Enter email: ")
  acc_pin = input("Create account pin: ")

  conn = mysql.connector.connect(database="bankapp", user="root", password="0saeAnnett3")
  cursor = conn.cursor()
  cursor.execute("INSERT INTO accounts (username, email, acc_pin) VALUES (%s, %s, %s)", (username, email, acc_pin))
  conn.commit()

  cursor.execute("SELECT LAST_INSERT_ID()")
  acc_num = cursor.fetchone()[0]

  conn.close()

  print("Account created successfully!")
  print("Your account number is:", acc_num)
  #  print("After making your account, you will be sent to the welcome menue. Then you will select sign in.")
  
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

def withdraw():
  acc_num = acc_num_entry.get()
  amount = float(amount_entry.get())
  conn = mysql.connector.connect(database="bankapp", user="root", password="0saeAnnett3")
  cursor = conn.cursor()
  cursor.execute("SELECT balance FROM accounts WHERE acc_num = %s", (acc_num,))
  balance = cursor.fetchone()[0]
  if balance >= amount:
    new_balance = balance - amount
    cursor.execute("UPDATE accounts SET balance = %s WHERE acc_num = %s", (new_balance, acc_num))
    conn.commit()
    print(f"Withdrawal successful. Your balance is now {new_balance}")
  else:
    print("Error", "Insufficient funds.")
  conn.close()

def deposit():
  acc_num = acc_num_entry.get()
  amount = float(deposit_amount_entry.get())
  deposit(acc_num, amount)
  balance = check_balance(acc_num)
  new_balance = balance + amount
  cursor.execute("UPDATE accounts SET balance = %s WHERE acc_num = %s", (new_balance, acc_num))
  conn.commit()
  print(f"Deposit successful. Your balance is now {new_balance}")
  conn.close()

def modify_account():
  acc_num = acc_num_entry.get()
  new_email = new_email_entry.get()
  new_password = new_password_entry.get()
  modify(acc_num, new_email, new_password)
  modify_success_label.config(text="Modification successful.")

def delete_account():
  acc_num = acc_num_entry.get()
  delete(acc_num)
  delete_success_label.config(text="Your account has been deleted. Goodbye.")


def on_sign_in():
  acc_num = acc_num_entry.get()
  acc_pin = acc_pin_entry.get()
  sign_in()

def on_create_account():
  create_acc()

def on_balance_check():
  acc_num = acc_num_entry.get()
  balance = check_balance(acc_num)
  balance_label.config(text="Your balance is: " + str(balance))

window = tk.Tk()

greeting = tk.Label(text="BigBucks Bank",width=10) 
font=("Times",100)
greeting.pack()
window.mainloop()




welcome_menu()
while True:
    option = user_selection()
    if option == 1:
      sign_in()

      bank_menu()
      choice = user_choice()
      if choice == 1: #check balance
        acc_num = input("Enter your account number: ")
        balance = check_balance(acc_num)
        print("Your balance is:", balance)         
        
      elif choice == 2: #withdraw
        acc_num = input("Enter your account number: ")
        amount = float(input("Enter amount to withdraw: "))
        withdraw(acc_num, amount)
        
      elif choice == 3:#deposit
        acc_num = input("Enter your account number: ")
        amount = float(input("Enter amount to deposit: "))
        deposit(acc_num, amount)
        
      elif choice == 4: #modify acc
        acc_num = input("Enter your account number: ")
        new_email = input("Enter new email: ")
        new_password = input("Enter new password: ")
        modify(acc_num, new_email, new_password)
        
      elif choice == 5: #delete acc
        acc_num = input("Enter your account number: ")
        delete(acc_num)
        break   
    
    elif option == 2:
        create_acc()
        print("Thank you for making an account with BigBucks Bank. Please sign in.")
        bank_menu()
        break


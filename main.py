program_loop = True

print("Hello and welcome to BigBucks Bank.")
print("-----------------------------------")

def bank_menu():
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

bank_menu()
while program_loop:
  option = user_selection()

  if option in range:
    if option == 1:
      sign_in()
    elif option == 2:
      create_acc()
def add(num1,num2):
  sum = num1+num2
  print("Addition is " + str(sum) + ".")

def sub(num1,num2):
  difference = num1-num2
  print("Subtraction is " + str(difference) + ".")

def mul(num1,num2):
  product = num1*num2
  print("Multiplication is " + str(product) + ".")

def div(num1,num2):
  quotient = num1/num2
  remainder = num1%num2
  print("Division is " + str(quotient) + ". The remainder is " + str(remainder) + ".")

def main():
  print("\n********Simple Calculator********\n")
  print("Press 1 for Addition\n")
  print("Press 2 for Subtraction\n")
  print("Press 3 for Multiplication\n")
  print("Press 4 for Division\n")
  print()
  option = input("Enter the number that corresponds to the operation that you would like to perform. ") 
  print("\n")
  if option == "1":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    add(num1,num2)
  if option == "2":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    sub(num1,num2)
  if option == "3":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    mul(num1,num2)
  if option == "4":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    div(num1,num2)
  print("\n")
  again = input("Would you like to continue? y/n? ")
  if again.upper() == "Y":
    main()
  else:
    print("Alright. See you soon!")
main()

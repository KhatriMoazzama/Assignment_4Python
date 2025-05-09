# sum of two integers taken from user as input

def main():
  print("********Sum of two numbers********")
  print("**********************************")
  num1 : str = input("Enter first number : ")
  num1 = int(num1)
  num2 : str = input("Enter second number : ")
  num2 = int(num2)
  sum : int = num1 + num2
  print(f" Sum of {num1} and {num2} is {sum} ")
  print("**********************************")


if __name__ == '__main__':
  main()
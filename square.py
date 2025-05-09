# taking input from user and make a square of it

def main():
  number :str  = input("Enter number to see it's square : ")
  number = float(number)
  print(f"square of {number:.2f} is {number**2:.2f} ")

if __name__ == "__main__":
  main()
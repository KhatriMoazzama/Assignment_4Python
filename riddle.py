#Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.


def main():
  Anthon: int = 21
  Beth: int = Anthon + 6
  Chen: int = Beth + 20
  Drew : int = Chen + Anthon
  Ethan: int = Chen

  print("*******Riddle*******\n")
  print("""Anton is 21 years old.
        \n Beth is 6 years older than Anton.
        \n Chen is 20 years older than Beth.
        \n Drew is as old as Chen's age plus Anton's age.
        \n Ethan is the same age as Chen.\n\n""")

  print(f" Anthon is {Anthon} years old")
  print(f" Beth is {Beth} years old")
  print(f" Chen is {Chen} years old")
  print(f" Drew is {Drew} years old")
  print(f" Ethan is {Ethan} years old") 


if __name__ == '__main__':
  main()
  
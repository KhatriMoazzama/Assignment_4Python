#perimeter of triangle my taking sides input from user


def main():
  print("Perimeter of Triangle")
  s1: str = input("Enter length of first side : ")
  s1 = int(s1)
  s2 : str = input("Enter length of secoond side : ")
  s2 = int(s2)
  s3 : str = input("Enter length of third side : ")
  s3 = int(s3)
  perimter :int = s1 + s2 + s3

  print(f"Perimeter of Triangle is {perimter}") 


if __name__  == "__main__" :
 main()


# conversion of temperature from farenheit to celcius scale

def main():
  print("Conversion of temperature form farenheit to celcius")
  temperature_F : str = input("Enter temperature in degree farenheit : ")
  temperature_F = float(temperature_F)
  temperature_C : float = (temperature_F - 32) * 5.0/9.0
  print(f" Temperature {temperature_F:.2f} ∘F = {temperature_C:.2f} ∘C")



if __name__ == '__main__':
  main()


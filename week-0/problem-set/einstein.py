# Prompt the user for input of a mass in kilograms.
# Convert that mass into energy using Einstein's formula.
# Output the result.


def main():
  mass = int(input("Enter a number: "))
  result = convert_mass_to_energy(mass)
  print(result)


def convert_mass_to_energy(m):
  e = m * pow(300000000, 2)
  return e

if __name__ == "__main__":
  main()

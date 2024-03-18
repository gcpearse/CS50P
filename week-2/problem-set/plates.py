# Prompt the user for a vanity plate
# Plate must begin with at least 2 letters
# Plate must contain between 2 and 6 characters
# Numbers must come at the end
# The first number cannot be 0
# Only alphanumeric characters are allowed
# Print "Valid" if the plate is valid
# Otherwise, print "Invalid"


def main():
  plate = input("Plate: ").strip()
  if validate_plate(plate):
    print("Valid")
  else:
    print("Invalid")


def validate_plate(plate: str):
  count = 0
  if (2 <= len(plate) <= 6 and 
      plate.isalnum() and
      plate[0:2].isalpha()):
    for i in range(len(plate)):
      if plate[i].isnumeric():
        count += 1
        if not plate[i:].isnumeric():
          return False
      if (plate[i] == "0" and
          count == 1):
        return False
    return True


if __name__ == "__main__":
  main()

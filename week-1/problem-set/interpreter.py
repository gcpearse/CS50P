# Prompt the user for an arithmetic expression
# Output the result as floating-point value
# Ensure the result is rounded to 1 decimal place


def main():
  expression = input("Enter an expression: ").strip()
  result = calculate(expression)
  print(result)


def calculate(expression: str):
  x, y, z = expression.split(" ")
  x = float(x)
  z = float(z)
  match y:
    case "+":
      result = x + z
    case "-":
      result = x - z
    case "*":
      result = x * z
    case "/":
      result = x / z
  return round(result, 1)


if __name__ == "__main__":
  main()

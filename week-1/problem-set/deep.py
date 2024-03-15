# Prompt the user for an answer.
# If the input is 42, forty-two, or forty two, output Yes.
# Otherwise, output No.


def main():
  answer = input("Enter your answer: ").lower()
  if check_answer(answer):
    print("Yes")
  else:
    print("No")


def check_answer(answer):
  match answer:
    case "42" | "forty-two" | "forty two":
      return True
    case _:
      return False


main()

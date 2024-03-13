def main():
  score = int(input("Enter score out of 100: "))
  result = set_grade(score)
  print(result)


def set_grade(score):
  if score >= 90:
    return "Grade: A"
  elif score >= 80:
    return "Grade: B"
  elif score >= 70:
    return "Grade: C"
  elif score >= 60:
    return "Grade: D"
  else:
    return "Grade: F"


main()

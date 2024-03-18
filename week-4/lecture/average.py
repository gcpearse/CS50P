import statistics


def main():
  res = find_average([80, 40])
  print(res)


def find_average(numbers):
  return statistics.mean(numbers)


if __name__ == "__main__":
  main()

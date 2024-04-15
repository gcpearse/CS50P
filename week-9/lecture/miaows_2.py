def miaow(n: int) -> str:
  """
  Miaow n times.

  :param n: Number of times to miaow
  :type n: int
  :raise TypeError: If n is not an int
  :return: A string of n miaows, one per line
  :rtype: str
  """
  return "Miaow!\n" * n


number: int = int(input("Number: "))
miaows: str = miaow(number)
print(miaows, end="")

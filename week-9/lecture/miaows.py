class Cat:
  MIAOWS = 3

  def miaow(self):
    for _ in range(Cat.MIAOWS):
      print("Miaow!")


cat = Cat()
cat.miaow()

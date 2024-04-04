class Student:
  def __init__(self, name, house):
    self.name = name
    self.house = house

  def __str__(self):
    return f"{self.name} is in {self.house}."
  
  @classmethod
  def get(cls):
    name = input("Name: ").strip().title()
    house = input("House: ").strip().title()
    return cls(name, house)
  
  # Getter
  @property
  def name(self):
    return self._name
  
  # Setter
  @name.setter
  def name(self, name):
    if not name:
      raise ValueError("Missing name.")
    self._name = name

  @property
  def house(self):
    return self._house

  @house.setter
  def house(self, house):
    if house not in [
      "Gryffindor",
      "Hufflepuff",
      "Ravenclaw",
      "Slytherin"
    ]:
      raise ValueError("Invalid house.")
    self._house = house


def main():
  print(Student.get())


if __name__ == "__main__":
  main()

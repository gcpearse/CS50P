# Implement a class called Jar
# __init__ should initialise the jar with the given capacity
# If capacity is not a positive integer, __init__ should raise a ValueError
# __str__ should return a string with n 🍪, where n is the number of cookies in the jar
# deposit should add n cookies to the jar
# If the capacity would be exceeded, deposit should raise a ValueError
# withdraw should remove n cookies from the jar
# If n is greater than the number of cookies in the jar, withdraw should raise a ValueError
# capacity should return the jar's capacity
# size should return the number of cookies in the jar


class Jar:
  def __init__(self, capacity=12):
    self.capacity = capacity
    self.size = 0

  def __str__(self):
    return "🍪" * self.size

  def deposit(self, n):
    if self.size + n <= self.capacity:
      self.size += n
    else:
      raise ValueError("Cookie jar is full!")
  
  def withdraw(self, n):
    if self.size - n >= 0:
      self.size -= n
    else:
      raise ValueError("Not enough cookies!")
  
  @property
  def capacity(self):
    return self._capacity
  
  @capacity.setter
  def capacity(self, capacity):
    if capacity < 0 or type(capacity) is not int:
      raise ValueError("Capacity should be a positive integer.")
    self._capacity = capacity
  
  @property
  def size(self):
    return self._size
  
  @size.setter
  def size(self, size):
    self._size = size

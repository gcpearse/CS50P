class Vault:
  def __init__(self, galleons=0, sickles=0, knuts=0):
    self.galleons = galleons
    self.sickles = sickles
    self.knuts = knuts

  def __str__(self):
    return f"{self.galleons} galleons, {self.sickles} sickles, {self.knuts} knuts."
  
  def __add__(self, other):
    galleons = self.galleons + other.galleons
    sickles = self.sickles + other.sickles
    knuts = self.knuts + other.knuts
    return Vault(galleons, sickles, knuts)


potter_vault = Vault(100, 50, 25)
print(f"Potter vault: {potter_vault}")

weasley_vault = Vault(25, 50, 100)
print(f"Weasley vault: {weasley_vault}")

combined_vault = potter_vault + weasley_vault
print(f"Combined vault: {combined_vault}")

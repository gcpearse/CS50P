def total(galleons, sickles, knuts):
  return (galleons * 17 + sickles) * 29 + knuts

coins_list = [100, 50, 25]

coins_dict = {
  "galleons": 100,
  "sickles": 50,
  "knuts": 25
}

print(f"{total(*coins_list)} knuts")
print(f"{total(**coins_dict)} knuts")

def f(*args, **kwargs):
  print(f"Positional: {args}")
  print(f"Named: {kwargs}")


f(100, 50, 25)
f(galleons=100, sickles=50, knuts=25)

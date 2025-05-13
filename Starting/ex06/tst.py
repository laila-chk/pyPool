from ft_filter import ft_filter

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = ft_filter(myFunc, ages)

for x in adults:
  print(x)

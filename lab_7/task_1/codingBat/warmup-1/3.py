def near_hundred(n):
  dif = abs(100-n)
  diff = abs(200-n)
  if dif <= 10 or diff <= 10:
    return True
  else:
    return False
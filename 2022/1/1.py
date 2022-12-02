

highest = 0
current = 0

while True:
  try:
    n = input()
    if n != "":
      n = int(n)
      current += n
    else:
      if current > highest:
        highest = current
      current = 0
  except EOFError:
    if current > highest:
      highest = current
    break

print(highest)

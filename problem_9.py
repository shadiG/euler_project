try:
      for c in range(10001):
            for b in range (c):
                  for a in range(b):
                        if c**2 == a**2+b**2 and a+b+c == 1000:
                              print(a*b*c)
                              raise StopIteration
except StopIteration: pass

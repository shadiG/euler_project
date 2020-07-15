total = 0
a,b = 1,1
while b<4000000:
      c = a+b
      a = b
      b = c
      if b%2==0: total+=b
print(total)
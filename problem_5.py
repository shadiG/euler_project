def is_divisible(n):
      for i in range(1,21):
            if n%i!=0:
                  return False
      return True
n = 20
while not is_divisible(n):
      n+=1
print(n)
from math import sqrt
def is_prime(n):
      if n in [0, 1]: return False
      for i in range(2, int(sqrt(n))+1):
            if n%i==0:
                  return False
      return True
def next_prime(n):
      n = n+1
      while not is_prime(n):
            n += 1
      return n
position = 0
n = 1
while position<10001:
      position+=1
      n = next_prime(n)
print(n)
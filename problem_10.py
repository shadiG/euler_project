from math import sqrt
def is_prime(n):
      if n in [0, 1]: return False
      for i in range(2, int(sqrt(n))+1):
            if n%i==0:
                  return False
      return True
print(sum([i for i in range(2000000) if is_prime(i)]))
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

n = 600851475143
prime = 2
factors = []
while n>=prime:
      if n%prime==0:
            n = n//prime
            factors.append(prime)
      prime = next_prime(prime)
print(factors[-1])
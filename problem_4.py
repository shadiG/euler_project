def is_palindrome(n):
      n = str(n)
      return n[::-1]==n
palindrome = None
for i in range(999,99, -1):
      for j in range(999, 99, -1):
            n = i*j
            if is_palindrome(n):
                  if palindrome == None:
                        palindrome = n
                  elif n> palindrome:
                        palindrome = n
print(palindrome)
from math import prod
with open('number.txt', 'r') as f:
      n =  f.read().replace('\n', '').replace('\r','')
      highest, adj = 0, 13
      for i in range(len(n)):
            if i+adj>len(n):
                  break
            computed = prod([int(n[j]) for j in range(i, i+adj)])
            if computed > highest:
                  highest = computed
print(highest)  

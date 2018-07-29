n = int(input())

def produceFibsList(n):
   if n <= 1:
       return n
   else:
       return(produceFibsList(n-1) + produceFibsList(n-2))

for i in range(n):
   print(produceFibsList(i))

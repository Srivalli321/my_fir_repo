
num = int(input("Enter your number : "))
print()
prime = []
def my_prime(n):
     if n > 1:
        for i in range(2,n):
          if (n % i) == 0:
              print(False)
              break
          else:
              print(True) 
              break      
my_prime(num)
for i in range(1,51):
  if i>1:
    for j in range(2,i):
      if(i%j) == 0:
        break
    else:
      prime.append(i)
print(prime)


      
       
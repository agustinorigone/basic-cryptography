import sys
import time
from math import sqrt

start = time.time()

#initilize with the number 1 since it is a factor of every number
factors = [1]
primeFactors = []

def isPrime(p):
  #utilizing the sqrt optimization
  for i in range(2, int(sqrt(p)) + 1):
    #check if p is divisible by any number between 2 and sqrt(p)
    if(p % i) == 0:
      return 0
  else:
    return 1

def factorize(p):
  for i in range(2, int(p/2) + 1):
    if(p % i) == 0:
      #appending factors
      factors.append(i)

def primeFactorize(p):
  #here we will neatly divide p by 2 as many times as we can
  #on each iteration we will save 2 as the factor
  while p % 2 == 0:
    #append 2 as the factor
    primeFactors.append(2)
    p = p / 2

  #here we will be strating iterating in 3 (since 2 was covered in the previos loop)
  #we will iterate still the sqrt of p
  #we will be incrementing by 2 every iterating (since even number are already covered)
  for i in range(3, int(sqrt(p)) + 1, 2):
    if(p % i) == 0:
      #appending i as the factor
      primeFactors.append(i)
      p = p / i
  
  if(p > 2):
    primeFactors.append(int(p))

#check if p is provided as an argument
if len(sys.argv) < 2:
  print("ERROR: You must provide p as an argument")
  print("USAGE: python3 q3.py 24")
else:
  #initilialize p
  p = int(sys.argv[1])
  if isPrime(p):
    print("RESULT:",p,"is prime then it won't get factorised")
  else:
    print("RESULT:",p,"is composite then it will get factorised")
    #run prime factorize function
    primeFactorize(p)

    #run factorize function
    factorize(p)    

    #appending p since every number is a factor of itself
    factors.append(p)

    print("PRIME FACTORIZATION:",primeFactors)
    print("FACTORS:",factors)

end = time.time()
print("TIME:",end - start, "seconds")
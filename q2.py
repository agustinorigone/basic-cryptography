import sys
import time
from math import sqrt

start = time.time()

def isPrime(p):
  #exclude 1
  if p == 1:
    return 0

  #utilizing the sqrt optimization
  for i in range(2, int(sqrt(p)) + 1):
    #check if p is divisible by any number between 2 and sqrt(p)
    if(p % i) == 0:
      return 0
  else:
    return 1
  

#check if p is provided as an argument
if len(sys.argv) < 2:
  print("ERROR: You must provide p as an argument")
  print("USAGE: python3 q1.py 9")
else:
  #initilialize p
  p = int(sys.argv[1])

  #run isPrime function
  result = isPrime(int(p))

  if result == 1:
    print("RESULT:", p, "is a prime number")
  else:
    print("RESULT:", p, "is not a prime number")

end = time.time()
print("TIME:",end - start, "seconds")
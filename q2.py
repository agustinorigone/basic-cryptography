import sys
import time
from math import sqrt

start = time.time()

def isPrime(p):
  #utilizing the sqrt optimization
  for i in range(2, int(sqrt(p)) + 1):
    #check if p is divisible by any number between 2 and sqrt(p)
    if(p % i) == 0:
      #print result and break (there is no need to keep on iterating)
      print("RESULT:", p, "is not a prime number")
      break
  else:
    print("RESULT:",p, "is a prime number")
  

#check if p is provided as an argument
if len(sys.argv) < 2:
  print("ERROR: You must provide p as an argument")
  print("USAGE: python3 q1.py 9")
else:
  #initilialize p
  p = sys.argv[1]

  #run isPrime function
  isPrime(int(p))

end = time.time()
print("TIME:",end - start, "seconds")
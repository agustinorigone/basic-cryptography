import sys
import time

start = time.time()

def isPrime(p):
  #iterate from p-1 until 1
  for i in range(p,2,-1):
    #get the quotient
    quotient = p/(i-1)
    
    #if we can find any integer quotient then p is not prime
    if(int(quotient) == quotient):
      #print result and break (there is no need to keep on iterating)
      print("RESULT:",p,"is not a prime number")
      break
  else:
    print("RESULT:",p,"is a prime number")
  

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
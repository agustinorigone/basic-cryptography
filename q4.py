import sys
import time
from math import sqrt

start = time.time()

def euclideanAlgorithm(a,b):
  #breaking condition: when b is zero => a is the hcf
  if b == 0:
    return a
 
  #calculate the remainder
  r = a % b
  
  #next recursive call we will:
    #shift b for a
    #shift r for b
  return euclideanAlgorithm(b, r)
  

#check if p is provided as an argument
if len(sys.argv) < 3:
  print("ERROR: You must provide a,b as an argument")
  print("USAGE: python3 q4.py 499017086208 676126714752")
else:
  #initilialize a
  a = sys.argv[1]

  #initilialize b
  b = sys.argv[2]

  #run hcf recursive function
  hcf = euclideanAlgorithm(int(a),int(b))
  print("RESULT: The hcf is",hcf)

end = time.time()
print("TIME:",end - start, "seconds")
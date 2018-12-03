
def fizzbuzzPrint(number, Fizz, Buzz):
  output = ""
  if (number%Fizz == 0) :	output = "Fizz"
  if (number%Buzz == 0) :	output += "Buzz"
  if (output == "") : output = str(number)
  return output 

def goThrough(start, end):
  for i in range (start,end) : print(fizzbuzzPrint(i, 5, 7))

def main():goThrough(1, 350)
 
if __name__ == "__main__":
  main()

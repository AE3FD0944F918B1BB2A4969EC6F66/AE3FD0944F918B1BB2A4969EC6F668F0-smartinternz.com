import math

n = int(input("Enter input number : "))

if n < 0:
  print("Factorial does not exist for negative numbers")
elif n == 0:
  print("The factorial of 0 is 1")
else:
  print("The factorial of", n, "is", math.factorial(n))

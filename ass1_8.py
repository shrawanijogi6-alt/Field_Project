def find_factorial_loop(number):
  if number < 0:
    return "Factorial is not defined for negative numbers."
  elif number == 0:
    return 1  
  else:
    factorial = 1
    for i in range(1, number + 1):
      factorial *= i
    return factorial

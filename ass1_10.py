def reverse_number(num):
  reversed_num = 0
  is_negative = False
  if num < 0:
    is_negative = True
    num = abs(num)
  while num > 0:
    remainder = num % 10 
    reversed_num = reversed_num * 10 + remainder  
    num //= 10  
  if is_negative:
    return -reversed_num
  else:
    return reversed_num
number_to_reverse = 12345
reversed_result = reverse_number(number_to_reverse)
print(f"The reversed number is: {reversed_result}")
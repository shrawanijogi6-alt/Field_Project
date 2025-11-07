def print_multiplication_table(number, limit=10):
    print(f"Multiplication Table of {number}:")
    for i in range(1, limit + 1):
        product = number * i
        print(f"{number} x {i} = {product}")
try:
    num_to_multiply = int(input("Enter a number to print its multiplication table: "))
    table_limit = int(input("Enter the limit for the multiplication table (e.g., 10 for up to 10x): "))
    print_multiplication_table(num_to_multiply, table_limit)
    print("Invalid input. Please enter an integer.")
 number = int(input("Enter an integer: "))
    print("Invalid input. Please enter an integer.")
else:
    if number > 0:
        print(f"The number {number} is positive.")
    elif number < 0:
        print(f"The number {number} is negative.")
    else:
        print(f"The number {number} is zero.")
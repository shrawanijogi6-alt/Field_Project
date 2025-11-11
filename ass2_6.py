def calculate_simple_interest():
    try:
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the annual interest rate (as a percentage, e.g., 5 for 5%): "))
        time = float(input("Enter the time in years: "))
        if principal < 0 or rate < 0 or time < 0:
            print("Principal, rate, and time cannot be negative.")
            return
    simple_interest = (principal * rate * time) / 100
        print(f"\nSimple Interest: {simple_interest:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for principal, rate, and time.")
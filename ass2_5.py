try:
    celsius = float(input("Enter temperature in Celsius: "))
except ValueError:
    print("Invalid input. Please enter a numerical value for temperature.")
else:
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F")
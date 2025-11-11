def convert_to_hex_and_binary():
    try:
        decimal_number = int(input("Enter an integer: "))
        hex_representation = hex(decimal_number)
        binary_representation = bin(decimal_number)
        print(f"The number in decimal: {decimal_number}")
        print(f"The number in hexadecimal: {hex_representation}")
        print(f"The number in binary: {binary_representation}")
except ValueError:
        print("Invalid input. Please enter an integer.")
if __name__ == "__main__":
    
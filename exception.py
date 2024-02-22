try:
    x = int(input("Enter a number:"))
    y = 10/x
    print("Result:",y)
except ZeroDivisionError:
    print("Error:Division by zero")

except ValueError: 
    print("Error: Invalid input")   
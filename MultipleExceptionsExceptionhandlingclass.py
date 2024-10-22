try:
    num1, num2 = eval(input("Enter the two numbers, separated by comma = "))
    result = num1 / num2
    print("Result is", result)

except ZeroDivisionError:
    print("Division by zero is error !!")
except SyntaxError:
    print("Comma is missing. Enter numbers separated by comma like this e.g. 1,2")
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("This will execute no matter what.")
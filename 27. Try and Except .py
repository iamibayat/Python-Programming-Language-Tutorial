# This code will give an error,
# ValueError: invalid literal for int() with base 10: 'ykyk'
'''number = int(input("Enter a number: "))
print(number)'''



# but if we use try and except we can avoid the error message and print out something instead of the error message
'''try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Integer")'''
# but here is a downside of this code is SINGLE EXCEPT, which allows any error or multiple error and prints out the error message
# does not matter whether any of the code is right or wrong, it will print out the same message for all error



'''number = 100/0
ZeroDivisionError: division by zero'''



# here there are one error and other can be right also but still the message will be appeared
'''try:
    number = 100/0
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Integer")'''



# here we can catch diff kinds of error and print message for ecah specific message
'''try:
    #number = 100/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("This is ZeroDivisionError")
except ValueError:
    print("This is ValueError")'''



# here the error messaged saved as a variable and then it is printed out the detail message
'''try:
    number = 100/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as error1:
    print(error1)
except ValueError as error2:
    print(error2)'''
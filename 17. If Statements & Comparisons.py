'''
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
'''

a = 3
b = 3
if a == b:
    print("same")


a = 3
b = 5
if a != b:
    print("not same")


a = 5
b = 3
if a > b:
    print("a is greater")


a = 5
b = 7
if b > a:
    print("b is greater")


print("\n")
print("\n")


def find_max(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        # print(num1)
        return num1
    elif num2 >= num1 and num2 >= num3:
        # print(num2)
        return num2
    else:
        # print(num3)
        return num3


# find_max(10, 9, 8)
print(find_max(4500, 47, 39))
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

string_addition = num1 + num2
int_addition = int(num1) + int(num2)

print(string_addition)                  # this is without making the variable integer, which python creates as string
print(int_addition)                     # these variables are integers


print("\n")

num3 = input("Enter an integer: ")
num4 = input("Enter a decimel number: ")

# integer_add = int(num3) + float(num4)            it gives error message since input is float but variable type is int

float_addition = int(num3) + float(num4)

# float (float_addition)

print(float_addition)

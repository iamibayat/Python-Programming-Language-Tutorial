# Exponent 
print(2 ** 2)
print(4 ** 2)
print("\n")




# Exponent using For loop and Function
def raise_to_power(base, power):
    result = 1
    for i in range(power):
        result = base * result
    return result

print(raise_to_power(4, 2))
print("\n")




# Exponent using For loop and Function by User Input
def raise_to_power(base, power):
    result = 1
    for i in range(power):
        result = base * result
    return result

b  = int(input("Enter base: "))
p  = int(input("Enter power: "))

print(raise_to_power(b,p))




def to_the_power(base, power):
    temp = 1
    a = 0
    while a != power:
        result = base * temp
        temp = result
        a += 1
    return result


print(to_the_power(4, 3))
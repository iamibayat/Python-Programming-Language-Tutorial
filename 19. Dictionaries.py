'''
monthly_names = {
    "Jan": "January",               # here Jan is a key and January is a value of both the string type
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
}

print(monthly_names)
print(monthly_names["Feb"])
print(monthly_names.get("Feb"))         # both of them are same, both will output same
print("\n")


print(monthly_names.get("Dec"))
# here we use GET in order to if the key is not found it will display a prompt instead of NONE
print(monthly_names.get("Dec", "Sorry couldn't find this keywords."))
print("\n")
'''


numeric_to_number = {
    0: "Zero",                          # here key is in integer
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
}

print(numeric_to_number)
print(numeric_to_number[2])
print(numeric_to_number.get(5))
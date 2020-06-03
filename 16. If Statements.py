'''
is_male = True
is_female = False

if is_male:
    print("You are a Male.")

if is_female:
    print("You are a Female.")
'''



'''
is_male = False

if is_male:
    print("You are a Male.")
else:
    print("You are not a Male.")
'''



'''
is_male = False
is_tall = False

if is_male or is_tall:                                  # OR means either one of the statements or both needs to be true
    print("You are either Male or Tall or both.")
else:
    print("You are neither Male nor Tall.")
'''



'''
is_male = True
is_tall = False

if is_male and is_tall:                                 # AND means both statements has to be true
    print("You are a Male and Tall as well.")
else:
    print("You are either not a Male or a Tall or both.")
'''


is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a Male and Tall as well.")
elif is_male and not is_tall:
    print("Yor are a Male but not Tall")
elif not is_male and is_tall:
    print("Yor are not a Male but Tall")
else:
    print("You are neither a Male nor Tall.")
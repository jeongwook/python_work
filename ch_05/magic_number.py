answer = 17
if answer != 42:
	print("That is not the correct answer. Please try again!")

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

age_1 = 18
print(age_0 >= 21 or age_1 >= 21)

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

print("\n'IN' conditional") 
requested_toppings = ['mushrooms', 'onion', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

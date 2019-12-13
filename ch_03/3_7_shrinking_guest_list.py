list = ['Jason', 'Dave', 'Josh']
print(list[0] + ", you are invited to dinner.")
print(list[1] + ", you are invited to dinner.")
print(list[2] + ", you are invited to dinner.")

print("\nI have found a bigger table\n")

list.insert(0, 'Jin')
list.insert(2, 'Rodney')
list.append('Kevin')

print(list[0] + ", you are invited to dinner.")
print(list[1] + ", you are invited to dinner.")
print(list[2] + ", you are invited to dinner.")
print(list[3] + ", you are invited to dinner.")
print(list[4] + ", you are invited to dinner.")
print(list[5] + ", you are invited to dinner.")

print("\nUnfortunately the desk will not arrive in time and I only have space for 2 people.\n")
print("I am sorry " + list.pop() + " but I cannot accomodate you for dinner.")
print("I am sorry " + list.pop() + " but I cannot accomodate you for dinner.")
print("I am sorry " + list.pop() + " but I cannot accomodate you for dinner.")
print("I am sorry " + list.pop() + " but I cannot accomodate you for dinner.")

print("\n" + list[0] + ", you are still invited to dinner.")
print(list[1] + ", you are still invited to dinner.")
places_to_visit = ['Korea', 'Japan', 'Hawaii', 'Buenos Aires', 'Jackson Hole']
print("Original list:")
print(places_to_visit)

print("\nTemporarily sorted alphabetically:")
print(sorted(places_to_visit))

print("\nOriginal list again:")
print(places_to_visit)

print("\nTemporarily sorted in reverse (alphabetically)")
print(sorted(places_to_visit, reverse=True))

print("\nOriginal list again:")
print(places_to_visit)

print("\nReverse order:")
places_to_visit.reverse()
print(places_to_visit)

print("\nOriginal list again:")
places_to_visit.reverse()
print(places_to_visit)

print("\nSorted alphabetically:")
places_to_visit.sort()
print(places_to_visit)

print("\nSorted in reverse (alphabetically):")
places_to_visit.sort(reverse=True)
print(places_to_visit)

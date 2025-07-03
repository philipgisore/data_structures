import random

count = int(input("How many random numbers do you want to generate (between 1 and 10)?"))

if count <= 0:
    print("Number must be greater than zero")
else:
    # Generate a list of 10 random numbers between 1 and 10 (may contain duplicates)
    randon_numbers = [random.randint(1, 10) for _ in range(10)]

# Convert to set to remove duplicates
unique_numbers = set(randon_numbers)

print("Original numbers:", randon_numbers)
print("Unique numbers (after removing duplicates):", unique_numbers)
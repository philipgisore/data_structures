num = int(input("How many favorite fruits do you want to enter?"))
# Create a list from user input
favorite_fruits = []

for i in range(num):
    fruit = input("Enter fruit #{i + 1}: ")
    favorite_fruits.append(fruit)
#Print the entire list
print("\nYour favorite fruits:", favorite_fruits)

# Print the second fruit if it exists
if len(favorite_fruits) >= 2:
    print("Second_fruit:", favorite_fruits[1])
else:
    print("You didn't enter enough fruits to access the second one.")

# Create a dictionary with book information
title = input("Enter the title of your favorite book: ")
author = input("Enter the author: ")
genre = input("Enter the genre: ")

favorite_book = {
    'title': 'Atomic habits',
    'author': 'James Clear',
    'genre': 'Self-help'
}

print("\nBook Details:")
print("Title: ", favorite_book.get('title'))
print("Author:", favorite_book.get('author'))
print("Your favorite book is :", favorite_book.get('genre'))


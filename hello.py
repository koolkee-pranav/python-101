#!/usr/bin/python3
print("Hello Pranav & Amogh - Welcome to Python programming!")
# Print "Hello, World!" backward in Spanish (Hola, Mundo!)
print("Hola, Mundo!"[::-1])
# Print "Hello, World!" backward in French (Bonjour, le monde!)
print("Bonjour, le monde!"[::-1])

# ask user any integer in the range 2-15 and print multiplication tables for it 
number = input("Enter any integer in the range 2-15: ")
print("Multiplication for:" + number)
for i in range(1, 11):
    print(number + " X " + str(i) + " = " + str(int(number) * i))


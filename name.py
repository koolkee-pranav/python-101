#!/usr/bin/python3
import sys

# Print "Hello, World!" to your terminal window using Python.  
print("Hello, GitHub CoPilot World! This line was written by CoPilot.") 

# ask user his name and print it
name = input("What is your name? ")
print("Hello, " + name + "!")

# ask user his age and print it
age = input("What is your age? ")
print("You are " + age + " years old.")

# ask user his favorite color and print it
color = input("What is your favorite color? ")

# print a sentence about this color, check for red, blue, green, violet, yellow, orange, black, white, brown, gray and pink
if color == "red":
    print("Red is the color of blood and fire.")    
elif color == "blue":
    print("Blue is the color of the sky and sea.")
elif color == "green":  
    print("Green is the color of grass and leaves.")
elif color == "violet":
    print("Violet is the color of violets.")
elif color == "yellow":
    print("Yellow is the color of the sun.")
elif color == "orange":
    print("Orange is the color of oranges.")
elif color == "black":
    print("Black is the color of coal, ebony, and of outer space.")
elif color == "white":
    print("White is the color of milk and snow.")
elif color == "brown":
    print("Brown is the color of wood and chocolate.")
elif color == "gray":
    print("Gray is the color of an overcast sky.")
elif color == "pink":
    print("Pink is the color of cherry blossoms and salmon.")
else:
    print("ah ! that is an interesting color - I don't know much about it.")   

sys.exit()

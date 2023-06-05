#!/usr/bin/python3
import sys

print("Python program to print stars *")

howManyStars = input("Hey you! How many stars do you want to print? ")
for i in range(int(howManyStars)):
    print("*")

sys.exit()
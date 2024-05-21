#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

greet_programmer();    

def greet(name):
    print(f"Hello, {name}!") 

greet("Naureen");       

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default()

greet_with_default("Sunny")

def add(num1, num2):
  return num1 + num2

sum = add(1, 2)

print(sum)

def halve(number):
    return number / 2

sum = halve(100)

print(sum)


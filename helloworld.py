# print() in py = console.log in js
print("Hello World")

# Function to find sum of 2 numbers
# def X(): in py = function X(){ in js
def addition(a, b):
    return a + b
# Tests for function addition
print("answer for 3 + 7 should be 10, got", addition(3, 7))
print("answer for -13 + 47 should be 34, got", addition(-13, 47))
print("answer for 34 - 7 should be 27, got", addition(34, -7))

# function that adds 1 to number
def addOne(num):
	return num + 1

print("answer for 47 should be 48, got", addOne(47))
print("answer for -7 should be -6, got", addOne(-7))

#  a function that takes a positive integer and return its factorial.
def factorial(Z):
		return 1 if Z <= 1 else Z*factorial(Z-1)

print("factorial of 4 should be 24, got", factorial(4))
print("factorial of 9 should be 362880, got", factorial(9))
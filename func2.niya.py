'''
Author : Niya Pius
Date : 03-11-2024
Python program to find factorial
Version 1.0
'''
def factorial(n):
    if n==0:
        return 1
    else :
        return (n*factorial(n-1))
print(factorial(5))

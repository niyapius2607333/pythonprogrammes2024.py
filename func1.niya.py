'''
Author : Niya Pius
Date : 03-11-2024
Python program to find gcd 
Version 1.0
'''
def gcd(n1,n2):
    if n1%n2==0:
        return n2
    else:
     return (gcd(n2,n1%n2))
print(gcd(1220,516))

import math
n=int(input("Choose first prime number "))
g=int(input("Choose second prime number "))
x=int(input("Alice Choose number "))
print("ASYMMETRIC KEY GENERATION BY ALICE ")
A= (g**x)%n
print("Public key of Alice is ",A)
y=int(input("Bob Choosen number "))
print("ASYMMETRIC KEY GENERATION BY BOB ")
B= (g**y)%n
print("Public key of Bob is ",B)
print("Alice calculates the shared secret key")
k1= (B**x)%n
print("Shared secret key calculated by Alice is ",k1)
print("Bob calculates the shared secret key")
k2= (A**y)%n
print("Shared secret key calculated by Bob is ",k2)
if k1==k2:
    print("Shared secret keys match. Key exchange successful.")
else:    print("Shared secret keys do not match. Key exchange failed.")
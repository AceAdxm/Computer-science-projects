import math

print("Welcome to calculating rectangles! Try not to use decimals!!")

S = int(input("Area: "))
P = int(input("Perimeter: "))

if P**2 < 16*S:
    print("Error: No real rectangle possible with those values!")
else:
    B = (math.sqrt(P**2 - 16*S) + P) / 4
    A = P/2 - B
    print(f"Length = {A}, Width = {B}")

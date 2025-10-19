"""
There exists exactly 1 Pythagorean triplet where a + b + c = 1000.
Find the product abc.
"""

a = 1
b = a + 1
sum = 0
while sum != 1000:
    square = a ** 2 + b ** 2
    c = square ** 0.5
    sum = a + b + c
    if sum == 1000:
        break
    elif sum < 1000:
        b += 1
    else: 
        a += 1
        b = a + 1
product = int(a * b * c)
print(product)
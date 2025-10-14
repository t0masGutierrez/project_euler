"""
Find the sum of all the odd squares for the first 784 thousand square numbers?
"""

sum = 0
for i in range(754001):
    if i % 2 != 0:
        sum += i ** 2
print(sum)
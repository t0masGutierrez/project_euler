"""
Among the first 784 thousand square numbers, what is the sum of all the odd squares?
"""

sum = 0
for i in range(754001):
    if i % 2 != 0:
        sum += i ** 2
print(f"sum = {sum}")
"""
A Pythagorean triplet is a set of three natural numbers a < b < c, for which a^2 + b^2 = c^2.
For example, 3^2 + 4^2 = 5^2. and 3 + 4 + 5 = 12
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

# initialize n1, n2
# while sum(a, b, c) != 1000:
    # n2 = n1 + 1
    # while sum <= 1000 increment
        # increment n2 
    # n1 += 1
    # if a^2 + b^2 equal perfect square then sum a, b, and c
        # if sum equal 1000 then store addends and break
        # elif sum > 1000 then increment n1 and reset n2
        # else increment n2

n1 = 1
a, b, c = 0, 0, 0
sum = 0
while sum != 12:
    n2 = n1 + 1
    while sum < 12:
        square = n1 ** 2 + n2 ** 2
        root = square ** 0.5
        print(f"root = {root}")
        print(f"square = {square}")
        if root % 1 == 0:
            a = n1
            b = n2
            c = int(root)
            sum = a + b + c
            print(f"{a} + {b} + {c} = {sum}")
        n2 += 1
    n1 += 1
print(f"{a} + {b} + {c} = {sum}")
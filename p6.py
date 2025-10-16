"""
Find the difference between the square of the sum and sum of the squares of the first 100 natural numbers.
"""

sum_squares = 0
squared_sum = 0
for i in range(1, 101):
    sum_squares += i ** 2
    squared_sum += i

squared_sum **= 2
diff = squared_sum - sum_squares
print(diff)
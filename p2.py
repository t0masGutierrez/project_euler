"""
Find the sum of all the even-valued terms in the Fibonacci sequence which do not exceed four million.
"""

fibonacci_seq = [1, 2]
while fibonacci_seq[-1] < 4000000:
    fibonacci_num = fibonacci_seq[-1] + fibonacci_seq[-2]
    fibonacci_seq.append(fibonacci_num)

sum = 0
for num in fibonacci_seq[:-1]:
    if num % 2 == 0:
        sum += num
print(sum)
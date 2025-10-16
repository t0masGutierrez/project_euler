"""
Find the smallest number divisible by all of the numbers from 1 to 20?
"""

n = 1
is_div = False
while is_div == False:
    num_indiv = 0
    for i in range(1, 21):
        remainder = n % i
        if remainder != 0:
            num_indiv += 1
    if num_indiv == 0:
        is_div = True
    else:
        n += 1
print(n)
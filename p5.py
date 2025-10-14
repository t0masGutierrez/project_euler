"""
What is the smallest number divisible by all of the numbers from 1 to 20?
"""

number = 1
is_div = False
while is_div == False:
    num_indiv = 0
    for i in range(1, 21):
        remainder = number % i
        if remainder != 0:
            num_indiv += 1
    if num_indiv == 0:
        is_div = True
    else:
        number += 1
print(f"number = {number}")
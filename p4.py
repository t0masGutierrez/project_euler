"""
Find the largest palindrome made from the product of two 3-digit numbers.
"""

factors = []
palindromes = []
for num1 in range(100, 1000):
    for num2 in range(100, 1000):
        product = str(num1 * num2)
        is_palindrome = True

        for i, digit in enumerate(product):
            if product[i] != product[-i-1]:
                is_palindrome = False
        
        if is_palindrome:
            facts = [num1, num2]
            product = int(product)
            factors.append(facts)
            palindromes.append(product)

largest_palindrome_factors = factors[0]
largest_palindrome = palindromes[0]
for i, p in enumerate(palindromes):
    if p > largest_palindrome:
        largest_palindrome_factors = factors[i]
        largest_palindrome = p
    else:
        continue
print(f"factors = {largest_palindrome_factors}")
print(f"largest palindrome = {largest_palindrome}")

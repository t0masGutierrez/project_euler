"""
Find the largest palindrome created from the product of two 3-digit numbers.
"""

palindromes = []
for num1 in range(100, 1000):
    for num2 in range(100, 1000):
        product = str(num1 * num2)
        is_palindrome = True

        for i, digit in enumerate(product):
            if product[i] != product[-i-1]:
                is_palindrome = False
        
        if is_palindrome:
            product = int(product)
            palindromes.append(product)

largest_palindrome = palindromes[0]
for i, p in enumerate(palindromes):
    if p > largest_palindrome:
        largest_palindrome = p
    else:
        continue
print(largest_palindrome)
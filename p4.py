def solution():
    """
    Find the largest palindrome created from the product of two 3-digit numbers.

    Returns
    -------
    largest_palindrome : int
        The largest palindrome
    """
    palindromes = []
    for n1 in range(100, 1000):
        for n2 in range(100, 1000):
            product = str(n1 * n2)
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
    return largest_palindrome

def main():
    y = solution()
    print(y)

if __name__ == "__main__":
    main()

def solution(N):
    """
    There exists exactly 1 Pythagorean triplet where a + b + c = N. Find the product abc.

    Parameters
    ----------
    N: int
        The sum of the pythagorean triplet

    Returns
    -------
    product : int
        The product of the pythagorean triplet addends
    """
    a = 1
    b = a + 1
    sum = 0
    while sum != N:
        square = a ** 2 + b ** 2
        c = square ** 0.5
        sum = a + b + c
        if sum == N:
            break
        elif sum < N:
            b += 1
        else: 
            a += 1
            b = a + 1
    product = int(a * b * c)
    return product

def main():
    y = solution(1000)
    print(y)

if __name__ == "__main__":
    main()

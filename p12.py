def solution(N):
    """
    Find the first triangle number to have over N divisors.

    Parameters
    ----------
    N: int
        The minimum number of divisors

    Returns
    -------
    triangle_num : int
        The value of the triangle number 
    """
    max_addend = 1
    num_divisors = 0
    while num_divisors <= N:
        triangle_num = 0
        for n in range(1, max_addend):
            triangle_num += n
        
        num_divisors = 0
        MAX_DIVISOR = int(triangle_num ** 0.5)
        if MAX_DIVISOR ** 2 == triangle_num:
            num_divisors += 1
        
        for n in range(1, MAX_DIVISOR):
            if triangle_num % n == 0:
                num_divisors += 2
        max_addend += 1
    return triangle_num

def main():
    y = solution(500)
    print(y)

if __name__ == "__main__":
    main()

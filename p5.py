def solution(a, b):
    """
    Find the smallest number divisible by all of the numbers from a to b. 

    Parameters
    ----------
    a : int
        The minimum divisor
    b : int
        The maximum divisor

    Returns
    -------
    minimum_dividend : int
        The minimum dividend
    """
    minimum_dividend = 1
    is_div = False
    while not is_div:
        not_div = False
        for i in range(a, b+1):
            remainder = minimum_dividend % i
            if remainder != 0:
                not_div = True
        if not_div:
            minimum_dividend += 1
        else:
            is_div = True
    return minimum_dividend

def main():
    y = solution(1, 20)
    print(y)

if __name__ == "__main__":
    main()

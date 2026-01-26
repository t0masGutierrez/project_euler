from decimal import getcontext, Decimal

def solution(N):
    """
    Find the unit fraction denominator < N with the longest recurring decimal.  

    Parameters
    ----------
    N : int
        The maximum denominator

    Returns
    -------
    denominator : int
        The denominator with the longest recurring decimal
    """
    getcontext().prec = 2 * N
    max_length = 0
    denominator = 0
    for i in range(2, N):
        if i % 2 != 0 and i % 5 != 0:
            unit_fract = Decimal(1) / Decimal(i)
            length = 1
            for j in range(1, N):
                if i >= 100:
                    j += 2
                deci = str(unit_fract * 10 ** j).split(".")
                pre_deci = deci[0]
                post_deci = deci[1][:j]
                if int(pre_deci) == int(post_deci):
                    length = j
                    break
            if length > max_length:
                max_length = length
                denominator = i
    return denominator

def main():
    y = solution(1000)
    print(y)

if __name__ == "__main__":
    main()

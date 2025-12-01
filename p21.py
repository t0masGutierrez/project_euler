def solution(N):
    """
    Evaluate the sum of all the amicable numbers below N.

    Parameters
    ----------
    N : int
        The maximum amicable number

    Returns
    -------
    amicable_sum : int
        The sum of amicable numbers
    """
    amicable_nums = []
    for n in range(1, N):
        divisors1 = []
        for i in range(1, n):
            if n % i == 0:
                divisors1.append(i)
        sum1 = sum(divisors1)

        divisors2 = []
        for j in range(1, sum1):
            if sum1 % j == 0:
                divisors2.append(j)
        sum2 = sum(divisors2)

        if n == sum2 and sum1 != sum2 and n not in amicable_nums:
            amicable_nums.append(n)
            amicable_nums.append(sum1)
    amicable_sum = sum(amicable_nums)
    return amicable_sum

def main():
    y = solution(10000)
    print(y)

if __name__ == "__main__":
    main()

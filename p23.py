def solution(N):
    """
    Abundant numbers are numbers whose sum of proper divisors is greater than the number itself. 
    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

    Parameters
    ----------
    N : int
        Maximum abundant number

    Returns
    -------
    sum : int
        The sum of positive integers not expressible as sum of two abundant numbers
    """
    sum = 0
    abundant_nums = []
    for n in range(N):
        sum_divisors = 0
        for i in range(1, n):
            if n % i == 0:
                sum_divisors += i

        if sum_divisors > n:
            abundant_nums.append(n)
        
        abundance = True
        for num in abundant_nums:
            diff = abs(n - num)
            if diff in abundant_nums:
                abundance = False

        if abundance:
            sum += n
    return sum

def main():
    y = solution(28123)
    print(y)

if __name__ == "__main__":
    main()

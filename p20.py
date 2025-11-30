def solution(N):
    """
    Find the sum of the digits in the number N factorial.

    Parameters
    ----------
    N : int
        The factorial number

    Returns
    -------
    sum : int
        The sum of digits
    """
    fact = 1
    for i in range(100, 1, -1):
        fact *= i
    
    sum = 0
    for char in str(fact):
        sum += int(char)
    return sum
                
def main():
    y = solution(100)
    print(y)

if __name__ == "__main__":
    main()

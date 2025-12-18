def solution(N, k):
    """
    If permutations are arranged in numerical or alphabetical order then they're lexicographically ordered.
    Find the Nth lexicographic permutation of the k-digit number. 

    Parameters
    ----------
    N : int
        The index of the permutation
    k : int
        The number of digits

    Returns
    -------
    nPk : int
        The Nth permutation
    """
    def compute_factorial(k):
        facto = 1
        for i in range(1, k + 1):
            facto *= i
        return facto
    
    N -= 1
    nPk = ""
    digits = [i for i in range(k)]
    for i in range(k - 1, -1, -1):
        facto = compute_factorial(i)
        digit = digits.pop(N // facto)
        N %= facto
        nPk += str(digit)
    return nPk

def main():
    y = solution(1000000, 10)
    print(y)

if __name__ == "__main__":
    main()

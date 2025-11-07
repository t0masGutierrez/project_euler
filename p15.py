def solution(N):
    """
    Starting in the top left corner, and only being able to move to the right and down, find the number of routes to the bottom right corner of N*N grid.

    Parameters
    ----------
    N: int
        The grid size

    Returns
    -------
    num_routes : int
        The number of distinct routes
    """
    # nCk = n! / k!(n - k)!
    n = 2 * N
    k = N
    nk_diff = n - k
    
    n_fact = 1
    for i in range(1, n+1):
        n_fact *= i
    
    k_fact = 1
    for i in range(1, k+1):
        k_fact *= i

    nk_fact = 1
    for i in range(1, nk_diff+1):
        nk_fact *= i

    num_routes = n_fact // (k_fact * nk_fact)
    return num_routes

def main():
    y = solution(20)
    print(y)

if __name__ == "__main__":
    main()

def solution(N):
    """
    The 12th term of the fibonacci sequence is the 1st term with 3-digits. 
    Find the index of the 1st term of the fibonacci sequence with N-digits. 

    Parameters
    ----------
    N : int
        The number of digits

    Returns
    -------
    fib_index : int
        The index of 1st fibonacci number with N-digits
    """
    count = 4 # the starting number of indices between new digits
    seq_index = 2 # the starting index of the index sequence
    fib_index = 12 # the starting index of the fibonacci sequence
    seq = [4, 5, 5] # the index sequence between new digits
    for i in range(1, N - 2):
        if count / seq[seq_index % len(seq)] == 1:
            fib_index += 4
            count = 0
            seq_index += 1
        else:
            fib_index += 5
        count += 1
    return fib_index

def main():
    y = solution(1000)
    print(y)

if __name__ == "__main__":
    main()

def solution(N):
    """
    Find the number of Sundays on the first of the month during the Nth century.

    Parameters
    ----------
    N : int
        The century

    Returns
    -------
    num_sundays : int
        The number of sundays on the first of the month
    """
    start = (N - 1) * 100 + 1
    end = N * 100 + 1
    num_sundays = 0
    for i in range(start, end):
        leap_days = 0
        month_days = {}
        for j in range(12):
            APRIL_INDEX = 3
            JUNE_INDEX = 5
            SEPTEMBER_INDEX = 8
            NOVEMBER_INDEX = 10
            FEBRUARY_INDEX = 1
            if j in [APRIL_INDEX, JUNE_INDEX, SEPTEMBER_INDEX, NOVEMBER_INDEX]:
                month_days[j] = 30
            elif j == FEBRUARY_INDEX:
                if i % 4 == 0 and i % 400 != 0:
                    month_days[j] = 29
                    leap_days += 1
                else:
                    month_days[j] = 28
            else:
                month_days[j] = 31
        
        for month in month_days:
            # +6 days for sunday and +1 day for leap year
            num_days = 7
            for m in range(month):
                num_days += month_days[m]
            num_days += 365 * (i - start) + leap_days
            if num_days % 7 == 0:
                num_sundays += 1
    return num_sundays
                
def main():
    y = solution(20)
    print(y)

if __name__ == "__main__":
    main()

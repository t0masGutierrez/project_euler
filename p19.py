def solution(N):
    """
    Find the number of Sundays on the first of the month during the Nth century.

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
            if j in [3, 5, 8, 10]:
                month_days[j] = 30
            elif j == 1:
                if i % 4 == 0 and i % 400 != 0:
                    month_days[j] = 29
                    leap_days += 1
                else:
                    month_days[j] = 28
            else:
                month_days[j] = 31
        
        for month in month_days:
            # 1 jan 1990 +6 days equal sunday and +1 day for leap year
            num_days = 7
            for m in range(month):
                num_days += month_days[m]
            num_days += 365 * (i - 1901) + leap_days
            if num_days % 7 == 0:
                num_sundays += 1
    return num_sundays
                
def main():
    y = solution(20)
    print(y)

if __name__ == "__main__":
    main()

def solution(N):
    """
    Find the number of letters used to write out in words all the numbers from 1 to N.

    Parameters
    ----------
    N: int
        The maximum number

    Returns
    -------
    num_letters : int
        The number of letters
    """
    nums = {None: "",
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen",
            20: "twenty",
            30: "thirty",
            40: "forty",
            50: "fifty",
            60: "sixty",
            70: "seventy",
            80: "eighty",
            90: "ninety",
            000: "hundred"}        
    num_letters = 0
    for n in range(1, N+1):
        if len(str(n)) == 1:
            num_letters += len(nums[n])

        elif len(str(n)) == 2:
            if 10 <= n <= 20:
                zeroth_digit = n
                first_digit = None

            else:
                zeroth_digit = int(str(n)[0]) * 10

                if int(str(n)[1]) == 0:
                    first_digit = None

                else:
                    first_digit = int(str(n)[1])
            num_letters += len(nums[zeroth_digit]) + len(nums[first_digit])

        elif len(str(n)) == 3:
            zeroth_digit = int(str(n)[0])

            if 10 <= int(str(n)[1:]) <= 20:
                first_digit = int(str(n)[1:])
                second_digit = None

            else:
                if int(str(n)[1]) == 0:
                    first_digit = None

                else:
                    first_digit = int(str(n)[1]) * 10

                if int(str(n)[2]) == 0:
                    second_digit = None

                else:
                    second_digit = int(str(n)[2])

            # if number does not end in "00" then add 3 letters for "and" 
            if int(str(n)[1]) or int(str(n)[2]):
                num_letters += 3

            num_letters += len(nums[zeroth_digit]) + len(nums[000]) + len(nums[first_digit]) + len(nums[second_digit])
        elif len(str(n)) == 4:
            num_letters += len("one") + len("thousand")
    return num_letters

def main():
    y = solution(1000)
    print(y)

if __name__ == "__main__":
    main()

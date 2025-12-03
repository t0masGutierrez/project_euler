def solution(file):
    """
    Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order.
    Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
    For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 * 53 = 49714.
    Find the total of all the name scores in the file.

    Parameters
    ----------
    file : str
        Name of input file

    Returns
    -------
    sum : int
        The sum of name scores
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    with open(file, "r") as f:
        contents = f.read().replace("\"", "")
    names = contents.split(",")
    names.sort()

    scores = {}
    for n in names:
        scores[n] = 0
        for letter in n:
            index = alphabet.index(letter) + 1
            scores[n] += index
    
    sum = 0
    for i in range(len(names)):
        sum += (i + 1) * scores[names[i]]
    return sum

def main():
    y = solution("names.txt")
    print(y)

if __name__ == "__main__":
    main()

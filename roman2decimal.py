romanNums = { # init dictionary with roman numerals "translations" per se
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}
def findNum(ogVal): # takes roman numeral and returns integer value
    ans = 0
    for i in range(len(ogVal) - 1):
        left, right = ogVal[i], ogVal[i+1]
        if romanNums[left] < romanNums[right]: ans -= romanNums[left]
        else: ans += romanNums[left]
    ans += romanNums[ogVal[-1]]
    return ans
def main(): # program to run if independent (aka not running under another program).
    num = input("Input Roman Numeral Value to Convert: ")
    print("Output Number: " + str(findNum(num)))
    findNum(num)
if __name__ == '__main__': main()
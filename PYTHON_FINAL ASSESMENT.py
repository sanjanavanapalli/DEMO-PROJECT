# PROGRAM TO PRINT COMMON ELEMENTS IN A LIST

LIST1 = [2, 3, 4, 5]

LIST2 = [3, 5, 7, 9]


def common(a, b):
    LIST = [value for value in LIST1 if value in LIST2]
    return LIST


RESULT = common(LIST1, LIST2)
print(RESULT)


# PROGRAM TO PRINT MAX PALINDROME

def isPalindrome(P):
    divisor = 1
    while int(P / divisor) >= 10:
        divisor *= 10
    while P != 0:
        leading = int(P / divisor)
        trailing = P % 10
        if leading != trailing:
            return False
        P = int((P % divisor) / 10)

        divisor = int(divisor / 100)
    return True


def largestPalindrome(List, P):
    currentMax = -1
    for i in range(0, P, 1):
        if List[i] > currentMax and isPalindrome(List[i]):
            currentMax = List[i]
    return currentMax


List = [13, 15, 66, 77, 151, 101, 141, 171, 291, 131, 121, 99, 111, 161, 88, 199, 201]
P = len(List)

print(largestPalindrome(List, P))

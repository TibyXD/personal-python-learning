GivenNum = int(input())


def calculate_palindrome(ReffNum):
    x = 0
    while ReffNum >= 1:
        x = int((x * 10) + (ReffNum % 10))
        ReffNum /= 10

    return x


print(calculate_palindrome(GivenNum))

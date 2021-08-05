GivenNum = int(input())


def check_prime_number(CheckedNum):
    if CheckedNum < 2:
        return False
    if CheckedNum == 2:
        return True
    if CheckedNum % 2 == 0:
        return False

    for x in range(3, int(CheckedNum / 2), 2):
        if CheckedNum % x == 0:
            return False

    return True


def first_prime_after_given(ReffNum):
    x = ReffNum + 1
    while True:
        if check_prime_number(x) == True:
            break
        else:
            x += 1

    return x


print(first_prime_after_given(GivenNum))

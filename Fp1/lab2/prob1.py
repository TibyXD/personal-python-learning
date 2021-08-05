given_number = int(input())


def check_prime_number(checked_number):
    if checked_number < 2:
        return False
    if checked_number == 2:
        return True
    if checked_number % 2 == 0:
        return False

    for x in range(3, int(checked_number / 2), 2):
        if checked_number % x == 0:
            return False

    return True


def first_prime_after_given(reff_number):
    x = reff_number + 1
    while True:
        if check_prime_number(x) == True:
            break
        else:
            x += 1

    return x


print(first_prime_after_given(given_number))

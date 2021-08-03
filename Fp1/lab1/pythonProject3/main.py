a = int(input("Nr. 1 = "))
b = int(input("Nr. 2 = "))


def cmmdc(a, b):
    if a < 0 or b < 0:
        return 0
    while b != 0:
        r = int(a % b)
        a = b
        b = r
    return a


if cmmdc(a, b) == 0:
    print("ValueError")
else:
    print(cmmdc(a, b))

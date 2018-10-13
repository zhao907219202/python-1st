def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


def power(x, n):
    if n == 1:
        return x
    else:
        return power(x, n - 1) * x


print(power(2, 3))


# 二元查找 bisect
def search(sequence, number, lower, upper):
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)


seq = [34, 67, 9, 123, 4, 100, 96]
seq.sort()
print(seq)
print(search(seq, 96, 0, 6))

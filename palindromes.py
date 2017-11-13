def is_palindrome(word):
    """ """
    word_len = len(word)
    for i in range(len(word)//2):
        if word[i] != word[(i + 1) * -1]:
            return False
    return True


def change_base(n, b):
    """ Changes n from base 10 to base b, type(n) == type(b) == int """
    if type(n) not in (int, float) or type(b) not in (int, float) or (type(n) == float and n != int(n)) or (type(b) == float and b != int(b)):
        raise ValueError("Both arguments must be integers")
    if n < 1 or b < 1:
        raise ValueError("Both integers must be positive")

    if n == 0:
        return [0]
    digits = []
    while n:
        digits.insert(0, n % b)
        n = n // b
    return digits


def find_lowest_palindrome_base(n):
    if type(n) not in (int, float) or (type(n) == float and n != int(n)):
        raise ValueError("Argument must be integer")
    if n < 1:
        raise ValueError("Integer must be positive")

    if n < 3:
        return n + 1

    for b in range(2, n-1):
        if (n % b) and  is_palindrome(change_base(n, b)):
            return b
    return n - 1

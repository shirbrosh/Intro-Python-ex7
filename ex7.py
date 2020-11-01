def print_to_n(n):
    """A function that prints each number from 1 to n, if given a number n
    lower from 1 the function wont print anything"""
    if n <= 1:
        if n == 1:
            print(n)
    else:
        print_to_n(n - 1)
        print(n)


def print_reversed(n):
    """A function that prints each number from n to 1, if given a number n
    lower from 1 the function wont print anything"""
    if n <= 1:
        if n == 1:
            print(n)
    else:
        print(n)
        print_reversed(n - 1)


def has_divisor_smaller_than(n, i):
    """A function that checks if the input n has a divider (different from 1)
    smaller from the input i"""
    if i <= 2:
        return False
    else:
        if n % (i - 1) == 0:
            return True
        else:
            return has_divisor_smaller_than(n, i - 1)


def is_prime(n):
    """A function that returns True if the input n is prime or False
    otherwise"""
    if n > 1 and not has_divisor_smaller_than(n, int(n ** 0.5 + 1)):
        return True
    else:
        return False


def factorial(n):
    """A function that calculate factorial of the number n"""
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def exp_n_x(n, x):
    """A function that calculate the exponent amount of n and x"""
    if n == 0:
        return 1
    else:
        return (x ** n / factorial(n)) + exp_n_x(n - 1, x)


def play_hanoi(hanoi, n, src, dest, temp):
    """A function that plays the 'hanoi tower' game and wins"""
    if n == 1:
        hanoi.move(src, dest)
    elif n > 1:
        play_hanoi(hanoi, n - 1, src, temp, dest)
        hanoi.move(src, dest)
        play_hanoi(hanoi, n - 1, temp, dest, src)

def print_sequences(char_list, n, char_string=""):
    """A function that receives a list of chars and prints every combination of
    strings in length n containing the chars from the list"""
    if n == 0:
        if len(char_string) == 0:
            return
        print(char_string)
    else:
        for char in char_list:
            print_sequences(char_list, n - 1, char_string + char)


def print_no_repetition_sequences(char_list, n, char_string=""):
    """A function that receives a list of chars and prints every combination of
    strings in length n containing the chars from the list without
    repetition"""
    if n == 0:
        if len(char_string) == 0:
            return
        print(char_string)
    else:
        for char in char_list:
            if char not in char_string:
                print_no_repetition_sequences(char_list, n - 1,
                                              char_string + char)


def parentheses_string(n, list_pare, string_pare=""):
    """A function that receives n- number of parentheses pairs and adds to a
    list every legal combination of n pairs, legal combination means that each
    open parentheses has a close parentheses"""
    if len(string_pare) == n * 2:
        list_pare.append(string_pare)
        return
    else:
        if string_pare.count("(") < n:
            parentheses_string(n, list_pare, string_pare + "(")
        if string_pare.count("(") > string_pare.count(")"):
            parentheses_string(n, list_pare, string_pare + ")")


def parentheses(n):
    """A function that receives n- number of parentheses pairs, creates a new
    empty list and adds to the list all the legal parentheses combination using
    the function parentheses_string and returns the list"""
    list_pare = []
    parentheses_string(n, list_pare)
    return list_pare


def up_and_right(n, k, directions=""):
    """A function that receives the number of steps allowed right and left and
    print every legal combinations of steps to preform, legal combination means
    only n times right and k times left"""
    if len(directions) == n + k:
        if directions == "":
            return
        else:
            print(directions)
            return
    else:
        if directions.count("r") < n:
            up_and_right(n, k, directions + "r")
        if directions.count("u") < k:
            up_and_right(n, k, directions + "u")


def flood_fill(image, start):
    """A function that receives an image and a start coordinate and changes
    every other coordinate that can be reached from the start (by moving only
    up, down, right and left) from "." to "*" """
    row = start[0]
    col = start[1]
    image[row][col] = "*"
    if image[row + 1][col] != "*":
        flood_fill(image, (row + 1, col))
    if image[row - 1][col] != "*":
        flood_fill(image, (row - 1, col))
    if image[row][col + 1] != "*":
        flood_fill(image, (row, col + 1))
    if image[row][col - 1] != "*":
        flood_fill(image, (row, col - 1))

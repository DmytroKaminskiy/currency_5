# from time import time


# def timeit(function):
#     def wrapper():
#         start = time()
#         result = function()
#         end = time()
#         print(end - start)
#         return result
#     return wrapper


# @timeit
# def foo():
#     from time import sleep
#     sleep(5)
#     return 1

# foo = timeit(foo)

# print(foo())

'''
length > 8
length < 32
one char should be uppercase
one char should be lowercase
one char should be digit
one char should be special
True, False
'''
# def check_password(p):
#     is_upper = False
#     is_lower = False
#     is_digit = False
#     is_special = False
#     result = False
#
#     if len(p) < 8:
#         return False
#
#     if len(p) > 32:
#         return False
#
#     for c in p:
#         if c.isupper():
#             is_upper = True
#
#     for c in p:
#         if c.islower():
#             is_lower = True
#
#     for c in p:
#         if c.isdigit():
#             is_digit = True
#
#     for c in p:
#         special = [
#             '$',
#             '%',
#             '&',
#         ]
#         if c in special:
#             is_special = True
#
#     if is_upper and is_lower and is_digit and is_special:
#         result = True
#
#     return result

# def check_password(password: str) -> bool:
#     """
#     check if password is strong enough
#     length > 8
#     length < 32
#     one char should be uppercase
#     one char should be lowercase
#     one char should be digit
#     one char should be special
#     """
#     is_upper = False
#     is_lower = False
#     is_digit = False
#     is_special = False
#
#     if len(password) < 8:
#         return False
#
#     if len(password) > 32:
#         return False
#
#     special = (
#         '$',
#         '%',
#         '&',
#     )
#
#     for char in password:
#         if char.isupper():
#             is_upper = True
#         if char.islower():
#             is_lower = True
#         if char.isdigit():
#             is_digit = True
#         if char in special:
#             is_special = True
#
#     return is_upper and is_lower and is_digit and is_special
#
# # length > 8
# assert check_password('123') is False
# # length < 32
# assert check_password('1' * 33) is False
# # one char should be uppercase
# assert check_password('1234567890qwerty%%') is False
# # one char should be lowercase
# assert check_password('1234567890QWERTY%%') is False
# # one char should be special
# assert check_password('1234567890QWErty') is False
# # correct
# assert check_password('1234567890QWErty&&') is True

import string


def check_password(password: str) -> bool:
    """
    check if password is strong enough
    length > 8
    length < 32
    one char should be uppercase
    one char should be lowercase
    one char should be digit
    one char should be special
    """
    if len(password) < 8:
        return False

    if len(password) > 32:
        return False

    password_set = frozenset(password)
    result = password_set & frozenset(string.ascii_lowercase) and \
         password_set & frozenset(string.ascii_uppercase) and \
         password_set & frozenset(string.digits) and \
         password_set & frozenset(string.punctuation)

    return bool(result)


# length > 8
assert check_password('123') is False
# length < 32
assert check_password('1' * 33) is False
# one char should be uppercase
assert check_password('1234567890qwerty%%') is False
# one char should be lowercase
assert check_password('1234567890QWERTY%%') is False
# one char should be special
assert check_password('1234567890QWErty') is False
# correct
assert check_password('1234567890QWErty&&') is True


def split(items: list, num):
    return []


assert split([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]
assert split([1, 2, 3, 4, 5, 6], 3) == [[1, 2, 3], [4, 5, 6]]
assert split([1, 2, 3, 4, 5, 6], 2) == [[1, 2], [3, 4], [5, 6]]
assert split([1, 2, 3, 4, 5], 3) == [[1, 2, 3], [4, 5]]



#########################
def flatten(lst: list):
    return []

assert flatten([1, 2, [3, [4, [], [[[[[5]]]]]]]]) == [1, 2, 3, 4, 5]



# class User(db.models):
#     name = models.CharField()
#     age = models.IntegerField()
#
# User.objects.filter(age__gt=18)

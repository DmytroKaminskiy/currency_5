# import time
#
# CACHE = None
#
#
# def slow_func():
#     global CACHE
#
#     if CACHE is None:  # 1st call
#         print('CACHE DOES NOT EXISTS.')
#         result = 3
#         time.sleep(result)
#         CACHE = result
#         return result
#     else:  # cache exists (CACHE == 3)
#         print('CACHE EXISTS.')
#         return CACHE
#
# start = time.time()
#
# print(slow_func())
# print(slow_func())
# print(slow_func())
#
# end = time.time()
#
# print(f'took time: {end - start}')

####################################

# import time
#
# CACHE = {}
#
#
# def slow_func(sleep_time: int):
#     print(CACHE)
#
#     if sleep_time in CACHE:
#         return CACHE[sleep_time]
#     else:
#         time.sleep(sleep_time)
#         result = sleep_time ** 2
#         CACHE[sleep_time] = result
#         print(CACHE)
#         return result
#
# start = time.time()
#
# print(slow_func(2))  # 4/2sec
# print(slow_func(3))  # 9/3sec
# print(slow_func(3))  # 9/3sec
# print(slow_func(2))  # 4/2sec
#
# end = time.time()
#
# print(f'took time: {end - start}')

###################################


# import time
#
# CACHE = {}
#
#
# def factorial(n):
#     '''
#     5! 5 * 4 * 3 * 2 == 120
#     4! 4 * 3 * 2 == 24
#     '''
#     global CACHE
#     print(CACHE)
#
#     if n in CACHE:
#         return CACHE[n]
#     else:
#         result = 1
#         for num in range(n, 1, -1):
#             time.sleep(1)
#             result *= num
#
#         CACHE[n] = result
#         return result
#
#
# start = time.time()
#
# print(factorial(5))
# print(factorial(5))
# print(factorial(5))
# print(factorial(5))
# print(factorial(4))
# print(factorial(4))
# print(factorial(4))
#
# end = time.time()
#
# print(f'took time: {end - start}')

#########################
# import time
#
# CACHE = {}
#
#
# def add(x, y):
#     global CACHE
#     print(CACHE)
#
#     key = f'add::{x}::{y}'
#     print(CACHE)
#
#     if key in CACHE:
#         return CACHE[key]
#     else:
#         result = x + y
#         CACHE[key] = result
#         return result
#
#
# def diff(x, y):
#     global CACHE
#     print(CACHE)
#
#     key = f'currency::models::Rate::diff::{x}::{y}'
#     print(CACHE)
#
#     if key in CACHE:
#         return CACHE[key]
#     else:
#         result = x - y
#         CACHE[key] = result
#         return result
#
#
# start = time.time()
#
# print('Adding', add(22, 2))
# print('Diff', diff(22, 2))
# print(CACHE)
# # print(add(2, 22))
# # print(add(2, 3))
# # print(add(2, 4))
# # print(add(2, 4))
#
# end = time.time()
#
# print(f'took time: {end - start}')


'''
10,000 | 0.1 - 250
10,000 | 0.2 - 350
11,000 | 0.1 - 300
'''
import time

class User:
    def __init__(self, name):
        self.name = name
        self._slow_method_cache = None

    def slow_method(self):
        if self._slow_method_cache is not None:
            return self._slow_method_cache
        else:
            time.sleep(1)
            result = self.name
            self._slow_method_cache = result
            return result

h1 = User('Dima')
h1.slow_method()
h1.slow_method()
h1.slow_method()
h1.slow_method()
h1.slow_method()

h2 = User('Alex')
h2.slow_method()
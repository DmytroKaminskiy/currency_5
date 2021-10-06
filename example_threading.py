# from time import sleep, time
# from threading import Thread, current_thread

# print(current_thread())
# def foo():
#     print(current_thread())
#     sleep(5)

# start = time()
# foo()
# foo()
# print(f'{time() - start}')

# start = time()
# threads = []
# for _ in range(10):
#     th = Thread(target=foo)
#     th.start()
#     threads.append(th)

# for thread_ in threads:
#     thread_.join()

# print(f'{time() - start}')
# import requests
# from concurrent.futures import ThreadPoolExecutor
#
# def print_content_length(url):
#     print(
#         len(requests.get(url).content)
#     )
#
# urls = [
#     'https://google.com/',
#     'https://lms.ithillel.ua/',
#     'https://ru.wikipedia.org/wiki/%D0%92%D0%B8%D0%BA%D0%B8',
#     'https://habr.com/ru/all/',
# ] * 100
#
# start = time()
# for url in urls:
#     print_content_length(url)

# threads = []
# for url in urls:
#     th = Thread(target=print_content_length, args=[url])
#     th.start()
#     threads.append(th)
#
# for thread_ in threads:
#     thread_.join()

# with ThreadPoolExecutor(max_workers=25) as executor:
#     for url in urls:
#         future = executor.submit(print_content_length, url)
#
# print(f'{time() - start}')
# 25 - 9.7
# 50 - 8.6
# 100 - 8.8
# 400 - 9.8

##########################
# from threading import Thread
# from multiprocessing import Process, current_process
# from time import time
# N = 100_000_0000
#
# print(current_process())
# def countdown(num):
#     print(current_process())
#     while num:
#         num -= 1
#
# start = time()
#
#
# th1 = Process(target=countdown, args=[N / 2])
# th2 = Process(target=countdown, args=[N / 2])
# th1.start()
# th2.start()
# th1.join()
# th2.join()
#
# print(f'{time() - start}')

"""
ThreadPoolExecutor
thread works inside process
GIL - global interpreter lock

CPU bound - Process
I/O bound - Thread

write/read Database - Thread
write to file - Thread
prime number - CPU

parse wiki - Thread
"""
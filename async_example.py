import time


def foo():
    print('One')
    time.sleep(1)
    print('Two')


start = time.time()

# for _ in range(3):
#     foo()

print(f'Took: {time.time() - start}')

print('#####################################')
import asyncio

async def foo_async():
    print('One')
    # time.sleep(1)  # IO bound
    await asyncio.sleep(1)
    print('Two')


async def main():
    await asyncio.gather(foo_async(), foo_async(), foo_async())

start = time.time()
# asyncio.run(main())
print(f'Took: {time.time() - start}')


print('#########################################')
URLS = [
    'https://realpython.com/async-io-python/#the-10000-foot-view-of-async-io',
    'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0',
    'https://ru.wikipedia.org/wiki/Animal_Crossing:_Let%E2%80%99s_Go_to_the_City',
    'https://ru.wikipedia.org/wiki/Nintendo',
    'https://ru.wikipedia.org/wiki/Game_Boy_Advance',
] * 20


start = time.time()
import requests

def fetch_sync(url: str) -> None:
    response = requests.get(url)
    print(response.status_code)

# for url in URLS:
#     fetch_sync(url)


# threading example
from threading import Thread
threads = []
for url in URLS:
    th = Thread(target=fetch_sync, args=[url])
    th.start()
    threads.append(th)

for th in threads:
    th.join()

print(f'Took: {time.time() - start}')

#####################################
import httpx

start = time.time()

async def fetch_async(url):
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        print(r.status_code)

async def main2():
    tasks = [
        fetch_async(url)
        for url in URLS
    ]
    await asyncio.gather(*tasks)


asyncio.run(main2())
print(f'Took: {time.time() - start}')
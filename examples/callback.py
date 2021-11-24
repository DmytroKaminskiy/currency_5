import sys

def send_to_google(payload):
    print(f'sending to google..')
    print(payload)


def send_to_yandex(payload):
    print(f'sending to yandex..')
    print(payload)

default_callback = []
if 'google' in sys.argv:
    default_callback.append(send_to_google)
if 'yandex' in sys.argv:
    default_callback.append(send_to_yandex)


def add(x, y, callbacks=None):
    result = x + y

    if callbacks is not None:
        for callback in callbacks:
            callback(result)

    return result


a = add(2, 4, callbacks=default_callback)
# print(a)

b = add(5, 6, callbacks=default_callback)
# print(b)

c = add(7, 8, callbacks=default_callback)
# print(c)

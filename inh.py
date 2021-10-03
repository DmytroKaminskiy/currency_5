

# class A(object):  # <-- class A
#     pass
#
#
# class B(A):
#     pass
#
#
# print(1)
# print(int)

#
# int_ = 5
# bool_ = True
#
# # print(type(5) is int)
# # print(type(True) is int)
#
# print(isinstance(5, int))
# print(isinstance(True, int))
# print(bool.__mro__)
from urllib.parse import urlencode


class QueryDict(dict):

    def encode(self):
        return urlencode(self)

qd = QueryDict({'a': 1, 'b': 2})
print(qd.encode())

if isinstance(qd, dict):
    print(qd.items())

# 380. Insert Delete GetRandom O(1)

import random


# class RandomizedSet:
#
#     def __init__(self):
#         self._table = {}  # key = 숫자, value = 숫자가 저장되어있는 배열의 위치
#         self._arry = []  # 입력되는 숫자를 저장할 배열
#
#     def insert(self, val: int) -> bool:
#         idx = self._table.get(val)
#
#         if idx is not None:  # if idx 로 하는 경우 0은 false로 받아들이기 때문
#             return False
#
#         idx = len(self._arry)
#         self._arry.append(val)
#         self._table[val] = idx
#         return True
#
#     def remove(self, val: int) -> bool:
#         idx = self._table.get(val)
#
#         if idx is None:
#             return False
#
#         # 배열의 맨 마지막 데이터를 해당 숫자가 있던 위치에 덮어쓰고 배열 마지막을 pop
#         last_val = self._arry[-1]
#         self._arry[idx] = last_val
#         self._table[last_val] = idx
#         self._arry.pop()  # list pop() = o(1)
#         self._table.pop(val)  # dict pop(key) = o(1)
#
#         return True
#
#     def getRandom(self) -> int:
#         return random.choice(self._arry)

# 내풀이
class RandomizedSet:

    def __init__(self):
        self._table = {}

    def insert(self, val: int) -> bool:
        idx = self._table.get(val)

        if idx is not None:  # if idx 로 하는 경우 0은 false로 받아들이기 때문
            return False

        self._table[val] = 1
        return True

    def remove(self, val: int) -> bool:
        idx = self._table.get(val)

        if idx is None:
            return False

        self._table.pop(val)  # dict pop(key) = o(1)
        return True

    def getRandom(self) -> int:
        # list()의 시간복잡도는 o(len(list))라지만,,, 지나치게 길지 않으면 o(1)로 수렴
        return random.choice(list(self._table.keys()))


res = []
obj = RandomizedSet()
res.append(obj.insert(1))
res.append(obj.insert(2))
res.append(obj.insert(3))
res.append(obj.insert(4))
res.append(obj.insert(1))
res.append(obj.remove(1))

res.append(obj.getRandom())
print(res)

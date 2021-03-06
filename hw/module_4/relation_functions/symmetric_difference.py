# coding=utf-8

""""
Напишите reducer, который реализует симметричную разность множеств A и B
(т.е. оставляет только те элементы, которые есть только в одном из множеств).
На вход в reducer приходят пары key / value, где key - элемент множества,
value - маркер множества (A или B)

Sample Input:

    1	A
    2	A
    2	B
    3	B

Sample Output:

    1
    3
"""

import sys

key, prev = '', ''
duplicate = False

for line in sys.stdin:
    key, value = line.strip().split('\t')

    if not prev:
        pass
    elif prev != key:
        if not duplicate:
            print(prev)
        else:
            duplicate = False
    else:
        duplicate = True

    prev = key

if not duplicate:
    print(key)

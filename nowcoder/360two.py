# -*- coding: UTF-8 -*-
import sys

if __name__ == '__main__':
    lines = str(sys.stdin.readline().strip()).split("/")

    hsize = int(lines[0])
    nums = lines[1].split(",")
    maxdeepth = 0
    hashtable = [[] for _ in range(hsize)]
    idx = 0
    for num in nums:
        if "-" in num:
            reals = num.split("-")
            for i in range(int(reals[0]), int(reals[1]) + 1):
                if i not in hashtable[i % hsize]:
                    hashtable[i % hsize].append(i)
                    if maxdeepth < len(hashtable[i % hsize]):
                        maxdeepth = len(hashtable[i % hsize])
                        idx = i % hsize
        else:
            if int(num) not in hashtable[int(num) % hsize]:
                hashtable[int(num) % hsize].append(int(num))
                if maxdeepth < len(hashtable[int(num) % hsize]):
                    maxdeepth = len(hashtable[int(num) % hsize])
                    idx = int(num) % hsize
    result = str(maxdeepth) + "-" + str(idx) + "-"

    res = list(set(hashtable[idx]))
    res = sorted(res, reverse=True)
    for idx, r in enumerate(res):
        if idx == 0:

            result += str(r)
        else:
            result += " " + str(r)
    print(result)

# -*- coding: UTF-8 -*-
if __name__ == '__main__':

n = int(input())
mlist = list(map(lambda x: int(x), input().split(" ")))
t= int(input())
nums=[]
for i in range(t):
    nums.append(list(map(lambda x: int(x), input().split(" "))))
for i in range(t):
    tmp = 0
    for j in range(nums[i][0]-1,nums[i][1] ):
        if mlist[j] == nums[i][2]:
            tmp += 1
    print(tmp)

# -*- coding: UTF-8 -*-

class MyMetaClass(type):

    def __new__(cls, *args, **kwargs):
        # print(cls)
        # print("\n")
        # print(args[1])
        kwargs["add"] = lambda self, value: self.append(value)
        # print("\n")
        # print(kwargs.keys())
        # print("\n")
        # return type( "add",(list,), kwargs)
        return type(args[0], args[1], kwargs)


class MyList(list, metaclass=MyMetaClass):
    '''
    一、最优解的机结构特征
    当求解数组长度为1时，有两种情况
        （1）当nums[0]为正数：最优解为nums[0]
        （2）当nums[0]为负数：最优解为nums[0]
    当长度更长时，最大子序列的第一项不可能为负数，因为负数一定会让子数组减小
    最后一项也不会是负数，同上，所以常规情况下的解，一定都是整数开始和结束
    二、根据最优解的特征建立递归式     
        res 代表最优值
        sum 代表局部最优值
            +
            | nums.length ==1        ,res=nums[0]
        res=| nums.length  >1        ,res = sum>res?sum:res;
            +
    三、自底向上计算最优值        
    '''


def maxSubArray(nums):
    sum = 0
    res = nums[0]
    for i in nums:
        if sum + i < i:
            sum = i
        else:
            sum += i
        if sum > res:
            res = sum
    return res





if __name__ == '__main__':
    # print(maxSubArray([-1]))
    # print(lengthOfLastWord("a"))
    print((uniquePaths(3, 2)))
    # li = MyList()
    # li.add(1)
    # li.add(2)
    # print(li)
    # print(li.__class__)

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
    '''
    53.最大子序和
    思路：唯一要考虑的事情就是负数，按照动态规划的考虑方式，
    到最后一位索引的时候，如果之前的序列和+当前元素比当前元素大，
    有两种情况 1、当前是正数，之前序列和是正数
    2，当前是负数，之前是正数。
    第一种情况只需要记录现在最大值，
    第二种情况，还需要记录之前的最大值，便于比较。
    所以合二为一就可以了
    :param nums:
    :return:
    '''
    res = nums[0]
    max_val = 0
    for i in nums:
        if i + max_val >= i:
            max_val += i
        else:
            max_val = i
        res = max(max_val, res)
    return res


if __name__ == '__main__':
    # print(maxSubArray([-1]))
    # print(lengthOfLastWord("a"))
    print((maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])))
    # li = MyList()
    # li.add(1)
    # li.add(2)
    # print(li)
    # print(li.__class__)

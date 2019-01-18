# -*- coding: UTF-8 -*-
def fullJustify(words, maxWidth):
    """
    68. 文本左右对齐
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    idx = 0
    res = []
    while idx < len(words):
        count = len(words[idx])
        now_len = 1
        while idx + 1 < len(words) and count + len(words[idx + 1]) + 1 <= maxWidth:  # 贪心选择，找出能在一行放置的最大单词数
            count += len(words[idx + 1]) + 1
            now_len += 1
            idx += 1
        tmp = ""
        if idx != len(words) - 1 and now_len > 1:  # 单词数大于1 而且不是最后一行
            space = max(1, (maxWidth - count) // (now_len - 1) + 1)  # 求每个区间空格数量
            block = (maxWidth - count) % (now_len - 1) + (idx - now_len + 1)  # 求多余的空格应该分布在前几个区间
            for i in range(idx - now_len + 1, idx):
                tmp += words[i]
                tmp += " " * space
                if i < block:
                    tmp += " "
            tmp += words[idx]

        elif idx != len(words) - 1 and now_len == 1:  # 单词数等于 1 而且不是最后一行
            tmp = words[idx]
            tmp += " " * (maxWidth - count)
        else:  # 最后一行
            for i in range(idx - now_len + 1, idx):
                tmp += words[i]
                tmp += " "
            tmp += words[idx]
            tmp += " " * (maxWidth - len(tmp))
        res.append(tmp)
        idx += 1

    return res


if __name__ == '__main__':
    print(fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"],
                      16))
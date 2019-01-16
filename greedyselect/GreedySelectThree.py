# -*- coding: UTF-8 -*-
def fullJustify(words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    idx = 0
    res = []
    while idx < len(words):
        count = len(words[idx])
        now_len = 1
        while idx + 1 < len(words) and count + len(words[idx + 1]) + 1 <= maxWidth:
            count += len(words[idx + 1]) + 1
            now_len += 1
            idx += 1
        tmp = ""
        if idx != len(words) - 1 and now_len > 1:
            space = max(1, (maxWidth - count) // (now_len - 1) + 1)
            block = (maxWidth - count) % (now_len - 1) + (idx - now_len + 1)
            for i in range(idx - now_len + 1, idx):
                tmp += words[i]
                tmp += " " * space
                if i < block:
                    tmp += " "
            tmp += words[idx]

        elif idx != len(words) - 1 and now_len == 1:
            tmp = words[idx]
            tmp += " " * (maxWidth - count)
        else:
            for i in range(idx - now_len + 1, idx):
                tmp += words[i]
                tmp += " "
            tmp += words[idx]
            tmp += " " * (maxWidth - len(tmp))
        # print(len(tmp))
        res.append(tmp)
        idx += 1

    return res


if __name__ == '__main__':
    print(fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"],
                      16))

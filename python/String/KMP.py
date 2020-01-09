def kmp(str1, str2):
    """
    KMP算法：判断str1是否存在字串str2
    :param str1:
    :param str2:
    :return:
    """
    # 子串str2的部分匹配表
    match = [0]
    prefix = []
    for i in range(1, len(str2)):
        prefix.append(str2[:i])  # 补充前缀
        # 判断前缀与后缀最长的共有元素的长度
        length = 0
        for m in range(1, i+1):
            if str2[m:i+1] in prefix:  # 后缀与所有前缀对比判断是否为共有元素
                if length < i + 1 - m:
                    length = i + 1 - m
        match.append(length)

    print(match)

    i1 = 0
    while True:
        if i1 > len(str1) - 1:
            break

        substr = ''
        for s1, s2 in zip(str1[i1:], str2):
            if s1 != s2:
                break
            else:
                substr += s1
        if len(substr) == len(str2):
            return i1
        elif substr == '':
            i1 += 1
        else:
            # 这里时最关键的优化：移动位数 = 已匹配的字符数 - 对应的部分匹配值
            i1 += len(substr) - match[len(substr)-1]

    return -1


if __name__ == '__main__':
    print(kmp('BBC ABCDAB ABCDABCDABDE', 'ABCDABD'))

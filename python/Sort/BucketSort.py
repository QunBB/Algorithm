from typing import List


def bucket_sort(arr: List[int], max_len: int):
    """
    基数排序（桶排序）
    :param arr:
    :param max_len: 最大值的位数
    :return:
    """
    temp = arr.copy()  # 用于存放每次从桶取出的数据

    # 建立0-9 10个桶
    bucket = dict()
    for i in range(10):
        bucket[i] = []

    # 最大值只有三位数的情况下
    for i in range(1, max_len):
        # 将数值放入对应的桶中
        for a in temp:
            bucket[get_digit(a, i)].append(a)
        # 将数值从桶按顺序取出，并将桶清空
        temp = []
        for n in range(10):
            temp.extend(bucket[n])
            bucket[n] = []

    return temp


def get_digit(num: int, n: int):
    """
    取出num对应位数的数值，1代表个位数，2代表十位数，以此类推
    :param num:
    :param n: n位数
    :return:
    """
    num_str = str(num)
    if n > len(num_str):
        return 0
    else:
        return int(num_str[-n])


if __name__ == '__main__':
    print(bucket_sort([10, 5, 321, 33, 11, 100]))

from typing import List


def merge(arr1: List, arr2: List):
    """
    将两个有序数组合并为一个数组，仍保持有序
    :param arr1:
    :param arr2:
    :return:
    """
    res = []
    i1 = 0
    i2 = 0
    while i2 < len(arr2):
        if i1 >= len(arr1):
            res.extend(arr2[i2:])
            break

        if arr2[i2] <= arr1[i1]:
            res.append(arr2[i2])
            i2 += 1
        else:
            while i1 < len(arr1):
                if arr1[i1] < arr2[i2]:
                    res.append(arr1[i1])
                    i1 += 1
                else:
                    break

    if i1 < len(arr1):
        res.extend(arr1[i1:])

    return res


def merge_sort(arr: List):
    """
    归并排序
    :param arr:
    :return:
    """
    # 归并排序中分治思想的"分"阶段：将原数组分为长度为1的子序列数组，可能会有一个长度为2的（数组的长度为奇数时）
    res = []
    i = 0
    while i < len(arr):
        if len(arr) - i == 3:
            res.append([arr[i]])
            res.append(sorted(arr[i+1:]))
            i += 3
        else:
            res.append([arr[i]])
            res.append([arr[i+1]])
            i += 2
    # 归并排序中分治思想的"治"阶段：将两两之间的有序子序列进行合并为一个新的有序子序列，直到只剩一个有序子序列，即为最终的排序结果
    while len(res) > 1:
        temp = []
        i = 0
        while i <= len(res)-1:
            if i == len(res)-1:
                temp.append(res[i])
                break
            else:
                temp.append(merge(res[i], res[i+1]))
                i += 2
        res = temp

    return res[0]


if __name__ == '__main__':
    # print(merge([4, 8], [3, 5, 9, 10]))
    print(merge_sort([8, 4, 5, 7, 1, 3, 6]))


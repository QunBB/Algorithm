import math
import time
import random


def bubbleSort(arr):
    """
    BubbleSort 冒泡排序
    :param arr: 待排序数组
    :return:
    """

    flag = False
    for n in range(len(arr) - 1):
        for i in range(len(arr) - n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                flag = True
        if not flag:  # 如果没有进行过数据交换，则无需再进行排序
            break
        else:
            flag = False

    return arr


def selectionSort(arr):
    """
    SelectionSort 选择排序
    :param arr: 待排序数组
    :return:
    """

    for i in range(len(arr) - 1):
        _min = arr[i]
        min_index = i
        for j in range(i + 1, len(arr)):
            if _min > arr[j]:
                _min = arr[j]
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def insertSort(arr):
    """
    InsertSort 插入排序
    :param arr: 待排序数组
    :return:
    """

    for i in range(1, len(arr)):
        val = arr[i]
        index = i - 1
        while (index >= 0) & (val < arr[index]):
            arr[index + 1] = arr[index]
            index -= 1

        arr[index + 1] = val

    return arr


def shellSotr(arr):
    """
    ShellSort 希尔排序
    :param arr: 待排序数组
    :return:
    """

    n = len(arr) // 2  # n：分组数，其实也是每组的步长
    while n > 0:
        for i in range(n):
            for j in range(i + n, len(arr), n):  # 对每组数据进行遍历
                # 进行插入排序
                val = arr[j]
                index = j - n
                while (index >= i) & (val < arr[index]):
                    arr[index + n] = arr[index]
                    index -= n
                arr[index + n] = val

        n = n // 2


def quickSortRecursion(arr, left, right):
    """
    The recursion of quickSort
    :param arr:
    :param left: 此次排序数组范围的最左索引
    :param right: 最右索引
    :return:
    """
    mid = arr[(right + left) // 2]  # 取数组中间位置的数值作为划分左右区域的依据
    LEFT = left  # 将输入的left固定住，用于递归的输入
    RIGHT = right  # 同上

    while left < right:
        while arr[left] < mid:
            left += 1
        while arr[right] > mid:
            right -= 1
        arr[left], arr[right] = arr[right], arr[left]
    # 确定最终中间数值mid的位置
    if arr[left] == mid:
        MID = left
    else:
        MID = right

    # 对划分后的左边区域和右边区域分别进行快速排序的递归
    # 当左边或右边区域只剩下一个元素时，则无需再进行排序了
    if (RIGHT - MID) > 1:
        quickSortRecursion(arr, MID+1, RIGHT)
    if (MID - LEFT) > 1:
        quickSortRecursion(arr, LEFT, MID-1)


def quickSort(arr):
    """
    quickSort 快速排序
    :param arr: 待排序数组
    :return:
    """
    quickSortRecursion(arr, 0, len(arr)-1)


if __name__ == '__main__':
    # 检验算法的正确性
    l = [8, 9, 1, 7, 2, 3, 5, 4, 6, 0]
    print(l)
    quickSort(l)
    print(l)

    # 检验算法的运行时间
    n = 100000
    l = [random.randint(0, n) for i in range(n)]
    s1 = time.time()
    quickSort()
    s2 = time.time()
    print(s2 - s1)
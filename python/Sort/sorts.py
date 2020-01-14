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


def shellSort(arr):
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

        if left >= right:
            break

        arr[left], arr[right] = arr[right], arr[left]

        # 先达到中间位置的一边继续移动（或者遇到与中间位置的数值相等），另一边暂停移动
        if arr[left] == mid:
            right -= 1
        if arr[right] == mid:
            left += 1

    # 此时有一边已经完成排序，需要移动一个位置，否则会无限递归
    if left == right:
        left += 1
        right -= 1

    if LEFT < right:
        quickSortRecursion(arr, LEFT, right)
    if RIGHT > left:
        quickSortRecursion(arr, left, RIGHT)


def quickSort(arr):
    """
    quickSort 快速排序
    :param arr: 待排序数组
    :return:
    """
    quickSortRecursion(arr, 0, len(arr)-1)


if __name__ == '__main__':
    # 检验算法的正确性
    l = [8, 9, 1, 7, 2, 0, 3, 5, -1, 6, 0]
    print(l)
    quickSort(l)
    print(l)

    # 检验算法的运行时间
    n = 100
    l = [random.randint(0, n) for i in range(n)]
    s1 = time.time()
    quickSort(l)
    s2 = time.time()
    print(s2 - s1)
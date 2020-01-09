import random
import time


# 以index=root作为根节点，向下进行递归：将父节点与子节点中进行比较，将父节点替换为较大值
def heap(arr, root, length):
    # 左子树的index
    left = 2 * root + 1
    # 右子树的index
    right = 2 * root + 2

    head = root

    if left < length:
        if arr[head] < arr[left]:
            head = left

    if right < length:
        if arr[head] < arr[right]:
            head = right

    if head != root:
        arr[root], arr[head] = arr[head], arr[root]
        heap(arr, head, length)


# 从最后一个非叶子节点向前调整，不然无法保证大顶堆的建立
def max_heap(arr, length):
    for i in range(int(len(arr)/2)-1, -1, -1):
        heap(arr, i, length)


# 建立大顶堆之后，数组的第一个元素就为最大值了
# 然后将第一个元素替换到最后的位置
# 忽略最后一个元素，继续建立大顶堆
def heap_sort(arr):
    length = len(arr)
    for i in range(length):
        max_heap(arr, length-i)
        arr[0], arr[length-i-1] = arr[length-i-1], arr[0]


if __name__ == '__main__':
    # 检验算法的正确性
    l = [8, 9, 1, 7, 2, 3, 5, 4, 6, 0]
    print(l)
    heap_sort(l)
    print(l)

    # 检验算法的运行时间
    n = 10000
    l = [random.randint(0, n) for i in range(n)]
    s1 = time.time()
    heap_sort(l)
    s2 = time.time()
    print(s2 - s1)

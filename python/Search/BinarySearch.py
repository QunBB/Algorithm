def search(arr, target):
    """
    不使用递归的二分查找
    :param arr: 待查询数组
    :param target: 查找目标
    :return:
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = int((left + right) / 2)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def search2(arr, target):
    index = search_recursion(arr, target, 0, len(arr)-1)
    return index


def search_recursion(arr, target, left, right):
    if left > right:
        return -1
    mid = int((left + right) / 2)
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return search_recursion(arr, target, left, mid-1)
    else:
        return search_recursion(arr, target, mid+1, right)


if __name__ == '__main__':
    arr = [1, 3, 5, 6, 7, 10, 15]
    print(search2(arr, 5))

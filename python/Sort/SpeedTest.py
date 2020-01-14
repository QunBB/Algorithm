import random
import time
from python.Sort.sorts import bubbleSort, selectionSort, insertSort, shellSort, quickSort
from python.Sort.MergeSort import merge_sort
from python.Sort.HeapSort import heap_sort


"""
各种排序算法性能测试对比：
    bubbleSort : 7.5025200843811035
    selectionSort : 2.3237240314483643
    insertSort : 3.212090253829956
    shellSort : 0.04243206977844238
    merge_sort : 0.042969703674316406
    heap_sort : 14.020823001861572
    sorted : 0.0009388923645019531
嘤嘤嘤，事实证明python尽量还是用自带的方法，毕竟很多底层都是c实现的，速度比你自己实现的快了不止一点点
"""

n = 10000
methods = ["bubbleSort", "selectionSort", "insertSort", "shellSort", "merge_sort", "heap_sort", "sorted"]
for method in methods:
    l = [random.randint(0, n) for i in range(n)]
    s1 = time.time()
    eval(method)(l)
    s2 = time.time()
    print(method, ":", s2-s1)

import random
import time
from python.Sort.sorts import bubbleSort, selectionSort, insertSort, shellSort, quickSort
from python.Sort.MergeSort import merge_sort
from python.Sort.HeapSort import heap_sort


"""
各种排序算法性能测试对比：
    bubbleSort : 7.712609052658081
    selectionSort : 2.404778003692627
    insertSort : 3.383096218109131
    shellSort : 0.043745994567871094
    quickSort : 0.020576000213623047
    merge_sort : 0.04463386535644531
    heap_sort : 15.450256109237671
    sorted : 0.0013229846954345703
嘤嘤嘤，事实证明python尽量还是用自带的方法，毕竟很多底层都是c实现的，速度比你自己实现的快了不止一点点
"""

n = 10000
methods = ["bubbleSort", "selectionSort", "insertSort", "shellSort", "quickSort", "merge_sort", "heap_sort", "sorted"]
for method in methods:
    l = [random.randint(0, n) for i in range(n)]
    s1 = time.time()
    eval(method)(l)
    s2 = time.time()
    print(method, ":", s2-s1)

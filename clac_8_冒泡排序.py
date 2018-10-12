# -*- coding:utf-8 -*-
def bubbleSort(test):
    """ 冒泡排序的时间复杂度是O(N^2) """
    for i in range(len(test) - 1):
        for j in range(len(test) - i - 1):
            if test[j] > test[j + 1]:
                test[j], test[j + 1] = test[j + 1], test[j]
    return test


if __name__ == '__main__':
    res = bubbleSort([2, 4, 3, 2, 111])
    print(res)

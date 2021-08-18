Binary search

二分模板一共有两个，分别适用于不同情况。

算法思路：假设目标值在闭区间[l, r]中， 每次将区间长度缩小一半，当l = r时，我们就找到了目标值。

假设数组 arr = [1, 2, 3, 3, 3, 5]

版本1

当我们将区间[l, r]划分成[l, mid]和[mid + 1, r]时，其更新操作是r = mid或者l = mid + 1; 计算mid时不需要加1。

返回结果为 第一个 大于等于 某个数的 下标
arr = [1,2,3,3,3,5]

def binarySearch1(k): # lower_bound,
    l, r = 0, len(arr) - 1
    while l < r:
        mid = l + r >> 1
        if arr[mid] < k:
            l = mid + 1
        else:
            r = mid
    return l

print(binarySearch1(0))
print(binarySearch1(1))
print(binarySearch1(2))
print(binarySearch1(3))
print(binarySearch1(4))
print(binarySearch1(5))
print(binarySearch1(6))
'''
0
0
1
2
5
5
5
'''
版本2

当我们将区间[l, r]划分成[l, mid - 1]和[mid, r]时，其更新操作是r = mid - 1或者l = mid;，此时为了防止死循环，计算mid时需要加1。

返回结果为 最后一个 小于等于 某个数的 下标
def binarySearch2(k): 
    l, r = 0, len(arr) - 1
    while l < r:
        mid = (l + r + 1) >> 1
        if arr[mid] <= k:
            l = mid
        else:
            r = mid - 1
    return l

print(binarySearch2(0))
print(binarySearch2(1))
print(binarySearch2(2))
print(binarySearch2(3))
print(binarySearch2(4))
print(binarySearch2(5))
print(binarySearch2(6))
'''
0
0
1
4
4
5
5
'''

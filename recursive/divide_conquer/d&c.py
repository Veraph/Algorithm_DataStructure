# sum.py -- use D&C thinking to write sum function
def sum(arr):
    '''calculate the sum of an arrary'''
    if arr:
        return arr.pop() + sum(arr)
    else:
        return 0

def cnt(arr):
    '''count the elements in an arrary'''
    if arr:
        arr.pop()
        return 1 + cnt(arr)
    else:
        return 0

def fmax(arr):
    '''find the max num in an arrary'''
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_fmax = fmax(arr[1:])
    return arr[0] if arr[0] > sub_fmax else sub_fmax

def binary(arr, target):
    '''binary search is also a D&C thinking way'''
    begin = 0
    end = len(arr) - 1

    while begin <= end:
        mid = (begin+end)//2
        guess = arr[mid]
        if target > guess:
            begin = mid + 1
        elif target < guess:
            end = mid - 1
        else:
            return mid
    return None
    

arr = [1, 2, 3, 4, 5]
arr_sum = arr_cnt = arr[:]

sum_result = sum(arr_sum)
cnt_result = cnt(arr_cnt)
fmax_result = fmax(arr)
binary_result = binary(arr, 2)

print(sum_result, cnt_result, fmax_result, binary_result)




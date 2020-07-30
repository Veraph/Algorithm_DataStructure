# find the longest increasing subsequence
'''
    寻找一个长度为N的序列中最长的上升子序列，可以把其子问题看为
    求以ak(k=1, 2...n)为终点的最长上升子序列长度。
    默认集合里全为1
    当k大于1时，如果后一个数i大于前一个数j，则以i为终点的最长上升子序列为
    自身已经标明的长度，和j位置+1两个中更大的值
'''
def longest_sub(nums):
    if not nums:
        return 0

    length = len(nums)
    maxLen = [1 for i in range(length)]
    for i in range(1, length):
        for j in range(0, i):
            if nums[i] > nums[j]:
                maxLen[i] = max(maxLen[i], maxLen[j]+1)

    return max(maxLen)

print(longest_sub([-2,-1]))
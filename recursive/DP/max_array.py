# find the longest common array in two arrays
# 时间复杂度O(s1s2)

def max_array(s1, s2):
    '''解决最长公共子序列问题''' 
    len_s1, len_s2 = len(s1), len(s2)
    cell = [[0 for i in range(len_s2 + 1)] for j in range(len_s1 + 1)] # 开一个二维数组, 注意x轴和y轴

    for i in range(len_s1):
        for j in range(len_s2):
            if s1[i] == s2[j]:
                cell[i+1][j+1] = cell[i][j] + 1
            else:
                cell[i+1][j+1] = max(cell[i][j+1],cell[i+1][j])
    return cell[-1][-1]

print(max_array('fishdaw', 'fish'))
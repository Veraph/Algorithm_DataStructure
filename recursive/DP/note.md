## Notes of Dynamic Programming
1. 动态规划虽然理论上可以通过普通递归解决，但是会严重超时因为产生了很多重复计算，可以在递归时记录已递归出的结果来解决，即记忆化递归
2. 但是递归型动归本身存在在栈溢出的风险，因此我们可以使用另外的方法来解决，递推型动归
3. 空间优化，可以使用滚动数组
4. 动归的一般思路
   1. 原问题分解为子问题，子问题求出就会被保存
   2. 确定状态
   3. 确定一些初始状态（边界状态）的值
   4. 确定状态转移方程
5. 能用动归解决的问题的特点
   1. 问题具有最优子结构性质（问题的最优解所包含的子问题的解也是最优的）
   2. 无后效行（当前的若干状态值一旦确定，此后过程演变只和这些状态值有关）
6. 动归类似于分治，不过分治是从上到下分解出最小的问题，解决就ok，动归虽然也从最下面或最后面的问题开始，不过解出来后需要保存子问题，然后回到最初问题得解
7. git diff也用动态规划实现
8. 找到边界情况率先处理
9. 动归的三种形式：
   1.  记忆递归（相比递推只经过有用状态，没有浪费 / 可能因为递归层数太深导致爆栈，比递推慢）
   2.  我为人人递推（无明显优势）
   3.  人人为我递推（状态i的值Fi由已知的状态值Fk,Fm..Fy推出)
10. 例题
#### 最长公共子序列(递推) / 如果是最长子串则要求连续

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

#### 最长上升子序列（不要求连续）

    # 求以ak(k=1, 2, 3...n)为终点（一个上升子序列中最右边的那个数）的最长上升子序列的长度
    # 将这N个子问题求解后，在这N个子问题的解中最大的就是整个问题的解
    # 人人为我型
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

#### 方盒游戏




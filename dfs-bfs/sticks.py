
'此实现在mac上是爆栈的情况。。'

#若干木棒，能否全部用来拼成若干棍子，使单根棍子尽可能短
#思路
#尝试枚举，从最长的木棒长度到木棒总长度的一半
#优化，对于不是木棍总长度的因子的长度可以直接否定（不能被整除的）
#状态，二元组(R,M)，R指还没被有掉的木棒数目，M指当前正在拼的棍子还缺少的长度
#初始状态（N，L），全部N根木棒，假定棍子长度L
#终止状态（0，0）

#以上思路花费时间太长，需要剪枝
#1.不要在同一个位置多次尝试相同长度木棒
#2.如果由于以后的拼接失败需要重新调整第i根棍子的拼法，则不会考虑替换第i根棍子中的第一根木棒（换了也没用，因为以后还是会用到这根木棒）
#3.不要希望通过仅仅替换已拼好棍子的最后一根木棒就能够改变失败的局面
#4.确保拼每一根棍子时，已拼好的部分的长度是从长到短排列的（每次找木棒时，从刚接上去的木棒的下一条开始寻找）

#深搜函数
def dfs(R,M):
    global L, N, lens, used, laststick
    #总是先录入退出条件
    if R == 0 and M == 0:
        return True
    #一根完成后，如果还有剩余，开始尝试下一根
    if M == 0:
        M = L 
    #剪枝4
    start_no = 0
    if M != L:
        start_no = laststick + 1

    for i in range(start_no, N):
        #剪枝1
        if used[i] == 0 and lens[i] == lens[i-1]:
            continue

        used[i] = 1
        laststick = i
        if dfs(R-1, M-lens[i]):
            return True
        else:
            used[i] = 0 #本次不能使用第i根木棒
            #剪枝2，3
            if M == L or lens[i] == M:
                return False
    return False

#读取数据
N = int(input())
lens = list(map(int, input().split(' ')))
total_len = sum(lens) #记录总长
lens.sort(reverse=True) #将木棍从长到短进行排序

#从最长的木棒长度开始尝试棍子长度
half_len = int(total_len/2)
for L in range(lens[0], half_len):
    #不能整除，进入下一个L
    if total_len % L != 0:
        continue
    #初始化木棒使用情况，进入搜索流程
    laststick = 0
    used = [0 for i in range(N)]
    if dfs(N, L):
        print(L)
        break
    #如果当前长度大于总长的一半，直接返回总长作为棍子长度
    if L > half_len:
        print(total_len)



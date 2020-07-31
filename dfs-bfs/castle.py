## castle.py -- return the number of rooms and the biggest room


#创建一个跟城堡图大小一致的染色矩阵并初始化全部为0
#从第一个点开始进行循环遍历，遇到被染色的点直接返回，否则开始探索
#当使用[[0]*cols] * rows创建矩阵时，改变某个位置的值并不是如我们所想
#如果矩阵为m，那么m[n][1] = 1执行的操作是将第一列全部变为0，不论n是多少
#这是因为乘法创建的是引用，而不是新的对象


#所以创建矩阵应该使用[[0 for i in range(m)] for i in range(n)]的方式

def dfs(i, j):
    '''深度优先搜索算法'''
    global room_area
    global room_no
    if color[i][j] != 0:
        return
    color[i][j] = room_no
    room_area += 1
    
    if castle[i][j] & 1 == 0:
        dfs(i, j-1)
    if castle[i][j] & 2 == 0:
        dfs(i-1, j)
    if castle[i][j] & 4 == 0:
        dfs(i, j+1)
    if castle[i][j] & 8 == 0:
        dfs(i+1, j)
        
'''接受用户参数输入和矩阵输入, 创建color矩阵，调用dfs'''
rows = int(input())
cols = int(input())
castle = [[0 for i in range(cols)] for i in range(rows)] # 初始化矩阵
for i in range(rows):
    castle[i] = list(map(int, input().split(' '))) # 同行数字用空格分开，不同行用回车换行

room_no = 0
room_max = 0
color = [[0 for i in range(cols)] for i in range(rows)] # 创建color
for i in range(rows):
    for j in range(cols):
        if color[i][j] == 0:
            room_no += 1
            room_area = 0
            dfs(i, j)
            room_max = max(room_max, room_area)

print('The no. of room is %s' % room_no)
print('The max room is %s' % room_max)
print(castle)
print(color[0][0])
    



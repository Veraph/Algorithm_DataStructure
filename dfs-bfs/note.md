## Notes of DFS and BFS
### 深度优先搜索DFS
1. 一般来说用递归来实现，归根到底是用栈来实现的（递归编写的代码帮助我们去维护那个栈,递归return即推出栈）
2. 注意事项：
   1. 要选择合适的搜索顺序，优先尝试可能性较少的步骤
   2. 发现表面上不同实际上相同的重复状态，避免重复搜索
   3. 根据实际问题发掘剪枝方案

### 广度优先搜索BFS
1. 用来解决最短路径问题的算法
2. 帮助解决两类问题：
   1. 从A出发，有前往B的路径吗
   2. 从A出发，前往B的哪条路径最短
3. 广度优先算法先检查一度关系，再检查二度关系，而只有按照顺序查找才能实现这样的目的，数据结构队列(queue)可以实现此目的
4. 队列（先进先出），栈（后进先出）
5. 可以用哈希表实现图
6. Python中使用collections里的deque()创建一个双端队列；popleft()与pop()不同，是弹出左边第一个
7. 注意检查过的人名要进行标记
#### 实例
    from collections import deque

    #建立字典graph
    pass
    #搜索函数
    def search(name):
        search_queue = deque()
        search_queue += graph[name]
        searched = [] #创建一个用于标记的列表
    while search_queue:
       people = search_queue.popleft()
       if people not in searched:
           if is_seller(people):
              print(people)
              return True
           else:
              search_queue += graph[people]
              searched.append(people)
    return False
    #判断函数
    def is_seller(name):
       return name[-1] == 'm'
      

   
    
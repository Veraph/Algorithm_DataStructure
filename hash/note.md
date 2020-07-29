## Notes of Hash

1. 哈希表又称散列表，即python中的字典
2. 哈希表使用hash function进行映射，所需查找时间为O(1)
3. 哈希表是实现DNS解析（网址映射到IP地址）的方式之一
4. 数组使用下标进行随机访问以及哈希表查找的实现都是因为电脑已经记住了内存中每个位置的值，所以不用重新计算
5. 网站缓存的数据也存储在哈希表中
6. 哈希表适用于：  
   1. 模拟映射关系
   2. 防止重复（算法题常见）
   3. 记住数据
7. 冲突时在冲突位置存储一个链表
8. 填装因子 = 哈希表包含总元素数 / 位置总数， 当因子越小，冲突可能越小，性能越高。如果因子过大（大于0.7？），则需要调整长度，或开链表
9. hash函数的结果应该是均匀分布的
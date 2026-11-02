# Python 数据结构与算法（Data Structures & Algorithms）

> **唯一维护文件**：Python 算法常见模板及复杂度。普通 Python 语言特性请更新 [python-interview.md](python-interview.md)。

## 学习索引

- [x] Union Find / Disjoint Set Union
- [x] Priority Queue / Binary Heap (`heapq`)
- [ ] Array / Hash Map / Hash Set
- [ ] Two Pointers / Sliding Window
- [ ] Stack / Monotonic Stack / Queue
- [ ] Linked List / Fast & Slow Pointers
- [ ] Binary Search
- [ ] Tree DFS / BFS
- [ ] Graph Traversal / Topological Sort
- [ ] Backtracking
- [ ] Dynamic Programming
- [ ] Greedy / Intervals

## 1. Union Find / Disjoint Set Union

用途：动态集合合并、判断连通性、计算连通分量。路径压缩 + 按大小合并，均摊单次操作 `O(α(n))`。

```python
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.count -= 1
        return True
```

**记忆法**：初始化 parent/size/count → find 路径压缩 → union 比较 size → count 减一。

**练习题**：Number of Connected Components、Redundant Connection、Accounts Merge。

## 2. Priority Queue / Heap — `heapq`

Python `heapq` 默认是 min-heap。入堆 / 出堆 `O(log n)`；查看最小值 `heap[0]` 为 `O(1)`；`heapq.heapify(items)` 是 `O(n)`。

```python
import heapq

pq = []
heapq.heappush(pq, (2, "low"))
heapq.heappush(pq, (1, "high"))
priority, job = heapq.heappop(pq)   # (1, "high")
```

最大堆的通用兼容写法（适合优先级为数字时）：

```python
max_pq = []
heapq.heappush(max_pq, (-10, "highest"))
heapq.heappush(max_pq, (-5, "lower"))
neg_priority, task = heapq.heappop(max_pq)  # (-10, "highest")
```

有相同优先级且任务对象不可比较时，使用单调计数器避免 tuple 比较错误：

```python
from itertools import count

counter = count()
pq = []
heapq.heappush(pq, (1, next(counter), {"task": "A"}))
heapq.heappush(pq, (1, next(counter), {"task": "B"}))
```

**练习题**：Top K Frequent Elements、Kth Largest、Merge K Sorted Lists、Meeting Rooms II。

## 3. 面试答题检查

1. 先说思路、边界情况和复杂度。
2. Python 内置容器选型：`dict` / `set` / `deque` / `heapq`。
3. 检查空数组、重复元素、负数、大输入和索引范围。
4. 写出复杂度并解释来源，不只报答案。

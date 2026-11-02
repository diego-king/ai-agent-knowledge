# Data Structures & Algorithms — Python

> 维护一个可背诵的规范版本；新增题型直接更新本文件。

## Union Find / Disjoint Set Union

用途：判断连通性、动态合并集合、无向图连通分量。路径压缩 + 按大小合并的均摊单次操作复杂度为 `O(α(n))`，其中 α 为反 Ackermann 函数。

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

**记忆点**：初始化 → find 路径压缩 → union 按 size → count 减一。

## Priority Queue / Heap — `heapq`

Python 内置 `heapq` 默认是 **min-heap**；push/pop 是 `O(log n)`，读取最小值 `heap[0]` 是 `O(1)`。

```python
import heapq

pq = []
heapq.heappush(pq, (2, "low"))
heapq.heappush(pq, (1, "high"))
priority, job = heapq.heappop(pq)  # (1, "high")
```

最大堆常用负数优先级：`heapq.heappush(pq, (-priority, item))`。相同优先级且 item 不可比较时，增加单调递增的序号作为第二个 tuple 元素。

## 面试复习

- [ ] Number of Connected Components
- [ ] Redundant Connection
- [ ] Top K Elements
- [ ] Merge K Sorted Lists
- [ ] Meeting Rooms / Task Scheduling

可运行演示见 [../code/examples.py](../code/examples.py)。

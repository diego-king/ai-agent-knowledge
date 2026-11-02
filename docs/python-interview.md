# Python 面试知识主笔记

> 本文件是 Python 面试主题的规范文字源。新增笔记直接补充本文件，而不是生成新版本文件。

## 核心考点清单

- [ ] 类型与类型转换：`str`、`int`、`float`、`bool`
- [ ] List / Dict / Set Comprehension
- [ ] 可变对象、浅拷贝、深拷贝、默认参数
- [ ] `==` 与 `is`，引用和哈希
- [ ] Iterator / Generator 与 `yield`
- [ ] Exceptions 与 context manager
- [ ] `heapq` / `collections.deque` / `Counter`
- [ ] GIL、threading、multiprocessing、asyncio 的适用场景
- [ ] 常见算法复杂度与边界条件

## 小题 1：字符串与数字

```python
age = 36
message = "Age: " + str(age)  # 显式转换
message2 = f"Age: {age}"       # 更推荐的格式化
```

Python 不会自动把 `int` 拼接成 `str`。

## 小题 2：List Comprehension

```python
squares_of_even = [x * x for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]
```

## 小题 3：线程、进程与 async

- **线程**：I/O-bound 任务常可受益于并发执行。
- **进程**：在传统 CPython GIL 条件下，CPU-bound 纯 Python 并行计算通常考虑多进程。
- **asyncio**：适合大量可等待的异步 I/O；不是自动的 CPU 并行计算方案。
- 具体行为与 Python 实现、版本及 free-threaded 配置有关，面试时要说明前提。

## 代码模板

见 [data-structures.md](data-structures.md) 和 [../code/examples.py](../code/examples.py)。

## 待补充
按“概念 → 面试问题 → 最小示例 → 复杂度 / 陷阱 → 复习状态”的格式持续增补。

# Python 常规面试（General Python Interview）

> **唯一维护文件**：涵盖 Python 语言特性、常见 Karat screening 考点、Python 与 Java/Kotlin 的区别。数据结构与算法题归入 [data-structures.md](data-structures.md)。

## 复习清单

- [ ] 基础类型、显式转换、Truthiness、`None`
- [ ] List/Dict/Set/Tuple、Comprehension、切片与排序
- [ ] `==` / `is`、hashable、mutable / immutable
- [ ] 函数参数、`*args`、`**kwargs`、mutable default argument
- [ ] 作用域、闭包、Decorator
- [ ] Iterator / Iterable / Generator (`yield`)
- [ ] Exceptions、`try/except/else/finally`、`with` context manager
- [ ] GIL、threading、multiprocessing、asyncio、I/O-bound vs CPU-bound
- [ ] OOP、`dataclass`、类型注解、运行时动态类型

## 典型 Karat 快问快答

### 1. 字符串与数字拼接

```python
age = 36
# "Age: " + age  # TypeError
message = "Age: " + str(age)
message2 = f"Age: {age}"
```

**考点**：Python 不会为字符串拼接隐式转换 `int`。Java/Kotlin 的字符串拼接直觉不能直接套到 Python。

### 2. List Comprehension

```python
squares_of_even = [x * x for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]
```

**考点**：先遍历 `range(10)`，筛选偶数，再映射为平方。

### 3. `==` vs `is`

```python
a = [1, 2]
b = [1, 2]
assert a == b
assert a is not b
```

**考点**：`==` 判断值相等；`is` 判断对象标识是否相同。判断 `None` 使用 `is None`。

### 4. Mutable default argument

```python
def add_item(value, items=None):
    if items is None:
        items = []
    items.append(value)
    return items
```

**考点**：默认参数在函数定义时求值；共享的可变默认对象可导致意外状态泄漏。

### 5. GIL / Thread / Process / Async

| 模式 | 常见用途 | 面试表述 |
| --- | --- | --- |
| `threading` | Blocking I/O | 线程可在等待 I/O 时并发处理其他工作 |
| `multiprocessing` | CPU 密集型计算 | 独立进程可利用多个 CPU 核心，代价是进程间通信 |
| `asyncio` | 大量异步 I/O | 单线程也可通过 `await` 合作式调度，不能自动并行 CPU 运算 |

**版本注意**：GIL 结论需说明 CPython 版本及是否启用 free-threaded Python。

## 后续统一补充模板

新考点采用：**概念 → 最小运行示例 → 输出和原因 → 陷阱 → Java/Kotlin 类比 → 面试追问**。

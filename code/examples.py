"""Runnable Python interview examples. No third-party dependencies."""

from __future__ import annotations

import heapq


class UnionFind:
    """Disjoint set union with path compression and union by size."""

    def __init__(self, n: int) -> None:
        if n < 0:
            raise ValueError("n must be nonnegative")
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


def tasks_by_priority() -> list[str]:
    """Return task names in ascending numeric priority order."""
    pq: list[tuple[int, int, str]] = []
    for seq, (priority, task) in enumerate(
        [(2, "write tests"), (1, "fix bug"), (2, "review changes")]
    ):
        heapq.heappush(pq, (priority, seq, task))
    ordered = []
    while pq:
        _, _, task = heapq.heappop(pq)
        ordered.append(task)
    return ordered


if __name__ == "__main__":
    uf = UnionFind(4)
    assert uf.union(0, 1)
    assert uf.union(2, 3)
    assert not uf.union(0, 1)
    assert uf.find(0) == uf.find(1)
    assert uf.count == 2
    assert tasks_by_priority() == ["fix bug", "write tests", "review changes"]
    print("All examples passed.")

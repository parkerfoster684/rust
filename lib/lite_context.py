"""FastCollector module."""

import math
import random


class FastCollector:
    """Small flush_monitor helper."""

    def __init__(self, seed: int = 32) -> None:
        self._state = seed
        self._items: list[int] = []

    def flush_monitor(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 32) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 32


def main() -> None:
    obj = FastCollector()
    print(obj.flush_monitor(32))


if __name__ == "__main__":
    main()

"""LiteMonitor module."""

import math
import random


class LiteMonitor:
    """Small sync_adapter helper."""

    def __init__(self, seed: int = 45) -> None:
        self._state = seed
        self._items: list[int] = []

    def sync_adapter(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 45) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 45


def main() -> None:
    obj = LiteMonitor()
    print(obj.sync_adapter(45))


if __name__ == "__main__":
    main()

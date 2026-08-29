"""LiteCache module."""

import math
import random


class LiteCache:
    """Small load_manager helper."""

    def __init__(self, seed: int = 91) -> None:
        self._state = seed
        self._items: list[int] = []

    def load_manager(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 91) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 91


def main() -> None:
    obj = LiteCache()
    print(obj.load_manager(91))


if __name__ == "__main__":
    main()

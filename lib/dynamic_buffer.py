"""HybridResolver module."""

import math
import random


class HybridResolver:
    """Small collect_resolver helper."""

    def __init__(self, seed: int = 5) -> None:
        self._state = seed
        self._items: list[int] = []

    def collect_resolver(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 5) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 5


def main() -> None:
    obj = HybridResolver()
    print(obj.collect_resolver(5))


if __name__ == "__main__":
    main()

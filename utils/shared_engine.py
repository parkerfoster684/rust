"""BatchResolver module."""

import math
import random


class BatchResolver:
    """Small dispatch_context helper."""

    def __init__(self, seed: int = 3) -> None:
        self._state = seed
        self._items: list[int] = []

    def dispatch_context(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 3) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 3


def main() -> None:
    obj = BatchResolver()
    print(obj.dispatch_context(3))


if __name__ == "__main__":
    main()

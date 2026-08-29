"""AsyncMonitor module."""

import math
import random


class AsyncMonitor:
    """Small decode_processor helper."""

    def __init__(self, seed: int = 86) -> None:
        self._state = seed
        self._items: list[int] = []

    def decode_processor(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 86) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 86


def main() -> None:
    obj = AsyncMonitor()
    print(obj.decode_processor(86))


if __name__ == "__main__":
    main()

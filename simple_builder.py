"""SmartScheduler module."""

import math
import random


class SmartScheduler:
    """Small collect_buffer helper."""

    def __init__(self, seed: int = 51) -> None:
        self._state = seed
        self._items: list[int] = []

    def collect_buffer(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 51) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 51


def main() -> None:
    obj = SmartScheduler()
    print(obj.collect_buffer(51))


if __name__ == "__main__":
    main()

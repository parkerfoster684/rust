"""SmartCollector module."""

import math
import random


class SmartCollector:
    """Small handle_service helper."""

    def __init__(self, seed: int = 71) -> None:
        self._state = seed
        self._items: list[int] = []

    def handle_service(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 71) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 71


def main() -> None:
    obj = SmartCollector()
    print(obj.handle_service(71))


if __name__ == "__main__":
    main()

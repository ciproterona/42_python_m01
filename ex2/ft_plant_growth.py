#!/usr/bin/env python3

from __future__ import annotations


class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float = 0.8,
    ) -> None:
        self.name = name
        self.height = height
        self._age = age
        self.growth_rate = growth_rate

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self._age} days old")


def main() -> None:
    plant = Plant("Rose", 25.0, 30)
    initial_height = plant.height

    print("=== Garden Plant Growth ===")
    plant.show()
    for day in range(1, 8):
        plant.grow()
        plant.age()
        print(f"=== Day {day} ===")
        plant.show()
    print(f"Growth this week: {round(plant.height - initial_height, 1):.1f}cm")


if __name__ == "__main__":
    main()

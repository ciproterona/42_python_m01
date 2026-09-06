#!/usr/bin/env python3

from __future__ import annotations


class Plant:
    class _Stats:
        def __init__(self) -> None:
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self) -> str:
            return (
                f"Stats: {self.grow_calls} grow, {self.age_calls} age, "
                f"{self.show_calls} show"
            )

        def extra_display(self) -> str:
            return ""

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float = 0.8,
    ) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._growth_rate = growth_rate
        self._stats = self._Stats()

    def grow(self) -> None:
        self._height += self._growth_rate
        self._stats.grow_calls += 1

    def age(self, days: int = 1) -> None:
        self._age += days
        self._stats.age_calls += 1

    def show(self) -> None:
        self._stats.show_calls += 1
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    @staticmethod
    def is_more_than_year(age_days: int) -> bool:
        return age_days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age, 0.8)
        self.color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    class _Stats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self.shade_calls = 0

        def extra_display(self) -> str:
            return f"{self.shade_calls} shade"

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, age, 0.0)
        self.trunk_diameter = trunk_diameter
        self._stats = self._Stats()

    def produce_shade(self) -> None:
        self._stats.shade_calls += 1
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height:.1f}cm long and {self.trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant._name}]")
    print(plant._stats.display())
    extra = plant._stats.extra_display()
    if extra:
        print(extra)


def main() -> None:
    flower = Flower("Rose", 15.0, 10, "red")
    tree = Tree("Oak", 200.0, 365, 5.0)
    seed = Seed("Sunflower", 80.0, 45, "yellow")
    anonymous = Plant.create_anonymous()

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(
        f"Is 30 days more than a year? -> {Plant.is_more_than_year(30)}"
    )
    print(
        f"Is 400 days more than a year? -> {Plant.is_more_than_year(400)}"
    )

    print("=== Flower")
    flower.show()
    display_statistics(flower)
    print("[asking the rose to grow and bloom]")
    flower.grow()
    flower.bloom()
    flower.show()
    display_statistics(flower)

    print("=== Tree")
    tree.show()
    display_statistics(tree)
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    display_statistics(tree)

    print("=== Seed")
    seed.show()
    print("[make sunflower grow, age and bloom]")
    seed.grow()
    seed.age(20)
    seed.bloom()
    seed.show()
    display_statistics(seed)

    print("=== Anonymous")
    anonymous.show()
    display_statistics(anonymous)


if __name__ == "__main__":
    main()

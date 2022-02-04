from dataclasses import dataclass


@dataclass
class AARectXYWHInt:
    x: int
    y: int
    w: int
    h: int

    def area(self) -> int:
        return self.h * self.w

"""Cosmic Path Optimization solution
"""

from typing import List

def average(planet_count: int, temps: List[int]) -> int:
    average = 0
    total = 0
    for planet in temps:
        total = total + planet
    average = total / planet_count
    return int(average)

def main() -> None:
    planet_count = int(input())
    temps = list(map(int, input().split()))
    print(average(planet_count, temps))

if __name__ == "__main__":
    main()
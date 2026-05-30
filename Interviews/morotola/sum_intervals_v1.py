"""
Esta foi uma das questões para entrevista do novo estagiário 30/05/2026

Task:
Write a function called sum_intervals() that accepts an array of intervals,
and returns the sum of all the interval lengths. Overlapping intervals
should only be counted once.

Intervals:
Intervals are represented by a pair of integers in the form of an array.
The first value of the interval will always be less than the second value.
Example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

Overlapping Intervals:
See a list containing overlapping intervals:
[
  [1, 4],
  [7, 10],
  [3, 5]
]
The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5]
overlap, the combined interval becomes [1, 5] with a length of 4.

Examples:
Input:
- [[1, 4], [7, 10], [3, 5]]  -> Output: 7
- [[1, 2], [6, 10], [11, 15]] -> Output: 9
- [[-1, 1], [2, 8], [3, 10]]   -> Output: 10

"""


def sum_intervals(intervals: list[list[int]]):
    seen = set()
    for interval in intervals:
        start, end = interval[0], interval[1]
        for num in range(start, end):
            if num not in seen:
                seen.add(num)

    return len(seen)


assert sum_intervals([[1, 4], [7, 10], [3, 5]]) == 7
assert sum_intervals([[1, 2], [6, 10], [11, 15]]) == 9
assert sum_intervals([[-1, 1], [2, 8], [3, 10]]) == 10

print("All tests passed")

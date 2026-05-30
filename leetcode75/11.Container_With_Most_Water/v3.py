"""

11. Container With Most Water
You are given an integer array height of length n. 
There are n vertical lines drawn such that 
-> the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

"""

def container_with_most_water(heights: list[int]):
    left = 0
    right = len(heights) - 1
    max_area = 0

    while left < right:
        area = min(heights[right], heights[left]) * (right - left)
        max_area = max(max_area, area)

        if left > right:
            right -= 1
        else:
            left += 1

    return max_area

assert (result := container_with_most_water([1,8,6,2,5,4,8,3,7])) == 49, f"Expected 49, got {result}"

print("All tests passed")
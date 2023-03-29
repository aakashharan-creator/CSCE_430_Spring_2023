from sys import stdin
from bisect import bisect_right

n, k = list(map(int, stdin.readline().split()))
cars = list(map(int, stdin.readline().split()))

left = sorted([-car for car in cars if car < 0])
right = sorted([car for car in cars if car > 0])

curr_time = 0
left_index = 0
right_index = 0
MAX_TIME = 1000000 + k
while left_index < len(left) or right_index < len(right):
    left_car = MAX_TIME if left_index >= len(left) else left[left_index]
    right_car = MAX_TIME if right_index >= len(right) else right[right_index]

    left_time = left_car - curr_time
    right_time = right_car - curr_time

    if left_time >= k and right_time >= k:
        print("YES")
        break

    curr_time = min(left_car, right_car)

    left_index = bisect_right(left, curr_time)
    right_index = bisect_right(right, curr_time)

else:
    print("IMPOSSIBLE")

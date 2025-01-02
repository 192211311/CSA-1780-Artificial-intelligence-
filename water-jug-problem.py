from collections import deque
def water_jug_problem(jug1, jug2, target):
    visited = set()
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if x == target or y == target:
            return True
        queue.extend([
            (jug1, y),
            (x, jug2),
            (0, y),
            (x, 0),
            (max(0, x + y - jug2), min(jug2, x + y)),
            (min(jug1, x + y), max(0, x + y - jug1))
        ])
    return False
jug1_capacity = int(input("enter jug1 capacity:"))
jug2_capacity = int(input("enter jug2 capacity:"))
target_amount = int(input("enter goal"))
if water_jug_problem(jug1_capacity, jug2_capacity, target_amount):
    print(f"Yes, it is possible to measure {target_amount} liters.")
else:
    print(f"No, it is not possible to measure {target_amount} liters.")

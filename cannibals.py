from collections import deque

def is_valid(state):
    m, c, boat = state
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and m < c:  # Missionaries can't be outnumbered on one side
        return False
    if (3 - m) > 0 and (3 - m) < (3 - c):  # Same for the other side
        return False
    return True

def missionaries_and_cannibals():
    start = (3, 3, 1)  # (Missionaries, Cannibals, Boat)
    goal = (0, 0, 0)
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (m, c, boat), path = queue.popleft()
        if (m, c, boat) == goal:
            return path + [goal]
        if (m, c, boat) in visited:
            continue
        visited.add((m, c, boat))

        moves = [(-1, 0), (0, -1), (-2, 0), (0, -2), (-1, -1)]
        for dm, dc in moves:
            new_state = (m + dm * boat, c + dc * boat, 1 - boat)
            if is_valid(new_state):
                queue.append((new_state, path + [(m, c, boat)]))

    return None

solution = missionaries_and_cannibals()
if solution:
    print("Solution steps:")
    for step in solution:
        print(step)
else:
    print("No solution found.")

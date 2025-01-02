def vacuum_cleaner_problem(room, start):
    def all_clean(room):
        return all(all(cell == 0 for cell in row) for row in room)

    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    path = []
    x, y = start

    while not all_clean(room):
        if room[x][y] == 1:  # Clean the current cell
            room[x][y] = 0
            path.append((x, y, "Clean"))

        for dx, dy in moves:  # Try all directions
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(room) and 0 <= ny < len(room[0]) and room[nx][ny] == 1:
                x, y = nx, ny
                path.append((x, y, "Move"))
                break
        else:  # No dirty cell found, just move sequentially
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(room) and 0 <= ny < len(room[0]):
                    x, y = nx, ny
                    path.append((x, y, "Move"))
                    break

    return path

room = [
    [1, 0, 1],
    [1, 1, 0],
    [0, 1, 1]
]
start_position = (0, 0)

solution = vacuum_cleaner_problem(room, start_position)
print("Cleaning path:")
for step in solution:
    print(step)

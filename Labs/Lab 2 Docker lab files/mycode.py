# Solve maze BFS

import random
import time
from collections import deque

def initialize_grid(size, obstacle_count):
    grid = [['*' for _ in range(size)] for _ in range(size)]
    # Place obstacles
    for _ in range(obstacle_count):
        x, y = random.randint(0, size-1), random.randint(0, size-1)
        grid[x][y] = 'O'
    return grid

def print_grid(grid):
    for row in grid:
        print(' '.join(row))
    print()

def bfs(grid, start):
    queue = deque([start])
    visited = set([tuple(start)])

    while queue:
        position = queue.popleft()
        if grid[position[0]][position[1]] == '*':  # Only update if it's water
            grid[position[0]][position[1]] = '#'
        print_grid(grid)
        time.sleep(0.5)  # Pause for visibility

        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Right, Down, Left, Up
            new_row, new_col = position[0] + direction[0], position[1] + direction[1]
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] != 'O' and (new_row, new_col) not in visited:
                queue.append((new_row, new_col))
                visited.add((new_row, new_col))

def main():
    size = 5
    obstacle_count = 5  # Number of obstacles
    grid = initialize_grid(size, obstacle_count)
    bfs(grid, [0, 0])  # Start BFS from top-left corner

if __name__ == '__main__':
    main()


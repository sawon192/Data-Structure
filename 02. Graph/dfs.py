import os
import json

os.chdir(r"E:\Riadul sir")
with open("maze.txt", "r") as f:
    maze = [list(line.strip()) for line in f]

start = None
goal = None

for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == "S":
            start = (i, j)
        if maze[i][j] == "G":
            goal = (i, j)

if start is None or goal is None:
    print("Start or Goal not found!")
    exit()

# DFS uses stack
stack = [start]
visited = [start]
parent = {start: None}

# 4 possible directions (up, down, left, right)
directions = [(-1,0), (1,0), (0,-1), (0,1)]

found = False

while stack:
    current = stack.pop()   # LIFO (last in, first out)

    if current == goal:
        found = True
        break

    for d in directions:
        nr = current[0] + d[0]
        nc = current[1] + d[1]

        if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]):
            if maze[nr][nc] != "#" and (nr, nc) not in visited:
                stack.append((nr, nc))
                visited.append((nr, nc))
                parent[(nr, nc)] = current
if found:
    cur = goal
    while cur != start:
        if maze[cur[0]][cur[1]] not in ("S", "G"):
            maze[cur[0]][cur[1]] = "*"
        cur = parent[cur]
else:
    print("No path found")

for row in maze:
    print("".join(row))

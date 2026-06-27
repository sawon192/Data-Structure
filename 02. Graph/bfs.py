import os

os.chdir(r"E:\Riadul sir")

with open("maze.txt", "r") as f:
    maze = [list(line.strip()) for line in f]

start = None
goal = None

# Find Start and Goal
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == "S":
            start = (i, j)
        if maze[i][j] == "G":
            goal = (i, j)

if start is None or goal is None:
    print("Start or Goal not found!")
    exit()

# BFS uses Queue
queue = [start]
visited = [start]
parent = {start: None}

# Up, Down, Left, Right
directions = [(-1,0), (1,0), (0,-1), (0,1)]

found = False

while queue:
    current = queue.pop(0)      # FIFO

    if current == goal:
        found = True
        break

    for d in directions:
        nr = current[0] + d[0]
        nc = current[1] + d[1]

        if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]):
            if maze[nr][nc] != "#" and (nr, nc) not in visited:
                queue.append((nr, nc))
                visited.append((nr, nc))
                parent[(nr, nc)] = current

# Mark shortest path
if found:
    cur = goal

    while cur != start:
        if maze[cur[0]][cur[1]] != "S" and maze[cur[0]][cur[1]] != "G":
            maze[cur[0]][cur[1]] = "*"
        cur = parent[cur]

    print("Path Found!\n")

else:
    print("No Path Found!\n")

# Print Maze
for row in maze:
    print("".join(row))
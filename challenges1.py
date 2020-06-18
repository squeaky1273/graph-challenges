from collections import deque

def timeToRot(self, grid):
    """
    Take in a grid of numbers, where 0 is an empty space, 1 is a fresh orange, and 2 is a rotten
    orange. Each minute, a rotten orange contaminates its 4-directional neighbors. Return the number
    of minutes until all oranges rot.
    """
    pass
    # rows = len(grid)
    # cols = len(grid[0])
    # # psuedocode:
    # # init queue
    # queue = list()
    # visited = set()
    # # STEP 1: find the first rotten orange
    #     # iterate over each element
    #         # if none found --> return -1
    #         # if it is found
    # for x, row in enumerate(grid):
    #     for y, col in enumerate(row):
    #         if grid[x][y] == 2:
    #             queue.append((x, y))
    # if len(queue) == 0:
    #     return None
    # # STEP 2: perform BFS
    # # init minutes count, to increment during BFS
    # minutes = 0
    # # while the queue is not empty, then ...
    # while len(queue) > 0:
    #     # dequeue from the enqueue
    #     x, y = queue.pop(0)
    #     orange = grid[x][y]
    #     # "visit" -- if the orange is fresh (2), then make it rotten
    #     if orange == 1:
    #         grid[x][y] = 2
    #     visited.add(orange)
    #     # calculate (x, y)'s of potential neighbors
    #     potentials = [
    #         (x, y - 1),
    #         (x, y + 1),
    #         (x - 1, y),
    #         (x + 2, y)
    #     ]
    #     # check if the potential is a fresh orange
    #     for potential in potentials:
    #         try:
    #             x, y = potential
    #             potentail_orange = grid[x][y]
    #             # if the potential = 1, then enqueue them
    #             if potentail_orange == 1:
    #                 queue.append(potential)
    #         except IndexError:
    #             break
    #     # increment minutes
    #     minutes += 1
    # # STEP 3: return minutes
    # return minutes


# Test Cases
oranges1 = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]
assert timeToRot(oranges1) == 4

oranges2 = [
    [2,1,1],
    [0,1,1],
    [1,0,1]
]
assert timeToRot(oranges2) == -1

oranges3 = [
    [0,2]
]
assert timeToRot(oranges3) == 0

    # queue = deque()

    # time = 0
    # rows = len(grid)
    # cols = len(grid[0])

    # for row in range(rows):
    #     for col in range(cols):
    #         if grid[row][col] == 2:
    #             queue.append((row, col, 0))
    # while queue:
    #     (row, col, time) = queue.popleft()

    #     if row > 0 and grid[row - 1][col] == 1:
    #         grid[row - 1][col] == 2
    #         queue.append((row - 1, col, time + 1))

    #     if row > 0 and grid[row - 1][col] == 1:
    #         grid[row - 1][col] == 2
    #         queue.append((row - 1, col, time + 1))

    #     if col > 0 and grid[row][col - 1] == 1:
    #         grid[row - 1][col] == 2
    #         queue.append((row - 1, col, time + 1))

    #     if col < cols - 1 and grid[row][col + 1] == 1:
    #         grid[row][col + 1] == 2
    #         queue.append((row, col + 1, time + 1))
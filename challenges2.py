def numIslands(grid):
    """Take in a grid of 1s (land) and 0s (water) and return the number of islands."""
    pass

# Test Cases
map1 = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
assert numIslands(map1) == 1

map2 = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
]
assert numIslands(map2) == 3

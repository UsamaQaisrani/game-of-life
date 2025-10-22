class Node:
    def __init__(self, level, val=0,  nw=None, ne=None, sw=None, se=None) -> None:
        self.nw = nw
        self.ne = ne
        self.sw = sw
        self.se = se
        self.val = val
        self.level = level

def built_tree(grid):
    next_level = []
    n = len(grid)
    for i in range(n):
        row = []
        for j in range(n):
            cell = grid[i][j]
            node = Node(0, cell)
            row.append(node)
        next_level.append(row)

    level = 0
    while n > 0:
        n = n // 2
        level_array = []
        for y in range(0, len(next_level), 2):
            parent_row = []
            for x in range(0, len(next_level), 2):
                nw = next_level[y][x]
                ne = next_level[y][x+1]
                sw = next_level[y+1][x]
                se = next_level[y+1][x+1]

                node = Node(level+1, nw, ne, sw, se)
                parent_row.append(node)
            level_array.append(parent_row)

        next_level = level_array
        level += 1

    root = next_level[0][0]
    return root
 

from board import *

def main():
    board = Board()
    board.setup()

def evolve(grid):
    evolved = [[0 for _ in row] for row in grid]
    ROWS, COLS = len(grid), len(grid[0])
    directions = [
        [-1,0], [1,0], [0,1], [0,-1],
        [1,1], [-1,-1], [-1,1], [1,-1]
    ]

    def valid_index(r, c):
        return 0 <= r < ROWS and 0 <= c < COLS

    for r in range(ROWS):
        for c in range(COLS):
            n_count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if valid_index(nr, nc) and grid[nr][nc] == 1:
                    n_count += 1

            cell_val = grid[r][c]
            if cell_val == 1:
                if n_count < 2 or n_count > 3:
                    evolved[r][c] = 0
                else:
                    evolved[r][c] = 1
            else:
                if n_count == 3:
                    evolved[r][c] = 1

    return evolved
                        



if __name__ == "__main__":
    main()

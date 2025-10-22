class Pattern:
    def __init__(self) -> None:
        pass

    def setup(self):
        grid = [[0 for _ in range(80)] for _ in range(80)]
        gliders = [
            (2, 25), (3, 26), (4, 24), (4, 25), (4, 26),
            (20, 55), (21, 56), (22, 54), (22, 55), (22, 56),
            (50, 10), (51, 11), (52, 9), (52, 10), (52, 11)
        ]
        blinkers = [
            (10, 10), (11, 10), (12, 10),
            (60, 60), (60, 61), (60, 62)
        ]
        blocks = [
            (30, 30), (30, 31), (31, 30), (31, 31),
            (70, 20), (70, 21), (71, 20), (71, 21)
        ]

        for r, c in gliders + blinkers + blocks:
            grid[r][c] = 1

        return grid


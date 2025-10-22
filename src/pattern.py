class Pattern:
    def __init__(self) -> None:
        pass

    def setup(self):
        return self.pattern4()

    def pattern1(self):
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


    def pattern2(self):
        grid = [[0 for _ in range(80)] for _ in range(80)]

        def set_pattern(cells):
            for r, c in cells:
                if 0 <= r < 80 and 0 <= c < 80:
                    grid[r][c] = 1

        gun = [
            (5,1),(5,2),(6,1),(6,2),
            (5,11),(6,11),(7,11),(4,12),(8,12),(3,13),(9,13),(3,14),(9,14),
            (6,15),(4,16),(8,16),(5,17),(6,17),(7,17),(6,18),
            (3,21),(4,21),(5,21),(3,22),(4,22),(5,22),(2,23),(6,23),
            (1,25),(2,25),(6,25),(7,25),
            (3,35),(4,35),(3,36),(4,36)
        ]
        set_pattern(gun)

        gliders = [
            (40, 10), (41, 11), (42, 9), (42, 10), (42, 11),
            (60, 60), (61, 61), (62, 59), (62, 60), (62, 61)
        ]
        set_pattern(gliders)

        lwss = [
            (20,50),(20,53),(21,54),(22,50),(22,54),(23,51),(23,52),(23,53),(23,54)
        ]
        set_pattern(lwss)

        blinkers = [
            (10,30),(11,30),(12,30),
            (50,20),(50,21),(50,22)
        ]
        set_pattern(blinkers)

        blocks = [
            (70,10),(70,11),(71,10),(71,11),
            (75,70),(75,71),(76,70),(76,71)
        ]
        set_pattern(blocks)

        return grid



    def pattern3(self):
        grid = [[0 for _ in range(80)] for _ in range(80)]

        def set_pattern(cells):
            for r, c in cells:
                if 0 <= r < 80 and 0 <= c < 80:
                    grid[r][c] = 1

        gun = [
            (5,1),(5,2),(6,1),(6,2),
            (5,11),(6,11),(7,11),(4,12),(8,12),(3,13),(9,13),(3,14),(9,14),
            (6,15),(4,16),(8,16),(5,17),(6,17),(7,17),(6,18),
            (3,21),(4,21),(5,21),(3,22),(4,22),(5,22),(2,23),(6,23),
            (1,25),(2,25),(6,25),(7,25),
            (3,35),(4,35),(3,36),(4,36)
        ]
        set_pattern(gun)

        center_cluster = []
        for r in range(35, 45):
            for c in range(35, 45):
                if (r + c) % 2 == 0 or (r * c) % 7 == 0:
                    center_cluster.append((r, c))
        set_pattern(center_cluster)

        blinkers = [
            (33, 40), (34, 40), (35, 40),
            (45, 38), (45, 39), (45, 40),
            (38, 33), (39, 33), (40, 33),
            (40, 45), (41, 45), (42, 45)
        ]
        set_pattern(blinkers)

        spaceships = [
             
            (10,70),(11,73),(12,69),(12,70),(12,71),(12,72),(12,73),
             
            (70,10),(71,13),(72,9),(72,10),(72,11),(72,12),(72,13),
             
            (5,38),(5,39),(5,40),(5,41),(6,39),(7,40),(8,38),(8,39),(8,40),(8,41)
        ]
        set_pattern(spaceships)

         
        gliders = [
            (10,10), (11,11), (12,9), (12,10), (12,11),
            (65,60), (66,61), (67,59), (67,60), (67,61),
            (60,20), (61,21), (62,19), (62,20), (62,21),
            (20,60), (21,61), (22,59), (22,60), (22,61)
        ]
        set_pattern(gliders)

         
        blocks = [
            (15,15),(15,16),(16,15),(16,16),
            (63,63),(63,64),(64,63),(64,64)
        ]
        set_pattern(blocks)

        return grid

    def pattern4(self):
        grid = [[0 for _ in range(80)] for _ in range(80)]

        def set_pattern(cells):
            for r, c in cells:
                if 0 <= r < 80 and 0 <= c < 80:
                    grid[r][c] = 1

        center_r, center_c = 40, 40   

         
        gun = [
            (center_r-5, center_c-10),(center_r-5, center_c-9),
            (center_r-4, center_c-10),(center_r-4, center_c-9),

            (center_r-5, center_c+1),(center_r-4, center_c+1),(center_r-3, center_c+1),
            (center_r-6, center_c+2),(center_r-2, center_c+2),
            (center_r-7, center_c+3),(center_r-1, center_c+3),
            (center_r-7, center_c+4),(center_r-1, center_c+4),
            (center_r-4, center_c+5),
            (center_r-6, center_c+6),(center_r-2, center_c+6),
            (center_r-5, center_c+7),(center_r-4, center_c+7),(center_r-3, center_c+7),
            (center_r-4, center_c+8)
        ]
        set_pattern(gun)

         
        blinkers = [
             
            (center_r-10, center_c),(center_r-9, center_c),(center_r-8, center_c),
             
            (center_r+8, center_c),(center_r+9, center_c),(center_r+10, center_c),
             
            (center_r, center_c-10),(center_r, center_c-9),(center_r, center_c-8),
             
            (center_r, center_c+8),(center_r, center_c+9),(center_r, center_c+10)
        ]
        set_pattern(blinkers)

         
        gliders = [
             
            (center_r-15, center_c-15),(center_r-14, center_c-14),(center_r-13, center_c-16),
            (center_r-13, center_c-15),(center_r-13, center_c-14),
             
            (center_r+13, center_c+13),(center_r+14, center_c+12),(center_r+15, center_c+14),
            (center_r+15, center_c+13),(center_r+15, center_c+12),
             
            (center_r+13, center_c-15),(center_r+14, center_c-14),(center_r+15, center_c-16),
            (center_r+15, center_c-15),(center_r+15, center_c-14),
             
            (center_r-15, center_c+15),(center_r-14, center_c+16),(center_r-13, center_c+14),
            (center_r-13, center_c+15),(center_r-13, center_c+16)
        ]
        set_pattern(gliders)

         
        blocks = [
            (center_r-2, center_c-2),(center_r-2, center_c-1),
            (center_r-1, center_c-2),(center_r-1, center_c-1),

            (center_r+1, center_c+1),(center_r+1, center_c+2),
            (center_r+2, center_c+1),(center_r+2, center_c+2)
        ]
        set_pattern(blocks)

        return grid


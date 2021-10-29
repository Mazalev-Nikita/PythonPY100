EMPTY_CELL = "-"

def get_first_player()


def init_field(size = 3)
    field = [
        [empty_cell for _ in range(size)]
        for _ in range(size)
    ]

    return field


def is_win(field) -> bool:
    win_combinations = [
        [(1, 1), (1, 2), (1, 3)],
        [(2, 1), (2, 2), (2, 3)],
        [(3, 1), (3, 2), (3, 3)],

        [(1, 1), (2, 1), (3, 1)],
        [(1, 2), (2, 2), (3, 2)],
        [(1, 3), (2, 3), (3, 3)],

        [(1, 1), (2, 2), (3, 3)],
        [(1, 3), (2, 2), (3, 1)],
    ]
    for win_comb in win_combinations:
        cell_1 = field[win_comb[0][0]][win_comb[0][1]]
        cell_2 = field[win_comb[1][0]][win_comb[1][1]]
        cell_3 = field[win_comb[2][0]][win_comb[2][1]]

def get_cell(field, row_index: int, col_index: )

def is_availiable_cell(field) -> bool
    for row in field:
        for cell in row
            if cell == EMPTY_CELL:
                return True
    return False

def is_empty_cell(field: list, x: int, y: int) -> bool
   cell = field[x][y]
   return True if cell == EMPTY_CELL else False

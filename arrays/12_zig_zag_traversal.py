def zig_zag_traverse(arr):
    h = len(arr) - 1
    w = len(arr[0]) - 1
    res = []
    row, col = 0, 0
    going_down = True
    while not is_out_of_bounds(row, col, h, w):
        res.append(arr[row][col])
        if going_down:
            if col == 0 or row == h:
                going_down = False
                if row == h:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == w:
                going_down = True
                if col == w:
                    row += 1
                else:
                    col += 1

            else:
                row -= 1
                col += 1
        return res


def is_out_of_bounds(row, col, h, w):
    return row < 0 or row > h or col < 0 or col > w

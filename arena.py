from random import choice


def arena(snake_head=None, snake_body=None, food=None):
    board = [
        ["#"] * 27,
        ["#"] + [" "] * 25 + ["#"],
        ["#"] + [" "] * 25 + ["#"],
        ["#"] + [" "] * 25 + ["#"],
        ["#"] + [" "] * 25 + ["#"],
        ["#"] + [" "] * 25 + ["#"],
        ["#"] + [" "] * 25 + ["#"],
        ["#"] + [" "] * 25 + ["#"],
        ["#"] + [" "] * 25 + ["#"],
        ["#"] + [" "] * 25 + ["#"],
        ["#"] + [" "] * 25 + ["#"],
        ["#"] + [" "] * 25 + ["#"],
        ["#"] + [" "] * 25 + ["#"],
        ["#"] + [" "] * 25 + ["#"],
        ["#"] + [" "] * 25 + ["#"],
        ["#"] + [" "] * 25 + ["#"],
        ["#"] + [" "] * 25 + ["#"],
        ["#"] + [" "] * 25 + ["#"],
        ["#"] + [" "] * 25 + ["#"],
        ["#"] + [" "] * 25 + ["#"],
        ["#"] + [" "] * 25 + ["#"],
        ["#"] + [" "] * 25 + ["#"],
        ["#"] + [" "] * 25 + ["#"],
        ["#"] + [" "] * 25 + ["#"],
        ["#"] + [" "] * 25 + ["#"],
        ["#"] + [" "] * 25 + ["#"],
        ["#"] * 27
    ]

    if snake_head is not None and snake_body is not None:
        row, column = snake_head
        board[row][column] = "π"

        for row, column in snake_body:
            board[row][column] = "π"

    if food is not None:
        board[food[0]][food[1]] = choice(["t", "h", "o", "n"])

    return board


def printing(board):
    display = ""
    for row in board:
        line = ""
        for column in row:
            line += column + " "
        display += line + "\n"
    return display

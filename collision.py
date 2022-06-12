def collision(snake_head):
    vertical_pos, horizontal_pos = snake_head
    if vertical_pos == 0 or vertical_pos == 27:
        return True
    elif horizontal_pos == 0 or horizontal_pos == 27:
        return True
    else:
        return False
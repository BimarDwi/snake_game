def collision(head, body):
    vertical_pos, horizontal_pos = head
    if vertical_pos == 0 or vertical_pos == 27:
        return True
    elif horizontal_pos == 0 or horizontal_pos == 27:
        return True
    elif head in body:
        return True
    else:
        return False
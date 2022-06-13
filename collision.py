def collision(head, body):
    # vertical_pos, horizontal_pos = head
    # if vertical_pos == 0 or vertical_pos == 26:
    #     return True
    # elif horizontal_pos == 0 or horizontal_pos == 26:
    #     return True
    if head in body:
        return True
    else:
        return False

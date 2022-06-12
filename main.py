from snake import Snake
from arena import *
from clear import clear
from collision import collision
import time

snake = Snake()

while True:
    snake.direction()
    snake.move()
    if collision(snake.head_before, snake.body_before) is True:
        break
    board = arena(snake.head_before, snake.body_before)
    print(printing(board))
    time.sleep(1/15)
    clear()
    print(f"fps = {1/(time.time()-start)}")

print("mati nabrak dinding aot")

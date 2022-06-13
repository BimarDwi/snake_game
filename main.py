from snake import Snake
from arena import *
from clear import clear
from food import Food
from collision import collision
from random import randint
from time import time, sleep

snake = Snake()
apple = Food([randint(1, 25), randint(1, 25)])
board = arena(snake.head_before, snake.body_before, apple.position)
score = 0

while True:
    start = time()
    snake.direction()
    snake.move()

    if snake.head_before == apple.position:
        snake.add_length()
        apple.new_position()
        score += 1

    if collision(snake.head_before, snake.body_before):
        for i in range(4, 1, -1):
            print(f"score = {score}")
            print(printing(board))
            print(f"Exit in ...{i-1}")
            sleep(1)
            clear()
        break

    board = arena(snake.head_before, snake.body_before, apple.position)
    print(printing(board))
    sleep(1/15)
    clear()
    print(f"fps = {1/(time()-start)}\nscore = {score}")

from snake import Snake
import arena

# snake = Snake()
# for i in range(10):
#     print(snake.head, snake.body_before)
#     board = arena.arena(snake.head, snake.body_before)
#     print(arena.printing(board))
#     snake.direction()
#     snake.snake_move()

snake = Snake()
for i in range(100):
    print(snake.head_before, snake.body_before)
    snake.direction()
    snake.snake_move()
    print(snake.head_before, snake.body_before)

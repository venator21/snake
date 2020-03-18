import app
import snake
import apple

app = app.App()
snake = snake.Snake()
apple = apple.Apple()


if __name__ == "__main__":
	app.play(snake, apple)
	

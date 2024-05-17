import pygame
import random

# 定義顏色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 定義遊戲視窗的大小
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# 定義貪吃蛇的尺寸
SNAKE_SIZE = 20

# 初始化 Pygame
pygame.init()

# 設置遊戲視窗大小
window_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("貪吃蛇遊戲")

clock = pygame.time.Clock()

# 貪吃蛇類別
class Snake:
    def __init__(self):
        self.size = SNAKE_SIZE
        self.x = WINDOW_WIDTH // 2
        self.y = WINDOW_HEIGHT // 2
        self.dx = self.size
        self.dy = 0
        self.body = []
        self.length = 1
        self.score = 0

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], self.size, self.size))

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # 檢查是否吃到食物
        if self.x == food.x and self.y == food.y:
            self.length += 1
            self.score += 10
            food.spawn()

        # 更新蛇的身體
        self.body.append((self.x, self.y))
        if len(self.body) > self.length:
            del self.body[0]

        # 處理邊界通行
        if self.x < 0:
            self.x = WINDOW_WIDTH - self.size
        elif self.x >= WINDOW_WIDTH:
            self.x = 0
        elif self.y < 0:
            self.y = WINDOW_HEIGHT - self.size
        elif self.y >= WINDOW_HEIGHT:
            self.y = 0

    def change_direction(self, direction):
        if direction == "UP" and self.dy != self.size:
            self.dx = 0
            self.dy = -self.size
        elif direction == "DOWN" and self.dy != -self.size:
            self.dx = 0
            self.dy = self.size
        elif direction == "LEFT" and self.dx != self.size:
            self.dx = -self.size
            self.dy = 0
        elif direction == "RIGHT" and self.dx != -self.size:
            self.dx = self.size
            self.dy = 0

# 食物類別
class Food:
    def __init__(self):
        self.size = SNAKE_SIZE
        self.x = random.randint(0, WINDOW_WIDTH // self.size - 1) * self.size
        self.y = random.randint(0, WINDOW_HEIGHT // self.size - 1) * self.size

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.size, self.size))

    def spawn(self):
        self.x = random.randint(0, WINDOW_WIDTH // self.size - 1) * self.size
        self.y = random.randint(0, WINDOW_HEIGHT // self.size - 1) * self.size

# 遊戲結束
def game_over():
    pygame.quit()
    quit()

# 創建貪吃蛇和食物對象
snake = Snake()
food = Food()



# 遊戲迴圈
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction("UP")
            elif event.key == pygame.K_DOWN:
                snake.change_direction("DOWN")
            elif event.key == pygame.K_LEFT:
                snake.change_direction("LEFT")
            elif event.key == pygame.K_RIGHT:
                snake.change_direction("RIGHT")

    screen.fill(BLACK)  # 清空畫面

    snake.move()  # 移動貪吃蛇
    snake.draw()  # 繪製貪吃蛇

    food.draw()  # 繪製食物

    pygame.display.flip()  # 更新視窗顯示

    clock.tick(10)  # 控制遊戲速度

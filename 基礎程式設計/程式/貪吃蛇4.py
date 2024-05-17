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

# 定義遊戲狀態
GAME_STATE_MENU = 0
GAME_STATE_PLAYING = 1
GAME_STATE_GAMEOVER = 2

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

        # 檢查是否撞到自己或牆壁
        if self.x < 0 or self.x >= WINDOW_WIDTH or self.y < 0 or self.y >= WINDOW_HEIGHT:
            change_game_state(GAME_STATE_GAMEOVER)

        for segment in self.body[:-1]:
            if segment[0] == self.x and segment[1] == self.y:
                change_game_state(GAME_STATE_GAMEOVER)

        # 更新蛇的身體
        self.body.append((self.x, self.y))
        if len(self.body) > self.length:
            del self.body[0]

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

# 遊戲狀態變數
game_state = GAME_STATE_MENU

# 創建貪吃蛇和食物對象
snake = Snake()
food = Food()

# 變更遊戲狀態
def change_game_state(state):
    global game_state
    game_state = state

# 顯示首頁
def show_menu():
    screen.fill(BLACK)
    font = pygame.font.SysFont(None, 40)
    title_text = font.render("貪吃蛇遊戲", True, WHITE)
    screen.blit(title_text, (WINDOW_WIDTH // 2 - title_text.get_width() // 2, 200))

    start_text = font.render("按下任意鍵開始遊戲", True, WHITE)
    screen.blit(start_text, (WINDOW_WIDTH // 2 - start_text.get_width() // 2, 300))

# 顯示遊戲結束畫面
def show_gameover():
    screen.fill(BLACK)
    font = pygame.font.SysFont(None, 40)
    gameover_text = font.render("遊戲結束", True, WHITE)
    screen.blit(gameover_text, (WINDOW_WIDTH // 2 - gameover_text.get_width() // 2, 200))

    score_text = font.render("獲得分數: " + str(snake.score), True, WHITE)
    screen.blit(score_text, (WINDOW_WIDTH // 2 - score_text.get_width() // 2, 300))

    restart_text = font.render("按下任意鍵重新開始", True, WHITE)
    screen.blit(restart_text, (WINDOW_WIDTH // 2 - restart_text.get_width() // 2, 400))

# 遊戲迴圈
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if game_state == GAME_STATE_MENU or game_state == GAME_STATE_GAMEOVER:
                change_game_state(GAME_STATE_PLAYING)
            elif game_state == GAME_STATE_PLAYING:
                if event.key == pygame.K_UP:
                    snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction("RIGHT")

    if game_state == GAME_STATE_MENU:
        show_menu()
    elif game_state == GAME_STATE_PLAYING:
        screen.fill(BLACK)  # 清空畫面

        snake.move()  # 移動貪吃蛇
        snake.draw()  # 繪製貪吃蛇

        food.draw()  # 繪製食物

        # 顯示計分
        font = pygame.font.SysFont(None, 25)
        score_text = font.render("Score: " + str(snake.score), True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()  # 更新視窗顯示

        # 控制遊戲速度
        clock.tick(10 + snake.score // 10)

        # 檢查遊戲結束條件
        if snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT:
            change_game_state(GAME_STATE_GAMEOVER)
        for segment in snake.body[:-1]:
            if segment[0] == snake.x and segment[1] == snake.y:
                change_game_state(GAME_STATE_GAMEOVER)
    elif game_state == GAME_STATE_GAMEOVER:
        show_gameover()

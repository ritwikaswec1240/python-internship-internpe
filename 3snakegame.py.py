import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cute Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (144, 238, 144)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
SNAKE_COLOR = (0, 100, 0)

# Snake settings
snake_size = 15
snake_speed = 15

# Font for score
def show_score(score):
    font = pygame.font.Font(None, 30)
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, [10, 10])

# Main game loop
def game_loop():
    game_over = False
    game_close = False
    
    x, y = WIDTH // 2, HEIGHT // 2
    x_change, y_change = 0, 0
    
    snake_body = []
    length = 1
    
    food_x = random.randint(0, (WIDTH // snake_size) - 1) * snake_size
    food_y = random.randint(0, (HEIGHT // snake_size) - 1) * snake_size
    
    clock = pygame.time.Clock()
    
    while not game_over:
        while game_close:
            screen.fill(WHITE)
            font = pygame.font.Font(None, 50)
            message = font.render("Game Over! Press R to Restart", True, RED)
            screen.blit(message, [WIDTH // 6, HEIGHT // 3])
            show_score(length - 1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        return  # Restart the game properly
                    elif event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change, y_change = -snake_size, 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change, y_change = snake_size, 0
                elif event.key == pygame.K_UP and y_change == 0:
                    x_change, y_change = 0, -snake_size
                elif event.key == pygame.K_DOWN and y_change == 0:
                    x_change, y_change = 0, snake_size
                    
        x += x_change
        y += y_change
        
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_close = True
        
        screen.fill(GREEN)
        pygame.draw.rect(screen, RED, [food_x, food_y, snake_size, snake_size], border_radius=5)
        
        snake_body.append([x, y])
        if len(snake_body) > length:
            del snake_body[0]
        
        for segment in snake_body[:-1]:
            if segment == [x, y]:
                game_close = True
        
        for part in snake_body:
            pygame.draw.rect(screen, SNAKE_COLOR, [part[0], part[1], snake_size, snake_size], border_radius=8)
        
        show_score(length - 1)
        pygame.display.update()
        
        if x == food_x and y == food_y:  # Fix food collision detection
            food_x = random.randint(0, (WIDTH // snake_size) - 1) * snake_size
            food_y = random.randint(0, (HEIGHT // snake_size) - 1) * snake_size
            length += 1
        
        clock.tick(snake_speed)
    
    pygame.quit()
    quit()

# Start the game
game_loop()

import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 40
PLAYER_COLOR = (0, 0, 255)
ENEMY_COLOR = (255, 0, 0)
WALL_COLOR = (255, 255, 255)
BG_COLOR = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the player
player = pygame.Rect(WIDTH // 2, HEIGHT // 2, TILE_SIZE, TILE_SIZE)

# Set up the enemies
enemies = [pygame.Rect(random.randint(0, WIDTH - TILE_SIZE), random.randint(0, HEIGHT - TILE_SIZE), TILE_SIZE, TILE_SIZE) for _ in range(5)]

# Set up the maze
maze = [[random.choice([0, 1]) for _ in range(WIDTH // TILE_SIZE)] for _ in range(HEIGHT // TILE_SIZE)]

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move_ip(0, -TILE_SIZE)
            elif event.key == pygame.K_DOWN:
                player.move_ip(0, TILE_SIZE)
            elif event.key == pygame.K_LEFT:
                player.move_ip(-TILE_SIZE, 0)
            elif event.key == pygame.K_RIGHT:
                player.move_ip(TILE_SIZE, 0)

    # Enemy movement
    for enemy in enemies:
        dx, dy = player.centerx - enemy.centerx, player.centery - enemy.centery
        mag = math.hypot(dx, dy)
        dx, dy = dx / mag, dy / mag  # Normalize
        enemy.move_ip(dx, dy)

        # Collision with player
        if player.colliderect(enemy):
            running = False

    # Draw everything
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, PLAYER_COLOR, player)
    for enemy in enemies:
        pygame.draw.rect(screen, ENEMY_COLOR, enemy)
    for y in range(HEIGHT // TILE_SIZE):
        for x in range(WIDTH // TILE_SIZE):
            if maze[y][x] == 1:
                pygame.draw.rect(screen, WALL_COLOR, pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
import pygame
from pygame import display
import random

# pygame initialize
pygame.init()

# Set window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Setting color
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Settings to change the direction of the mouse
mouse_dx = 2
mouse_dy = 2

# Window Settings
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Paste Image")

clock = pygame.time.Clock()
scores = 0

# Past image and setting
elephant_image = pygame.image.load("elephant.png")
elephant_rect = elephant_image.get_rect()
elephant_rect.centerx = (WINDOW_WIDTH // 2)
elephant_rect.bottom = (WINDOW_HEIGHT // 2)

# Paste the moust image and set it
mouse_image = pygame.image.load("mouse.png")
mouse_rect = mouse_image.get_rect()
mouse_rect.centerx = (WINDOW_WIDTH // 2)
elephant_rect.bottom = (WINDOW_HEIGHT // 2)

# Paste and set the banana image
banana_image = pygame.image.load("banana.png")
banana_rect = banana_image.get_rect()

score_live = 3
# Creating a text object
system_font = pygame.font.SysFont("calibri", 30)
game_live = system_font.render("Lives : " + str(score_live), True, GREEN, BLACK)
game_live_rect = game_live.get_rect()
game_live_rect.topleft = (10, 10)

# Creating a scoreboard object
score_font = pygame.font.SysFont("verdanai", 30)
score_board = score_font.render("Score : " + str(scores), True, GREEN, BLACK)
game_score_rect = score_board.get_rect()
game_score_rect.topleft = (10, 30)

# Main Loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  keys = pygame.key.get_pressed()


  
  if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and elephant_rect.left > 0:
    elephant_rect.x -= 2
  if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and elephant_rect.right < WINDOW_WIDTH:
    elephant_rect.x += 2
  if (keys[pygame.K_UP] or keys[pygame.K_w]) and elephant_rect.top > 0:
    elephant_rect.y -= 2
  if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and elephant_rect.bottom < WINDOW_HEIGHT:
    elephant_rect.y += 2
  
  # if event.type == pygame.MOUSEBUTTONDOWN:
  #   mouse_x = event.pos[0]
  #   mouse_y = event.pos[1]
  #   elephant_rect.centerx = mouse_x
  #   elephant_rect.centery = mouse_y

  # # Apply event when mouse moves
  # if event.type == pygame.MOUSEMOTION and event.buttons [0] == 1:
  #   mouse_x = event.pos[0]
  #   mouse_y = event.pos[1]
  #   elephant_rect.centerx = mouse_x
  #   elephant_rect.centery = mouse_y

  # Character collision event test
  if elephant_rect.colliderect(mouse_rect):
    print("collision")
    score_live = score_live - 1
    mouse_rect.x = random.randint(0, WINDOW_WIDTH - 50)
    mouse_rect.y = random.randint(0, WINDOW_HEIGHT - 50)

  # Set the mouse to move regularly
  mouse_rect.x += mouse_dx
  mouse_rect.y += mouse_dy

  # Set the mouse to bounce off the walls
  if (mouse_rect.x) > WINDOW_WIDTH or (mouse_rect.x) < 0:
    mouse_dx = mouse_dx * -1
  if (mouse_rect.y) > WINDOW_HEIGHT or (mouse_rect.y) < 0:
    mouse_dy = mouse_dy * -1

  # If the banana moves to the left side of the screen, 1 point is deducted from the score.
  # The banana continues to move -10 units in x-coordinate.
  if banana_rect.x < 0:
    scores -= 1
    banana_rect.x = WINDOW_WIDTH + 50
    banana_rect.y = random.randint(64, WINDOW_HEIGHT - 50)
  else:
    banana_rect.x -= 3

  # If the elephant collides with (eats) a banana, you get 1 point.
  # Banana appears randomly on the screen.
  if elephant_rect.colliderect(banana_rect):
    scores += 1
    banana_rect.x = WINDOW_WIDTH + 50
    banana_rect.y = random.randint(64, WINDOW_HEIGHT - 50)
  
  # Display Scoreboard
  if score_live > 0:
    game_live = system_font.render("Lives : " + str(score_live), True, GREEN, BLACK)
  else:
    game_live = system_font.render("Game Over : ", True, GREEN, BLACK)
    running = False

  # Score Display
  game_score = score_font.render("Score : " + str(scores), True, GREEN, BLACK)
  
  # Background color
  display_surface.fill((255 , 255, 255))

  # Blit (paste) image
  display_surface.blit(elephant_image, elephant_rect)
  display_surface.blit(mouse_image, mouse_rect)

  display_surface.blit(banana_image, banana_rect)
  
  # Display Text
  display_surface.blit(game_live, game_live_rect)

  display_surface.blit(game_score, game_score_rect)
  
  # Update display
  pygame.display.update()

# Wait for the game to end message to be displayed
pygame.time.wait(3000)

pygame.quit()
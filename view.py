import pygame
from model import main

pygame.init() # Initialize pygame

cell_size = 40
cell_num = 20

WIDTH = cell_size * cell_num
HEIGHT = cell_size * cell_num

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(pygame.Color("black")) # Screen bg color

framerate = 30
clock = pygame.time.Clock()

running = True

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = main(screen, cell_size)
if __name__ == "__main__":
  while running:
    # Poll all events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if event.type == SCREEN_UPDATE:
        main_game.update()
      
      # Player Input
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          if main_game.snake.direction.y != 1: # Stops player from turning head inside itself
            main_game.snake.direction = pygame.Vector2(0,-1)
        if event.key == pygame.K_DOWN:
          if main_game.snake.direction.y != -1:
            main_game.snake.direction = pygame.Vector2(0,1)
        if event.key == pygame.K_LEFT:
          if main_game.snake.direction.x != 1:
            main_game.snake.direction = pygame.Vector2(-1,0)
        if event.key == pygame.K_RIGHT:
          if main_game.snake.direction.x != -1:
            main_game.snake.direction = pygame.Vector2(1,0)
  
    screen.fill(pygame.Color("black"))

    # Render Game
    main_game.draw_elements()
        
    clock.tick(framerate) # Limits FPS to framerate(25)
    pygame.display.update() # or pygame.display.flip() 
  pygame.quit()
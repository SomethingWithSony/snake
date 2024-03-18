import pygame 
import random

class snake:
  def __init__(self, screen, size ):
    self.screen = screen
    self.color = "green"
    self.size= size
    self.direction = pygame.Vector2(0,0)
    self.add_new_block = False
    self.reset()

  # Resets cobra body to inital state
  def reset(self):
    self.body = [pygame.Vector2(5,6),pygame.Vector2(5,7),pygame.Vector2(5,8)]

  def draw_snake(self):
    for block in self.body:
      # Create rectangle
      snake_rect = pygame.Rect(int(block.x * self.size),int(block.y * self.size),self.size,self.size)
      # Draw rectangle
      pygame.draw.rect(self.screen,pygame.Color(self.color),snake_rect)
    
  """
  If a new block is added , create a copy of the body
  else
  Removes block from the end of the list 
  Head moves forward
  """
  def move_snake(self):
    if self.add_new_block:
      body_copy = self.body[:]
    else:
      body_copy = self.body[:-1]
    body_copy.insert(0, body_copy[0] + self.direction)
    self.body = body_copy
    self.add_new_block = False

 
    
    

class fruit:
  def __init__(self, screen, size):
    self.randomize()

    self.color = "red"
    self.screen = screen
    self.size= size

  def randomize(self):
    self.x = random.randint(0 , 20 - 1)
    self.y = random.randint(0 , 20 - 1)
    self.position =  pygame.math.Vector2(self.x,self.y)

  def draw_fruit(self):
    # Create rectangle
    fruit_rect = pygame.Rect(int(self.position.x * self.size),int(self.position.y * self.size),self.size,self.size)
    # Draw rectangle
    pygame.draw.rect(self.screen,pygame.Color(self.color),fruit_rect)

"""
Contains all the game logic and game objects (snake & fruit)
"""
class main:
  def __init__(self, screen, cell_size):
    self.snake = snake(screen, cell_size)
    self.fruit = fruit(screen, cell_size)

  def update(self):
    self.snake.move_snake() # moves the snake
    self.check_collisions() 
    self.check_fail()

  def draw_elements(self):
    self.snake.draw_snake()
    self.fruit.draw_fruit()

  # Checks snake collision with fruit
  def check_collisions(self):
    if self.fruit.position == self.snake.body[0]:
      # reposition fruit
      self.fruit.randomize()
      # add block to snake
      self.snake.add_new_block = True

  # Checks collisions with snake & walls
  def check_fail(self):
    # Check if snake is off screen
    if not 0 <= self.snake.body[0].x < 20 or not 0 <= self.snake.body[0].y < 20:
      self.game_over()

    for block in self.snake.body[1:]:
        if self.snake.body[0] == block:
          self.game_over()
          
  # Resets snake to it's intial state
  def game_over(self):
    self.snake.reset()




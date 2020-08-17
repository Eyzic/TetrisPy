import pygame
from block import Block
from coord import Coord

class GameBoard:
    def __init__(self, screen, playarea_block_height, playarea_block_width, playarea_starting_point, BLOCK_SIZE, grid_thickness):
       self.game_board = [[Block((x,y)) for y in range(playarea_block_height)] for x in range(playarea_block_width)]
       self.height = playarea_block_height
       self.width = playarea_block_width
       self.starting_x = playarea_starting_point[0]
       self.starting_y = playarea_starting_point[1]
       self.block_size = BLOCK_SIZE
       self.grid_thickness = grid_thickness
       self.screen = screen

   
    def draw_grid(self):
        nr_of_vertical_lines = self.height+1
        nr_of_horizontal_lines = self.width+1
        for x in range(nr_of_horizontal_lines):
            for y in range(nr_of_vertical_lines):
                if x == 0:
                    pygame.draw.line(self.screen, (127,127,127), 
                                (self.starting_x, self.starting_y + y * self.block_size), 
                                (self.starting_x + self.width * self.block_size, self.starting_y + y * self.block_size), 
                                 self.grid_thickness)
                if y == 0:
                    pygame.draw.line(self.screen, (127,127,127), 
                                (self.starting_x + x * self.block_size, self.starting_y), 
                                (self.starting_x + x * self.block_size,self.starting_y + self.height * self.block_size), 
                                 self.grid_thickness)
   
    def draw(self):
       for x in range(self.width):
          for y in range(self.height):
             rect = pygame.Rect(self.starting_x + x * self.block_size, self.starting_y + y * self.block_size, self.block_size, self.block_size)
             pygame.draw.rect(self.screen, self.game_board[x][y].color, rect)
       self.draw_grid()

    def place(self, coord, block):
              block.x = coord[0]
              block.y = coord[1]
              self.game_board[block.x][block.y] = block
   
    def move(self, blocks, direction):
        #self.delete(blocks)
        if self.valid_move(blocks, direction):
            for block in blocks:
                new_coord = Coord.add(block.get_coord(), direction)
                block.x = new_coord[0]
                block.y = new_coord[1]
                self.game_board[block.x][block.y] = block

    def delete(self, blocks):
        for block in blocks:
           self.game_board[block.x][block.y] = Block((block.x,block.y))

    def valid_move(self, blocks, direction):
        for block in blocks:
           new_coord = Coord.add(block.get_coord(), direction)
           x, y = int(new_coord[0]), int(new_coord[1])
           if x < 0 or x > self.width-1:
              return False
           elif (block.y + direction[1]) > self.height-1 or (block.x + direction[0]) > self.width-1:
              return False
           elif self.game_board[block.x + direction[0]][block.y+ direction[1]].color != (0,0,0):
              return False

        return True

    def get_finished_lines(self):
        finished_lines = []
        for i in range(self.height):
            counter = 0
            for j in range(self.width):
               if self.game_board[j][i].color != (0,0,0):
                  counter += 1
            if counter == 10:
               finished_lines.append(i)
        return finished_lines

    def color_lines(self, line_numbers):
        for number in line_numbers:
           for i in range(self.width):
               self.game_board[i][number].color = (255,192,1)

    def remove_lines(self, line_numbers):
        for number in line_numbers:
           self.remove_line(number)
               
    def remove_line(self, line_number):
            self.move_down_until_line(line_number) 
  
    def move_down_until_line(self, line_number):
        for i in reversed(range(line_number)):
            for j in range(self.width):
               self.game_board[j][i+1].color = self.game_board[j][i].color
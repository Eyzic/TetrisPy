from block import Block
from coord import Coord
import random

## Rotations for rest of T shape
##[(1,0), (0,-1), (0,0), (0,1)],
    ##      [(0,0), (-1,-1), (0,-1), (1,-1)],
      ##    [(0,0), (0,1), (0,-1), (-1,0)]

#The relationsship between the coordinates for each shape
shape = {
    'T': [(0,0), (-1,1), (0,1), (1,1), (200,0,200)], #lägg eventuellt in color sist.
    'I': [(0,0), (0,1), (0,2), (0,3), (0,255,255)], #lägg eventuellt in color sist.
    'O': [(0,0), (1,0), (0,1), (1,1), (255,255,0)], #lägg eventuellt in color sist.
    'J': [(0,0), (0,1), (1,1), (2,1), (0,70,255)], #lägg eventuellt in color sist.
    'L': [(0,0), (0,1), (-1,1), (-2,1), (255,165,0)], #lägg eventuellt in color sist.
    'Z': [(0,0), (0,1), (-1,1), (-1,2), (255,0,0)], #lägg eventuellt in color sist.
    'S': [(0,0), (0,1), (1,1), (1,2), (0,255,0)], #lägg eventuellt in color sist.
    ' ': [(0,0), (0,0), (0,0), (0,0), (0,0,0)] #lägg eventuellt in color sist.
}

class Shape:
    def __init__(self, form=None):
        if form is None:
           form = random.choice(['T','I','O','J','L','Z','S'])
        self.rotation = 0
        self.form = form
        self.relative_positions = shape[form]
        self.blocks = [(Block(shape[form][i])) for i in range(4)] #Behöver förenklas.
        
        for block in self.blocks:
            block.color = shape[form][4]

    def print_blocks(self):
        for i in range(4):
            print(self.blocks[i].get_coord())

    def place(self, tetrimino_coord, game_board):
        for i in range(4):
            block = self.blocks[i]
            block_position = Coord.add(self.relative_positions[i], tetrimino_coord)
            game_board.place(block_position, block)

    # def rotate(self):
        # self.rotation += 1
        # self.relative_positions = shape[self.form][self.rotation%4]
        # self.place((0,0))

    def move_left(self, game_board):
        self.move((-1,0), game_board)

    def move_right(self, game_board):
        self.move((1,0), game_board)
   
    def move(self, direction, game_board):
            game_board.delete(self.blocks) 
        
            game_board.move(self.blocks, direction)

    def move_down(self, game_board):
        result = True
        game_board.delete(self.blocks) 

        for block in self.blocks:
            if not block.down_is_valid(game_board):
               result = False
      
        if result == False:
            for block in self.blocks:
                new_coords = Coord.add(block.get_coord(),(0,0))
                game_board.place(new_coords,block)

        elif result == True:
                game_board.move(self.blocks, (0,1))

        return result
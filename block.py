from coord import Coord

class Block:
    def __init__(self, coord):
        self.color = (0,0,0)
        self.x = coord[0]
        self.y = coord[1]

    def get_coord(self):
        return (self.x, self.y) 
  
    def down_is_valid(self, game_board):
        if self.y >= 19:
           return False
        elif game_board.game_board[self.x][self.y+1].color != (0,0,0):
           return False
        else:
           return True
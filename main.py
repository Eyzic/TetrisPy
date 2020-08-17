import sys, pygame
from gameboard import GameBoard
from shape import Shape

BLOCK_SIZE = 30
PLAYAREA_BLOCK_WIDTH = 10
PLAYAREA_BLOCK_HEIGHT = 20
DOWN_SPEED = 30
playarea_starting_point = (30,30)
grid_thickness = 2
move_speed = 1
clock = pygame.time.Clock()

def setup():
    pygame.init()
    pygame.key.set_repeat(50)
    screen = pygame.display.set_mode((440, 800))
    return GameBoard(screen, PLAYAREA_BLOCK_HEIGHT, PLAYAREA_BLOCK_WIDTH, playarea_starting_point, BLOCK_SIZE, grid_thickness)


def main():
    game_board = setup()
    game_loop = True
    fallspeed_counter = 0
    tetrimino_is_done = False

    tetrimino = Shape('T')
    tetrimino.place((5,0),game_board)

    while game_loop:
        if tetrimino_is_done:
           tetrimino = Shape()   #Spawn a new shape at the top
           tetrimino.place((4,0), game_board)
           tetrimino_is_done = False
        if fallspeed_counter == DOWN_SPEED and not tetrimino_is_done:
            tetrimino_is_done = not tetrimino.move_down(game_board)
            fallspeed_counter = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
               # if event.key == pygame.K_SPACE:
              #      tetrimino.dunk(game_board)
               # if event.key == pygame.K_UP:
               #     tetrimino.rotate(game_board)
                if event.key == pygame.K_LEFT:
                    tetrimino.move_left(game_board)
                if event.key == pygame.K_RIGHT:
                    tetrimino.move_right(game_board)
                if event.key == pygame.K_DOWN:
                    tetrimino_is_done = not tetrimino.move_down(game_board)
        lines = game_board.get_finished_lines()
        if lines:
           game_board.color_lines(lines) 
        game_board.draw()
        pygame.display.flip()
        clock.tick(60)
        fallspeed_counter += 1

if __name__ == "__main__":
    main()
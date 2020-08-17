import sys, pygame
from gameboard import GameBoard
from shape import Shape
from ui import UI

BLOCK_SIZE = 30
PLAYAREA_BLOCK_WIDTH = 10
PLAYAREA_BLOCK_HEIGHT = 20
DOWN_SPEED = 30
playarea_starting_point = (30,30)
grid_thickness = 2
move_speed = 1
clock = pygame.time.Clock()

def setup_pygame():
    pygame.init()
    pygame.key.set_repeat(50)
    return pygame.display.set_mode((440, 800))

def setup_gameboard(screen):
    return GameBoard(screen, PLAYAREA_BLOCK_HEIGHT, PLAYAREA_BLOCK_WIDTH, playarea_starting_point, BLOCK_SIZE, grid_thickness)

def setup_UI(screen):
    return UI(screen)

def main():
    screen = setup_pygame()
    game_board = setup_gameboard(screen)
    ui = setup_UI(screen)
    game_loop = True
    fallspeed_counter = 0
    tetrimino_is_done = False
    score = 0
    level = 1
    LEVEL_GAP  = 1000 * level
    BASE_POINT = 100

    tetrimino = Shape('T')
    tetrimino.place((5,0),game_board)

    while game_loop:
        if tetrimino_is_done:
           lines = game_board.get_finished_lines()   #Returns a list of finished line numbers or empty if none
           if lines:
              game_board.color_lines(lines)
              score += level * BASE_POINT * len(lines)		  
              if score >= LEVEL_GAP:
                 level += 1
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
        game_board.draw()
        ui.draw_score(score)
        pygame.display.flip()
        clock.tick(60)
        fallspeed_counter += 1

if __name__ == "__main__":
    main()
import pygame
import time
import random

## Direction Constants
UP    = (0, -1)
DOWN  = (0, 1)
LEFT  = (-1, 0)
RIGHT = (1, 0)

OPPOSITE = {UP:DOWN, DOWN:UP, LEFT:RIGHT, RIGHT:LEFT}

## Color Constants
BLACK  = (0, 0, 0)
RED    = (255, 0, 0)
GREEN  = (0, 255, 0)
BLUE   = (0, 0, 255)
CYAN   = (0, 255, 255)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
WHITE  = (255, 255, 255)

class Cell:
    def __init__(self):
        self.top_wall    = True
        self.bottom_wall = True
        self.left_wall   = True
        self.right_wall  = True
        
        self.visited     = False

    def remove_wall(self, direction):
        if direction == UP:
            self.top_wall    = False
        elif direction == DOWN:
            self.bottom_wall = False
        elif direction == LEFT:
            self.left_wall   = False
        elif direction == RIGHT:
            self.right_wall  = False

    ## Does the opposite of remove_wall
    ## Add the wall in direction
    def add_wall(self, direction):
        ## TODO

    ## Make a copy of Cell object
    def copy(self):
        new_cell = Cell()

        new_cell.top_wall = self.top_wall
        new_cell.bottom_wall = self.bottom_wall
        new_cell.left_wall = self.left_wall
        new_cell.right_wall = self.right_wall

        return new_cell

class Maze:
    def __init__(self, width=20, height=20, tile_size=20, border_width=20, animate=True):
        self.width        = width
        self.height       = height
        self.tile_size    = tile_size
        self.border_width = border_width
        self.animate      = animate

        self.maze         = [[Cell() for _ in range(self.height)] for _ in range(self.width)]

        pwidth = (width * tile_size) + (2 * border_width)
        pheight = (height * tile_size) + (2 * border_width)
        
        self.screen = pygame.display.set_mode((pwidth, pheight))
        self.screen.fill(CYAN)
        pygame.display.set_caption("Python Maze Generator")
        
    def build_grid(self):
        s = self.tile_size
        b = self.border_width

        x = b
        y = b
        
        for i in range(0, self.width):
            for j in range(0, self.height):
                pygame.draw.line(self.screen, BLACK, [x, y], [x + s, y])
                pygame.draw.line(self.screen, BLACK, [x + s, y], [x + s, y + s])
                pygame.draw.line(self.screen, BLACK, [x + s, y + s], [x, y + s])
                pygame.draw.line(self.screen, BLACK, [x, y + s], [x, y])
                y += s
                
            x += s
            y = b
        if self.animate == True:
            pygame.display.update()

    def push(self, x, y, direction):
        s = self.tile_size
        b = self.border_width

        
        px = (x * s) + b + 1
        py = (y * s) + b + 1

        if direction in (UP, LEFT):
            px += direction[0] * s
            py += direction[1] * s

        if direction in (UP, DOWN):
            pygame.draw.rect(self.screen, WHITE, (px, py, s - 1, (2 * s) - 1), 0)
        else:
            pygame.draw.rect(self.screen, WHITE, (px, py, (2 * s) - 1, s - 1), 0)

        if self.animate == True:
            pygame.display.update()

    def draw_tile(self, x, y, color):
        s = self.tile_size
        b = self.border_width
        
        px = (x * s) + b + 1
        py = (y * s) + b + 1
        
        pygame.draw.rect(self.screen, color, (px, py, s - 1, s - 1), 0)

        if self.animate == True:
            pygame.display.update()

    def draw_small_tile(self, x, y, color):
        s = self.tile_size
        b = self.border_width
        
        px = (x * s) + b + ((s - 2) // 2)
        py = (y * s) + b + ((s - 2) // 2)
        
        pygame.draw.rect(self.screen, color, (px, py, 3, 3), 0)

        if self.animate == True:
            pygame.display.update()

    def make_maze(self, start_x, start_y):
        self.build_grid()
        time.sleep(5)
        clock = pygame.time.Clock()

        tick = 0

        if self.animate == True:
            tick = 20
        
        x = start_x
        y = start_y
        stack = list()
        cell_matrix = [[Cell() for _ in range(self.height)] for _ in range(self.width)]
        
        stack.append((x, y))
        cell_matrix[x][y].visited = True

        while len(stack) > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
            clock.tick(tick)
            branches = list()
            
            for direction in (UP, DOWN, LEFT, RIGHT):
                newx = x + direction[0]
                newy = y + direction[1]

                if newx < 0 or newx >= self.width:
                    continue

                if newy < 0 or newy >= self.height:
                    continue

                if cell_matrix[newx][newy].visited == False:
                    branches.append(direction)

            if len(branches) > 0:
                rand_direction = random.choice(branches)

                self.push(x, y, rand_direction)

                cell_matrix[x][y].remove_wall(rand_direction)
                
                x += rand_direction[0]
                y += rand_direction[1]

                cell_matrix[x][y].remove_wall(OPPOSITE[rand_direction])

                cell_matrix[x][y].visited = True
                stack.append((x, y))

            else:
                x, y = stack.pop()
                self.draw_tile(x, y, RED)
                clock.tick(tick)
                self.draw_tile(x, y, WHITE)

        pygame.display.update()

        self.maze = cell_matrix

    ## Save an image of the maze
    def save_maze(self, filename='maze.jpg'):
        pygame.image.save(self.screen, filename)

    def solve_maze(self, start_coord, end_coord):
        stack = list()
        clock = pygame.time.Clock()
        maze_info = [[self.maze[x][y].copy() for y in range(self.height)] for x in range(self.width)]

        tick = 0

        if self.animate == True:
            tick = 20

        x = start_coord[0]
        ## TODO: Check if starting x coordinate is valid
        
        
        y = start_coord[1]
        ## TODO: Check if starting x coordinate is valid
        

        end_x = end_coord[0]
        ## TODO: Check if ending x coordinate is valid
        
        
        end_y = end_coord[1]
        ## TODO: Check if ending y coordinate is valid
        

        ## Run until our current coordinate is equal to the ending coordinate
        while not ____________:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            ## TODO: Draw a small red tile (use function draw_small_tile())
            
                    
            clock.tick(tick)

            branches = list()

            ## Checks if the top wall is present
            ## If the top wall is not present, we can move up so we add it to branches
            if maze_info[x][y].top_wall == False:
                branches.append(UP)

            ## TODO: Check all other walls and add valid directions to branches

            
            if len(branches) > 0:
                ## TODO: Add our current coordinates to the stack

                ## We just choose the first direction because randomness does not matter
                direction = branches[0]

                ## TODO: Seal off the wall in direction to help me remeber that I have been there before
                

                ## TODO: Update my X and y
                

                ## TODO: Seal off the wall in the opposite direction of my new position
                ## The same as sealing off the wall to the cell that I came from
                

                
            else:
                ## Draw a white tile over the small red_tile to 'erase' it from our screen

                
                clock.tick(tick)
                x, y = stack.pop()


        self.draw_small_tile(x, y, RED)
                
if __name__ == "__main__":
    pygame.init()

    ## Try changing up the size and starting/ending locations for fun
    m = Maze(10,10, animate=True)
    m.make_maze(0, 0)
    m.save_maze()
    m.solve_maze((0,0), (m.width-1, m.height-1))
    m.save_maze('solved_maze.jpg')

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                break

import pygame
# RETRIEVES BUTTON CONTEXT FROM MOUSE

class Mouse:
    def __init__(self, grid):
        self.grid_dimensions = grid.dimensions
        self.mouse = pygame.mouse

    def get_square(self, dim, pixels_per_col):
        self.cell_size = dim[0] / pixels_per_col
        pos = self.mouse.get_pos() 
        relative_pos = (int(pos[0] / self.cell_size), int(pos[1] / self.cell_size))
        return relative_pos
    
    def get_function(self, functions):
        x, y = self.mouse.get_pos()
        x -= 512
        relative_x = int(x / 64)
        relative_y = int(y / 32)
        try:
            return functions[relative_y][relative_x]
        except IndexError:
            pass
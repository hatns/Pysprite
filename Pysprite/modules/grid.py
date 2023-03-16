import pygame

class RGBA:
    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

class Grid:
    def __init__(self, dimensions: tuple[int, int], cells_per_row: int):
        self.dimensions = dimensions 
        self.surface = pygame.surface.Surface((dimensions[0], dimensions[1]))
        self.cells_per_row = cells_per_row
        self.cell_size = {"x": int(dimensions[0] / cells_per_row), "y": int(dimensions[1] / cells_per_row)}
    
    def populate(self):
        self.cell_rows = []
        for y in range(self.cells_per_row):
            self.cell_rows.append([])
            for x in range(self.cells_per_row):
                self.cell_rows[y].append(RGBA(0, 0, 0, 0))
    
    def draw(self):
        ## RESPONSIBLE FOR DRAWING THE BACKGROUND {
        backlay_surface = pygame.Surface(self.dimensions)
        backlay_surface.fill((155,155,155))
        for i in range(self.cells_per_row):
            for j in range(self.cells_per_row):
                cell_size = self.cell_size["x"]
                coordinate1 = (i*cell_size, j*cell_size, cell_size/2, cell_size/2)
                coordinate2 = (i*cell_size+cell_size/2, j*cell_size+cell_size/2, cell_size/2, cell_size/2)
                color = (200,200,200) 
                pygame.draw.rect(backlay_surface, color, coordinate1)
                pygame.draw.rect(backlay_surface, color, coordinate2)


        self.surface.blit(backlay_surface, (0,0))


        x_color = (int(90 - 0.8*self.cells_per_row),int(90 - 0.8*self.cells_per_row),int(90 - 0.8*self.cells_per_row))
        if x_color[0] < 0:
            x_color = (0,0,0)
        y_color = (int(130 - 0.5*self.cells_per_row),int(130 - 0.5*self.cells_per_row),int(130 - 0.5*self.cells_per_row))
        if y_color[0] < 0:
            y_color = (0,0,0)
        for y in range(self.cells_per_row):
            pygame.draw.rect(self.surface, x_color, (0, y*self.cell_size["y"]-1, self.dimensions[1], 2))
        for x in range(self.cells_per_row):
            pygame.draw.rect(self.surface, y_color, (x*self.cell_size["x"]-1, 0, 2, self.dimensions[0]))
        pygame.draw.rect(self.surface, x_color, (0, self.dimensions[1]-1, self.dimensions[1], 1))
        pygame.draw.rect(self.surface, y_color, (self.dimensions[0]-1, 0, 1, self.dimensions[0]))

        ## }
        
        for y, row in enumerate(self.cell_rows):
            for x, cell in enumerate(row):
                cell_surface = pygame.surface.Surface((self.cell_size["x"], self.cell_size["y"]))
                pygame.draw.rect(cell_surface, (cell.r, cell.g, cell.b), (0, 0, self.cell_size["x"], self.cell_size["y"]))
                cell_surface.set_alpha(cell.a)
                self.surface.blit(cell_surface, (x*self.cell_size["x"], y*self.cell_size["y"]))

    def from_grid(grid, dimensions=None, cells_per_row=None):
        if dimensions != None:
            dim = dimensions
        else:
            dim = grid.dimensions
        if cells_per_row != None:
            cpr = cells_per_row
        else:
            cpr = grid.cells_per_row
        return Grid(dim, cpr)
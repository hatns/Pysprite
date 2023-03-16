import time
import pygame
from modules.gameutils import EventHandler, GameHandler
from modules.grid import Grid, RGBA
from modules.mouse import Mouse
from PIL import Image
# Global variables
game_enabled = True
screen_dimensions = (512+128, 512)
frames_per_second = 1000

# Initiate PyGame
window = pygame.display.set_mode(screen_dimensions)
pygame_clock = pygame.time.Clock()

# Function definitions
def game_exit(): # Function to exit game:
    # Here you can add things that will happen before or after the game exits. You can also -
    # add to the end of this code file, outside the while loop, but keep in mind pygame screen will close.
    global game_enabled
    pygame.quit()
    game_enabled = False

def increment_grid(my_grid: Grid, add = 0, mult = 1):
    global grid, sprite_pixels
    sprite_pixels = int(my_grid.cells_per_row * mult + add)
    my_grid = Grid.from_grid(my_grid, my_grid.dimensions, sprite_pixels)
    my_grid.populate()
    my_grid.draw()
    grid = my_grid

# Create EventHandler
events = EventHandler()
events.add(pygame.QUIT, game_exit) 

# --- GAME CODE BELOW THIS LINE ---
grid_dimensions = (512, 512)
sprite_pixels = 16

# Define Grid
grid = Grid(grid_dimensions, sprite_pixels)

# Populate Grid Surface
grid.populate()
grid.draw()

# Draw sidebar buttons
sidebar = pygame.surface.Surface((128, 512))

current_color = (255, 255, 255, 255) #rgba

def draw_plus(index_x, index_y):
    x = index_x*64-32 - 5
    y = index_y*32 - 16 - 5
    pygame.draw.rect(window, (190,190,190), (516 + x, y, 2, 10))
    pygame.draw.rect(window, (190,190,190), (512 + x, y + 4, 10, 2))

def draw_minus(index_x, index_y):
    x = index_x*64-32 - 5
    y = index_y*32 - 16 - 5
    pygame.draw.rect(window, (200,200,200), (512 + x, y + 4, 10, 2))


pygame.font.init()
with open("font.ttf") as f:
    font = pygame.font.Font("font.ttf", 28)

def draw_value(color, index_y, color_rgbazname):
    mid_y = index_y*32 - 16
    if color_rgbazname == "z":
        surface = font.render(str(color)+"x"+str(color), True, (256-color*4,256-color*4,256-color*4))
    if color_rgbazname == "r":
        surface = font.render(str(color), True, (255-color, 0, 0))
    if color_rgbazname == "g":
        surface = font.render(str(color), True, (0, 255-color, 0))
    if color_rgbazname == "b":
        surface = font.render(str(color), True, (0, 0, 255-color))
    if color_rgbazname == "a":
        surface = font.render(str(color), True, (255-color, 255-color, 255-color))
    if color_rgbazname == "s":
        surface = font.render("Save", True, (0, 0, 0))
    x = int(64 - surface.get_width() / 2)
    y = int(mid_y - surface.get_height() / 2)
    window.blit(surface, (512 + x, y))

def save_button():
    pygame.draw.rect(sidebar, (0, 255, 0), (0, 448, 128, 64))
    draw_value(0, 15.5, "s")


def update_sidebar():
    # decrease grid size
    pygame.draw.rect(sidebar, (130, 130, 130), (0, 32, 64, 32))
    # increase grid size
    pygame.draw.rect(sidebar, (90, 90, 90), (64, 32, 64, 32))
    # decrease red
    pygame.draw.rect(sidebar, (155, 155, 155), (0, 96, 64, 32))
    # increase red
    pygame.draw.rect(sidebar, (95, 95, 95), (64, 96, 64, 32))
    # decrease green
    pygame.draw.rect(sidebar, (155, 155, 155), (0, 160, 64, 32))
    # increase green
    pygame.draw.rect(sidebar, (95, 95, 95), (64, 160, 64, 32))
    # decrease blue
    pygame.draw.rect(sidebar, (155, 155, 155), (0, 224, 64, 32))
    # increase blue
    pygame.draw.rect(sidebar, (95, 95, 95), (64, 224, 64, 32))
    # decrease alpha
    pygame.draw.rect(sidebar, (155, 155, 155), (0, 288, 64, 32))
    # increase alpha
    pygame.draw.rect(sidebar, (95, 95, 95), (64, 288, 64, 32))
    r, g, b, a = current_color
    # Red bar
    pygame.draw.rect(sidebar, (r, 0, 0), (0, 64, 128, 32))
    # Green bar
    pygame.draw.rect(sidebar, (0, g, 0), (0, 128, 128, 32))
    # Blue bar
    pygame.draw.rect(sidebar, (0, 0, b), (0, 192, 128, 32))
    # Preview square to display the current color with alpha.
    alpha_square = pygame.surface.Surface((128, 32))
    alpha_square.fill((r, g, b))
    alpha_square.set_alpha(a)
    pygame.draw.rect(sidebar, (155, 155, 155), (0, 256, 128, 32))
    pygame.draw.rect(sidebar, (200, 200, 200), (0, 256, 64, 16))
    pygame.draw.rect(sidebar, (200, 200, 200), (64, 272, 64, 16))
    sidebar.blit(alpha_square, (0, 256))
    # Draw pluses and minuses
    draw_minus(1, 2)
    draw_plus(2, 2)
    draw_minus(1, 4)
    draw_plus(2, 4)
    draw_minus(1, 6)
    draw_plus(2, 6)
    draw_minus(1, 8)
    draw_plus(2, 8)
    draw_minus(1, 10)
    draw_plus(2, 10)
    draw_value(sprite_pixels, 1, "z")
    draw_value(r, 3, "r")
    draw_value(g, 5, "g")
    draw_value(b, 7, "b")
    draw_value(a, 9, "a")
    save_button()



last_call_time = 0
def decrease_grid():
    global last_call_time
    if sprite_pixels > 1 and (time.time() - last_call_time) > 0.1:
        increment_grid(grid, 0, 0.5)
    last_call_time = time.time()
def increase_grid():
    global last_call_time
    if sprite_pixels < 64 and (time.time() - last_call_time) > 0.1:
        increment_grid(grid, 0, 2)
    last_call_time = time.time()

def dec_red():
    global current_color
    r, g, b, a = current_color
    if 0 < r <= 255:
        current_color = (r - 1, g, b, a)
def inc_red():
    global current_color
    r, g, b, a = current_color
    if 0 <= r < 255:
        current_color = (r + 1, g, b, a)

def dec_green():
    global current_color
    r, g, b, a = current_color
    if 0 < g <= 255:
        current_color = (r, g - 1, b, a)
def inc_green():
    global current_color
    r, g, b, a = current_color
    if 0 <= g < 255:
        current_color = (r, g + 1, b, a)

def dec_blue():
    global current_color
    r, g, b, a = current_color
    if 0 < b <= 255:
        current_color = (r, g, b-1, a)
def inc_blue():
    global current_color
    r, g, b, a = current_color
    if 0 <= b < 255:
        current_color = (r, g, b+1, a)

def dec_alpha():
    global current_color
    r, g, b, a = current_color
    if 0 < a <= 255:
        current_color = (r, g, b, a-1)

def inc_alpha():
    global current_color
    r, g, b, a = current_color
    if 0 <= a < 255:
        current_color = (r, g, b, a+1)

def save():
    img = Image.new("RGBA", (grid.cells_per_row, grid.cells_per_row))
    for y, row in enumerate(grid.cell_rows):
        for x, col in enumerate(row):
            img.putpixel((x, y), (col.r, col.g, col.b, col.a))
    img.save("image.png")
            


# Functions to be called for clicks inside each 64x32 pixel area on the sidebar.
sidebar_functions = [
    [None, None],
    [decrease_grid, increase_grid],
    [None, None],
    [dec_red, inc_red],
    [None, None],
    [dec_green, inc_green],
    [None, None],
    [dec_blue, inc_blue],
    [None, None],
    [dec_alpha, inc_alpha],
    [None, None],
    [None, None],
    [None, None],
    [None, None],
    [save, save],
    [save, save],
]



# Create mouse reference
mouse = Mouse(grid, sidebar)


# Function for drawing squares

def mouse_update():
    # Check for left clicks
    if pygame.mouse.get_pressed()[0]:
        # If mouse is positioned within the "grid" area, draw.
        if pygame.mouse.get_pos()[0] < grid_dimensions[0] and pygame.mouse.get_pos()[1] < grid_dimensions[1]: 
            grid.cell_rows[mouse.get_square(grid_dimensions, sprite_pixels)[1]][mouse.get_square(grid_dimensions, sprite_pixels)[0]] = RGBA(*current_color)
        
        # Otherwise, get which button on the sidebar is pressed.
        else:
            try:
                mouse.get_function(sidebar_functions)()
            except TypeError:
                pass

# Create GameHandler
functions_to_call = [update_sidebar, mouse_update]
game = GameHandler(functions_to_call, events, window, frames_per_second)

# Main Loop
game_loop_count = 0
while game_enabled:
    window.fill((0,0,0))
    grid.draw()
    window.blits([(grid.surface, (0,0)), (sidebar, (512, 0))])
    # No more code allowed after this comment unless u have a good reason for it.
    game.update()
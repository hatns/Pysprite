import time
import pygame
from modules.gameutils import EventHandler, GameHandler
from modules.grid import Grid, RGBA
from modules.mouse import Mouse
from modules.overlay import draw_overlay
from PIL import Image
from tkinter import Tk, filedialog
from os.path import join as pathjoin
import sys
import modules.icon as ico
root = Tk()
root.withdraw()
# Global variables
game_enabled = True
screen_dimensions = (512+128, 512)
frames_per_second = 1000

# Initiate PyGame
window = pygame.display.set_mode(screen_dimensions)
pygame_clock = pygame.time.Clock()
pygame.display.set_icon(ico.get_surface())

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
font = pygame.font.SysFont("notosans.ttf", 28)

def draw_value(value, index_y, color_rgbazname):
    mid_y = index_y*32 - 16
    if color_rgbazname == "z":
        surface = font.render(str(value)+"x"+str(value), True, (256-value*2,256-value*2,256-value*2))
    if color_rgbazname == "r":
        surface = font.render(str(value), True, (255-value, 0, 0))
    if color_rgbazname == "g":
        surface = font.render(str(value), True, (0, 255-value, 0))
    if color_rgbazname == "b":
        surface = font.render(str(value), True, (0, 0, 255-value))
    if color_rgbazname == "a":
        surface = font.render(str(value), True, (255-value, 255-value, 255-value))
    if color_rgbazname == "o":
        surface = font.render(value, True, (0,0,0))
    x = int(64 - surface.get_width() / 2)
    y = int(mid_y - surface.get_height() / 2)
    window.blit(surface, (512 + x, y))
import requests

def save_button():
    pygame.draw.rect(sidebar, (0, 255, 0), (0, 448, 128, 64))
    draw_value("Save & Exit", 15.5, "o")

def fill_button():
    pygame.draw.rect(sidebar, (124, 124, 124), (0, 320, 128, 32))
    draw_value("Fill Screen", 11, "o")

def clear_button():
    pygame.draw.rect(sidebar, (173, 173, 173), (0, 352, 128, 32))
    draw_value("Clear", 12, "o")

eraser_active = False
def eraser_button():
    y = 416
    pygame.draw.rect(sidebar, (255, 255, 255), (0, y, 128, 32))
    if eraser_active:
        pygame.draw.rect(sidebar, (100, 200, 100), (0, y, 128, 4))
        pygame.draw.rect(sidebar, (100, 200, 100), (0, y, 4, 32))
        pygame.draw.rect(sidebar, (100, 200, 100), (0, y+28, 128, 4))
        pygame.draw.rect(sidebar, (100, 200, 100), (124, y, 4, 32))
    draw_value("Eraser", 14, "o")

colorpicker_active = False
def color_picker_button():
    pygame.draw.rect(sidebar, (223, 223, 223), (0, 384, 128, 32))
    if colorpicker_active:
        pygame.draw.rect(sidebar, (100, 200, 100), (0, 384, 128, 4))
        pygame.draw.rect(sidebar, (100, 200, 100), (0, 384, 4, 32))
        pygame.draw.rect(sidebar, (100, 200, 100), (0, 412, 128, 4))
        pygame.draw.rect(sidebar, (100, 200, 100), (124, 384, 4, 32))
    draw_value("Color Picker", 13, "o")

def sidebar_update():
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
    fill_button()
    clear_button()
    color_picker_button()
    eraser_button()



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
    file_path = filedialog.asksaveasfilename(defaultextension='.png', initialfile="image.png", initialdir=".")
    try:
        img.save(file_path)
    except Exception:
        pass
    exit()
            
def fill():
    for y, row in enumerate(grid.cell_rows):
        for x, col in enumerate(row):
            col.r = current_color[0]
            col.g = current_color[1]
            col.b = current_color[2]
            col.a = current_color[3]

def clear():
    for y, row in enumerate(grid.cell_rows):
        for x, col in enumerate(row):
            col.r = 0
            col.g = 0
            col.b = 0
            col.a = 0

mcp_t = time.time() # Throttle
def colorpicker():
    global colorpicker_active, mcp_t, eraser_active
    if time.time() - mcp_t > 0.1:
        colorpicker_active = not colorpicker_active
        eraser_active = False
    mcp_t = time.time()   

mer_t = time.time() 
def eraser():
    global eraser_active, mer_t, colorpicker_active
    if time.time() - mer_t > 0.1:
        colorpicker_active = False
        eraser_active = not eraser_active
    mer_t = time.time() 

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
    [fill, fill],
    [clear, clear],
    [colorpicker, colorpicker],
    [eraser, eraser],
    [save, save],
    [save, save],
]



# Create mouse reference
mouse = Mouse(grid)


# Function for drawing squares

is_drawing = False

def mouse_update():
    global is_drawing, colorpicker_active, current_color
    # Check for left clicks
    if not pygame.mouse.get_pressed()[0]:
        is_drawing = False
    if pygame.mouse.get_pressed()[0]:
        # If mouse is positioned within the "grid" area, draw.
        if 0 < pygame.mouse.get_pos()[0] < grid_dimensions[0] and 0 < pygame.mouse.get_pos()[1] < grid_dimensions[1]: 
            if colorpicker_active:
                square = grid.cell_rows[mouse.get_square(grid_dimensions, sprite_pixels)[1]][mouse.get_square(grid_dimensions, sprite_pixels)[0]]
                current_color = (square.r, square.g, square.b, square.a)
                return
            is_drawing = True
            if eraser_active:
                grid.cell_rows[mouse.get_square(grid_dimensions, sprite_pixels)[1]][mouse.get_square(grid_dimensions, sprite_pixels)[0]] = RGBA(0,0,0,0)
                return
            grid.cell_rows[mouse.get_square(grid_dimensions, sprite_pixels)[1]][mouse.get_square(grid_dimensions, sprite_pixels)[0]] = RGBA(*current_color)
        # Otherwise, get which button on the sidebar is pressed.
        else:
            try:
                # Try to prevent the mouse going off screen from causing unintended presses
                if not is_drawing:
                    mouse.get_function(sidebar_functions)()
            except TypeError:
                pass


overlay = pygame.Surface(screen_dimensions, pygame.SRCALPHA)

# Create GameHandler
functions_to_call = [sidebar_update, mouse_update]
game = GameHandler(functions_to_call, events, window, frames_per_second)
draw_overlay(overlay)

# Main Loop
game_loop_count = 0
while game_enabled:
    pygame.display.set_caption(str("Pyxelart | 1.0"))
    window.fill((0,0,0))
    grid.draw()
    window.blits([(grid.surface, (0,0)), (sidebar, (512, 0)), (overlay, (0,0))])
    # No more code allowed after this comment unless u have a good reason for it.
    game.update()
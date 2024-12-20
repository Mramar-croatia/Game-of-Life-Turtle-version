from turtle import Screen

from const import *

import grid
from music import MusicPlayer
from grid import GridDrawer
from life import Life

# Set up the screen
screen=Screen()
screen.bgcolor(BACKGROUND_COLOR)
screen.title("Game of Life")
screen.cv._rootwindow.attributes('-fullscreen', True)
screen.tracer(0)

# Get the size of the screen
root = screen._root  # This gets the tkinter root window used by Turtle
x_max = root.winfo_screenwidth() * 0.48  # Full screen width
y_max = root.winfo_screenheight() * 0.48 # Full screen height

# Create a music player object
music_player = MusicPlayer()
screen.listen()

# Create a grid object, determine the number of squares in the grid
n = int((x_max*2)//SQUARE_SIZE) # po x
m = int((y_max*2)//SQUARE_SIZE) # po y

grid_drawer = GridDrawer(n, m, x_max, y_max)
grid_drawer.draw_grid()
grid = grid_drawer.generate_grid(is_random=True)

life_drawer = Life(n, m, x_max, y_max, grid, screen, music_player)
life_drawer.draw_all_life()
life_drawer.update_life()


screen.onkeypress(screen.bye, "q")
screen.onkeypress(screen.bye, "Escape")

screen.onkeypress(life_drawer.update_life, "Right")
screen.onkeypress(life_drawer.update_life, "Return")

screen.onkeypress(life_drawer.increase_speed, "plus")
screen.onkeypress(life_drawer.decrease_speed, "minus")

def reset_life():
	life_drawer.life = [[0 for i in range(m)] for j in range(n)]
screen.onkeypress(reset_life, "r")

def get_cell_from_click(x, y):
    col = int(x / SQUARE_SIZE + x_max // SQUARE_SIZE)
    row = int(y / SQUARE_SIZE + y_max // SQUARE_SIZE)
    if col < n and row < m:
        life_drawer.life[col][row] = 1 - life_drawer.life[col][row]
        life_drawer.draw_all_life()
screen.onclick(get_cell_from_click)

screen.mainloop()
from turtle import Turtle
import random
from const import *

# Class for drawing the grid and also creating the starting grid
class GridDrawer(Turtle):
    '''
    Class for drawing the grid and also creating the starting grid
    '''
    
    # Initialize the grid drawer
    def __init__(self, n: int, m: int, x_max: int, y_max: int):
        
        super().__init__()
        self.hideturtle()
        self.speed(0)
        
        self.n = n
        self.m = m
        self.x_max = x_max
        self.y_max = y_max
        
        
    # Function to draw a single line between two points
    def draw_line(self, x1: int, y1: int, x2: int, y2: int):
        self.penup()
        self.goto(x1,y1)
        self.down()
        self.goto(x2,y2)
        self.penup()
    
    
    # Function to draw the grid
    def draw_grid(self):
        
        self.pencolor('gray')
        self.pensize(GRID_LINE_WIDTH)
        self.pendown()
        
        # Draw vertical lines
        x = -self.x_max
        for i in range(self.n+1):
            self.draw_line(x, -self.y_max, x, self.y_max)
            x += self.x_max*2/self.n
            
        # Draw horizontal lines     
        y = -self.y_max
        for i in range(self.m+1):
            self.draw_line(-self.x_max, y, self.x_max, y)
            y += self.y_max*2/self.m


    # Function to generate the starting grid as a 2d array
    def generate_grid(self, is_random: bool = False) -> list[list[int]]:
        
        grid = [[0 for i in range(self.m)] for j in range(self.n)]
        
        if is_random:
            for i in range(self.n):
                for j in range(self.m):
                    if random.randint(0,CHANCE) == 0:
                        grid[i][j] = 1
        
        return grid
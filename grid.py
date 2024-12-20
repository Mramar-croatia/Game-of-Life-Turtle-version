from turtle import Turtle
import random
from const import *

class GridDrawer(Turtle):
    
    def __init__(self, n, m, x_max, y_max):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        
        self.n = n
        self.m = m
        
        self.x_max = x_max
        self.y_max = y_max
        
    def draw_line(self, x1, y1, x2, y2):
        self.penup()
        self.goto(x1,y1)
        self.down()
        self.goto(x2,y2)
        self.penup()
    
    def draw_grid(self):
        
        self.pencolor('gray')
        self.pensize(3)
        
        x = -self.x_max
        for i in range(self.n+1):
            self.draw_line(x, -self.y_max, x, self.y_max)
            x += self.x_max*2/self.n
            
        y = -self.y_max
        for i in range(self.m+1):
            self.draw_line(-self.x_max, y, self.x_max, y)
            y += self.y_max*2/self.m

    def generate_grid(self, is_random = False):
        
        grid = [[0 for i in range(self.m)] for j in range(self.n)]
        
        if is_random:
            for i in range(self.n):
                for j in range(self.m):
                    if random.randint(0,CHANCE) == 0:
                        grid[i][j] = 1
        
        return grid
from turtle import Turtle, Screen
from const import *
import copy
from music import MusicPlayer

class Life(Turtle):
    '''
    Class for managing "life" in the game of life. It updates the life and draws it on the screen.
    '''
    
    def __init__(self, n: int, m: int, x_max: int, y_max: int, grid: list[list[int]], screen: Screen, music_player: MusicPlayer):
        
        super().__init__()
        self.up()
        self.hideturtle()
        self.speed(0)
        
        self.n = n
        self.m = m
        self.x_max = x_max
        self.y_max = y_max
        
        self.life = grid
        self.screen = screen
        self.music_player = music_player
        
        self.paused = START_PAUSED
        self.update_speed = 20
        
        # Set up the keybinds
        self.screen.onkey(self.pause, "p")
        self.screen.onkey(self.unpause, "u")
        self.screen.onkey(self.change_state, "space")


    # Function to color a single square at a given position
    def draw_square(self, x: float, y: float, size: int, color: str = 'black'):
        
        self.up()
        self.color(color)
        self.goto(x,y)
        self.down()
        self.seth(0)
        
        self.begin_fill()
        
        for i in range(4):
            self.fd(size)
            self.left(90)
            
        self.end_fill()
        

    # Function to draw a single life cell at a given position
    def draw_life(self, x, y):
        
        lx = self.x_max*2/self.n*x - self.x_max
        ly = self.y_max*2/self.m*y - self.y_max
        
        self.draw_square(lx+1,ly+1,SQUARE_SIZE)


    # Function to draw all life cells on the screen
    def draw_all_life(self):
        
        for i in range(self.n):
            for j in range(self.m):
                if self.life[i][j] == 1: self.draw_life(i,j)


    # Function to count the number of neighbors of a cell
    def num_neighbors(self, x, y):
        sum = 0
        
        for i in range(max(x-1,0),min(x+1,self.n-1)+1):
            for j in range(max(y-1,0),min(y+1,self.m-1)+1):
                sum += self.life[i][j]
                
        return sum - self.life[x][y]
    
    
    # Functions to pause and unpause the game
    def pause(self):
        self.paused = True
        self.music_player.pause()
    def unpause(self):
        self.paused = False
        self.music_player.unpause()
        self.screen.ontimer(self.update_life, self.update_speed)
    def change_state(self):
        if self.paused:
            self.unpause()
        else:
            self.pause()
           
    # Functions to update the speed of the game     
    def decrease_speed(self):
        self.update_speed += 10
        
        self.penup()
        self.color('red')
        self.goto(0,0)
        self.write(self.update_speed, font=("Arial", 42, "normal"))
        self.color('black')
        
    def increase_speed(self):
        self.update_speed -= 10
        if self.update_speed <= 5:
            self.update_speed = 5
            
        self.penup()
        self.color('red')
        self.goto(0,0)
        self.write(self.update_speed, font=("Arial", 42, "normal"))
        self.color('black')
            
    # Update all life cells        
    def update_life(self):
        
        newlife = copy.deepcopy(self.life)
        
        for i in range(self.n):
            for j in range(self.m):
                k = self.num_neighbors(i,j)
                if k < 2 or k > 3:
                    newlife[i][j] = 0
                elif k == 3:
                    newlife[i][j] = 1
                    
        self.life = copy.deepcopy(newlife)
        
        self.clear()
        self.draw_all_life()
        self.screen.update() 
        
        if not self.paused:
            self.screen.ontimer(self.update_life, self.update_speed)
import turtle
import pygame

# Initialize pygame for music
pygame.mixer.init()
pygame.mixer.music.load("Katyusha.mp3")
pygame.mixer.music.play(-1)  # Loop the music indefinitely

# Create a screen instance
screen = turtle.Screen()

# Set the screen to fullscreen mode
screen.bgcolor("yellow")             # Set background color (optional)
screen.title("Turtle Graphics")     # Set title of the window (optional)
screen.cv._rootwindow.attributes('-fullscreen', True)  # Enable fullscreen mode

# You can create a turtle to draw
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

t.penup()
t.goto(0, 0)
t.color("dark red")
t.write("COMMUNIST TANK", align="center", font=("Arial", 75, "bold"))

# Keep the window open
screen.mainloop()
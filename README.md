**John Conway's Game of Life, Python turtle version**

The program is a game, a version of classic John Conway's game of life but made in python using the built-in module "turtle".


GAME OF LIFE
Game of life is simple. It plays itself and there is no input needed from the user (but there is a way of interacting).
It is played on a grid consisting of colored and non-colored spaces. Each "turn" the following happens:

- Each colored cell with one or no neighbors dies.
- Each colored cell with four or more neighbors dies.
- Each colored cell with two or three neighbors dies.

- Each non-colored cell with three neighbors becomes colored.

In the background are playing: "Bella Ciao", "Bandiera Rossa", "Kalinka", "Katyusha", "Uz Maršala Tita".


To run the program one must only install the modules required from the requirements.txt file, than run main.py.

There are certain commands that can be used once the program starts:
"q" - exit
"p" - pause
"u" - unpause
"space" - pause/unpause
"+" - increase speed
"-" - decrease speed
"->" - next turn
"r" - reset all


By tweaking the constants in const.py file you can further change the way game works.
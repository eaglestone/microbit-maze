# Simple maze game by Tim Eaglestone, February 2016
#
# This program has been placed into the public domain.

from microbit import *

# screen constants
WIDTH = 20
HEIGHT = 10
MAZE = [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,
        4,0,4,0,0,0,0,0,0,0,4,0,0,0,0,0,0,4,0,4,
        4,0,4,0,4,4,4,0,4,0,4,0,4,4,0,4,0,4,0,4,
        4,0,4,0,4,0,4,0,4,0,4,0,4,0,0,4,0,0,0,4,
        4,0,0,0,4,0,0,0,4,0,0,0,4,0,4,4,0,4,4,4,
        4,4,4,4,4,4,0,4,4,4,4,4,4,0,0,4,0,0,0,4,
        4,0,0,0,0,0,0,4,0,0,0,0,4,4,4,4,0,4,0,4,
        4,4,0,4,4,4,4,4,0,4,0,4,4,0,0,0,0,4,0,4,
        4,0,0,0,0,0,0,0,0,4,0,0,0,0,4,4,0,4,0,4,
        4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]

# set accelerometer sensitivity
SENSITIVITY = 100

# initial positions
old_x_pos = x_pos = 1
old_y_pos = y_pos = 1


def display_maze(x_pos,y_pos):    
    x_home = x_pos-2
    y_home = y_pos-2
    
    # stop it going out of bounds
    if x_home < 0: x_home = 0
    if y_home < 0: y_home = 0
    if x_home >= WIDTH-5: x_home = WIDTH - 5 
    if y_home >= HEIGHT-5: y_home = HEIGHT - 5
    
    # draw the maze
    for y in range(0,5):
        for x in range(0,5):
            display.set_pixel(x,y,MAZE[(WIDTH*(y_home+y) + (x_home+x))])


def display_player(x_pos, y_pos):
    # move the ball when at the edge
    # because the maze does not move
    x = y = 2
    if x_pos < 2: x = x_pos 
    if y_pos < 2: y = y_pos 
    if x_pos >= WIDTH - 2: x = 5 - (WIDTH-x_pos) 
    if y_pos >= HEIGHT - 2: y = 5 - (HEIGHT-y_pos) 
    
    display.set_pixel(x,y,9)


def player_can_move(x_pos, y_pos):
    return MAZE[(WIDTH*(y_pos) + (x_pos))] == 0
        
# Display the maze and start the input loop
while(True):
    horiz = accelerometer.get_x()
    vert = accelerometer.get_y()
    
    if horiz > 0 and abs(horiz) > SENSITIVITY:
        if x_pos < WIDTH-2 and player_can_move(x_pos+1,y_pos): x_pos += 1
    
    if horiz < 0 and abs(horiz) > SENSITIVITY:
        if x_pos > 0 and player_can_move(x_pos-1,y_pos): x_pos -= 1
    
    if vert > 0 and abs(vert) > SENSITIVITY:
        if y_pos < HEIGHT-2 and player_can_move(x_pos,y_pos+1): y_pos += 1
    
    if vert < 0 and abs(vert) > SENSITIVITY:
        if y_pos > 0 and player_can_move(x_pos,y_pos-1): y_pos -= 1
        
    display_maze(x_pos,y_pos)
    display_player(x_pos, y_pos)
    sleep(80)

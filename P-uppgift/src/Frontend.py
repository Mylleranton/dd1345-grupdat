''' 
    @author Anton Möller
    File: Frontend.py
    2015, November 24th 
'''
from src.Backend import *;
import src.Static;
from src.Validate import *;

    
# The basic movement/shoot prompt. If player want to move, move_shoot is called,
# if the player wants to shoot, shoot_prompt is called. If the input validation is negative,
# just prompt the player again.
def basic_prompt():
    move_shoot_input = input(MSG_MOVE_OR_SHOOT);
    move_shoot = getAssertMoveShoot(move_shoot_input);
    if not move_shoot == None:
        if move_shoot == MOVE:
            move_prompt();
            return;
        elif move_shoot == SHOOT:
            shoot_prompt(0, backend.getCurrentRoom());
            return;
    else:
        basic_prompt();
        return;
    
# Handles player movement. Prompts for a direction, if validation fails, just ask again, otherwise
# we move the player and then returns to the basic_prompt.
def move_prompt():
    direction_input = input(MSG_MOVE_DIRECTION);
    direction = getAssertDirection(direction_input);
    if not direction == None:
        backend.move(direction);
        basic_prompt();
        return;
    else:
        move_prompt();
        return;
    
# Handles player shooting an arrow. Prompts for a direction, validates it and shoots an arrow in that direction,
# then calls itself recursively until the player has directed the arrow through all three rooms. 
def shoot_prompt(itr,roomFrom):
    if backend.getArrowsLeft() < 1:
        print(MSG_NO_ARROWS_LEFT);
        basic_prompt();
        return;
            
    for i in range(itr,3):
        print(MSG_SHOOT[i]);
        direction_input = input(MSG_SHOOT_DIRECTION);
        
        direction = getAssertDirection(direction_input);
        if not direction == None:
            backend.shoot(direction, roomFrom);
            room = roomFrom.go(direction);
            shoot_prompt(i+1,room);
            return;
        else:
            shoot_prompt(i,roomFrom);
            return;
                    
    backend.setCurrentArrows(backend.getArrowsLeft()-1);
    basic_prompt();
    
print(MSG_INTRO);
backend = Backend();
basic_prompt();


        
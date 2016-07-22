''' 
    @author Anton Möller
    File: Validated.py
    2015, November 24th 
'''
from src.Static import *;

# Asserts that the given argument is of the correct type and returns a 
# standardised action, otherwise None.
def getAssertMoveShoot(move_shoot):
    if not isinstance(move_shoot, str):
        print(MSG_ERROR_TYPE);
        return None;
    move_shoot = move_shoot.lower();
    
    if move_shoot in MOVE_INPUT:
        return MOVE;
    elif move_shoot in SHOOT_INPUT:
        return SHOOT;
    else:
        print(MSG_MOVE_SHOOT_ERROR);
        return None;
    
# Asserts that the given argument is of the correct type and returns a 
# standardised direction, otherwise None. 
def getAssertDirection(direction):
    if not isinstance(direction, str):
        print(MSG_ERROR_TYPE);
        return None;
    if (direction == DIRECTION_EAST or direction == DIRECTION_WEST or direction == DIRECTION_NORTH or direction == DIRECTION_SOUTH):
        return direction;
    
    direction = direction.lower();
    
    if direction in DIRECTION_INPUT_N:
        return DIRECTION_NORTH;
    elif direction in DIRECTION_INPUT_S:
        return DIRECTION_SOUTH;
    elif direction in DIRECTION_INPUT_W:
        return DIRECTION_WEST;
    elif direction in DIRECTION_INPUT_E:
        return DIRECTION_EAST;
    else:
        print(MSG_DIRECTION_ERROR);
        return None;

# Asserts that the given argument is of the correct type and returns a 
# standardised difficulty, otherwise None.
def getAssertDifficulty(difficulty):
    if not isinstance(difficulty, str):
        print(MSG_ERROR_TYPE);
        return None;
    difficulty = difficulty.lower();
    
    if difficulty in DIFFICULTY_EASY_INPUT:
        print(MSG_DIFFICULTY_CHOICE,DIFFICULTY_EASY_INPUT[0]);
        return DIFFICULTY_EASY;
    elif difficulty in DIFFICULTY_NORMAL_INPUT:
        print(MSG_DIFFICULTY_CHOICE,DIFFICULTY_NORMAL_INPUT[0]);
        return DIFFICULTY_NORMAL;
    elif difficulty in DIFFICULTY_HARD_INPUT:
        print(MSG_DIFFICULTY_CHOICE,DIFFICULTY_HARD_INPUT[0]);
        return DIFFICULTY_HARD;
    else:
        print(MSG_DIFFICULTY_ERROR);
        return None;
        
    
    
    
    

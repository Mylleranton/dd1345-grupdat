''' 
    @author Anton Möller
    File: main_backend.py
    2015, November 24th 
'''
from src.Room import *;
from random import randint, shuffle;
from src.Validate import getAssertDifficulty;
from src.Static import *;

# Handles all backend operations (all game actions) for the game.
class Backend():
    
    # On initialization a new set of rooms are generated, and the difficulty is set.
    # Also makes sure that the starting room has no danger in it.
    def __init__(self):
        self.__difficulty = self.__initializeDifficulty();
        self.__roomList = self.__initializeRoomlist(RoomList());
        self.__arrowsLeft = NUMBER_OF_ARROWS;
        self.__currentRoom = self.getRandomRoom();
        
        while not self.__currentRoom.getDanger() == NONE:
            self.__currentRoom = self.getRandomRoom();
        
        self.__playerSwitchedRoom(self.__currentRoom);
    
    def getCurrentRoom(self):
        return self.__currentRoom;
    
    def getArrowsLeft(self):
        return self.__arrowsLeft;
    
    def setCurrentArrows(self, arrows):
        self.__arrowsLeft = arrows;
    
    def getDifficulty(self):
        return self.__difficulty;
    
    def getRoomList(self):
        return self.__roomList;
    
    def getRandomRoom(self):
        return self.__roomList.get(randint(0, len(self.__roomList) - 1));
    
    # Move the player in a specified direction
    def move(self, direction):
        ''' Moves the player in the specified direction. Direction must be valid, otherwise an error is thrown '''
        assert not getAssertDirection(direction) == None, 'ERROR: Direction is not valid';
        self.__currentRoom = self.__currentRoom.go(direction);
        
        assert isinstance(self.__currentRoom, Room), 'ERROR: Switched to non-existent room';
        if self.getDifficulty() == DIFFICULTY_HARD:
            self.__wumpusMove();
        
        self.__playerSwitchedRoom(self.__currentRoom);
    
    # Moves the player to a random room (Danger == Bat)
    def __batMove(self):
        self.__currentRoom = self.getRandomRoom();
        assert isinstance(self.__currentRoom, Room), 'ERROR: Switched to non-existent room';
        print(MSG_BAT_MOVE, self.__currentRoom.getId());
        self.__playerSwitchedRoom(self.__currentRoom);
    
    # Moves Wumpus one room closer to the player's position
    def __wumpusMove(self):
        room = self.__currentRoom;
        wumpus_room = room;
        steps_E = 0;
        steps_N = 0;
        
        # Find Wumpus'es room
        while not wumpus_room.getDanger() == WUMPUS:
            wumpus_room = wumpus_room.go(DIRECTION_EAST);
        
        # Find the pathlength from the player's room to wumpus' in all directions (N/S/E/W)            
        while not room.getId() == wumpus_room.getId():
            room = room.go(DIRECTION_EAST);
            steps_E += 1;
            
        room = self.__currentRoom;
        while not room.getId() == wumpus_room.getId():
            room = room.go(DIRECTION_NORTH);
            steps_N += 1;
            
        steps_S = NUMBER_OF_ROOMS - steps_N;
        steps_W = NUMBER_OF_ROOMS - steps_E;
        
        direction = None;
        # Find out the shortest path from wumpus to the player and move in that direction
        shortestPath = min(steps_N, steps_S, steps_E, steps_W);
        if steps_E == shortestPath:
            direction = DIRECTION_EAST;
        elif steps_W == shortestPath:
            direction = DIRECTION_WEST;
        elif steps_N == shortestPath:
            direction = DIRECTION_NORTH;
        elif steps_S == shortestPath:
            direction = DIRECTION_SOUTH;
        else:
            raise Exception('Invalid move direction');
                
        wumpus_room.setDanger(wumpus_room.go(direction).getDanger());
        wumpus_room.go(direction).setDanger(WUMPUS);       
        
        print(MSG_WUMPUS_MOVED);
            
    # Shoots an arrow in a specified direction from a given room
    def shoot(self, direction, roomFrom): 
        ''' Shoots an arrow from the Room roomFrom in the specified direction. Direction and roomFrom must be valid, or else an exception is raised '''
        assert not getAssertDirection(direction) == None, 'Error: Direction is not valid';
        hitRoom = roomFrom.go(direction);
        assert isinstance(hitRoom, Room), 'Shot a non-existent room. roomFrom must be of Room.class';
        self.__roomGotHit(hitRoom);
        
    # Handles the effects of a player switching rooms and the reprecussions from that.
    def __playerSwitchedRoom(self, newRoom):
        if newRoom.getDanger() == WUMPUS:
            self.__finish(MSG_PLAYER_LOSE_WUMPUS);
        elif newRoom.getDanger() == HOLE:
            self.__finish(MSG_PLAYER_LOSE_HOLE);
        elif newRoom.getDanger() == BAT:
            self.__batMove();
            return;
        
        print(MSG_CURRENT_ROOM, self.__currentRoom.getId());
        print(MSG_ROOMS_NEAR, newRoom.getSurroundingRooms());
        
        dangers = newRoom.getSurroundingDangers();
        if WUMPUS in dangers:
            print(MSG_WUMPUS_NEAR);
        elif BAT in dangers:
            print(MSG_BAT_NEAR);
        elif HOLE in dangers:
            print(MSG_HOLE_NEAR);
            
    # Handles the effects of a room being hit by an arrow
    def __roomGotHit(self, hitRoom):
        if hitRoom.getDanger() == WUMPUS:
            print(MSG_PLAYER_SHOT_WUMPUS);
            self.__finish(MSG_PLAYER_WIN);
        elif hitRoom.getDanger() == BAT:
            hitRoom.setDanger(NONE);
            print(MSG_PLAYER_SHOT_BAT);
        elif hitRoom == self.__currentRoom:
            self.__finish(MSG_PLAYER_LOSE_SHOT);
            
    # Handles the different ending states of the game
    def __finish(self, message):
        print(message);
        quit();
    
    # Initializes and returns a roomlist with randomly generated rooms from the
    # parameters in Static.py with dangers and sets the game difficulty 
    def __initializeRoomlist(self, roomList = RoomList()):
        def __initRooms():
            # Creates the rooms
            tunnels = [];
            for i in range(0, NUMBER_OF_ROOMS):
                roomList.put(Room(i));
                tunnels += [i];
            
            # Connect the rooms
            shuffle(tunnels);
            for index_east in range(0, NUMBER_OF_ROOMS):
                room = roomList.get(tunnels[index_east]);
                index_west = index_east;
                
                if index_east + 1 == len(tunnels):
                    index_east = -1 ;
        
                room.setEast(roomList.get(tunnels[index_east + 1]));
                room.setWest(roomList.get(tunnels[index_west - 1]));
            
            shuffle(tunnels);
            for index_north in range(0, NUMBER_OF_ROOMS):
                room = roomList.get(tunnels[index_north]);
                index_south = index_north;
                if index_north + 1 == len(tunnels):
                    index_north = -1;
                
                room.setNorth(roomList.get(tunnels[index_north + 1]));
                room.setSouth(roomList.get(tunnels[index_south - 1]));
                
        def __initDangers():
            # Generate the dangers
            bats = int(NUMBER_OF_ROOMS * BAT_propability[self.__difficulty]);
            holes = int(NUMBER_OF_ROOMS * HOLE_propability[self.__difficulty]);
            none = NUMBER_OF_ROOMS - bats - holes - WUMPUS_number;
            dangers = list(bats * [BAT]);
            dangers += holes * [HOLE];
            dangers += none * [NONE];
            dangers += WUMPUS_number * [WUMPUS];
            
            
            shuffle(dangers);
            assert len(dangers) == NUMBER_OF_ROOMS, 'Probability failed';
            
            # Apply the dangers to the rooms
            for index in range(0, len(dangers)):
                roomList.get(index).setDanger(dangers[index]);
                            
        __initRooms();
        __initDangers();        
        return roomList;
    
    def __initializeDifficulty(self):
        # Prompts for a game difficulty 
        difficulty = getAssertDifficulty(input(MSG_DIFFICULTY));
        while difficulty == None:
            difficulty = getAssertDifficulty(input(MSG_DIFFICULTY));
        if difficulty == DIFFICULTY_HARD:
            print(MSG_DIFFICULTY_HARD_INFO);
            
        return difficulty;
        
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


''' 
    @author Anton Möller
    File: Room.py, containing Room.class and RoomList.class
    2015, November 24th 
'''
from src import Static;
from src.Validate import getAssertDirection;

# Room.class is a room object defining a room by its ID, neighbours and a specified danger.
class Room():
    __north = None;
    __south = None;
    __west = None;
    __east = None;
    
    def __init__(self, mId, danger = Static.NONE):
        self.__mId = mId;
        self.__danger = danger;
    
    def setDanger(self, danger):
        assert (danger == Static.WUMPUS or danger == Static.NONE or danger == Static.BAT or danger == Static.HOLE),'Must be a valid danger'
        self.__danger = danger;
        
    def getDanger(self):
        return self.__danger;
    
    def getId(self):
        return self.__mId;
    
    # Returns the neighbour in the given direction
    def go(self, direction):
        if not getAssertDirection(direction) == None:
            if direction == Static.DIRECTION_NORTH:
                return self.__north;
            elif direction == Static.DIRECTION_SOUTH:
                return self.__south;
            elif direction == Static.DIRECTION_EAST:
                return self.__east;
            elif direction == Static.DIRECTION_WEST:
                return self.__west;
        else:
            #raise Exception('Requested direction is not valid');
            return None;
    
    def setNorth(self, room):
        assert isinstance(room, Room),'Must be of type Room.class'
        self.__north = room;
    def setSouth(self, room):
        assert isinstance(room, Room),'Must be of type Room.class'
        self.__south = room;
    def setEast(self, room):
        assert isinstance(room, Room),'Must be of type Room.class'
        self.__east = room;
    def setWest(self, room):
        assert isinstance(room, Room),'Must be of type Room.class'
        self.__west = room;
    
    def __str__(self):
        return str(self.mId) + ' ' + self.danger;
    
    # Returns the dangers of the surrounding rooms
    def getSurroundingDangers(self):
        return [self.__north.getDanger(), self.__south.getDanger(), self.__east.getDanger(), self.__west.getDanger()];
    
    # Returns the surrounding rooms themselves
    def getSurroundingRooms(self):
        return [self.__north.getId(), self.__south.getId(), self.__east.getId(), self.__west.getId()];
         
# RoomList.class holds a list of Room objects, built on a dictionary.
class RoomList():
    def __init__(self):
        self.__mList = {};
    
    def put(self,item):
        assert isinstance(item, Room), 'Can only put rooms into a roomlist!';
        self.__mList[str(item.getId())] = item;
        
    def get(self, ID):
        return self.__mList.get(str(ID), None);
    
    def isempty(self):
        return (self.__len__() == 0);    
    
    def __str__(self):
        return self.__mList.__str__();
    
    def __iter__(self):
        return iter(self.__mList.values());
    
    def __len__(self):
        return self.__mList.__len__();
    
''' 
    @author Anton Möller
    File: Static.py
    2015, November 24th 
'''
# Static.py holds static values and messages for simplicity.
# Also contains accepted input and actions.

### Game settings ###
NUMBER_OF_ROOMS = 20;
NUMBER_OF_ARROWS = 5;
HOLE_propability = [0.1, 0.2, 0.2];
BAT_propability = [0.15, 0.3, 0.3];

### Static action/direction markers ###
NONE = 'D0None';
WUMPUS = 'D1Wumpus';
WUMPUS_number = 1;
BAT = 'D2Bat';
HOLE = 'D3Hole';
DIRECTION_NORTH = 'Dir_N';
DIRECTION_SOUTH = 'Dir_S';
DIRECTION_WEST = 'Dir_V';
DIRECTION_EAST = 'Dir_Ö';
MOVE = 'Action_Move';
SHOOT = 'Action_Shoot';
DIFFICULTY_NORMAL = 1;
DIFFICULTY_EASY = 0;
DIFFICULTY_HARD = 2;

### Accepted inputs for various actions ###
DIRECTION_INPUT_E = ['Ö', 'ö', 'öst', 'öster'];
DIRECTION_INPUT_W = ['V', 'v', 'väst', 'väster'];
DIRECTION_INPUT_N = ['N', 'n', 'norr', 'nord'];
DIRECTION_INPUT_S = ['S', 's', 'syd', 'söder'];
MOVE_INPUT = ['F', 'f', 'flytta', 'förflytta'];
SHOOT_INPUT = ['S', 's', 'skjut', 'skjuta'];
DIFFICULTY_EASY_INPUT = ['lätt', 'l', '0'];
DIFFICULTY_NORMAL_INPUT = ['normal', 'medel', 'n', '1'];
DIFFICULTY_HARD_INPUT = ['svår', 'svårt', 's', '2'];

### In-game messages ###
MSG_WUMPUS_NEAR = 'Jag känner lukten av Wumpus!';
MSG_BAT_NEAR = 'Jag hör fladdermöss!';
MSG_HOLE_NEAR = 'Jag känner vinddrag från ett bottenlöst hål...';
MSG_ROOMS_NEAR = 'Härifrån kan man komma till följande rum:';
MSG_BAT_MOVE = 'Du känner fladdermusvingar mot kinden och lyfts uppåt\nEfter en kort flygtur släppte fladdermössen ner dig i rum';
MSG_WUMPUS_MOVED = 'Wumpus hörde dina fotsteg och är nu ett rum närmre dig!';

MSG_PLAYER_WIN = 'Du vann!';
MSG_PLAYER_LOSE_SHOT = 'Du sköt dig själv, game over.';
MSG_PLAYER_LOSE_WUMPUS = 'Wumpus käkade dig. Game over.';
MSG_PLAYER_LOSE_HOLE = 'Du trillade ned i ett bottenlöst hål. Synd. Game over.';

MSG_PLAYER_SHOT_BAT = 'Du sköt en fladdermus';
MSG_PLAYER_SHOT_WUMPUS = 'Du sköt WUMPUS!!!';

MSG_MOVE_OR_SHOOT = 'Vill du förflytta dig eller skjuta (F/S)?';
MSG_SHOOT = ['Pilen lämnar första rummet.', 'Pilen lämnar andra rummet.', 'Pilen lämnar tredje rummet.'];
MSG_SHOOT_DIRECTION = 'Vilken riktning (N/S/V/Ö)?';
MSG_MOVE_DIRECTION = 'Vilken riktning (N/S/V/Ö)?';

MSG_DIRECTION_ERROR = 'Du måste välja mellan Norr (N), Söder (S), Väster (V) eller Öster (Ö).';
MSG_ERROR_TYPE = 'Du måste skriva en bokstav.';
MSG_MOVE_SHOOT_ERROR = 'Du måste välja mellan att förflytta dig (F) eller att skjuta en pil (S)';
MSG_NO_ARROWS_LEFT = 'Du har tyvärr inga pilar kvar. May the odds be in your favor...';

MSG_DIFFICULTY = 'Vilken svårighetsgrad vill du spela med, lätt (0), normal (1) eller svår (2)?';
MSG_DIFFICULTY_ERROR = 'Du måste välja mellan lätt (0), normal (1) eller svår (2).';
MSG_DIFFICULTY_CHOICE = 'Du valde svårighetsgrad';
MSG_DIFFICULTY_HARD_INFO = 'Wumpus kan nu höra dig gå runt och kommer hela tiden röra sig mot dig!';
MSG_CURRENT_ROOM = 'Du är nu i rum';
MSG_INTRO = 'Du befinner dig i kulvertarna under Nada, där den glupske Wumpus bor. För att undvika att bli uppäten måste du skjuta Wumpus med din pil och båge. Kulvertarna har 20 rum som är förenade med smala gångar. Du kan röra dig åt norr, öster, söder eller väster från ett rum till ett annat\nHär finns dock faror som lurar. I vissa rum finns bottenlösa hål. Kliver du ner i ett sådant dör du omedelbart. I andra rum finns fladdermöss som lyfter upp dig, flyger en bit och släpper dig i ett godtyckligt rum. I ett av rummen finns Wumpus, och om du vågar dig in i det rummet blir du genast uppäten. Som tur är kan du frå̊n rummen bredvid känna vinddraget från ett avgrundshål eller lukten av Wumpus. Du får också\ni varje rum reda på vilka rum som ligger intill.\nFör att vinna spelet måste du skjuta Wumpus. När du skjuter iväg en pil förflyttar den sig genom tre rum - du kan styra vilken riktning pilen ska välja i varje rum. Glöm inte bort att tunnlarna vindlar sig på oväntade sätt. Du kan råka skjuta dig själv...\nDu har fem pilar. Lycka till!\n-----------------------------------';


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
        
    
    
    
    

        
        
        

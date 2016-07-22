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
        
        
        
        
        

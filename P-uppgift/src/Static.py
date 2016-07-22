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




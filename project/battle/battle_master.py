from enum import Enum
from project.battle import battle_classes as bc
from project.print_statements import battle as p
from project.print_statements import commands as com
from project.player_name import name_player as response

COMPLETE = 0
IN_PROGRESS = 1

NO = 0
YES = 1

class Difficulty(Enum):
    UNKNOWN = 0
    EASY = 1
    MEDIUM = 2
    HARD = 3

def confirm_difficulty(difficulty):
    confirmed = NO

    p.selected_difficulty(difficulty.name)
    
    status = IN_PROGRESS
    while(status):
        confirmation = input(p.yes_or_no())
        confirmation = confirmation.lower()

        invalid = response.validateInput(confirmation)
        if(not(invalid)):
            status = COMPLETE
            if(confirmation == "y"):
                confirmed = YES
            else:
                confirmed = NO
        else:
            status = IN_PROGRESS
    return confirmed

def difficulty_selection(option):
    selection = option.upper()
    for d in Difficulty:
        if(selection == d.name):
            return d
    return Difficulty.UNKNOWN

def init_battle(name):
    difficulty_status = IN_PROGRESS
    while(difficulty_status):
        p.difficulty_options()
        com.input_command()
        option = input()
        difficulty = difficulty_selection(option)
        if(difficulty != Difficulty.UNKNOWN):
            confirmation = confirm_difficulty(difficulty)
            if(confirmation == YES):
                difficulty_status = COMPLETE
            else:
                difficulty_status = IN_PROGRESS
        else:
            p.unknown_difficulty()
            difficulty_status = IN_PROGRESS
    
    # add fighting class selection here
    fighting_class = bc.Fighter   
    player_info = bc.Player(name, fighting_class)     
    # add option for mode (such as RANDOM BATTLE or CUSTOM BATTLE)
            
    p.all_set(name)
    return difficulty, player_info

def battle_engine(settings, player):
    
    return 0
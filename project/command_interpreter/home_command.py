import numpy as np
from project.print_statements import commands as com
from project.battle import battle_master as bm

# STATUS CODES
EXIT = 0
BATTLE = 1
HELP = 2
UNKNOWN = 3
NO_COMMAND = 4

def readCommand():
    cmd = input()
    return cmd

def parseCommand(cmd):
    parse = cmd.split()
    return parse

def executeCommand(cmd, player_name):
    for c in cmd:
        match c:
            case "exit":
                com.exitCommand(player_name)
                return EXIT
            case "battle":
                com.battleCommand()
                bm.init_battle(player_name)
                return BATTLE
            case "help":
                com.helpCommand()
                return HELP
            case _:
                com.unknownCommand()
                return UNKNOWN
    return NO_COMMAND
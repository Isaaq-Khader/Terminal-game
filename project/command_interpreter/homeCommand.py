import numpy as np
from project.print_statements import commands as com

def readCommand():
    cmd = input()
    return cmd

def parseCommand(cmd):
    parse = cmd.split()
    return parse

def executeCommand(cmd):
    for c in cmd:
        match c:
            case "exit":
                com.exitCommand()
                return 0
            case "battle":
                com.battleCommand()
                return 1
            case "help":
                com.exitCommand()
                return 1
            case _:
                com.unknownCommand()
                return 2
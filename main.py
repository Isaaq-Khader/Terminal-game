import numpy as np
from project.player_name import name_player as pn 
from project.print_statements import greeting
from project.command_interpreter import home_command
from project.print_statements import introduction

def main():
    greeting.welcome()
    name = pn.namePlayer()
    introduction.intro(name)

    cmd = ""
    gameIsActive = True

    while(gameIsActive):
        cmd = home_command.readCommand()
        parseCMD = home_command.parseCommand(cmd)
        returnCode = home_command.executeCommand(parseCMD, name)
        
        gameIsActive = returnCode


    return 0

main()
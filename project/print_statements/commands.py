def exitCommand(name):
    print("\nThanks for playing, " + name + "!\n")

def battleCommand():
    print("Let's battle!\n")

def helpCommand():
    print("\nOptions:")
    print("battle")
    print("exit")
    print("help")
    print("**NOTE: Commands are case sensitive (for now)\n")

def unknownCommand():
    print("UNKNOWN COMMAND!\n")

def input_command():
    print("> ", end=" ")
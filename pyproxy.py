import sys
import os

while True:
    print(sys.argv)

    exitIM = False

    with open(sys.argv[1], 'r') as r:
        split1 = r.read().split("!--_--~")
        print(len(split1))
        if len(split1) > 3:
            print("PYPROXY ERROR: Too many split tags")
            input()
            sys.exit()
        elif len(split1) == 2:
            print("PYPROXY ERROR: No ending split tag")
            input()
            sys.exit()
        elif len(split1) == 1:
            pass
        else:
            modules = split1[1].split("\n")
            print(modules)
            modules.pop(0)
            modules.pop(len(modules)-1)
            if "SUBORDINATE" in modules:
                exitIM = True
                modules.remove("SUBORDINATE")

            for module in modules:
                try:
                    exec(f"import {module}")
                except ImportError:
                    os.system(f"py -m pip install {module}")

    os.system(f'py "{sys.argv[1]}"')

    if exitIM:
        print("Exited Immediately")
        sys.exit()
    else:
        print("Exited. Would you like to restart the program? (Y/N)")
        command = input("- ")
        if "COMMAND" in command:
            commandS = command.split(" ")
            if len(commandS) <= 2:
                pass
            else:
                if commandS[1] == "start":
                    os.system(f'py "{{ PATH TO PROGRAM MANAGER }}" {commandS[2]}')
                    sys.exit()
                
        elif command in ("Y", "y", "yes", "restart"):
            continue
        
        else:
            input("You can now close this window")
            sys.exit()
            break
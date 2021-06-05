import time, random
#made by JaCrispy4939
#feel free to make edits but don't steal the code and name it yours

# Edited by gtdt

def helpMenu():
    print('''\033[2J\033[1;1H
                    Help menu

    1. If you want to receive the ansvers press
    [enter] without any text in your choice input.

    2. If you want to exit application type [exit]
    or just press [ctrl + c]
    ''')

def exitAndMessage():
    print("\ngoodbye")
    time.sleep(1.5)
    exit()

def main():

    helpMenu()

    try:

        while True:

            vars = []

            chooseTimes = 1
            stillChoosing = True
            while stillChoosing:

                choice = input(f"choice {chooseTimes}: ")
                if choice == "exit":
                    exitAndMessage()

                if choice == "":
                    stillChoosing = False
                else:
                    vars.append(choice)

                chooseTimes += 1

            helpMenu()
            print (f'Answer: {vars[random.randint(1, len(vars)-1)]}\n')

    except:
        try:
            exitAndMessage()
        except:
            exit()

if __name__ == '__main__': main()

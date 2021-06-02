import random
import time
#made by JaCrispy4939
#feel free to make edits but dont steal the code and name it yours
while True:
    choice1 = input("choice 1: ")
    if choice1 == "exit":
        print("\ngoodbye")
        time.sleep(1.5)
        quit()
    choice2 = input("Choice 2: ")
    if choice2 == "exit":
        print("\ngoodbye")
        time.sleep(1.5)
        quit()
    vars = [choice1,choice2]

    print (random.sample(vars, 1))

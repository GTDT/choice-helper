from random import randint
from time import sleep

#made by JaCrispy4939 and edited by gtdt
#feel free to make edits but dont steal the code and name it yours
def main():
    choices = []
    while True:
        choice = input("add choice: ")
        if choice == "": break
        choices.append(choice)

    print( f" Choices: {choices} \n Result: {choices[randint(0, len(choices)-1)]}" )
	
if __name__ == "__main__":
    main()

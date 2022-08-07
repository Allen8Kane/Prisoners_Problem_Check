from operator import imod
from random import shuffle
import os
from pathlib import Path


def prisonerProblem(debug=False):
    if debug:
        my_file = Path("./result.txt")
        if my_file.is_file():
            os.remove("./result.txt")
    cells = list(range(100))
    prisoners = list(range(100))
    shuffle(cells)
    shuffle(prisoners)
    for prisoner in prisoners:
        game_over = True
        choose_num = prisoner
        for i in range(1,50 + 1):
            if debug:
                # print(f"#{i} prisoner[{prisoner}] open {choose_num} find {cells[choose_num]}") # too many text for console
                with open('result.txt', 'a') as f:
                    f.write(f"#{i} prisoner[{prisoner}] open {choose_num} find {cells[choose_num]}\n")
                
            if cells[choose_num] == prisoner:
                game_over = False
                break
            else:
                choose_num = cells[choose_num]
        if game_over:
            if debug:
                with open('result.txt', 'a') as f:
                    f.write("lose")
            return 'lose'  
    else:
        if debug:
                with open('result.txt', 'a') as f:
                    f.write("win")
        return 'win'

def checkPrecent():
    result = []
    for i in range(100):
        result.append(prisonerProblem())
    print('Win -> ', len([i for i, x in enumerate(result) if x == "win"]))
    print('Lose -> ', len([i for i, x in enumerate(result) if x == "lose"]))

if __name__ == "__main__":
    checkPrecent()
    print(prisonerProblem(debug=True))


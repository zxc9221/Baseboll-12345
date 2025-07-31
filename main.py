from random import randint
from game import Game
from game_result import GameResult


def CLI_Base_ball():
    game = Game()
    while(True):
        s = str(randint(102, 987))
        if len(set(s)) == 3:
            game.question = s
            break
    while(True):
        result = game.guess(input("입력: "))
        print(result.solved, result.strikes, result.balls)
        if(result.solved == True):
            break

CLI_Base_ball()
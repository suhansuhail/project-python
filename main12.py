import random
import math

def play():
    user = input("What's your choise? 'r' for rock, 'p' for paper, 's' for scissors\n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
       return "You and the computer have both chosen {}. it's a tie.".format(computer)

    # r > s, s > p, p > r
    if is_win(user, computer):
        return "You have chosen {} and the computer has chosen {}. You won!".format(user, computer)

    return "You have chosen {} and the computer has chosen {}. You lost :(".format(user, computer)

def is_win(player, opponent):
    # return true is the player beats the opponent
    # winning conditions: r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

def play_best_of(n):
    # play against the computer until someone wins best of n games
    # to win, you must win ceil(n/2) games (ie 2/3, 3/5, 4/7)
    player_win = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    print(wins_necessary)

if __name__ == '__main__':
    play_best_of(3) # 2
    play_best_of(9) # 5
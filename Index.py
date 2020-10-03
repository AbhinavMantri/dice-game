import sys
import random
import msvcrt
from functools import cmp_to_key

from player.player import Player

try:
    n = int(sys.argv[1])
    m = int(sys.argv[2])
except ValueError:
    print("Invalid input!!!")
    sys.exit()

players = dict()
player_queue = []
winners = []

for i in range(1, n + 1):
    players[i] = Player(i)
    player_queue.append(i)

random.shuffle(player_queue)

initial_queue = [] + player_queue


# validating player's score
def is_valid_score(player, score):
    return (player.get_score() + score) <= m


# rolling dice
def roll_dice(player):
    score = random.randint(1, 6)
    print("Player-" + str(player.get_number()) + " got score " + str(score))

    if score == 1 and score == player.get_prev_score():
        print("Warning: Player-" + str(player.get_number()) + " you have got 1 score twice continuously")

    return score


# add win status to the player
def add_win(player):
    player.set_won(True)
    winners.append(player.get_number())


# add score to the player
def add_score(player, score):
    player.set_prev_score(score)
    player.set_score(player.get_score() + score)

    if player.get_score() == m:
        add_win(player)
        player_queue.pop(0)


# compare for sorting
def compare_sort(a, b):
    if a[1] == b[1]:
        return a[1] - b[1]

    return b[1] - a[1]


# display the player's ranking
def show_rank():
    scores = []

    for item in initial_queue:
        if item not in winners:
            scores.append([item, players[item].get_score()])

    scores = list(sorted(scores, key=cmp_to_key(compare_sort)))

    ranks = list(map(lambda w: [w, m], winners)) + scores

    print("Player\tScore\tRank")

    i = 1
    for rank in ranks:
        print(str(rank[0]) + "\t" + str(rank[1]) + "\t" + str(i))
        i += 1


# process the game
def process_game():
    while True:
        if len(winners) == n:
            print("Game Over!!!\nFinal Result")
            show_rank()
            sys.exit()

        turn = player_queue[0]

        player = players[turn]

        print("Player-" + str(turn) + " its your turn (press 'r' to roll the dice)")

        key = msvcrt.getch()

        if key == b'r':
            score = roll_dice(player)

            if is_valid_score(player, score):
                add_score(player, score)

            show_rank()

            if score == 6 and not player.get_won():
                continue

            if not player.get_won():
                player_queue.append(turn)
                player_queue.pop(0)


if n > 1 and m > 0:
    print("=======Welcome to dice game========")
    print("No of Players: " + sys.argv[1])
    print("Max score: " + sys.argv[2])
    process_game()
else:
    if n < 0 or m < 0:
        print("Max score or number of players can't be negative value")
    elif n <= 1:
        print("We require at-least 2 players to play this game.")
    elif m <= 0:
        print("Max score can't be less than or equals to zero.")
    else:
        print("We can't play the dice with these inputs")

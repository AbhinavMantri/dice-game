import sys
import random
import msvcrt
from functools import cmp_to_key

from player.player import Player

n = int(sys.argv[1])
m = int(sys.argv[2])

print("=======Welcome to dice game========")
print("No of Players: " + sys.argv[1])
print("Max score: " + sys.argv[2])

players = dict()
player_queue = []
winners = []

for i in range(1, n + 1):
    players[i] = Player(i)
    player_queue.append(i)

random.shuffle(player_queue)

initial_queue = [] + player_queue


def is_valid_score(player, score):
    return (player.get_score() + score) <= m


def roll_dice(player):
    score = random.randint(1, 6)
    print("player-" + str(player.get_number()) + " got score " + str(score))

    if score == 1 and score == player.get_prev_score():
        print("warning: player-" + str(player.get_number()) + " you have got 1 score twice continuously")

    return score


def add_win(player):
    player.set_won(True)
    player.set_rank(len(winners) + 1)
    winners.append(player.get_number())


def add_score(player, score):
    player.set_prev_score(score)
    player.set_score(player.get_score() + score)

    if player.get_score() == m:
        add_win(player)
        player_queue.pop(0)


def compare_sort(a, b):
    if a[1] == b[1]:
        return a[1] - b[1]

    return b[1] - a[1]


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


process_game()


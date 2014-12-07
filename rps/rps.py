__author__ = 'charles'

import random


def winner(player, computer):
    """
        >>> player = 'rock'
        >>> computer = 'scissors'
        >>> winner(player, computer)
        'player'

    """

    choices = {'rock:scissors': 'player',
               'paper:rock': 'player',
               'scissors:paper': 'player',
               'scissors:rock': 'computer',
               'rock:paper': 'computer',
               'paper:scissors': 'computer',
               'rock:rock': 'draw',
               'paper:paper': 'draw',
               'scissors:scissors': 'draw'
               }

    win = choices.get(":".join([player, computer]), 'invalid')
    if win != 'invalid':
        return win
    else:
        raise ValueError('invalid choice')


def play():
    p_score = 0
    c_score = 0

    while True:
        player = input('Choose rock, paper or scissors: ')
        if player == 'quit':
            break

        computer = random.choice(['rock', 'paper', 'scissors'])

        try:
            win = winner(player, computer)
        except ValueError as e:
            print('invalid choice...')
            continue

        print("You chose: '{0}'".format(player))
        print('The computer chose: {0}'.format(computer))

        print('Winner: {0}'.format(win))

        if win == 'player':
            p_score += 1

        if win == 'computer':
            c_score += 1

        print('player: {0} / computer: {1}'.format(p_score, c_score))

__author__ = 'charles'

import unittest
from rps.rps import winner


class WinnerTests (unittest.TestCase):

    def test_player_rock(self):
        player = 'rock'
        computer = 'scissors'

        self.assertEqual(winner(player, computer), 'player')

    def test_player_paper(self):
        player = 'paper'
        computer = 'rock'

        self.assertEqual(winner(player, computer), 'player')

    def test_player_scissors(self):
        player = 'scissors'
        computer = 'paper'

        self.assertEqual(winner(player, computer), 'player')

    def test_computer_rock(self):
        computer = 'rock'
        player = 'scissors'

        self.assertEqual(winner(player, computer), 'computer')

    def test_computer_paper(self):
        computer = 'paper'
        player = 'rock'

        self.assertEqual(winner(player, computer), 'computer')

    def test_computer_scissors(self):
        computer = 'scissors'
        player = 'paper'

        self.assertEqual(winner(player, computer), 'computer')

    def test_player_and_computer_rock(self):
        player = computer = 'rock'

        self.assertEqual(winner(player, computer), 'draw')

    def test_player_and_computer_paper(self):
        player = computer = 'paper'

        self.assertEqual(winner(player, computer), 'draw')

    def test_player_and_computer_scissors(self):
        player = computer = 'scissors'

        self.assertEqual(winner(player, computer), 'draw')

    def test_invalid_choice(self):
        player = 'bad choice'
        computer = 'rock'

        self.assertRaises(ValueError, winner, player, computer)
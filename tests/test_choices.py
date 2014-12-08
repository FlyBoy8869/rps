import unittest
import rps.rps
from rps.rps import get_player_choice

__author__ = 'charles'


def my_input(message):
    return 'rock'


class ChoicesTests (unittest.TestCase):

    def test_computer_choice(self):
        self.assertIn(rps.rps.get_computer_choice(), ('rock', 'paper', 'scissors'))

    def test_player_choice(self):
        rps.rps.input = my_input
        self.assertIn(get_player_choice(), ('rock', 'paper', 'scissors'))
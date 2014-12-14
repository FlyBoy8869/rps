import unittest
import unittest.mock
import rps.rps
from rps.rps import get_player_choice, get_computer_choice

__author__ = 'charles'


def my_input(message):
    return 'rock'


class ChoiceTests (unittest.TestCase):

    def test_player_should_choose(self):
        # monkey patch the built-in input function
        rps.rps.input = unittest.mock.Mock(return_value='rock')
        self.assertIn(get_player_choice(), ('rock', 'paper', 'scissors'))
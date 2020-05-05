from unittest import TestCase

from student_code import game_stats


class Testgame_stats(TestCase):

    def test_full_boards(self):
        samp_stats = game_stats([0 for x in range(9)], 1)
        self.assertFalse(samp_stats.is_terminal())

        samp_stats.set_board([1 for x in range(9)])
        self.assertTrue(samp_stats.is_terminal())

        samp_stats.set_board([2 for x in range(9)])
        self.assertTrue(samp_stats.is_terminal())

    def test_ties(self):
        samp_stats = game_stats([1, 2, 1, 2, 1, 1, 2, 1, 2], 1)
        self.assertTrue(samp_stats.is_terminal())

        samp_stats.set_board([2, 2, 1, 1, 1, 2, 2, 1, 2])
        self.assertTrue(samp_stats.is_terminal())

    def test_incompletes(self):
        samp_stats = game_stats([1, 0, 1, 0, 0, 0, 0, 0, 2], 1)
        self.assertFalse(samp_stats.is_terminal())

        samp_stats.set_board([0, 0, 0, 0, 0, 0, 0, 0, 2])
        self.assertFalse(samp_stats.is_terminal())

    def test_quick_dubs(self):
        samp_stats = game_stats([1, 1, 1, 0, 0, 2, 0, 0, 2], 1)
        self.assertTrue(samp_stats.is_terminal())

        samp_stats.set_board([2, 2, 2, 0, 0, 1, 0, 0, 1])
        self.assertTrue(samp_stats.is_terminal())

        samp_stats.set_board([2, 0, 0, 2, 0, 1, 2, 0, 1])
        self.assertTrue(samp_stats.is_terminal())


from unittest import TestCase

from student_code import game_stats


class Testgame_stats(TestCase):

    def test_full_boards(self):
        samp_stats = game_stats()
        self.assertFalse(samp_stats.is_terminal([0 for x in range(9)]))
        self.assertTrue(samp_stats.is_terminal([1 for x in range(9)]))
        self.assertTrue(samp_stats.is_terminal([2 for x in range(9)]))

    def test_ties(self):
        samp_stats = game_stats()
        self.assertTrue(samp_stats.is_terminal([1, 2, 1, 2, 1, 1, 2, 1, 2]))
        self.assertTrue(samp_stats.is_terminal([2, 2, 1, 1, 1, 2, 2, 1, 2]))

    def test_incompletes(self):
        samp_stats = game_stats()
        self.assertFalse(samp_stats.is_terminal([1, 0, 1, 0, 0, 0, 0, 0, 2]))
        self.assertFalse(samp_stats.is_terminal([0, 0, 0, 0, 0, 0, 0, 0, 2]))

    def test_quick_dubs(self):
        samp_stats = game_stats()
        self.assertTrue(samp_stats.is_terminal([1, 1, 1, 0, 0, 2, 0, 0, 2]))
        self.assertTrue(samp_stats.is_terminal([2, 2, 2, 0, 0, 1, 0, 0, 1]))
        self.assertTrue(samp_stats.is_terminal([2, 0, 0, 2, 0, 1, 2, 0, 1]))


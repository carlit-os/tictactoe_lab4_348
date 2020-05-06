from unittest import TestCase

from student_code import game_stats, possible_moves, closer_to1, closer_to2


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

    def test_get_turn(self):
        samp_stats = game_stats([1, 1, 1, 0, 0, 2, 0, 0, 2], 1)
        self.assertTrue(samp_stats.get_turn() == 1)
        samp_stats.set_turn(2)
        self.assertTrue(samp_stats.get_turn() == 2)


class Test(TestCase):
    def test_possible_moves(self):
        self.assertTrue([] == possible_moves([1, 2, 1, 2, 1, 1, 2, 1, 2], 1))

        self.assertTrue([[1, 2, 1, 2, 1, 1, 2, 1, 1]] == possible_moves([1, 2, 1, 2, 1, 1, 2, 1, 0], 1))
        self.assertTrue([[1, 2, 1, 2, 1, 1, 2, 1, 2]] == possible_moves([1, 2, 1, 2, 1, 1, 2, 1, 0], 2))

        self.assertTrue(
            [[1, 2, 1, 2, 1, 1, 2, 1, 0], [0, 2, 1, 2, 1, 1, 2, 1, 1]] == possible_moves([0, 2, 1, 2, 1, 1, 2, 1, 0],
                                                                                         1))


class Test(TestCase):
    def test_closer_to1(self):
        self.assertTrue(1 == closer_to1([1, 1, 2, 0, 1, float("inf"), 1]))
        self.assertTrue(0 == closer_to1([2, 0, float("inf")]))
        self.assertTrue(2 == closer_to1([2, float("inf")]))
        self.assertTrue(float("inf") == closer_to1([float("inf")]))


class Test(TestCase):
    def test_closer_to2(self):
        self.assertTrue(2 == closer_to2([1, 1, 2, 0, 1, float("inf"), 1]))
        self.assertTrue(2 == closer_to2([2, 0, float("inf")]))
        self.assertTrue(2 == closer_to2([2, float("inf")]))
        self.assertTrue(float("-inf") == closer_to2([float("-inf")]))
        self.assertTrue(0 == closer_to2([1, 0, float("inf")]))
        self.assertTrue(1 == closer_to2([1, float("inf")]))

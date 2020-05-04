from unittest import TestCase


class TerminalTests(TestCase):

    def test_full_boards(self):
        from student_code import is_terminal
        self.assertFalse(is_terminal([0 for x in range(9)]))
        self.assertTrue(is_terminal([1 for x in range(9)]))
        self.assertTrue(is_terminal([2 for x in range(9)]))

    def test_ties(self):
        from student_code import is_terminal
        self.assertTrue(is_terminal([1, 2, 1, 2, 1, 1, 2, 1, 2]))
        self.assertTrue(is_terminal([2, 2, 1, 1, 1, 2, 2, 1, 2]))

    def test_incompletes(self):
        from student_code import is_terminal
        self.assertFalse(is_terminal([1, 0, 1, 0, 0, 0, 0, 0, 2]))
        self.assertFalse(is_terminal([0, 0, 0, 0, 0, 0, 0, 0, 2]))

    def test_quick_dubs(self):
        from student_code import is_terminal
        self.assertTrue(is_terminal([1, 1, 1, 0, 0, 2, 0, 0, 2]))
        self.assertTrue(is_terminal([2, 2, 2, 0, 0, 1, 0, 0, 1]))
        self.assertTrue(is_terminal([2, 0, 0, 2, 0, 1, 2, 0, 1]))


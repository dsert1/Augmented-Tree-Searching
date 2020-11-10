import unittest
from Rank import Node
from Rank import testTree

tests = (
    (
        (
            [('Reserve', 8058), ('Rank', 7973), ('Find', 0)]
        ),
        [0, 8058],
    ),
    (
        (
            [('Reserve', 1953), ('Rank', 1298), ('Find', 0), ('Land', 0), ('Reserve', 5937), ('Rank', 6592), ('Find', 0)]
        ),
        [0, 1953, 1, 5937],
    ),
    (
        (
            [('Reserve', 110), ('Rank', 6300), ('Find', 0), ('Reserve', 7810), ('Rank', 9793), ('Find', 1), ('Land', 0), ('Reserve', 7217), ('Rank', 5466), ('Find', 0)]
        ),
        [1, 110, 2, 7810, 0, 7217],
    ),
    (
        (
            [('Reserve', 834), ('Rank', 8794), ('Find', 0), ('Reserve', 3094), ('Rank', 9449), ('Find', 1), ('Land', 0), ('Reserve', 6641), ('Rank', 8531), ('Find', 0), ('Reserve', 9150), ('Rank', 4209), ('Find', 1), ('Reserve', 2601), ('Rank', 2719), ('Find', 0), ('Land', 0), ('Reserve', 5541), ('Rank', 2169), ('Find', 3), ('Reserve', 9350), ('Rank', 6311), ('Find', 4), ('Reserve', 6942), ('Rank', 3236), ('Find', 4), ('Land', 0), ('Reserve', 7445), ('Rank', 8518), ('Find', 1), ('Reserve', 5213), ('Rank', 4711), ('Find', 2)]
        ),
        [1, 834, 2, 3094, 2, 3094, 1, 6641, 1, 2601, 0, 9150, 2, 9350, 1, 9150, 4, 6641, 0, 6641],
    ),
    (
        (
           [('Reserve', 9319), ('Rank', 3168), ('Find', 0), ('Land', 0), ('Reserve', 6787), ('Rank', 333), ('Find', 0), ('Reserve', 2387), ('Rank', 3927), ('Find', 1), ('Reserve', 2092), ('Rank', 5615), ('Find', 1), ('Land', 0), ('Reserve', 4517), ('Rank', 5434), ('Find', 0), ('Reserve', 5405), ('Rank', 4341), ('Find', 2), ('Reserve', 6638), ('Rank', 4539), ('Find', 3), ('Land', 0), ('Reserve', 8798), ('Rank', 5506), ('Find', 4), ('Reserve', 5646), ('Rank', 2643), ('Find', 0), ('Reserve', 5588), ('Rank', 1242), ('Find', 3), ('Land', 0), ('Reserve', 4359), ('Rank', 7221), ('Find', 2), ('Reserve', 3973), ('Rank', 390), ('Find', 2), ('Reserve', 6899), ('Rank', 1455), ('Find', 3), ('Land', 0), ('Reserve', 2078), ('Rank', 2315), ('Find', 1), ('Reserve', 4731), ('Rank', 4732), ('Find', 6), ('Reserve', 9629), ('Rank', 3708), ('Find', 7), ('Land', 0), ('Reserve', 7016), ('Rank', 3879), ('Find', 4), ('Reserve', 3564), ('Rank', 2555), ('Find', 2), ('Reserve', 2863), ('Rank', 4003), ('Find', 7), ('Land', 0), ('Reserve', 1990), ('Rank', 5107), ('Find', 3)]
        ),
        [0, 9319, 0, 6787, 1, 6787, 2, 2387, 2, 2387, 1, 5405, 2, 6638, 2, 8798, 0, 4517, 0, 5646, 6, 5588, 0, 5405, 0, 5588, 1, 4359, 3, 6638, 1, 6787, 0, 5646, 0, 4731, 2, 6638, 4, 4731],
    ),
)


def check(test):
    args, staff_sol = test
    student_sol = testTree(args)
    return staff_sol == student_sol


class TestCases(unittest.TestCase):
    def test_01(self):
        self.assertTrue(check(tests[0]))

    def test_02(self):
        self.assertTrue(check(tests[1]))

    def test_03(self):
        self.assertTrue(check(tests[2]))

    def test_04(self):
        self.assertTrue(check(tests[3]))

    def test_05(self):
        self.assertTrue(check(tests[4]))


if __name__ == "__main__":
    res = unittest.main(verbosity=3, exit=False)
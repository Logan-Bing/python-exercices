import unittest
from can_vote import can_vote

class TestCanVote(unittest.TestCase):

    def test_can_vote_when_age_18_or_more(self):
        self.assertEqual(can_vote(18), "Vous pouvez voter")
        self.assertEqual(can_vote(25), "Vous pouvez voter")
        self.assertEqual(can_vote(100), "Vous pouvez voter")

    def test_can_vote_when_age_under_18(self):
        self.assertEqual(can_vote(17), "Vous êtes trop jeune")
        self.assertEqual(can_vote(10), "Vous êtes trop jeune")
        self.assertEqual(can_vote(0), "Vous êtes trop jeune")

if __name__ == '__main__':
    unittest.main()

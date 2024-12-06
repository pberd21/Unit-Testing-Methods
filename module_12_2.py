import unittest
from runner import Runner, Tournament

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", speed=10)
        self.andrei = Runner("Андрей", speed=9)
        self.nick = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        TournamentTest.all_results[1] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(str(results[max(results)]) == "Ник")

    def test_andrei_and_nick(self):
        tournament = Tournament(90, self.andrei, self.nick)
        results = tournament.start()
        TournamentTest.all_results[2] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(str(results[max(results)]) == "Ник")

    def test_usain_andrei_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrei, self.nick)
        results = tournament.start()
        TournamentTest.all_results[3] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(str(results[max(results)]) == "Ник")


if __name__ == "__main__":
    unittest.main()
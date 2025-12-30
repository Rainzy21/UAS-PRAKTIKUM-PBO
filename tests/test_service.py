import unittest
from services.counseling import TraumaService
from repositories.survivor_repo import InMemorySurvivorRepository
from models.users import Survivor

class TestTraumaService(unittest.TestCase):
    def setUp(self):
        self.repo = InMemorySurvivorRepository()
        self.service = TraumaService(self.repo)

    def test_register_survivor_success(self):
        self.service.register_survivor(1, "Test User", "Gempa", "Ringan")
        data = self.service.get_all_survivors()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0].name, "Test User")

    def test_calculate_impact_score_berat(self):
        self.service.register_survivor(2, "Budi", "Banjir", "Berat")
        score = self.service.calculate_impact_score(2)
        self.assertEqual(score, 90)

    def test_register_invalid_input(self):
        with self.assertRaises(ValueError):
            self.service.register_survivor(3, "", "Gempa", "Ringan")

if __name__ == '__main__':
    unittest.main()
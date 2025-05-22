import unittest
from agents.geonav_agent.geonav_agent import GeoNavAgent

class TestGeoNavAgent(unittest.TestCase):
    def setUp(self):
        self.agent = GeoNavAgent()

    def test_get_coordinates(self):
        result = self.agent.get_coordinates(target_id="target_1")
        self.assertIsInstance(result, dict)
        self.assertIn('latitude', result)
        self.assertIn('longitude', result)
        self.assertIn('altitude', result)

if __name__ == '__main__':
    unittest.main()

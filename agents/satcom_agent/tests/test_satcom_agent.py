import unittest
from agents.satcom_agent.satcom_agent import SatComAgent

class TestSatComAgent(unittest.TestCase):
    def setUp(self):
        self.agent = SatComAgent()

    def test_acquire_imagery(self):
        result = self.agent.acquire_imagery(latitude=35.6895, longitude=139.6917, radius=10.0)
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

if __name__ == '__main__':
    unittest.main()

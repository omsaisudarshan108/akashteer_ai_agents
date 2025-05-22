import unittest
from agents.threat_detection_agent.threat_detection_agent import ThreatDetectionAgent

class TestThreatDetectionAgent(unittest.TestCase):
    def setUp(self):
        self.agent = ThreatDetectionAgent()

    def test_analyze_data_with_input(self):
        # Provide some dummy data_sources
        data_sources = [{'source': 'sat_img', 'data': 'img_data_bytes'}, {'source': 'drone_feed', 'data': 'vid_data_stream'}]
        result = self.agent.analyze_data(data_sources=data_sources)
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0) # Expecting sample threats
        for threat in result:
            self.assertIn('threat_type', threat)
            self.assertIn('location', threat)
            self.assertIn('confidence', threat)

    def test_analyze_data_empty_input(self):
        result = self.agent.analyze_data(data_sources=[])
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0) # Expecting no threats for empty input

if __name__ == '__main__':
    unittest.main()

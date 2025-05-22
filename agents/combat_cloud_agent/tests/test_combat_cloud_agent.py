import unittest
from agents.combat_cloud_agent.combat_cloud_agent import CombatCloudAgent

class TestCombatCloudAgent(unittest.TestCase):
    def setUp(self):
        self.agent = CombatCloudAgent()

    def test_register_agent(self):
        result = self.agent.register_agent(agent_id="satcom_1", agent_type="SatComAgent")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        self.assertIn("satcom_1", self.agent.registered_agents)
        self.assertEqual(self.agent.registered_agents["satcom_1"], "SatComAgent")

    def test_coordinate_operation(self):
        operation_details = {'operation_type': 'RECONNAISSANCE', 'target_area': {'latitude': 34.0, 'longitude': -118.0}}
        result = self.agent.coordinate_operation(operation_details=operation_details)
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        self.assertIn("RECONNAISSANCE", result) # Check if operation type is in the confirmation

if __name__ == '__main__':
    unittest.main()

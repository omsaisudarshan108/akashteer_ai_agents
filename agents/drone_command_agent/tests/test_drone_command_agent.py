import unittest
from agents.drone_command_agent.drone_command_agent import DroneCommandAgent

class TestDroneCommandAgent(unittest.TestCase):
    def setUp(self):
        self.agent = DroneCommandAgent(num_drones=5)

    def test_send_command(self):
        coordinates = {'latitude': 34.0522, 'longitude': -118.2437, 'altitude': 100.0}
        result = self.agent.send_command(drone_id=0, command="SURVEIL", target_coordinates=coordinates)
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_get_drone_status(self):
        # First send a command to ensure there's a status to get
        coordinates = {'latitude': 34.0522, 'longitude': -118.2437, 'altitude': 100.0}
        self.agent.send_command(drone_id=1, command="TEST", target_coordinates=coordinates)
        
        result = self.agent.get_drone_status(drone_id=1)
        self.assertIsInstance(result, dict)
        self.assertIn('drone_id', result)
        self.assertIn('status', result)
        self.assertIn('current_location', result)
        self.assertIn('battery_level', result)

    def test_get_drone_status_invalid_id(self):
        result = self.agent.get_drone_status(drone_id=99) # Invalid ID
        self.assertIsInstance(result, dict)
        self.assertIn('error', result)

    def test_send_command_invalid_id(self):
        coordinates = {'latitude': 34.0522, 'longitude': -118.2437, 'altitude': 100.0}
        result = self.agent.send_command(drone_id=99, command="SURVEIL", target_coordinates=coordinates)
        self.assertIsInstance(result, str)
        self.assertIn("Error: Drone ID 99 is invalid", result)


if __name__ == '__main__':
    unittest.main()

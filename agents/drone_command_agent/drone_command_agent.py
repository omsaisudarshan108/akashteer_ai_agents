class DroneCommandAgent:
    def __init__(self, num_drones: int):
        self.num_drones = num_drones
        self.drone_statuses = {}  # To store status of each drone

    def send_command(self, drone_id: int, command: str, target_coordinates: dict) -> str:
        """
        Simulates sending a command to a specific drone.

        Args:
            drone_id: The ID of the drone.
            command: The command to send (e.g., "SURVEIL", "ENGAGE").
            target_coordinates: A dictionary with 'latitude', 'longitude', and 'altitude'.

        Returns:
            A confirmation message.
        """
        if drone_id < 0 or drone_id >= self.num_drones:
            return f"Error: Drone ID {drone_id} is invalid."

        # Simulate sending command
        # In a real scenario, this would involve communication with the drone
        self.drone_statuses[drone_id] = {
            'drone_id': drone_id,
            'status': f'EXECUTING_{command}',
            'current_location': target_coordinates, # Assume drone moves to target
            'battery_level': 0.80 # Example battery level after a command
        }
        return f"Command '{command}' sent to drone {drone_id} for target at {target_coordinates}"

    def get_drone_status(self, drone_id: int) -> dict:
        """
        Simulates getting the status of a specific drone.

        Args:
            drone_id: The ID of the drone.

        Returns:
            A dictionary with status information.
        """
        if drone_id < 0 or drone_id >= self.num_drones:
            return {'error': f"Drone ID {drone_id} is invalid."}

        # Return stored status or a default if not set
        return self.drone_statuses.get(drone_id, {
            'drone_id': drone_id,
            'status': 'IDLE',
            'current_location': {'latitude': 34.0522, 'longitude': -118.2437}, # Default location
            'battery_level': 0.85
        })


class Drone:
    def __init__(self, drone_id, trajectory):
        self.drone_id = drone_id
        self.trajectory = trajectory  # List of (x, y, z, t) tuples

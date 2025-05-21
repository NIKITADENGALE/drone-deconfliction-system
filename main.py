from drone import Drone
from trajectory import generate_trajectory
from conflict_checker import check_conflicts
from conflict_resolver import resolve_conflicts
from visualization import animate_trajectories

# Create sample drones
drones = []
drones.append(Drone(1, generate_trajectory((0, 0, 0), (1, 1, 0), 10)))
drones.append(Drone(2, generate_trajectory((5, 5, 0), (-1, -1, 0), 10)))

# Check for conflicts
conflicts = check_conflicts(drones)
print("Conflicts found:", conflicts)

# Get the conflict point (if any)
conflict_point = conflicts[0][1] if conflicts else None

# if conflicts:
#     print("\n--- Conflict Details ---")
#     for c in conflicts:
#         drone_id = c.get('conflict_with')
#         location = c.get('location')
#         time = c.get('time')
#         print(f"Drone: {drone_id} | Location: ({location['x']}, {location['y']}, {location['z']}) | Time: {time}")

for c in conflicts:
    (drone1_id, (x1, y1, z1, t1)), (drone2_id, (x2, y2, z2, t2)) = c
    print(f"Conflict between Drone {drone1_id} at ({x1},{y1},{z1}) time {t1} and Drone {drone2_id} at ({x2},{y2},{z2}) time {t2}")
else:
    print("\n--- Conflict Details ---")

# Resolve conflicts
drones = resolve_conflicts(drones, conflicts)

# Visualize results
# animate_trajectories(drones, conflict_point=conflict_point)
animate_trajectories(drones, conflict_point=conflict_point, save_as='drone_conflict.gif')


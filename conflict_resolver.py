
def resolve_conflicts(drones, conflicts):
    for conflict in conflicts:
        drone_id, pos = conflict[0]
        for drone in drones:
            if drone.drone_id == drone_id:
                drone.trajectory = [(x, y, z + 5, t) for (x, y, z, t) in drone.trajectory]
    return drones

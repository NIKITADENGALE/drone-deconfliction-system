
def check_conflicts(drones, spatial_threshold=2.0, time_threshold=1):
    conflicts = []
    for i, drone1 in enumerate(drones):
        for j, drone2 in enumerate(drones):
            if i >= j:
                continue
            for pos1 in drone1.trajectory:
                for pos2 in drone2.trajectory:
                    if abs(pos1[3] - pos2[3]) <= time_threshold:
                        dist = ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2 + (pos1[2] - pos2[2]) ** 2) ** 0.5
                        if dist <= spatial_threshold:
                            conflicts.append(((drone1.drone_id, pos1), (drone2.drone_id, pos2)))
    return conflicts


def generate_trajectory(start, velocity, time_steps):
    trajectory = []
    for t in range(time_steps):
        x = start[0] + velocity[0] * t
        y = start[1] + velocity[1] * t
        z = start[2] + velocity[2] * t
        trajectory.append((x, y, z, t))
    return trajectory

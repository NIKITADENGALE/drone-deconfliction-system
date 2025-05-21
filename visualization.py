import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np

def animate_trajectories(drones, conflict_point=None, save_as=None):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    colors = ['blue', 'green', 'orange', 'purple', 'cyan', 'magenta']
    lines = []
    max_len = max(len(drone.trajectory) for drone in drones)

    for i, drone in enumerate(drones):
        line, = ax.plot([], [], [], label=f"Drone {drone}", color=colors[i % len(colors)])
        lines.append(line)

    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([0, 15])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    conflict_plotted = [False]

    def init():
        return lines

    def update(frame):
        for i, drone in enumerate(drones):
            if frame < len(drone.trajectory):
                x = [p[0] for p in drone.trajectory[:frame + 1]]
                y = [p[1] for p in drone.trajectory[:frame + 1]]
                z = [p[2] for p in drone.trajectory[:frame + 1]]
                lines[i].set_data(x, y)
                lines[i].set_3d_properties(z)

        # Conflict point and time annotation
        if conflict_point and not conflict_plotted[0]:
            for i, drone in enumerate(drones):
                if frame < len(drone.trajectory) and drone.trajectory[frame] == conflict_point:
                    ax.scatter(*conflict_point, color='red', s=60)
                    ax.text(*conflict_point, f'Conflict @ t={frame}', color='red', fontsize=10)
                    conflict_plotted[0] = True
        return lines

    ani = FuncAnimation(fig, update, frames=max_len, init_func=init, blit=False, interval=500, repeat=False)
    ax.legend()

    if save_as:
        if save_as.endswith('.gif'):
            ani.save(save_as, writer=PillowWriter(fps=2))
        else:
            ani.save(save_as, writer='ffmpeg')
        print(f"Animation saved as {save_as}")
    else:
        plt.show()

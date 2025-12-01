import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def animate_pendulum(history, l=0.5):
    state = np.array(history["state"])
    theta = state[:, 2] if state.shape[1] == 4 else state[:,0]  # cart-pole or pendulum
    x_cart = state[:,0] if state.shape[1]==4 else np.zeros_like(theta)

    x_pole = x_cart + l*np.sin(theta)
    y_pole = -l*np.cos(theta)

    fig, ax = plt.subplots()
    ax.set_xlim(min(x_cart)-l-0.2, max(x_cart)+l+0.2)
    ax.set_ylim(-l-0.2, l+0.2)
    line, = ax.plot([], [], 'o-', lw=2)

    def init():
        line.set_data([], [])
        return line,

    def update(frame):
        line.set_data([x_cart[frame], x_pole[frame]], [0, y_pole[frame]])
        return line,

    ani = FuncAnimation(fig, update, frames=len(theta), init_func=init, blit=True, interval=10)
    plt.show()


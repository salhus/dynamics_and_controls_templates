"""support functions."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ------------------------------------------------------------
# Utility: compute energy
# ------------------------------------------------------------
def compute_energy(history, m, k):
    """ Sum of kinetic and potential energy."""
    states = np.array(history['state'])
    x = states[:, 0]
    x_dot = states[:, 1]
    kinetic = 0.5 * m * x_dot**2
    potential = 0.5 * k * x**2
    return kinetic + potential


# ------------------------------------------------------------
# 1. Tracking Plot
# ------------------------------------------------------------
def plot_tracking(history):
    t = np.array(history['t'])
    x = np.array(history['state'])[:, 0]
    ref = np.array(history['reference_signal'])

    xdot = np.array(history['state'])[:, 1]
    refdot = 10*np.pi*(np.cos(5 * 2 * np.pi * t) + np.cos(5 * 2 * np.pi * t))

    plt.figure(figsize=(10, 4))
    plt.plot(t, x, label='Position x(t)')
    plt.plot(t, ref, '--', label='Reference r(t)')
    plt.grid(True)
    plt.xlabel('Time (s)')
    plt.ylabel('Position')
    plt.title('Tracking Performance')
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 4))
    plt.plot(t, xdot, label='Velocity x(t)')
    plt.plot(t, refdot, '--', label='Velocity_Reference r(t)')
    plt.grid(True)
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity')
    plt.title('Tracking Performance')
    plt.legend()
    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 2. Tracking Error
# ------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

def plot_tracking_error(history):
    t = np.array(history["t"])

    # Extract states
    x = np.array(history["state"])[:, 0]
    xdot = np.array(history["state"])[:, 1]

    # Reference signals
    ref = np.array(history["reference_signal"])
    refdot = 10*np.pi*(np.cos(5 * 2 * np.pi * t) + np.cos(5 * 2 * np.pi * t))

    # Absolute magnitude errors
    error = np.abs(np.abs(ref) - np.abs(x))
    error_dot = np.abs(np.abs(refdot) - np.abs(xdot))

    # --- Position Absolute Magnitude Error ---
    plt.figure(figsize=(10, 4))
    plt.plot(t, error, label=r"$\left|\,|r(t)| - |x(t)|\,\right|$")
    plt.grid(True)
    plt.xlabel("Time (s)")
    plt.ylabel(r"Absolute Magnitude Error")
    plt.title(r"Position Absolute Magnitude Error")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # --- Velocity Absolute Magnitude Error ---
    plt.figure(figsize=(10, 4))
    plt.plot(t, error_dot, label=r"$\left|\,|\dot r(t)| - |\dot x(t)|\,\right|$")
    plt.grid(True)
    plt.xlabel("Time (s)")
    plt.ylabel(r"Absolute Magnitude Error")
    plt.title(r"Velocity Absolute Magnitude Error")
    plt.legend()
    plt.tight_layout()
    plt.show()

# ------------------------------------------------------------
# 3. Phase Portrait
# ------------------------------------------------------------
def plot_phase_portrait(history):
    states = np.array(history['state'])
    x = states[:, 0]
    x_dot = states[:, 1]

    plt.figure(figsize=(6, 6))
    plt.plot(x, x_dot)
    plt.xlabel('Position x')
    plt.ylabel('Velocity x_dot')
    plt.title('Phase Portrait (x vs x_dot)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 4. Control Effort
# ------------------------------------------------------------
def plot_control_effort(history):
    t = np.array(history['t'])
    u = np.array(history['u'])

    plt.figure(figsize=(10, 4))
    plt.plot(t, u, color='green', label='Control Input u(t)')
    plt.grid(True)
    plt.xlabel('Time (s)')
    plt.ylabel('Control Input')
    plt.title('Control Effort')
    plt.legend()
    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 5. Energy Plot
# ------------------------------------------------------------
def plot_energy(history, system):
    t = np.array(history['t'])
    E = compute_energy(history, system.m, system.k)

    plt.figure(figsize=(10, 4))
    plt.plot(t, E)
    plt.grid(True)
    plt.xlabel('Time (s)')
    plt.ylabel('Energy')
    plt.title('Mechanical Energy Over Time')
    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 6. Dashboard (3-panel standard set)
# ------------------------------------------------------------
def plot_dashboard(history):
    t = np.array(history['t'])
    ref = np.array(history['reference_signal'])
    x = np.array(history['state'])[:, 0]
    x_dot = np.array(history['state'])[:, 1]
    u = np.array(history['u'])

    fig, axs = plt.subplots(3, 1, figsize=(10, 10))

    # x(t) with reference
    axs[0].plot(t, x, label='x(t)')
    axs[0].plot(t, ref, '--', label='ref(t)')
    axs[0].set_ylabel('Position')
    axs[0].set_title('Position Tracking')
    axs[0].legend()
    axs[0].grid(True)

    # x_dot(t)
    axs[1].plot(t, x_dot, color='orange')
    axs[1].set_ylabel('Velocity')
    axs[1].set_title('Velocity')
    axs[1].grid(True)

    # u(t)
    axs[2].plot(t, u, color='green')
    axs[2].set_ylabel('Control Input')
    axs[2].set_xlabel('Time (s)')
    axs[2].set_title('Control Effort')
    axs[2].grid(True)

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 7. Animation of Mass-Spring-Damper
# ------------------------------------------------------------
def animate_mass_spring(history, system, save_path=None):
    states = np.array(history['state'])
    x = states[:, 0]

    fig, ax = plt.subplots(figsize=(8, 3))
    ax.set_xlim(-2, 2)
    ax.set_ylim(-0.5, 0.5)
    ax.set_title('Mass-Spring-Damper Animation')
    ax.set_xlabel('Position')

    # Spring anchor
    ax.plot([-2, -2], [-0.2, 0.2], color='black', linewidth=3)

    # Mass block
    mass_block, = ax.plot([], [], 's', markersize=20, color='blue')

    def update(frame):
        mass_block.set_data(x[frame], 0)
        return mass_block,

    anim = FuncAnimation(fig, update, frames=len(x), interval=10, blit=True)

    if save_path:
        anim.save(save_path, fps=60)

    plt.show()


# ------------------------------------------------------------
# Main Interface: plot everything
# ------------------------------------------------------------
def plot_everything(history, system):
    plot_dashboard(history)
    plot_tracking(history)
    plot_tracking_error(history)
    plot_phase_portrait(history)
    plot_control_effort(history)
    plot_energy(history, system)
    animate_mass_spring(history, system)

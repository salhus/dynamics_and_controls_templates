import matplotlib.pyplot as plt
import numpy as np

def plot_history(history, title="Simulation Results", show=True, save_path=None):
    import matplotlib.pyplot as plt
    import numpy as np

    t = np.array(history["t"])
    state = np.array(history["state"])
    u = np.array(history["u"])

    fig, axs = plt.subplots(state.shape[1]+1, 1, figsize=(8, 3*(state.shape[1]+1)))
    fig.suptitle(title)

    for i in range(state.shape[1]):
        axs[i].plot(t, state[:, i])
        axs[i].set_ylabel(f"State {i}")
        axs[i].grid(True)

    axs[-1].plot(t, u)
    axs[-1].set_ylabel("Control")
    axs[-1].set_xlabel("Time [s]")
    axs[-1].grid(True)

    plt.tight_layout()

    # Save figure if path provided
    if save_path is not None:
        fig.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close(fig)

    return fig  # <<<< return the figure


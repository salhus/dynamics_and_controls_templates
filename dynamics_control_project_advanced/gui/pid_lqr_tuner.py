import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from examples.run_mass_spring import run_mass_spring  # Adjust if needed

# Initial PID gains
kp0, ki0, kd0 = 30.0, 5.0, 8.0

fig, ax = plt.subplots(3, 1, figsize=(6,6))
plt.subplots_adjust(left=0.25, bottom=0.25)

# Sliders
ax_kp = plt.axes([0.25, 0.15, 0.65, 0.03])
ax_ki = plt.axes([0.25, 0.10, 0.65, 0.03])
ax_kd = plt.axes([0.25, 0.05, 0.65, 0.03])

s_kp = Slider(ax_kp, 'Kp', 0.0, 100.0, valinit=kp0)
s_ki = Slider(ax_ki, 'Ki', 0.0, 50.0, valinit=ki0)
s_kd = Slider(ax_kd, 'Kd', 0.0, 50.0, valinit=kd0)

def update(val):
    kp = s_kp.val
    ki = s_ki.val
    kd = s_kd.val
    # Run simulation with updated gains
    history = run_mass_spring(kp=kp, ki=ki, kd=kd)
    ax[0].cla()
    ax[0].plot([s[0] for s in history["state"]])
    ax[0].set_title("Position")
    ax[1].cla()
    ax[1].plot(history["u"])
    ax[1].set_title("Control")
    plt.draw()

s_kp.on_changed(update)
s_ki.on_changed(update)
s_kd.on_changed(update)

plt.show()


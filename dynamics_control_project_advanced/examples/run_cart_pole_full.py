import os
from systems.cart_pole import CartPole
from controllers.pid import PID
from simulation.simulator import Simulator
from simulation.plotting import plot_history
from simulation.animation_3d import animate_pendulum

# --- 1. System and controller ---
system = CartPole(m_cart=1.0, m_pole=0.1, l=0.5, g=9.81)
controller = PID(kp=100.0, ki=10.0, kd=20.0)
sim = Simulator(system, controller)

# --- 2. Run simulation ---
x0 = [0.0, 0.0, 0.1, 0.0]  # [x, x_dot, theta, theta_dot]
history = sim.run(x0=x0, dt=0.001, tf=5.0, reference=0.0)

# --- 3. Interactive plot (Figure 1) ---
plot_history(history, title="Cart-Pole Simulation", show=True)

# --- 4. 3D animation ---
animate_pendulum(history, l=system.l)

# --- 5. PDF report ---
report_dir = "report"
os.makedirs(report_dir, exist_ok=True)

# Save plot for PDF (Figure 2, headless, safe)
plot_path = os.path.join(report_dir, "cart_pole_plot.png")
plot_history(history, title="Cart-Pole Simulation", show=False, save_path=plot_path)

# Write LaTeX document
tex_content = fr"""
\documentclass{{article}}
\usepackage{{graphicx}}
\usepackage[margin=1in]{{geometry}}
\begin{{document}}
\section*{{Cart-Pole Simulation}}
\includegraphics[width=0.9\textwidth]{{cart_pole_plot.png}}
\end{{document}}
"""

tex_path = os.path.join(report_dir, "cart_pole_report.tex")
with open(tex_path, "w") as f:
    f.write(tex_content)

# Compile PDF using pdflatex inside the report folder
os.system(f"pdflatex -output-directory={report_dir} {tex_path}")

print("PDF report generated at:", os.path.join(report_dir, "cart_pole_report.pdf"))


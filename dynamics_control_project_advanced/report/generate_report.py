#import os
import matplotlib.pyplot as plt
from simulation.plotting import plot_history
from examples.run_mass_spring import run_mass_spring

report_dir = "report"
os.makedirs(report_dir, exist_ok=True)

# Run example
history = run_mass_spring()

# Save plots
plt.figure()
plot_history(history)
plt.savefig(os.path.join(report_dir, "mass_spring_plot.png"))

# Write minimal LaTeX
tex = r"""
\documentclass{article}
\usepackage{graphicx}
\begin{document}
\section*{Mass-Spring-Damper Simulation}
\includegraphics[width=0.8\textwidth]{mass_spring_plot.png}
\end{document}
"""
tex_path = os.path.join(report_dir, "report.tex")
with open(tex_path, "w") as f:
    f.write(tex)

# Compile PDF
os.system(f"pdflatex -output-directory={report_dir} {tex_path}")
print("PDF report generated in report/report.pdf")


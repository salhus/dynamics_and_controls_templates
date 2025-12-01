import os

# --- Directories ---
report_dir = "report"
os.makedirs(report_dir, exist_ok=True)

# --- LaTeX Content ---
latex_content = r"""
\documentclass{article}
\usepackage[margin=1in]{geometry}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage[utf8]{inputenc}

\title{Dynamics \& Control Learning Project}
\author{Generated Documentation}
\date{\today}

\begin{document}
\maketitle

\section*{Project Description}

The \textbf{Dynamics \& Control Learning Project} is a hands-on Python framework designed to help users explore \textbf{classical mechanics, control theory, and numerical simulation} using modular, reusable code.

\subsection*{Overview}
This project provides implementations for:
\begin{itemize}
  \item \textbf{Physical systems}: mass-spring-damper, pendulum, cart-pole, etc.
  \item \textbf{Controllers}: PID control and flexible base classes for custom controllers.
  \item \textbf{Simulation}: numerical integration using Euler method.
  \item \textbf{Visualization}: plots of system states and 3D animations.
  \item \textbf{Report generation}: automatic creation of plots and PDF reports.
\end{itemize}

\subsection*{Purpose}
The main goals of the project are:
\begin{enumerate}
  \item Teach Python programming concepts: classes, modules, abstract base classes, dataclasses.
  \item Introduce control theory: PID control, feedback loops, system response.
  \item Practice numerical simulation: Euler integration, collecting simulation history.
  \item Visualize and report results: generate plots, animations, and PDF reports.
\end{enumerate}

\subsection*{Target Audience}
\begin{itemize}
  \item Beginner to Intermediate Python programmers learning scientific computing.
  \item Engineering students in mechanical, electrical, or aerospace fields.
  \item Researchers or hobbyists testing control strategies on classical systems.
\end{itemize}

\subsection*{Required Knowledge}
\begin{itemize}
  \item Basic Python programming (functions, classes, modules).
  \item NumPy for numerical computation.
  \item Mechanics and dynamics (Newton’s laws, mass-spring-damper, pendulum).
  \item Control systems basics (PID, feedback loops).
  \item Optional: LaTeX for customizing PDF reports.
\end{itemize}

\subsection*{Learning Outcomes}
After completing examples and exercises, users will be able to:
\begin{itemize}
  \item Implement new dynamic systems and controllers.
  \item Simulate and visualize system behavior under different controllers.
  \item Analyze system response to various inputs.
  \item Generate professional reports summarizing simulations with plots and figures.
\end{itemize}

\section*{Project Structure}
\begin{verbatim}
+ systems/        # Physical systems (Mass-Spring, Pendulum, Cart-Pole)
+ controllers/    # Controllers (PID, etc.)
+ simulation/     # Simulation & plotting
+ examples/       # Example scripts
+ report/         # Generated PDFs & plots
+ requirements.txt
+ README.md
\end{verbatim}

\end{document}
"""

# --- Write LaTeX file ---
tex_path = os.path.join(report_dir, "PROJECT_DOC.tex")
with open(tex_path, "w") as f:
    f.write(latex_content)

# --- Compile PDF ---
os.system(f"pdflatex -output-directory={report_dir} {tex_path}")

print("PDF generated at:", os.path.join(report_dir, "PROJECT_DOC.pdf"))

# --- Markdown Content ---
markdown_content = """
# Dynamics & Control Learning Project

## Project Description

The **Dynamics & Control Learning Project** is a hands-on Python framework designed to explore classical mechanics, control theory, and numerical simulation.

### Overview

- **Physical systems**: mass-spring-damper, pendulum, cart-pole
- **Controllers**: PID and custom controllers
- **Simulation**: numerical integration (Euler)
- **Visualization**: plots and 3D animations
- **Report generation**: PDF reports with plots

### Purpose

1. Teach Python programming: classes, modules, ABCs, dataclasses
2. Introduce control theory: PID, feedback, system response
3. Practice simulation: Euler integration, history collection
4. Visualize & report results: plots, animations, PDF

### Target Audience

- Beginner to intermediate Python programmers
- Engineering students (mechanical, electrical, aerospace)
- Researchers/hobbyists testing control strategies

### Required Knowledge

- Python programming (functions, classes, modules)
- NumPy
- Mechanics & dynamics
- Control systems basics
- Optional: LaTeX

### Learning Outcomes

- Implement new systems and controllers
- Simulate & visualize behavior
- Analyze system response
- Generate professional reports

### Project Structure

systems/ # Physical systems (Mass-Spring, Pendulum, Cart-Pole)

controllers/ # Controllers (PID, etc.)

simulation/ # Simulation & plotting

examples/ # Example scripts

report/ # Generated PDFs & plots

requirements.txt

README.md

pgsql
Copy code
"""

md_path = os.path.join(report_dir, "PROJECT_DOC.md")
with open(md_path, "w") as f:
    f.write(markdown_content)

print("Markdown generated at:", md_path)

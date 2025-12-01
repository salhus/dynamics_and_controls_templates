
import numpy as np

class CartPole:
    def __init__(self, m_cart=1.0, m_pole=0.1, l=0.5, g=9.81):
        self.m_cart = m_cart
        self.m_pole = m_pole
        self.l = l
        self.g = g

    def dynamics(self, t, state, u):
        # state = [x, x_dot, theta, theta_dot]
        x, x_dot, theta, theta_dot = state
        M = self.m_cart + self.m_pole
        sin_theta = np.sin(theta)
        cos_theta = np.cos(theta)
        total = self.m_pole * self.l * theta_dot**2 * sin_theta
        theta_ddot = (self.g * sin_theta - cos_theta * (u + total)/M) / (self.l * (4.0/3 - self.m_pole * cos_theta**2 / M))
        x_ddot = (u + self.m_pole*self.l*(theta_dot**2*sin_theta - theta_ddot*cos_theta)) / M
        return np.array([x_dot, x_ddot, theta_dot, theta_ddot])


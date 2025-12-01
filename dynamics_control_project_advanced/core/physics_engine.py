
import sympy as sp
import numpy as np

# Minimal automatic Lagrangian dynamics engine for research-lab style
class PhysicsEngine:
    def __init__(self, q_symbols, dq_symbols, L):
        self.q = q_symbols
        self.dq = dq_symbols
        self.L = L
        self.n = len(q_symbols)
        self.eqns = self._lagrange_eqns()

    def _lagrange_eqns(self):
        eqns = []
        for i in range(self.n):
            dL_dq = sp.diff(self.L, self.q[i])
            dL_ddq = sp.diff(self.L, self.dq[i])
            dt_dL_ddq = sum(sp.diff(dL_ddq, self.q[j])*self.dq[j] + sp.diff(dL_ddq, self.dq[j])*sp.Symbol('ddq'+str(j)) for j in range(self.n))
            eqns.append(dt_dL_ddq - dL_dq)
        return eqns

    def numeric_f(self, q_val, dq_val, ddq_val=None):
        # Converts symbolic eqns to numeric function
        f = sp.lambdify([self.q, self.dq], self.eqns, 'numpy')
        return f(q_val, dq_val)

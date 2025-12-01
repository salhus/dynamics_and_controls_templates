# tests/test_pid.py
from controllers.pid import PID

def test_pid_compute():
    pid = PID(kp=1.0, ki=0.5, kd=0.1)
    u = pid.compute(error=1.0, dt=0.01)
    assert isinstance(u, float)

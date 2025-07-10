import pytest
from prana.prana_control import PIDController

def test_pid_step_response():
    # Given a setpoint of 10 and initial measurement 0
    pid = PIDController(kp=1.0, ki=0.5, kd=0.1, dt=1.0)
    pid.reset()

    # First update: error=10 → output = kp*10 + ki*10*1 + kd*0 = 10+5+0 = 15
    out1 = pid.update(setpoint=10, measurement=0)
    assert pytest.approx(out1, rel=1e-6) == 15.0

    # Second update, measurement jumped to 5: error=5
    # integral = 10 + 5*1 = 15; derivative = (5-10)/1 = -5
    # output = 1*5 + 0.5*15 + 0.1*(-5) = 5 + 7.5 - 0.5 = 12.0
    out2 = pid.update(setpoint=10, measurement=5)
    assert pytest.approx(out2, rel=1e-6) == 12.0

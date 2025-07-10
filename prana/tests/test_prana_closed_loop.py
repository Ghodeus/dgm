import numpy as np
import pytest
from prana.prana_control import PIDController
from prana.prana_plant import FirstOrderPlant

def test_closed_loop_convergence():
    dt = 0.1
    plant = FirstOrderPlant(tau=1.0, dt=dt)
    pid = PIDController(kp=2.0, ki=1.0, kd=0.0, dt=dt)
    plant.reset(0.0)
    pid.reset()

    setpoint = 1.0
    # run for 100 steps
    xs = []
    for _ in range(100):
        u = pid.update(setpoint, plant.state)
        x = plant.step(u)
        xs.append(x)

    # by the end, the plant output should be within 5% of the setpoint
    assert abs(xs[-1] - setpoint) < 0.05

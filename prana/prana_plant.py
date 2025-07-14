# prana/prana_plant.py

class FirstOrderPlant:
    """
    Simple first-order system:  dx/dt = (−x + u) / τ
    Discretized with Euler integration.
    """
    def __init__(self, tau: float, dt: float):
        self.tau = tau
        self.dt = dt
        self.state = 0.0

    def reset(self, x0: float = 0.0):
        self.state = x0

    def step(self, u: float) -> float:
        # x_{k+1} = x_k + dt*(−x_k + u)/τ
        self.state += self.dt * ((-self.state + u) / self.tau)
        return self.state

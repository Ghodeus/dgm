# prana/prana_control.py

class PIDController:
    """
    A simple PID controller.
    """
    def __init__(self, kp: float, ki: float, kd: float, dt: float):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.dt = dt
        self._integral = 0.0
        self._prev_error = None

    def reset(self):
        self._integral = 0.0
        self._prev_error = None

    def update(self, setpoint: float, measurement: float) -> float:
        """
        Compute the control output.
        """
        error = setpoint - measurement
        self._integral += error * self.dt
        derivative = 0.0
        if self._prev_error is not None:
            derivative = (error - self._prev_error) / self.dt
        self._prev_error = error

        # PID formula
        output = (
            self.kp * error +
            self.ki * self._integral +
            self.kd * derivative
        )
        return output

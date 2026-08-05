import time

class PIDController:
    def __init__(self, kp=1.0, ki=0.0, kd=0.0, setpoint=0.0, output_limits=(-100, 100)):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint
        self.output_limits = output_limits
        self._last_error = 0.0
        self._integral = 0.0
        self._last_time = None

    def update(self, current_value, dt=None):
        error = self.setpoint - current_value
        now = time.time()
        if dt is None:
            dt = now - self._last_time if self._last_time else 0.1
        self._last_time = now
        p = self.kp * error
        self._integral += error * dt
        i = self.ki * self._integral
        d = self.kd * (error - self._last_error) / dt if dt > 0 else 0.0
        self._last_error = error
        output = p + i + d
        output = max(self.output_limits[0], min(self.output_limits[1], output))
        return output

    def set_setpoint(self, setpoint):
        self.setpoint = setpoint

    def reset(self):
        self._integral = 0.0
        self._last_error = 0.0
        self._last_time = None

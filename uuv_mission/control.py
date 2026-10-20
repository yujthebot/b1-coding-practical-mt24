
class controller:

    def __init__(self):
        self.Kp = 0.15
        self.Kd = 0.6
        self.error_prev = 0.0
    def control(self, reference: float, current_depth: float):
        error = reference - current_depth
        derivative = error - self.error_prev
        self.error_prev = error
        control_signal = self.Kp * error + self.Kd * derivative
        return control_signal
    def reset(self):
        self.error_prev = 0.0


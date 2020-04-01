import time
import numpy as np

class peep:
    t0 = 0
    t1 = 2
    t2 = t1 + 1
    t3 = t2 + 0.25
    t4 = t3 + 0.75
    t5 = t4 + 1.2
    p1 = 70
    p2 = 95
    def __init__(self):
        self.t0 = time.time()
    def value(self):
        t = time.time() - self.t0
        p = 0
        if t > self.t1 and t < self.t2:
            a = self.p2/(self.t2-self.t1)
            b = -a*self.t1
            p = a*t + b
        elif t >= self.t2 and t < self.t3:
            tau = (self.t3 - self.t2)*0.3
            c = self.p1
            A = self.p2 - self.p1
            p = c+A*np.exp(-(t-self.t2)/tau)
        elif t >= self.t3 and t < self.t4:
            p = self.p1
        elif t >= self.t4 and t < self.t5:
            tau = (self.t5 - self.t4)*0.3
            A = self.p1
            p = A*np.exp(-(t-self.t4)/tau)
        elif t > self.t5:
            self.t0 = time.time()
        p += np.random.normal(scale = (self.p2 - self.p1)*0.05)
        return p


"""
A dummy class that can be used for testing the GUI when a real
ESP32 chip isn't available.

Currently just reports fixed values. Can be made more intelligent
as needed.
"""

from threading import Lock
import random
from communication.peep import peep

class FakeESP32Serial:
    peep = peep()
    def __init__(self):
        self.lock = Lock()
        self.set_params = {}
        self.random_params = ["mve", "vti", "vte", "pressure", "flow",
                              "o2", "bpm"]

    def set(self, name, value):
        """
        Set command wrapper

        arguments:
        - name           the parameter name as a string
        - value          the value to assign to the variable as any type
                         convertible to string

        returns: an "OK" string in case of success.
        """

        with self.lock:
            self.set_params[name] = value
            return "OK"

    def get(self, name):
        """
        Get command wrapper

        arguments:
        - name           the parameter name as a string

        returns: the requested value
        """

        with self.lock:
            retval = 0

            if name in self.set_params:
                retval = self.set_params[name]
            elif name in self.random_params:
                retval = random.uniform(10, 100)

            return str(retval)

    def get_all(self):
        """
        Get the pressure, flow, o2, and bpm at once and in this order.

        returns: a dict with member keys as written above and values as
        strings.
        """

        with self.lock:
            return {"pressure": self.peep.value(),
                    "flow":     random.uniform(10, 100),
                    "o2":       random.uniform(10, 100),
                    "bpm":      random.uniform(10, 100)}


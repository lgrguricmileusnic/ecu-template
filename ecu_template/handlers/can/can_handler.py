# File for implementing user defined handlers
from abc import abstractmethod

import can

from ecu_template.models.ecu_model import ECUModel
from ..handler import Handler


class CanHandler(Handler):
    def __init__(self, ecu: ECUModel):
        super().__init__()
        self.bus = None
        self.ecu = ecu

    @abstractmethod
    def handle_msg(self, msg: can.Message):
        raise NotImplementedError

    def set_bus(self, bus: can.BusABC):
        self.bus = bus

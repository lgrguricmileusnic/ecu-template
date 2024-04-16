import can

from .can_handler import CanHandler
from ...models.simple_ecu_model import SimpleECUModel


class SimpleCanHandler(CanHandler):
    def __init__(self, ecu: SimpleECUModel):
        super().__init__(ecu)

    def handle_msg(self, msg: can.Message):
        msg.arbitration_id += 1
        self.bus.send(msg)

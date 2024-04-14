import can
from ecu_template.controllers.can_controller.can_raw import CanController
from ecu_template.controllers.uds_controller.uds import UDSController
from .models.ecu_model import ECUModel


class ECU:
    def __init__(self, interface: str):
        self._bus = can.Bus(interface, "socketcan", ignore_config=True)
        self._ecu = ECUModel()
        self.can_controller = CanController(self._bus, self._ecu)
        self.uds_controller = UDSController(self._bus, self._ecu, rx_id=0x100, tx_id=0x101, canfd=False)

    def start(self):
        self.can_controller.start()
        self.uds_controller.start()

    def stop(self):
        self.can_controller.stop()
        self.uds_controller.stop()

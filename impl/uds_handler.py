from scapy.contrib.automotive.uds import UDS

from ecu_template.handler.uds.uds_handler import UDSHandler
from ecu_template.model.ecu_model import ECUModel


class UDSHandlerImpl(UDSHandler):
    def __init__(self, ecu: ECUModel):
        super().__init__(
            ecu,
        )

    def handle_msg(self, msg: UDS):
        print("Received UDS message!")

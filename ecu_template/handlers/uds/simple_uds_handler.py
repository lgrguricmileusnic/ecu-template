from ecu_template.handlers.uds.uds_handler import UDSHandler
from ecu_template.handlers.uds.uds_message import UDSMessage
from ecu_template.models.ecu_model import ECUModel


class SimpleUDSHandler(UDSHandler):
    def __init__(self, ecu: ECUModel):
        super().__init__(ecu)

    def handle_msg(self, msg: UDSMessage):
        print("Received UDS message!")

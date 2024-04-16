from abc import abstractmethod

import isotp

from ecu_template.models.ecu_model import ECUModel
from .uds_message import UDSMessage
from ..handler import Handler


class UDSHandler(Handler):
    def __init__(self, ecu: ECUModel):
        super().__init__()
        self.ecu = ecu
        self.isotp = None

    @abstractmethod
    def handle_msg(self, msg: UDSMessage):
        raise NotImplementedError

    def set_isotp_socket(self, isotp_socket: isotp.socket):
        self.isotp = isotp_socket

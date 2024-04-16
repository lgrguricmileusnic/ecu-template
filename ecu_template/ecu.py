import can
import isotp

from ecu_template.controllers.can.can_controller import CanController
from ecu_template.controllers.uds.uds_controller import UDSController
from .controllers.uds.isotp.notifier import IsoTpNotifier
from .handlers.can.can_handler import CanHandler
from .handlers.uds.uds_handler import UDSHandler

PYTHON_CAN_INTERFACE = "socketcan"


class ECU:
    def __init__(self, interface: str, canfd: bool, can_handler: CanHandler, uds_handler: UDSHandler,
                 uds_address: isotp.Address):

        self.controllers = []
        if can_handler is not None:
            self._bus = can.Bus(interface, PYTHON_CAN_INTERFACE, fd=canfd, ignore_config=True)
            can_handler.set_bus(self._bus)
            self.controllers.append(CanController(can_handler, can.Notifier(self._bus, [])))

        if uds_handler is not None:
            if uds_address is None:
                raise TypeError
            self._isotp = self._setup_isotp(interface, canfd, uds_address)
            uds_handler.set_isotp_socket(self._isotp)
            self.controllers.append(UDSController(uds_handler, IsoTpNotifier(socket=self._isotp)))

    @staticmethod
    def _setup_isotp(interface: str, canfd: bool, address: isotp.Address):
        socket = isotp.socket()
        socket.set_ll_opts(isotp.socket.LinkLayerProtocol.CAN_FD if canfd else isotp.socket.LinkLayerProtocol.CAN,
                           None,
                           None)
        socket.bind(interface, address)
        return socket

    def start(self):
        for controller in self.controllers:
            controller.start()

    def stop(self):
        for controller in self.controllers:
            controller.stop()
        self._bus.shutdown()

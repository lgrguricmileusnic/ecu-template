import can
import isotp
from ecu_template.models.ecu_model import ECUModel
from ecu_template.controllers.controller import Controller
from .isotp_notifier.listener import AbstractIsoTpListener
from .isotp_notifier.notifier import Notifier


class UDSController(Controller):
    class IsoTpListener(AbstractIsoTpListener):
        def __init__(self):
            super().__init__()

        def on_message_received(self, data: bytearray):
            print("Received isotp data:", data.hex())

    def __init__(self, interface: str, model: ECUModel, rx_id: int, tx_id: int, canfd: bool):
        self.isotp_address = isotp.Address(addressing_mode=isotp.AddressingMode.Normal_11bits,
                                           rxid=rx_id,
                                           txid=tx_id)
        self.socket = isotp.socket()
        self.socket.set_ll_opts(isotp.socket.LinkLayerProtocol.CAN_FD if canfd else isotp.socket.LinkLayerProtocol.CAN,
                                None,
                                None)
        self.socket.bind(interface, self.isotp_address)
        self.notifier = Notifier(self.socket)
        self.ecu = model
        self.running = False

    def start(self):
        if self.running:
            return
        self.running = True
        self.notifier.add_listener(self.IsoTpListener())
        self.notifier.start()

    def stop(self):
        if not self.running:
            return
        self.notifier.stop()

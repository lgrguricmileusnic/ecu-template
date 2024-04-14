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

    def __init__(self, bus: can.BusABC, model: ECUModel, rx_id: int, tx_id: int, canfd: bool):
        self.bus = bus
        self.can_notifier = can.Notifier(self.bus, [])

        self.isotp_address = isotp.Address(addressing_mode=isotp.AddressingMode.Normal_11bits,
                                           rxid=rx_id,
                                           txid=tx_id)

        self.transport_layer = isotp.NotifierBasedCanStack(self.bus,
                                                           self.can_notifier,
                                                           address=self.isotp_address,
                                                           params=dict(can_fd=canfd))

        self.notifier = Notifier(self.transport_layer)
        self.ecu = model
        self.running = False

    def start(self):
        if self.running:
            return
        self.running = True
        self.transport_layer.start()
        self.notifier.add_listener(self.IsoTpListener())
        self.notifier.start()

    def stop(self):
        if not self.running:
            return
        self.transport_layer.stop()
        self.notifier.stop()

from ecu_template.controllers.controller import Controller
from ecu_template.handlers.uds.uds_handler import UDSHandler
from .isotp.listener import IsoTpListener
from .isotp.notifier import IsoTpNotifier
from ...handlers.uds.uds_message import UDSMessage


class UDSController(Controller):
    class UDSIsoTpListener(IsoTpListener):
        def __init__(self, handler: UDSHandler):
            super().__init__()
            self.handler = handler

        def on_message_received(self, data: bytearray):
            self.handler.handle_msg(UDSMessage(data))

    def __init__(self, handler: UDSHandler, notifier: IsoTpNotifier):
        self.notifier = notifier
        self.handler = handler
        self.running = False

    def start(self):
        if self.running:
            return
        self.running = True
        self.notifier.start()

    def stop(self):
        if not self.running:
            return
        self.notifier.stop()

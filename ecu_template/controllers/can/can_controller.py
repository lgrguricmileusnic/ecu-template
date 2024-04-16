import can

from ecu_template.controllers.controller import Controller
from ecu_template.handlers.can.can_handler import CanHandler


class CanController(Controller):
    class CanBusListener(can.Listener):
        def __init__(self, handler: CanHandler):
            super().__init__(None, None)
            self.handler = handler

        def on_message_received(self, msg: can.Message):
            self.handler.handle_msg(msg)

    def __init__(self, handler: CanHandler, notifier: can.Notifier):
        self.notifier = notifier
        self.listener = self.CanBusListener(handler)
        self.running = False

    def start(self):
        if self.running:
            return
        self.running = True
        self.notifier.add_listener(self.listener)

    def stop(self):
        if not self.running:
            return
        self.notifier.stop()

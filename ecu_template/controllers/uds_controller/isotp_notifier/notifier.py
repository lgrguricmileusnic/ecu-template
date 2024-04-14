import time

import isotp
import threading
from .listener import AbstractIsoTpListener


class Notifier:
    def __init__(self, transport_layer: isotp.TransportLayer):
        self.rx_thread = None
        self._running = False
        if transport_layer is None:
            raise TypeError
        self.transport_layer = transport_layer
        self.listeners = []

    def _rx_thread(self):
        while self._running:
            if data := self.transport_layer.recv(block=False):
                for listener in self.listeners:
                    listener.on_message_received(data)

    def start(self):
        self._running = True
        self.rx_thread = threading.Thread(target=self._rx_thread, name="isotp.notifier")
        self.rx_thread.daemon = True
        self.rx_thread.start()

    def stop(self, timeout: float = 5.0):
        self._running = False
        if self.rx_thread is not None:
            self.rx_thread.join(timeout)

    def add_listener(self, listener: AbstractIsoTpListener):
        self.listeners.append(listener)

    def remove_listener(self, listener: AbstractIsoTpListener):
        self.listeners.remove(listener)

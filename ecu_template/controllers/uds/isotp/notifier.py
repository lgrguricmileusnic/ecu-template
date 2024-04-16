import threading

import isotp

from .listener import IsoTpListener


class IsoTpNotifier:
    def __init__(self, socket: isotp.socket):
        if socket is None:
            raise TypeError
        self.rx_thread = None
        self._running = False
        self.socket = socket
        self.listeners = []

    def _rx_thread(self):
        while self._running:
            if data := self.socket.recv():
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

    def add_listener(self, listener: IsoTpListener):
        self.listeners.append(listener)

    def remove_listener(self, listener: IsoTpListener):
        self.listeners.remove(listener)

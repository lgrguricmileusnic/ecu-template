from abc import ABCMeta, abstractmethod


class IsoTpListener(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def on_message_received(self, data: bytearray):
        pass

from abc import ABCMeta, abstractmethod


class AbstractIsoTpListener(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def on_message_received(self, data: bytearray):
        pass

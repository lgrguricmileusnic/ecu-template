from abc import abstractmethod

from scapy.contrib.automotive.xcp.xcp import XCPOnCAN

from ecu_template.listener.listener import PacketListener


class XCPListener(metaclass=PacketListener):
    def __init__(self):
        pass

    @abstractmethod
    def on_message_received(self, packet: XCPOnCAN):
        pass

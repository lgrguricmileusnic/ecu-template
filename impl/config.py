from scapy.layers.can import CAN_INV_FILTER

CAN_FILTERS = [
    {"can_id": 0x123, "can_mask": 0x7FF},
    {"can_id": 0x100 | CAN_INV_FILTER, "can_mask": 0x7FF},
]
UDS = dict(rx_id=0x100, tx_id=0x101)

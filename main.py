import argparse

import isotp

from ecu_template.ecu import ECU
from ecu_template.handlers.can.simple_can_handler import SimpleCanHandler
from ecu_template.handlers.uds.simple_uds_handler import SimpleUDSHandler
from ecu_template.models.simple_ecu_model import SimpleECUModel

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("interface", default="vcan0", type=str, nargs="?")
    argparser.add_argument("canfd", default=False, type=bool, nargs="?")
    args = argparser.parse_args()

    ecu = ECU(interface=args.interface,
              canfd=args.canfd,
              can_handler=SimpleCanHandler(SimpleECUModel()),
              uds_handler=SimpleUDSHandler(SimpleECUModel()),
              uds_address=isotp.Address(addressing_mode=isotp.AddressingMode.Normal_11bits, rxid=0x100, txid=0x101))

    ecu.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        ecu.stop()

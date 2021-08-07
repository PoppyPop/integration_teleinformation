import logging
import time

import serial

ser = serial.Serial(
    port="/workspaces/integration_teleinformation/writer",
    baudrate=1200,
    # bytesize=7,
    # parity=serial.PARITY_EVEN,
    # stopbits=serial.STOPBITS_ONE
)
count = 0
_LOGGER = logging.getLogger(__name__)


def getFrameWithCheckSum(frame):
    """Check if a frame is valid."""
    datas = frame.encode("ascii")
    computed_checksum = (sum(datas) & 0x3F) + 0x20

    return (frame + " " + chr(computed_checksum) + "\n").encode("ascii")


while 1:
    ser.write(b"\x02\n")
    ser.write(b"ADCO 700801422425 :\n")
    ser.write(b"OPTARIF BASE 0\n")
    ser.write(b"ISOUSC 30 9\n")
    # ser.write(b'BASE 008528238 /\n')

    ser.write(getFrameWithCheckSum("BASE " + str(count)))

    ser.write(b"PTEC TH.. $\n")
    ser.write(b"IINST 002 Y\n")
    ser.write(b"IMAX 090 H\n")
    ser.write(b"PAPP 00360 *\n")
    ser.write(b"\x03\n")

    _LOGGER.log(0, "Frame")

    time.sleep(5)
    count += 1

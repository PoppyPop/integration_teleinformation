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
    frame = frame + "\t"
    datas = frame.encode("ascii")
    computed_checksum = (sum(datas) & 0x3F) + 0x20

    return (frame + chr(computed_checksum) + "\n").encode("ascii")


def serveStandard(writer, count):
    writer.write(b"\x02\n")
    writer.write(getFrameWithCheckSum("ADSC\t700801422425"))
    writer.write(getFrameWithCheckSum("VTIC\t2"))
    writer.write(getFrameWithCheckSum("DATE\tH081225223518\t"))

    writer.write(getFrameWithCheckSum("NGTF\t1"))

    writer.write(getFrameWithCheckSum("EAST\t1"))
    writer.write(getFrameWithCheckSum("EASF01\t" + str(count)))
    writer.write(getFrameWithCheckSum("EASF02\t" + str(count)))

    writer.write(getFrameWithCheckSum("EAIT\t" + str(count)))

    writer.write(getFrameWithCheckSum("IRMS1\t241"))
    writer.write(getFrameWithCheckSum("IRMS2\t242"))
    writer.write(getFrameWithCheckSum("IRMS3\t243"))
    writer.write(getFrameWithCheckSum("URMS1\t1"))
    writer.write(getFrameWithCheckSum("URMS2\t2"))
    writer.write(getFrameWithCheckSum("URMS3\t3"))

    writer.write(getFrameWithCheckSum("SMAXSN\tH081225223518\t3"))
    writer.write(getFrameWithCheckSum("SMAXSN1\t 081225223518\t18"))

    writer.write(b"\x03\n")


def serveHistorical(writer, count):
    writer.write(b"\x02\n")
    writer.write(b"ADCO 700801422425 :\n")
    writer.write(b"OPTARIF BASE 0\n")
    writer.write(b"ISOUSC 30 9\n")
    # ser.write(b'BASE 008528238 /\n')

    writer.write(getFrameWithCheckSum("BASE " + str(count)))

    writer.write(b"PTEC TH.. $\n")
    writer.write(b"IINST 002 Y\n")
    writer.write(b"IMAX 090 H\n")
    writer.write(b"PAPP 00360 *\n")
    writer.write(b"\x03\n")


while 1:
    serveStandard(ser, count)

    time.sleep(5)
    count += 1

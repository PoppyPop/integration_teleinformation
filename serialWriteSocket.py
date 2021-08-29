import asyncio
import logging
import time


_LOGGER = logging.getLogger(__name__)


def getFrameWithCheckSum(frame):
    """Check if a frame is valid."""
    datas = frame.encode("ascii")
    computed_checksum = (sum(datas) & 0x3F) + 0x20

    return (frame + " " + chr(computed_checksum) + "\n").encode("ascii")


async def echo_server(reader, writer):
    count = 0
    while True:
        serveHistorical(writer, count)

        count += 1

        await writer.drain()  # Flow control, see later
        time.sleep(5)
    writer.close()


class EchoProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        count = 0
        while True:
            serveHistorical(self.transport, count)
            count += 1

    def data_received(self, data):
        self.transport.write(data)


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


async def main():
    loop = asyncio.get_running_loop()
    server = await loop.create_server(EchoProtocol, "127.0.0.1", "8888")
    await server.serve_forever()


asyncio.run(main())
# loop = asyncio.get_event_loop()

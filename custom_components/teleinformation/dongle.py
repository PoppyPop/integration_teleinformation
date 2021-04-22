"""Representation of an Teleinformation dongle."""
import asyncio
import glob
import logging

import serial
import serial_asyncio
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import EVENT_HOMEASSISTANT_STOP
from homeassistant.core import callback
from homeassistant.core import HomeAssistant

from .const import CONF_DEVICE
from .const import CONF_TIMEOUT
from .const import DEFAULT_CONF_TIMEOUT
from .const import SIGNAL_RECEIVE_MESSAGE


_LOGGER = logging.getLogger(__name__)


class TeleInformationDongle:
    """Representation of an TeleInformation dongle.

    The dongle is responsible for receiving the TeleInformation frames,
    creating devices if needed, and dispatching messages to platforms.
    """

    hass: HomeAssistant
    device_id: str = None

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry):
        """Initialize the TeleInformation dongle."""

        self._serial_loop_task = None
        self.hass = hass
        self.port = entry.data[CONF_DEVICE]
        self.timeout = entry.options.get(CONF_TIMEOUT, DEFAULT_CONF_TIMEOUT)

    def unload(self):
        """Disconnect callbacks established at init time."""
        _LOGGER.debug("Unload")
        self.stop_serial_read()

    # async def async_config_entry_first_refresh(self):
    #     """Refresh data for the first time when a config entry is setup."""
    #     _LOGGER.debug("First Refresh")
    #     return await self.hass.async_create_task(self.serial_read("ADCO"))
    #     # return await self.serial_read("ADCO")

    def initialize_reading(self):
        """Register read task to home assistant"""
        if self._serial_loop_task:
            _LOGGER.warn("task already initialized")
            return

        _LOGGER.info("Initialize teleinfo task")
        self.hass.bus.async_listen_once(
            EVENT_HOMEASSISTANT_STOP, self.stop_serial_read()
        )

        self._serial_loop_task = self.hass.loop.create_task(self.serial_read())

    async def serial_read(self):
        """Process the serial data."""
        _LOGGER.debug(u"Initializing Teleinfo")

        logged_error = False
        while True:
            try:
                reader, _ = await serial_asyncio.open_serial_connection(
                    url=self.port,
                    baudrate=1200,
                    bytesize=7,
                    parity=serial.PARITY_EVEN,
                    stopbits=serial.STOPBITS_ONE,
                    timeout=self.timeout,
                )
            except serial.SerialException as exc:
                if not logged_error:
                    _LOGGER.exception(
                        "Unable to connect to the serial device %s: %s. Will retry",
                        self.port,
                        exc,
                    )
                    logged_error = True
                await asyncio.sleep(5)
            else:

                is_over = True

                while True:
                    try:
                        rawline = await reader.readline()
                    except serial.SerialException as exc:
                        _LOGGER.exception(
                            "Error while reading serial device %s: %s", self.port, exc
                        )
                        await asyncio.sleep(5)
                        break
                    else:
                        line = rawline.replace(b"\r", b"").replace(b"\n", b"")

                        if is_over and (b"\x02" in line):
                            is_over = False
                            _LOGGER.debug("Start Frame")
                            continue

                        if (not is_over) and (b"\x03" not in line):
                            part_size = len(line.split())
                            if part_size == 2:
                                name, value = line.split()
                                checksum = b" "
                            elif part_size == 3:
                                name, value, checksum = line.split()
                            else:
                                continue

                            if await self._validate_checksum(line, checksum):
                                name = name.decode()
                                value = value.decode()
                                _LOGGER.debug("Got : [%s] =  (%s)", name, value)
                                self.hass.helpers.dispatcher.dispatcher_send(
                                    SIGNAL_RECEIVE_MESSAGE, {name: value}
                                )
                                if name == "ADCO" and self.device_id is None:
                                    self.device_id = value

                        if (not is_over) and (b"\x03" in line):
                            is_over = True
                            _LOGGER.debug(" End Frame")
                            continue

    async def _validate_checksum(self, frame, checksum):
        """Check if a frame is valid."""
        datas = frame[:-2]
        computed_checksum = (sum(datas) & 0x3F) + 0x20
        if computed_checksum == ord(checksum):
            return True
        _LOGGER.warning(
            u"Invalid checksum for %s : %s != %s",
            frame,
            computed_checksum,
            ord(checksum),
        )
        return False

    @callback
    def stop_serial_read(self):
        """Close resources."""
        if self._serial_loop_task:
            self._serial_loop_task.cancel()


async def detect():
    """Return a list of candidate paths for USB Teleinformation dongles.

    This method is currently a bit simplistic, it may need to be
    improved to support more configurations and OS.
    """
    globs_to_test = ["/dev/tty*", "/dev/serial/by-id/*"]
    found_paths = []
    for current_glob in globs_to_test:
        found_paths.extend(glob.glob(current_glob))

    return found_paths


async def validate_path(path: str):
    """Return True if the provided path points to a valid serial port, False otherwise."""
    try:
        # Creating the serial communicator will raise an exception
        # if it cannot connect
        with serial.Serial(port=path):
            return True

    except serial.SerialException as exception:
        _LOGGER.warning("Dongle path %s is invalid: %s", path, str(exception))
        return False

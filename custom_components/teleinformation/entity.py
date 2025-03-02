"""TeleinformationEntity class"""

from homeassistant.helpers.entity import Entity

from .const import DOMAIN
from .const import NAME
from .const import SIGNAL_RECEIVE_MESSAGE
from .const import VERSION


class TeleinformationEntity(Entity):
    def __init__(self, meter_id):
        """Initialize the device."""
        self.meter_id = meter_id

    @property
    def device_info(self):
        """Get device Info."""
        return {
            "identifiers": {(DOMAIN, self.meter_id)},
            "name": NAME,
            "model": self.meter_id,
            "sw_version": VERSION,
            "manufacturer": "Enedis",
        }

    @property
    def should_poll(self):
        """Push mode do not poll."""
        return False

    async def async_added_to_hass(self):
        """Register callbacks."""
        self.async_on_remove(
            self.hass.helpers.dispatcher.async_dispatcher_connect(
                SIGNAL_RECEIVE_MESSAGE, self._message_received_callback
            )
        )

    def _message_received_callback(self, frame):
        """Handle incoming packets."""
        self.value_changed(frame)

    def value_changed(self, frame):
        """Update the internal state of the device when a packet arrives."""

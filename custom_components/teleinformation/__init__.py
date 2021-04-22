"""
Custom integration to integrate teleinformation with Home Assistant.

For more details about this integration, please refer to
https://github.com/poppypop/integration_teleinformation
"""
import asyncio
from .dongle import TeleInformationDongle
from .const import DATA_DONGLE, DATA_SERIAL_NUMBER, DOMAIN, PLATFORMS
from datetime import timedelta

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import Config
from homeassistant.core import HomeAssistant

SCAN_INTERVAL = timedelta(minutes=900)


async def async_setup(hass: HomeAssistant, config: Config):
    """Set up this integration using YAML is not supported."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up this integration using UI."""
    if hass.data.get(DOMAIN) is None:
        hass.data.setdefault(DOMAIN, {})

    # First gather teleinfo frame for config
    hass.data[DOMAIN][entry.entry_id] = {}

    usb_dongle = TeleInformationDongle(hass, entry)

    hass.data[DOMAIN][entry.entry_id][DATA_DONGLE] = usb_dongle

    # serialnumber = await usb_dongle.async_config_entry_first_refresh()
    usb_dongle.initialize_reading()

    while usb_dongle.device_id == None:
        await asyncio.sleep(1)

    hass.data[DOMAIN][entry.entry_id][DATA_SERIAL_NUMBER] = usb_dongle.device_id

    for platform in PLATFORMS:
        hass.async_create_task(
            hass.config_entries.async_forward_entry_setup(entry, platform)
        )

    entry.add_update_listener(_async_reload_entry)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Handle removal of an entry."""

    usb_dongle = hass.data[DOMAIN][entry.entry_id][DATA_DONGLE]
    usb_dongle.unload()

    unloaded = all(
        await asyncio.gather(
            *[
                hass.config_entries.async_forward_entry_unload(entry, platform)
                for platform in PLATFORMS
            ]
        )
    )
    if unloaded:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unloaded


async def _async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Reload config entry."""
    await hass.config_entries.async_reload(entry.entry_id)

"""Adds config flow for teleinformation."""
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant import config_entries
from homeassistant.core import callback

from .const import (
    CONF_DEVICE,
    CONF_MONITORED_VARIABLES,
    CONF_TIMEOUT,
    DEFAULT_CONF_TIMEOUT,
    DOMAIN,
    ERROR_INVALID_DONGLE_PATH,
    MANUAL_PATH_VALUE,
    SENSOR_TYPES,
    SENSOR_TYPES_DEFAULT,
)

from . import dongle


class TeleinformationFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for teleinformation."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_PUSH

    def __init__(self):
        """Initialize."""

    async def async_step_user(self, user_input=None):
        """Handle an TeleInformation config flow start."""
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        return await self.async_step_detect()

    async def async_step_detect(self, user_input=None):
        """Propose a list of detected dongles."""
        errors = {}
        if user_input is not None:
            if user_input[CONF_DEVICE] == MANUAL_PATH_VALUE:
                return await self.async_step_manual()
            if await self.validate_teleinformation_device(user_input):
                return self.async_create_entry(title="TeleInformation", data=user_input)
            errors = {CONF_DEVICE: ERROR_INVALID_DONGLE_PATH}

        bridges = await dongle.detect()
        if len(bridges) == 0:
            return await self.async_step_manual(user_input)

        bridges.append(MANUAL_PATH_VALUE)
        return self.async_show_form(
            step_id="detect",
            data_schema=vol.Schema({vol.Required(CONF_DEVICE): vol.In(bridges)}),
            errors=errors,
        )

    async def async_step_manual(self, user_input=None):
        """Request manual USB dongle path."""
        default_value = None
        errors = {}

        if user_input is not None:
            if await self.validate_teleinformation_device(user_input):
                return self.async_create_entry(title="TeleInformation", data=user_input)
            default_value = user_input[CONF_DEVICE]
            errors = {CONF_DEVICE: ERROR_INVALID_DONGLE_PATH}

        return self.async_show_form(
            step_id="manual",
            data_schema=vol.Schema(
                {vol.Required(CONF_DEVICE, default=default_value): str}
            ),
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Get the options flow for this handler."""
        return OptionsFlowHandler(config_entry)

    async def validate_teleinformation_device(self, user_input) -> bool:
        """Return True if the user_input contains a valid dongle path."""
        dongle_path = user_input[CONF_DEVICE]
        path_is_valid = await dongle.validate_path(dongle_path)

        return path_is_valid


class OptionsFlowHandler(config_entries.OptionsFlow):
    """Handle a option flow for teleinformation."""

    def __init__(self, config_entry: config_entries.ConfigEntry):
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Handle options flow."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        known_available_resources = {
            sensor_id: sensor[0] for sensor_id, sensor in SENSOR_TYPES.items()
        }

        resources = self.config_entry.options.get(
            CONF_MONITORED_VARIABLES, SENSOR_TYPES_DEFAULT
        )
        scan_interval = self.config_entry.options.get(
            CONF_TIMEOUT, DEFAULT_CONF_TIMEOUT
        )

        errors = {}

        if errors:
            return self.async_show_form(step_id="abort", errors=errors)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Optional(CONF_TIMEOUT, default=scan_interval): cv.positive_int,
                    vol.Required(
                        CONF_MONITORED_VARIABLES, default=resources
                    ): cv.multi_select(known_available_resources),
                }
            ),
            errors=errors,
        )

    async def async_step_abort(self, user_input=None):
        """Abort options flow."""
        return self.async_create_entry(title="", data=self.config_entry.options)

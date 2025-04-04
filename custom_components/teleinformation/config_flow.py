"""Adds config flow for teleinformation."""

import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback

from . import dongle
from .const import CONF_COUNTERTYPE
from .const import CONF_DEVICE
from .const import CONF_MONITORED_VARIABLES
from .const import CONF_TIMEOUT
from .const import DEFAULT_CONF_TIMEOUT
from .const import DOMAIN
from .const import ERROR_INVALID_DONGLE_PATH
from .const import MANUAL_PATH_VALUE
from .const import SENSOR_HISTORICAL
from .const import SENSOR_RECOMMENDED_DEFAULT
from .const import SENSOR_STANDARD
from .const import SENSOR_TYPES_HISTO
from .const import SENSOR_TYPES_STANDARD


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

        return await self.async_step_metertype()

    async def async_step_metertype(self, user_input=None):
        """Propose a list of meter type."""
        errors = {}

        if user_input is not None:
            return await self.async_step_detect()

        known_meter = {
            SENSOR_HISTORICAL: "Mode historique",
            SENSOR_STANDARD: "Mode standard",
        }

        return self.async_show_form(
            step_id="detect",
            data_schema=vol.Schema(
                {vol.Required(CONF_COUNTERTYPE): vol.In(known_meter)}
            ),
            errors=errors,
        )

    async def async_step_detect(self, user_input=None):
        """Propose a list of detected dongles."""
        errors = {}
        if user_input is not None and CONF_DEVICE in user_input.keys():
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

        countert = self.config_entry.options.get(CONF_COUNTERTYPE)
        if countert == SENSOR_HISTORICAL:
            BASE_SENSORS = SENSOR_TYPES_HISTO
        else:
            BASE_SENSORS = SENSOR_TYPES_STANDARD

        DEFAULT_SENSORS = [
            sensor_id
            for sensor_id, sensor in BASE_SENSORS.items()
            if sensor_id in SENSOR_RECOMMENDED_DEFAULT
        ]

        known_available_resources = {
            sensor_id: sensor[0] for sensor_id, sensor in BASE_SENSORS.items()
        }

        resources = self.config_entry.options.get(
            CONF_MONITORED_VARIABLES, DEFAULT_SENSORS
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

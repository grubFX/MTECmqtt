from homeassistant import config_entries
import voluptuous as vol


class MTECConfigFlow(config_entries.ConfigFlow, domain="MTEC"):
    """Handle a config flow for MTEC."""

    VERSION = 0
    MINOR_VERSION = 0

    async def async_step_user_modbus(self, user_input=None):
        """Handle the Modbus config step."""

        if user_input is not None:
            pass  # TODO: process data

        return self.async_show_form(
            step_id="user_modbus",
            data_schema=vol.Schema(
                {
                    vol.Required("ip", default="espressif.local"): str,
                    vol.Required("port", default=5743): vol.All(
                        vol.Coerce(int), vol.Range(min=1, max=65535)
                    ),
                    vol.Required("slave", default=252): int,
                    vol.Required("timeout", default=5): int,
                    vol.Required("retries", default=3): int,
                    vol.Required("framer", default="rtu"): vol.In(
                        ["ascii", "binary", "rtu", "socket", "tls"]
                    ),
                }
            ),
            description_placeholders=user_input,
        )

    async def async_step_user_refresh(self, user_input=None):
        """Handle the refresh config step."""

        if user_input is not None:
            pass  # TODO: process data

        return self.async_show_form(
            step_id="user_refresh",
            data_schema=vol.Schema(
                {
                    vol.Required("now_s", default=10): vol.All(
                        vol.Coerce(int), vol.Range(min=1)
                    ),
                    vol.Required("day_m", default=5): int,
                    vol.Required("total_m", default=5): int,
                    vol.Required("config_m", default=60): int,
                }
            ),
        )

    async def async_step_user_extended_data(self, user_input=None):
        """Handle the extended data config step."""

        if user_input is not None:
            pass  # TODO: process data

        return self.async_show_form(
            step_id="user_extended_data",
            data_schema=vol.Schema(
                {
                    vol.Required("grid_data", default=True): bool,
                    vol.Required("inverter_data", default=True): bool,
                    vol.Required("backup_data", default=True): bool,
                    vol.Required("battery_data", default=True): bool,
                    vol.Required("pv_data", default=True): bool,
                }
            ),
        )

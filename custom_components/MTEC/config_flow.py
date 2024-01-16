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
                    vol.Required("ip"): str,
                    vol.Required("port"): int,
                    vol.Required("slave"): int,
                    vol.Required("timeout"): int,
                    vol.Required("retries"): int,
                    vol.Required("framer"): int,
                }
            ),
        )

    async def async_step_user_refresh(self, user_input=None):
        """Handle the refresh config step."""

        if user_input is not None:
            pass  # TODO: process data

        return self.async_show_form(
            step_id="user_refresh",
            data_schema=vol.Schema(
                {
                    vol.Required("now_s"): int,
                    vol.Required("day_m"): int,
                    vol.Required("total_m"): int,
                    vol.Required("config_m"): int,
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
                    vol.Required("grid_data"): bool,
                    vol.Required("inverter_data"): bool,
                    vol.Required("backup_data"): bool,
                    vol.Required("battery_data"): bool,
                    vol.Required("pv_data"): bool,
                }
            ),
        )

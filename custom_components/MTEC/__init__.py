"""The MTEC integration."""
import logging

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

_LOGGER = logging.getLogger(__name__)

DOMAIN = "MTEC"

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the MTEC integration."""
    _LOGGER.info("Setting up MTEC integration")
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up MTEC from a config entry."""
    _LOGGER.info("Setting up MTEC from config entry")
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    _LOGGER.info("Unloading MTEC config entry")
    return True

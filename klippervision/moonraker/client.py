"""
Moonraker client.
"""

from klippervision.config.settings import Settings
from klippervision.moonraker.models import PrinterStatus


class MoonrakerClient:
    """Moonraker API client."""

    def __init__(self, settings: Settings):
        self.settings = settings

    @property
    def base_url(self) -> str:
        return (
            f"http://{self.settings.moonraker_host}:"
            f"{self.settings.moonraker_port}"
        )

    def get_status(self) -> PrinterStatus:
        """
        Temporary mock response.

        This will become a real API call later.
        """

        return PrinterStatus(
            connected=True,
            state="Ready",
            progress=0.0,
            filename="",
            nozzle_temp=25.0,
            bed_temp=24.0,
        )
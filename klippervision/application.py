from klippervision.config.settings import Settings
from klippervision.moonraker.client import MoonrakerClient


class Application:
    """Main KlipperVision application."""

    def __init__(self):
        self.settings = Settings()
        self.moonraker = MoonrakerClient(self.settings)

    def run(self):
        status = self.moonraker.get_status()

        print("=================================")
        print("      KlipperVision v0.1.0")
        print("=================================")

        print(f"Printer      : {self.settings.printer_name}")
        print(f"Moonraker    : {self.moonraker.base_url}")
        print(f"State        : {status.state}")
        print(f"Connected    : {status.connected}")
        print(f"Nozzle Temp  : {status.nozzle_temp}°C")
        print(f"Bed Temp     : {status.bed_temp}°C")
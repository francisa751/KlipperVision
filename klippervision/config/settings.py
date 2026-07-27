from dataclasses import dataclass


@dataclass
class Settings:
    printer_name: str = "My Printer"
    moonraker_host: str = "localhost"
    moonraker_port: int = 7125
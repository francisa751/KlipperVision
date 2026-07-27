"""
Moonraker data models.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class PrinterStatus:
    """Represents the current printer status."""

    connected: bool
    state: str
    progress: float
    filename: str
    nozzle_temp: float
    bed_temp: float


@dataclass(slots=True)
class PrinterInfo:
    """Basic information about the printer."""

    hostname: str
    software_version: str
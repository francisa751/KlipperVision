"""
Moonraker exceptions.
"""


class MoonrakerError(Exception):
    """Base Moonraker exception."""


class ConnectionFailed(MoonrakerError):
    """Unable to connect to Moonraker."""


class InvalidResponse(MoonrakerError):
    """Moonraker returned invalid data."""
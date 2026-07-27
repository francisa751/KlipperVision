from dataclasses import dataclass


@dataclass(slots=True)
class CameraInfo:
    """Information about a connected camera."""

    index: int
    width: int
    height: int
    fps: float
    connected: bool
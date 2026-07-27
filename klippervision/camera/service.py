from __future__ import annotations

import threading
import cv2


class CameraService:
    """Continuously captures frames from a camera."""

    def __init__(self, camera_index: int = 0):
        self.camera_index = camera_index
        self.capture = None
        self.running = False
        self.frame = None
        self.thread = None

    def start(self) -> bool:
        self.capture = cv2.VideoCapture(self.camera_index, cv2.CAP_DSHOW)

        if not self.capture.isOpened():
            return False

        self.running = True
        self.thread = threading.Thread(target=self._capture_loop, daemon=True)
        self.thread.start()

        return True

    def _capture_loop(self):
        while self.running:
            success, frame = self.capture.read()

            if success:
                self.frame = frame

    def get_frame(self):
        return self.frame

    def stop(self):
        self.running = False

        if self.thread:
            self.thread.join(timeout=1)

        if self.capture:
            self.capture.release()
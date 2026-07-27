from __future__ import annotations

import cv2

from klippervision.camera.models import CameraInfo


class CameraManager:
    """Handles webcam access."""

    def __init__(self, camera_index: int = 0):
        self.camera_index = camera_index
        self.capture = None

    def start(self) -> bool:
        self.capture = cv2.VideoCapture(self.camera_index, cv2.CAP_DSHOW)

        if not self.capture.isOpened():
            return False

        return True

    def stop(self):
        if self.capture:
            self.capture.release()

        cv2.destroyAllWindows()

    def get_frame(self):
        if self.capture is None:
            return False, None

        return self.capture.read()

    def get_info(self) -> CameraInfo:
        return CameraInfo(
            index=self.camera_index,
            width=int(self.capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
            height=int(self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT)),
            fps=self.capture.get(cv2.CAP_PROP_FPS),
            connected=self.capture.isOpened(),
        )
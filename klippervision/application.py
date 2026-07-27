import cv2

from klippervision.camera.service import CameraService
from klippervision.utils.overlay import draw_overlay
from klippervision.detector.yolo import YoloDetector

class Application:
    """Main application."""

    def __init__(self):
        self.camera = CameraService()
        self.detector = YoloDetector()  # Assuming you have a YOLO detector class defined elsewhere

    def run(self):

        if not self.camera.start():
            print("Unable to connect to camera.")
            return

        print("Camera connected.")

        while True:

            frame = self.camera.get_frame()

            if frame is not None:
                results = self.detector.detect(frame)
                frame = results[0].plot() 
                frame = draw_overlay(frame)  # Assuming draw_overlay is a function that draws the detection results on the frame
                cv2.imshow("KlipperVision", frame)

            key = cv2.waitKey(1)

            if key == ord("q"):
                break

        self.camera.stop()
        cv2.destroyAllWindows()
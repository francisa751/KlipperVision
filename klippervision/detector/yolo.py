from ultralytics import YOLO


class YoloDetector:

    def __init__(self):

        print("Loading YOLO model...")

        self.model = YOLO("yolo11n.pt")

        print("YOLO ready.")

    def detect(self, frame):

        return self.model(frame, verbose=False)
import cv2

from klippervision.camera.service import CameraService


camera = CameraService()

if not camera.start():
    print("Unable to open camera.")
    raise SystemExit

while True:
    frame = camera.get_frame()

    if frame is not None:
        cv2.imshow("KlipperVision", frame)

    if cv2.waitKey(1) == ord("q"):
        break

camera.stop()
cv2.destroyAllWindows()
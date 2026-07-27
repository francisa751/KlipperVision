"""
Simple webcam test for KlipperVision.

Press Q to quit.
"""

import cv2


def main():
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not camera.isOpened():
        print("Unable to open camera.")
        return

    print("Camera opened successfully.")

    width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = camera.get(cv2.CAP_PROP_FPS)

    print(f"Resolution : {width} x {height}")
    print(f"FPS        : {fps}")

    while True:
        success, frame = camera.read()

        if not success:
            break

        cv2.imshow("KlipperVision Camera Test", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
from djitellopy import tello
import cv2

drone = tello.Tello()
drone.connect()
print(drone.get_battery())

drone.streamon()


def main():
    img = drone.get_frame_read().frame
    cv2.imshow("Image", img)
    cv2.waitKey(17)
    # 17 ms is approximately 60 fps.


if __name__ == "__main__":
    while True:
        main()

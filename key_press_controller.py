import key_press_module as kp
from djitellopy import tello
from time import sleep
import threading
import cv2

kp.init()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())
drone.streamon()


def get_keyboard_input():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.get_key("a"): lr = -speed
    if kp.get_key("d"): lr = speed
    if kp.get_key("w"): fb = speed
    if kp.get_key("s"): fb = -speed
    if kp.get_key("q"):
        drone.land()
        drone.send_rc_control(0, 0, 0, 0)
    if kp.get_key("l"):
        drone.takeoff()
    if kp.get_key("COMMA"): yv = 2 * speed
    if kp.get_key("PERIOD"): yv = -2 * speed
    if kp.get_key("n"): ud = speed
    if kp.get_key("m"): ud = -speed
    if kp.get_key("f") and drone.get_battery() > 50: drone.flip_forward()
    if kp.get_key("c") and drone.get_battery() > 50: drone.flip_back()
    # In case battery is under 50, in which case you can't flip. If I don't include this check here
    # it'll error.
    return [lr, fb, ud, yv]


def inputLoop():
    vals2 = []
    while True:
        vals = get_keyboard_input()
        if vals != vals2:
            drone.send_rc_control(vals[0], vals[1], vals [2], vals [3])
        vals2 = vals
        sleep(0.017)
def videoStreamLoop():
    while True:
        img.drone.get_frame_read().frame
        cv2.imshow("Image", img)
        sleep(0.017)

videoThread = threading.Thread(target = videoStreamLoop)
inputThread = threading.Thread(target = inputLoop)

videoThread.start()
inputThread.start()


"""
The code is derived from https://www.youtube.com/watch?v=LmEcyQnfpDA&t=1642s however I've added some of my own
pizzazz.

LIBRARIES:
please make sure you have the following libraries installed:
    -djitellopy
    -opencv-python
    -time
    -pygame
    -numpy (maybe, I may forget to delete this later if I end up never using numpy)
    -nvm im not using numpy rn
"""

"""
TODO:
-Add threading in keyboard controller to prevent camera freezing
-Get rid of annoying INFO prints
-Facial recognition with opencv
"""

from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()


battery_percentage = drone.get_battery()
print(battery_percentage)


def main():
    drone.takeoff()
    drone.send_rc_control(0, 0, 0, 50)
    sleep(1)
    drone.send_rc_control(0, -50, 0, 0)
    sleep(1.5)
    drone.send_rc_control(0,0,0,0)
    drone.land()


main()

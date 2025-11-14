#!/usr/bin/env python3

import time
import cozmo


def cozmo_program(robot: cozmo.robot.Robot):
    robot.drive_wheels(50, 100)
    time.sleep(3)
    robot.drive_wheels(0, 0)

    time.sleep(1)

    robot.drive_wheels(50, 100)
    time.sleep(3)
    robot.drive_wheels(0, 0)

    time.sleep(1)

    robot.drive_wheels(-100, 100)
    time.sleep(4)
    robot.drive_wheels(0, 0)

    time.sleep(1)

    robot.drive_wheels(-50, -50)
    time.sleep(3)
    robot.drive_wheels(0, 0)


cozmo.run_program(cozmo_program)

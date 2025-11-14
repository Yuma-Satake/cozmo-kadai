#!/usr/bin/env python3

import cozmo
from cozmo.util import degrees


def cozmo_program(robot: cozmo.robot.Robot):
    robot.set_head_angle(degrees(-22.0)).wait_for_completed()
    robot.set_lift_height(0.0).wait_for_completed()

    robot.set_head_angle(degrees(44.5)).wait_for_completed()
    robot.set_lift_height(1.0).wait_for_completed()

    robot.set_head_angle(degrees(-22.0)).wait_for_completed()
    robot.set_lift_height(1.0).wait_for_completed()

    robot.set_head_angle(degrees(44.5)).wait_for_completed()
    robot.set_lift_height(0.0).wait_for_completed()

    robot.set_head_angle(degrees(10.0)).wait_for_completed()
    robot.set_lift_height(0.5).wait_for_completed()

    robot.set_head_angle(degrees(0.0)).wait_for_completed()
    robot.set_lift_height(0.0).wait_for_completed()


cozmo.run_program(cozmo_program)

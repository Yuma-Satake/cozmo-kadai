#!/usr/bin/env python3

import sys
import tty
import termios
import time
import os
import cozmo
from cozmo.util import degrees

DRIVE_SPEED = 100
TURN_SPEED = 80
LIFT_SPEED = 3
HEAD_SPEED = 1
MOVE_DURATION = 0.3


def getch() -> str:
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def find_nearest_cube(robot: cozmo.robot.Robot) -> cozmo.objects.LightCube:
    nearest_cube = None
    min_distance = float('inf')

    for obj in robot.world.visible_objects:
        if isinstance(obj, cozmo.objects.LightCube):
            translation = robot.pose - obj.pose
            distance = translation.position.x ** 2 + translation.position.y ** 2
            if distance < min_distance:
                min_distance = distance
                nearest_cube = obj

    return nearest_cube


def clear_screen() -> None:
    os.system('clear')


def show_status(status: str, held_cube: bool) -> None:
    clear_screen()
    cube_status = "Holding cube" if held_cube else "No cube"
    print("=== Cozmo Remote Control ===")
    print("")
    print("  [W] Forward    [R] Lift Up    [T] Head Up")
    print("[A][S][D] Move   [F] Lift Down  [G] Head Down")
    print("")
    print("[L] Look for cubes  [P] Pickup  [O] Place  [Q] Quit")
    print("")
    print(f"Cube: {cube_status}")
    print(f"Status: {status}")


def cozmo_program(robot: cozmo.robot.Robot) -> None:
    robot.set_head_angle(degrees(0)).wait_for_completed()

    held_cube = None
    running = True
    show_status("Ready", held_cube is not None)

    while running:
        key = getch().lower()

        if key == 'w':
            show_status("Forward", held_cube is not None)
            robot.drive_wheels(DRIVE_SPEED, DRIVE_SPEED)
            time.sleep(MOVE_DURATION)
            robot.drive_wheels(0, 0)
        elif key == 's':
            show_status("Backward", held_cube is not None)
            robot.drive_wheels(-DRIVE_SPEED, -DRIVE_SPEED)
            time.sleep(MOVE_DURATION)
            robot.drive_wheels(0, 0)
        elif key == 'a':
            show_status("Turn Left", held_cube is not None)
            robot.drive_wheels(-TURN_SPEED, TURN_SPEED)
            time.sleep(MOVE_DURATION)
            robot.drive_wheels(0, 0)
        elif key == 'd':
            show_status("Turn Right", held_cube is not None)
            robot.drive_wheels(TURN_SPEED, -TURN_SPEED)
            time.sleep(MOVE_DURATION)
            robot.drive_wheels(0, 0)
        elif key == 'r':
            show_status("Lift Up", held_cube is not None)
            robot.move_lift(LIFT_SPEED)
            time.sleep(MOVE_DURATION)
            robot.move_lift(0)
        elif key == 'f':
            show_status("Lift Down", held_cube is not None)
            robot.move_lift(-LIFT_SPEED)
            time.sleep(MOVE_DURATION)
            robot.move_lift(0)
        elif key == 't':
            show_status("Head Up", held_cube is not None)
            robot.move_head(HEAD_SPEED)
            time.sleep(MOVE_DURATION)
            robot.move_head(0)
        elif key == 'g':
            show_status("Head Down", held_cube is not None)
            robot.move_head(-HEAD_SPEED)
            time.sleep(MOVE_DURATION)
            robot.move_head(0)
        elif key == 'l':
            show_status("Looking for cubes...", held_cube is not None)
            lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
            try:
                cubes = robot.world.wait_until_observe_num_objects(
                    num=1,
                    object_type=cozmo.objects.LightCube,
                    timeout=10
                )
                show_status(f"Found {len(cubes)} cube(s)", held_cube is not None)
            except Exception:
                show_status("No cubes found", held_cube is not None)
            finally:
                lookaround.stop()
        elif key == 'p':
            cube = find_nearest_cube(robot)
            if cube is None:
                show_status("No cube visible. Press L first.", held_cube is not None)
            else:
                show_status("Picking up...", held_cube is not None)
                action = robot.pickup_object(cube, num_retries=2)
                action.wait_for_completed()
                if action.has_failed:
                    show_status("Pickup failed", held_cube is not None)
                else:
                    held_cube = cube
                    show_status("Picked up!", held_cube is not None)
        elif key == 'o':
            if held_cube is None:
                show_status("No cube held", held_cube is not None)
            else:
                show_status("Placing...", held_cube is not None)
                action = robot.place_object_on_ground_here(held_cube, num_retries=2)
                action.wait_for_completed()
                if action.has_failed:
                    show_status("Place failed", held_cube is not None)
                else:
                    held_cube = None
                    show_status("Placed!", held_cube is not None)
        elif key == 'q' or key == '\x03':
            show_status("Quitting...", held_cube is not None)
            running = False

    robot.drive_wheels(0, 0)
    clear_screen()


cozmo.run_program(cozmo_program)

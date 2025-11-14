#!/usr/bin/env python3

import os
import sys
import time
import random

try:
    from PIL import Image
except ImportError:
    sys.exit("Cannot import from PIL: Do `pip3 install --user Pillow` to install")

import cozmo

ANIMATION_DURATION = 0.3
FINAL_DISPLAY_DURATION = 2.0
ANIMATION_LOOPS = 5

def get_in_position(robot: cozmo.robot.Robot) -> None:
    if (robot.lift_height.distance_mm > 45) or (robot.head_angle.degrees < 40):
        with robot.perform_off_charger():
            lift_action = robot.set_lift_height(0.0, in_parallel=True)
            head_action = robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE, in_parallel=True)
            lift_action.wait_for_completed()
            head_action.wait_for_completed()

def load_janken_images(current_directory: str) -> list:
    goo_png = os.path.join(current_directory, "goo.png")
    choki_png = os.path.join(current_directory, "choki.png")
    paa_png = os.path.join(current_directory, "paa.png")

    image_paths = [goo_png, choki_png, paa_png]
    face_images = []

    for image_path in image_paths:
        image = Image.open(image_path)
        resized_image = image.resize(cozmo.oled_face.dimensions(), Image.BICUBIC)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image, invert_image=True)
        face_images.append(face_image)

    return face_images

def play_janken(robot: cozmo.robot.Robot, face_images: list) -> None:
    robot.say_text("じゃんけんぽん").wait_for_completed()

    for _ in range(ANIMATION_LOOPS):
        for image in face_images:
            robot.display_oled_face_image(image, ANIMATION_DURATION * 1000.0)
            time.sleep(ANIMATION_DURATION)

    final_choice = random.choice(face_images)
    robot.display_oled_face_image(final_choice, FINAL_DISPLAY_DURATION * 1000.0)
    time.sleep(FINAL_DISPLAY_DURATION)

def cozmo_program(robot: cozmo.robot.Robot) -> None:
    current_directory = os.path.dirname(os.path.realpath(__file__))
    get_in_position(robot)

    face_images = load_janken_images(current_directory)

    while True:
        play_janken(robot, face_images)
        time.sleep(1)

cozmo.robot.Robot.drive_off_charger_on_connect = False
cozmo.run_program(cozmo_program)

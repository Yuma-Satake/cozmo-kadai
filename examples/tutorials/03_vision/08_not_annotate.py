#!/usr/bin/env python3

# Copyright (c) 2016 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''Display a GUI window showing an annotated camera view.

Note:
    This example requires Python to have Tkinter installed to display the GUI.
    It also requires the Pillow and numpy python packages to be pip installed.

The :class:`cozmo.world.World` object collects raw images from Cozmo's camera
and makes them available as a property (:attr:`~cozmo.world.World.latest_image`)
and by generating :class:`cozmo.world.EvtNewCamerImages` events as they come in.

Each image is an instance of :class:`cozmo.world.CameraImage` which provides
access both to the raw camera image, and to a scalable annotated image which
can show where Cozmo sees faces and objects, along with any other information
your program may wish to display.

This example uses the tkviewer to display the annotated camera on the screen
and adds a couple of custom annotations of its own using two different methods.
'''
#---------------------------------------------------------和訳↓
'''
注釈付きのカメラ ビューを示す GUI ウィンドウを表示します。

Note:
    この例では、GUI を表示するために Python に Tkinter がインストールされている必要があります。
    また、Pillow および numpy Python パッケージを pip インストールする必要があります。

:class:`cozmo.world.World` オブジェクトは、Cozmo のカメラから生の画像を収集します
それらをプロパティ (:attr:`~cozmo.world.World.latest_image`) として利用できるようにします。
そして、受信時に :class:`cozmo.world.EvtNewCamerImages` イベントを生成します。

各画像は、次の機能を提供する :class:`cozmo.world.CameraImage` のインスタンスです。
生のカメラ画像と、スケーラブルな注釈付き画像の両方にアクセスします。
Cozmo が顔や物体を認識する場所とその他の情報を表示できます
あなたのプログラムは表示したいかもしれません。

この例では、tkviewer を使用して、注釈付きのカメラを画面上に表示します。
そして、2 つの異なる方法を使用して、独自のカスタム アノテーションをいくつか追加します。
'''


import sys
import time
from cozmo.util import degrees, distance_mm, speed_mmps

try:
    from PIL import ImageDraw, ImageFont
except ImportError:
    sys.exit('run `pip3 install --user Pillow numpy` to run this example')

import cozmo


#
def cozmo_program(robot: cozmo.robot.Robot):

    # この処理の間は、キー入力を受け付けない？
    robot.turn_in_place(degrees(-90)).wait_for_completed()

    robot.turn_in_place(degrees(90)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()

    robot.turn_in_place(degrees(-90)).wait_for_completed()


    print("Shutdown the program after 10 seconds")
    #time.sleep(5)
    return
#def key_ctrl(robot: cozmo.robot.Robot):


cozmo.run_program(cozmo_program, use_viewer=True, force_viewer_on_top=True)

# while True:
#     cozmo.run_program(cozmo_program, use_viewer=True, force_viewer_on_top=True)
#     print('--------------- WASD操作 ----------------')
#     n = input('command: ')
#     print(f'your input: {n}')
#     if n == 'z':
#         print("---- 終了します ----")
#         exit()

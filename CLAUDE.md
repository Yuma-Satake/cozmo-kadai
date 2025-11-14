# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## プロジェクト概要

このリポジトリは、Anki Cozmo Python SDKを使用した学習課題のコレクションです。Cozmoロボットを制御するためのPythonプログラムのサンプルとチュートリアルが含まれています。

## プロジェクト構成

- `examples/` - Cozmo SDK の公式サンプルコード
  - `tutorials/` - 基本から応用までのチュートリアル
    - `01_basics/` - 基本的な動作（移動、音声、モーター制御など）
    - `02_cozmo_face/` - Cozmoの表情表示
    - `03_vision/` - カメラと画像認識
    - `04_cubes_and_objects/` - キューブやオブジェクトの操作
    - `05_async_python/` - 非同期プログラミング
    - `06_actions/` - アクション制御
  - `apps/` - 実用的なアプリケーション例
    - `quizmaster_cozmo.py` - クイズマスターアプリ（3つのキューブをブザーとして使用）
    - `remote_control_cozmo.py` - リモートコントロール
    - その他のアプリケーション
  - `if_this_then_that/` - IFTTT連携サンプル
  - `multi_robot/` - 複数ロボット制御
- `assignment_XX/` - 課題ディレクトリ（課題番号ごとにディレクトリを作成）
  - `assignment_09/` - 課題09（じゃんけんプログラム）
    - `assignment_09.pdf` - 課題資料
    - `nkc_09_janken.py` - 課題プログラム
    - `goo.png`, `choki.png`, `paa.png` - じゃんけん用画像（課題で使用するアセット）

## プログラムの実行方法

Cozmoプログラムは以下のパターンで実行されます：

```python
import cozmo

def cozmo_program(robot: cozmo.robot.Robot):
    # ロボット制御のコード
    robot.say_text("Hello!").wait_for_completed()

cozmo.run_program(cozmo_program)
```

実行コマンド：
```bash
python3 examples/tutorials/01_basics/01_hello_world.py
```

## 主要なCozmo SDK API

### 基本動作
- `robot.say_text(text)` - テキストを読み上げ
- `robot.drive_wheels(l_wheel_speed, r_wheel_speed)` - 左右のホイール速度を制御（mm/秒）
  - 正の値：前進、負の値：後退
  - 異なる速度で曲がりながら移動が可能

### モーター制御
- `robot.move_head(speed)` - 頭部を速度指定で動かす（rad/秒）
- `robot.set_head_angle(degrees(angle))` - 頭部を角度指定で動かす（-22.0 ～ 44.5度）
- `robot.move_lift(speed)` - リフトを速度指定で動かす（rad/秒）
- `robot.set_lift_height(height)` - リフトを高さ指定で動かす（0.0 ～ 1.0）

### 非同期処理
- `.wait_for_completed()` - アクションの完了を待つ
  - この後に`time.sleep()`は不要（エラーになる）
- `async`/`await` - 非同期プログラミングのサポート

### キューブとオブジェクト
- `robot.world.get_light_cube(cube_id)` - キューブオブジェクトの取得
- キューブのライト制御、タップイベント処理など

## 課題ファイルの命名規則と配置

課題を完成させる際は、課題ごとにディレクトリを作成し、以下の構成でファイルを配置します：

### ディレクトリ構成
```
assignment_XX/
  ├── assignment_XX.pdf         # 課題資料
  ├── nkc_XX_xxx.py            # 課題プログラム
  └── その他必要なファイル
```

### 命名規則
- ディレクトリ名：`assignment_XX`（XXは課題番号）
- 課題ファイル名：`nkc_XX_xxx.py`
  - 例：`nkc_09_janken.py`（課題09のじゃんけんプログラム）

### 例
- 元のファイル：`examples/tutorials/02_cozmo_face/01_cozmo_face_image.py`
- 課題ディレクトリ：`assignment_09/`
- 課題ファイル：`assignment_09/nkc_09_janken.py`
- 課題PDF：`assignment_09/assignment_09.pdf`

**重要：課題は必ず `assignment_XX/` ディレクトリ内に整理して配置すること**

## 重要な注意事項

1. **非同期処理の扱い**
   - `wait_for_completed()`の後に`time.sleep()`を使用するとエラーが発生する
   - アクションの完了待ちには`wait_for_completed()`を使用すること

2. **モーター制御のパターン**
   - `drive_wheels()`を使用する場合は、「開始」「継続時間（sleep）」「停止（0, 0）」の3コマンドをセットで使用する

3. **課題実装時の方針**
   - 元のサンプルファイルをコピーして新しいファイル名で作成
   - PDFの課題仕様に従って実装
   - **コメントは一切記載しないこと**（著作権表示、docstring、行コメント等を全て削除）
   - AIが作成したことがわからないようにシンプルなコードのみを記述

4. **画像やアセットファイルの配置**
   - 課題で使用する画像ファイルやその他のアセットは、必ず課題プログラムと同じ `assignment_XX/` ディレクトリ内に配置すること
   - **絶対に `/examples/face_images/` などの共有ディレクトリに配置しないこと**
   - 各課題は単一のディレクトリに展開して、独立して動作する構成にすること
   - プログラム内でのパス指定は、スクリプトと同じディレクトリを基準にする：
     ```python
     current_directory = os.path.dirname(os.path.realpath(__file__))
     image_path = os.path.join(current_directory, "image.png")
     ```

5. **Pythonバージョン**
   - Python 3を使用（`#!/usr/bin/env python3`）
   - ファイル内のインポートは`import cozmo`が基本

## 参考ドキュメント

- Cozmo SDK公式ドキュメント（一部のリンクは古い可能性あり）
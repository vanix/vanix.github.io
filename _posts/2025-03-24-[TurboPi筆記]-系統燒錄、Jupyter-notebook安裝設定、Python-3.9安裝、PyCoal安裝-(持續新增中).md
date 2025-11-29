---
author: 歐巴計概
date: 2025-03-24 04:20:00.026000+00:00
layout: post
permalink: /2025/03/turbopi-jupyter-notebook.html
title: '[TurboPi筆記] 系統燒錄、Jupyter notebook安裝設定、Python 3.9安裝、PyCoal安裝 (持續新增中)'
---

## [別人的TurboPi筆記](https://github.com/rartino/turbopi)

## TurboPi 系統燒錄

## `下載TurboPi提供的映像檔，並使用Win32DiskImager燒錄即可`

## TurboPi 遠端連線

`使用WIFI連線至TurboPi熱點，無線網路密碼為hiwonder`
`內建支援VNC、SSH連線，預設IP：192.168.149.1，帳號//密碼：pi//raspberrypi`

## Resize SD Card Partition

## `使用Gparted即可調整`

## 安裝Jupyter notebook

`$ sudo apt-get install python3-pip
$ pip3 install jupyter`

## 設定Jupyter notebook

`$ jupyter notebook --generate-config
$ jupyter notebook password
$ vi ~/.jupyter/jupyter_notebook_config.py
add this line
c.NotebookApp.ip='*'`

## 啟動Jupyter notebook

`$ jupyter notebook`

## 設定開機後自動啟動Jupyter notebook

`$ ...`

## 安裝人臉辨識套件

## `$ pip3 install face_recognition`

## 安裝Coral AI執行環境 以及 Python 3.9

## `參考資料 安裝Runtime $ echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list $ curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add - $ sudo apt-get update 安裝Pyenv (切換至Python 3.9) $ curl https://pyenv.run | bash 根據Terminal畫面，新增環境辨識至.zshrc or .bashrc $ pyenv install 3.9.18 $ pyenv global 3.9.18 $ python --version #重開Terminal後測試版本 如果要切回原本的版本 $ pyenv rehash $ pyenv global system 安裝driver? $ wget https://gist.githubusercontent.com/AdvancedHobbyLab/923e0e84543b986f482e0479e147d523/raw/6ef81cc44eb6d40d92f8c22cd019a1d302d14bee/coral-ai-pcie-edge-tpu-raspberrypi-5-setup $ chmod u+x coral-ai-pcie-edge-tpu-raspberrypi-5-setup $ ./coral-ai-pcie-edge-tpu-raspberrypi-5-setup $ rm ./coral-ai-pcie-edge-tpu-raspberrypi-5-setup 安裝library $ python3 -m pip install --extra-index-url https://google-coral.github.io/py-repo/ pycoral~=2.0 $ python3 -m pip install numpy==1.19.5 #downgrade 下載Pycoral並測試 $ git clone https://github.com/google-coral/pycoral.git $ cd pycoral $ bash examples/install_requirements.sh classify_image.py $ python3 examples/classify_image.py \ --model test_data/mobilenet_v2_1.0_224_inat_bird_quant_edgetpu.tflite \ --labels test_data/inat_bird_labels.txt \ --input test_data/parrot.jpg`

## TurboPi SDK 基本移動篇

```
# TurboPi範例 搭配 jupyter widget
import sys
sys.path.append('/home/pi/TurboPi/')
import time
import signal
import HiwonderSDK.mecanum as mecanum
import ipywidgets as widgets
from IPython.display import display, clear_output

if sys.version_info.major == 2:
    print('Please run this program with python3!')
    sys.exit(0)

chassis = mecanum.MecanumChassis()

# 创建输出区域
output = widgets.Output()

# 方向键按钮
btn_up = widgets.Button(description="↑", layout=widgets.Layout(width="50px"))
btn_down = widgets.Button(description="↓", layout=widgets.Layout(width="50px"))
btn_left = widgets.Button(description="←", layout=widgets.Layout(width="50px"))
btn_right = widgets.Button(description="→", layout=widgets.Layout(width="50px"))

# 额外功能按钮
btn_turn_left = widgets.Button(description="左转", layout=widgets.Layout(width="60px"))
btn_turn_right = widgets.Button(description="右转", layout=widgets.Layout(width="60px"))
btn_stop = widgets.Button(description="停止", layout=widgets.Layout(width="60px", background="red"))

# 设置默认速度（30~50）和旋转（0~1）
speed = 40  # 预设速度
turn_speed = 0.5  # 预设旋转速度

# 处理按钮点击事件
def on_button_click(direction, velocity, rotation):
    with output:
        clear_output(wait=True)
        print(f"你按下了: {direction}")
        print(f"执行指令: chassis.set_velocity({velocity}, {direction}, {rotation})")
        chassis.set_velocity(velocity, direction, rotation)
        time.sleep(0.1)

        chassis.set_velocity(0,0,0)

btn_up.on_click(lambda _: on_button_click(90, speed, 0))  # 前进
btn_down.on_click(lambda _: on_button_click(270, speed, 0))  # 后退
btn_left.on_click(lambda _: on_button_click(180, speed, 0))  # 左移
btn_right.on_click(lambda _: on_button_click(360, speed, 0))  # 右移
btn_turn_left.on_click(lambda _: on_button_click(90, speed, turn_speed))  # 左转
btn_turn_right.on_click(lambda _: on_button_click(90, speed, -turn_speed))  # 右转
btn_stop.on_click(lambda _: on_button_click(90, 0, 0))  # 停止

# 布局排列按钮
grid = widgets.VBox([
    widgets.HBox([widgets.Label(" "), btn_up, widgets.Label(" ")]),
    widgets.HBox([btn_left, widgets.Label(" "), btn_right]),
    widgets.HBox([widgets.Label(" "), btn_down, widgets.Label(" ")]),
    widgets.HBox([btn_turn_left, btn_stop, btn_turn_right])  # 额外按钮
])

# 显示按钮和输出框
display(grid, output)
```

## TurboPi 相機雲台篇

## ``` # TurboPi範例 ```
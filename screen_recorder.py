#
#  _                                _                __          __ _  _    _        _____      _ 
# | |                              (_)               \ \        / /(_)| |  | |      / ____|    | |
# | |      ___   __ _  _ __  _ __   _  _ __    __ _   \ \  /\  / /  _ | |_ | |__   | |         | |
# | |     / _ \ / _` || '__|| '_ \ | || '_ \  / _` |   \ \/  \/ /  | || __|| '_ \  | |     _   | |
# | |____|  __/| (_| || |   | | | || || | | || (_| |    \  /\  /   | || |_ | | | | | |____| |__| |
# |______|\___| \__,_||_|   |_| |_||_||_| |_| \__, |     \/  \/    |_| \__||_| |_|  \_____|\____/ 
#                                              __/ |                                              
#                                             |___/                         -  By CJ
#
# YouTube : www.youtube.com/@LearningWithCJ
# GitHub  : www.github.com/LearningWithCJ
# Telegram: t.me/LearningWithCJ
#

import cv2
import numpy as np
# pyautogui method
    # import pyautogui
# Pillow method
    # from PIL import ImageGrab



dst_path = "D:/your_file_name.avi"
resolution = (1920, 1080)
codec = cv2.VideoWriter_fourcc(*'XVID')
fps = 30
out = cv2.VideoWriter(dst_path, codec, fps, resolution)

time = 30 # in seconds
num_frames = time * fps

for i in range(num_frames):
    # pyautogui method
        #frame = pyautogui.screenshot()
    # Pillow method
        # frame = ImageGrab.grab(bbox = (0, 0, resolution[0], resolution[1])
    frame = np.array(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)

out.release()

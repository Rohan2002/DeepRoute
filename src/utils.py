import datetime
import os
import glob
import matplotlib.pyplot as plt
import numpy as np
import cv2

def remove_all_files(folder_path: str):
    files = glob.glob(f'{folder_path}/*')
    for f in files:
        os.remove(f)

def sec_to_time(sec):
    seconds_str = str(datetime.timedelta(seconds=sec))
    splt_time = seconds_str.split(":")
    if splt_time[0] == "0":
        return f"{splt_time[1]}:{splt_time[2]}"
    else:
        return seconds_str


def time_to_sec(time: str) -> int:
    if type(time) is not str:
        raise TypeError("Time must be a string")

    time_values = time.split(":")
    if len(time_values) == 3:
        time_in_seconds = (
            (int(time_values[0], base=10) * 3600)
            + (int(time_values[1]) * 60)
            + int(time_values[2])
        )
    elif len(time_values) == 2:
        time_in_seconds = (int(time_values[0], base=10) * 60) + int(time_values[1])
    else:
        raise ValueError(
            "Time to seconds coversion only supports HH:MM:SS and MM:SS as input"
        )
    return time_in_seconds


def time_to_frame(time, rate=30):
    time_in_seconds = time_to_sec(time)
    return time_in_seconds * rate

def plot_image(img):
    img_arr = img
    if type(img) == str and os.path.exists(img):
        img_arr = cv2.imread(img)
    plt.figure(figsize=(20, 20))
    plt.imshow(img_arr)
    plt.show()
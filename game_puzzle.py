#!/usr/bin/python
import threading
import DobotDllType as dType
import tkinter as tk
from tkinter import *
import time
import os
from PIL import ImageTk, Image
import webbrowser
from PIL import ImageTk, Image, ImageGrab, ImageOps
#import pyautogui
import numpy as np
##import sounddevice as sd
#import soundfile as sf
import random

class robot_move:
    def box_2():
        CON_STR = {
            dType.DobotConnect.DobotConnect_NoError: "DobotConnect_NoError",
            dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
            dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}
        # Load Dll
        api = dType.load()
        # Connect Dobot
        state = dType.ConnectDobot(api, "", 115200)[0]
        print("Connect status:", CON_STR[state])
        if (state == dType.DobotConnect.DobotConnect_NoError):
            dType.SetPTPJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200)
            dType.SetPTPCoordinateParams(api, 200, 200, 200, 200)
            dType.SetPTPJumpParams(api, 10, 200)
            dType.SetPTPCommonParams(api, 100, 100)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 186.8912, 39.9336, -5.004, 1.9758, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 157, -229, 59, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 16, -263, 65, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -68, -267, 26, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-68, -267, -6 , -80, 1)
            enableCtrl = 1
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -68, -267, 56, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 157, -229, 59, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 236, 49, 56, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 236, 49, -6, -80, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 236, 49, 66, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 182.8912, 39.9336, 15.004, 1.9758, 1)
            que_sts = dType.GetQueuedCmdCurrentIndex(api)
            chk = 0
            a = 1
            strt = time.time()
            while (chk == 0):
                strt = time.time()
                while (time.time() - strt < 4):
                    pass
                if (que_sts != dType.GetQueuedCmdCurrentIndex(api)):
                    que_sts = dType.GetQueuedCmdCurrentIndex(api)
                else:
                    break
            dType.DisconnectDobot(api)
    def box_1():
        
        CON_STR = {
            dType.DobotConnect.DobotConnect_NoError: "DobotConnect_NoError",
            dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
            dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}
        # Load Dll
        api = dType.load()
        # Connect Dobot
        state = dType.ConnectDobot(api, "", 115200)[0]
        print("Connect status:", CON_STR[state])
        if (state == dType.DobotConnect.DobotConnect_NoError):
            dType.SetPTPJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200)
            dType.SetPTPCoordinateParams(api, 200, 200, 200, 200)
            dType.SetPTPJumpParams(api, 10, 200)
            dType.SetPTPCommonParams(api, 100, 100)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 186.8912, 39.9336, -5.004, 1.9758, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 157, -229, 59, 0, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 16, -263, 65, 0, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -85, -180, 26, 20, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-86, -180, -40, 20, 1)
            enableCtrl = 1
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -85, -180, 36, 0, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 157, -229, 29, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 182.8912, 39.9336, 29, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 253, 127, 26, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 253, 127, -35, -100, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 253, 127, 66, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 182.8912, 39.9336, 15.004, 1.9758, 1)
            que_sts = dType.GetQueuedCmdCurrentIndex(api)
            chk = 0
            a = 1
            strt = time.time()
            while (chk == 0):
                strt = time.time()
                while (time.time() - strt < 4):
                    pass
                if (que_sts != dType.GetQueuedCmdCurrentIndex(api)):
                    que_sts = dType.GetQueuedCmdCurrentIndex(api)
                else:
                    break
            dType.DisconnectDobot(api)
    def box_imt():
        CON_STR = {
            dType.DobotConnect.DobotConnect_NoError: "DobotConnect_NoError",
            dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
            dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}
        # Load Dll
        api = dType.load()
        # Connect Dobot
        state = dType.ConnectDobot(api, "", 115200)[0]
        print("Connect status:", CON_STR[state])
        if (state == dType.DobotConnect.DobotConnect_NoError):
            dType.SetPTPJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200)
            dType.SetPTPCoordinateParams(api, 200, 200, 200, 200)
            dType.SetPTPJumpParams(api, 10, 200)
            dType.SetPTPCommonParams(api, 100, 100)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 186.8912, 39.9336, -5.004, 1.9758, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 157, -229, 59, 0, 1)
            
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -14, -289, 26, 0, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-14, -289, -40, -80, 1)
            enableCtrl = 1
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -14, -289, 26, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 157, -229, 29, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,240, -14, 15.004,-80 , 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,240, -14, -40,-80, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 240,-14,20, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 182.8912, 39.9336, 15.004, 1.9758, 1)
            que_sts = dType.GetQueuedCmdCurrentIndex(api)
            chk = 0
            a = 1
            strt = time.time()
            while (chk == 0):
                strt = time.time()
                while (time.time() - strt < 4):
                    pass
                if (que_sts != dType.GetQueuedCmdCurrentIndex(api)):
                    que_sts = dType.GetQueuedCmdCurrentIndex(api)
                else:
                    break
            dType.DisconnectDobot(api)
class robot_main:
    def main():
        obj=robot_move
        obj.box_1()
        obj.box_2()
        obj.box_imt()
    if __name__ == "__main__":
        main()

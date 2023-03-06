#!/usr/bin/python
import threading
import DobotDllType as dType
import tkinter as tk
from tkinter import *
import time

CON_STR = {
dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}
#Load Dll
api = dType.load()
que_sts = dType.GetQueuedCmdCurrentIndex(api)
#Connect Dobot
state = dType.ConnectDobot(api, "", 115200)[0]
print("Connect status:",CON_STR[state])
if (state == dType.DobotConnect.DobotConnect_NoError):
    dType.SetPTPJointParams(api,200,200,200,200,200,200,200,200)
    dType.SetPTPCoordinateParams(api,200,200,200,200)
    dType.SetPTPJumpParams(api, 10, 200)
    dType.SetPTPCommonParams(api, 100, 100)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 182.8912, 39.9336, -5.004, 1.9758, 1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,29.9292,191.8232,32.5679,76.7747,1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,29.9292,191.8232,-63.5737,82.5189,1)
    dType.SetEndEffectorSuctionCup(api, 1, 1, isQueued=1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,29.9292,191.8232,32.5679,76.7747,1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,300.8636,-15.6137,33.2344,-7.2428,1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,300.8636,-15.6137,-65.2344,-7.2428,1)
    dType.SetEndEffectorSuctionCup(api, 1, 0, isQueued=1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 182.8912, 39.9336, -5.004, 1.9758, 1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,169.69,-216.2801,67.6956,-67.24,1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-15.2098,-229.8867,76.8800,-98.1429,1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-16.9509,-214.1169,10.8164,-98.8841,1)
    dType.SetEndEffectorSuctionCup(api, 1, 1, isQueued=1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-15.2098,-229.8867,76.8800,-98.1429,1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,169.69,-216.2801,67.6956,-67.24,1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,296.2686,-29.6637,36.3577,-10.0753,1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,296.2686,-29.6637,16.3577,-10.0753,1)
    dType.SetEndEffectorSuctionCup(api, 1, 0, isQueued=1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 182.8912, 39.9336, -5.004, 1.9758, 1)
    dType.DisconnectDobot(api)

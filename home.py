#!/usr/bin/python
import threading
import DobotDllType as dType
import tkinter as tk
CON_STR = {
        dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
        dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
        dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}
        #Load Dll
api = dType.load()
#Connect Dobot
state = dType.ConnectDobot(api, "", 115200)[0]
print("Connect status:",CON_STR[state])
if (state == dType.DobotConnect.DobotConnect_NoError):
    dType.SetHOMECmd(api, 1, isQueued=0)
    dType.DisconnectDobot(api)

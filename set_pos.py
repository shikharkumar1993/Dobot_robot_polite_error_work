#!/usr/bin/python
import threading
import DobotDllType as dType
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
            dType.SetPTPJointParams(api,200,200,200,200,200,200,200,200)
            dType.SetPTPCoordinateParams(api,200,200,200,200)
            dType.SetPTPJumpParams(api, 10, 200)
            dType.SetPTPCommonParams(api, 100, 100)
            enableCtrl=1
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
            '''
            choice=int(input('Enter 1 for fork1'))
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,89.8247,1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
            dType.dSleep(5000)
            
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-18.5335,253.4467,35.2350,89.8247,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-18.5335,253.4467,-65.2350,89.8247,1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-18.5335,253.4467,35.2350,89.8247,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
            
            choice=int(input('Enter 2 for fork2'))
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,10.5278,1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
            dType.dSleep(3000)
            
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,127.7938,-244.6304,34.6886,-72.7589,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,127.7938,-244.6304,-64.6886,-72.7589,1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,127.7938,-244.6304,34.6886,-72.7589,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
            
            choice=int(input('Enter 3 for knife1'))
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,92.1277,1)
            dType.dSleep(5000)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-25.5099,224.4094,32.0154,92.1277,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-25.5099,224.4094,-65.0154,92.1277,1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-25.5099,224.4094,32.0154,92.1277,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,89.8247,1)
            
            choice=int(input('Enter 4 for knife2'))
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,83.3647,1)
            dType.dSleep(5000)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 285.4430,93.1836,48.6680,83.3647, 1)
                
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-12.1231,187.1717,35.6251,83.3647,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-12.1231,187.1717,-65.6251,83.3647,1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-12.1231,187.1717,35.6251,83.3647,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
                       
            choice=int(input('Enter 5 for glass'))
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,45.004,66.0012,1)
            dType.dSleep(5000)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,100.7043,295.9164,50.2867,66.0012, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,100.7043,295.9164,17.2867,66.0012, 1)

            dType.SetEndEffectorSuctionCup(api, enableCtrl, 0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 100.7043,295.9164,50.2867,66.0012, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,45.004,66.0012,1)
            '''
            choice=int(input('Enter 6 for plate'))
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,45.004,66.0012,1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
            dType.dSleep(5000)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,204.6735,196.1538,51.0921,39.4247,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-16.5221,313.4125,39.8368,85.2441,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-16.5221,313.4125,-66.8368,85.2441,1)
            enableCtrl=1
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-16.5221,313.4125,39.8368,85.2441,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,45.004,66.0012,1)
            
            choice=int(input('Enter 7 for napkin'))
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,45.004,6.0012,1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
            dType.dSleep(5000)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,159.3461,224.9547,35.0439,6.2754,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,159.3461,224.9547,-65.0439,6.2754,1)
            enableCtrl=1
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,159.3461,224.9547,35.0439,6.2754,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,45.004,66.0012,1)
            
            choice=int(input('Enter 8 for spoon'))
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,45.004,61.2223,1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
            dType.dSleep(5000)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,168.4479,-243.9648,35.0439,-14.3523,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,168.4479,-243.9648,-65.0439,-14.3523,1)
            enableCtrl=1
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,168.4479,-243.9648,35.0439,-14.3523,1)
            
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,45.004,66.0012,1)
            
            dType.DisconnectDobot(api)
            

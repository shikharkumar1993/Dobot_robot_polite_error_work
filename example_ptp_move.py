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
    moveX=0;moveY=0;moveZ=10;moveFlag=-1
    pos = dType.GetPose(api)
    x = pos[0]
    y = pos[1]
    z = pos[2]
    rHead = pos[3]
    while(True):
        moveFlag *= -1
        for i in range(5):
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, x+moveX, y+moveY, z+moveZ, rHead, 0)
            moveX += 10 * moveFlag
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, x+moveX, y+moveY, z+moveZ, rHead, 0)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, x+moveX, y+moveY, z, rHead, 0)



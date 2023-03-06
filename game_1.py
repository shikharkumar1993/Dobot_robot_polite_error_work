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
import pyautogui
import numpy as np
import sounddevice as sd
import soundfile as sf
import random


# Green Function
class greenfun:

    def destroy_window(top):
        top.destroy()

    def finish(top):
        obj_gr = greenfun
        obj_gr.destroy_window(top)
        root = Toplevel()
        root.geometry('1920x1080')
        path = 'C:/Politeness/game picture/Finish.png'
        img = ImageTk.PhotoImage(Image.open(path))
        msg = Label(root, image=img)
        msg.image = img
        msg.pack(side='right')

        root.update()

        #filename = r"C:\Users\Owner\Documents\Sound recordings\finish1576405544.wav"
        #data, fs = sf.read(filename, dtype='float')
        #sd.play(data, fs)
        #sd.wait()

    def GreenGUI():
        root = tk.Toplevel()
        root.geometry('1920x1080')
        root.config(bg='azure')
        path = 'C:/Politeness/game picture/Task_impolite.jpg'
        img = ImageTk.PhotoImage(Image.open(path))
        msg = Label(root, image=img)
        msg.image = img
        msg.pack()

        root.update()

        # filename = r"C:\Users\Owner\Documents\Sound recordings\i-am-setting-the-table1576402758.wav"
        # data, fs = sf.read(filename, dtype='float')
        # sd.play(data, fs)
        # sd.wait()
        return (root)
    def Greenlevel(tp,scenario):
        obj1 = greenfun
        obj2 = MoveRobot
        obj1.destroy_window(tp)
        top = obj1.GreenGUI()        
        if (scenario==1):
            box=[obj2.blackbox,obj2.yellowbox ,obj2.purplebox,obj2.greenbox,obj2.whitebox,obj2.oranagebox]
            print(box)
            result=[f() for f in box]
            obj1.finish(top)
        if (scenario==2):
            box=[obj2.oranagebox,obj2.greenbox,obj2.blackbox,obj2.purplebox,obj2.whitebox,obj2.yellowbox]
            print(box)
            result=[f() for f in box]
            obj1.finish(top)

# RED LEVEL
class redfun:
    def finish(top):
        obj_red = redfun
        obj_red.destroy_window(top)
        root = Toplevel()
        root.geometry('1920x1080')
        path = 'C:/Politeness/game picture/Finish_polite.png'
        img = ImageTk.PhotoImage(Image.open(path))
        msg = Label(root, image=img)
        msg.image = img
        msg.pack(side='right')

        root.update()

    def destroy_window(top):
        top.destroy()

    def redtask(top,choice,count,bk,o,wh,gr,ye,pu,scenario):
        obj = redfun
        obj.destroy_window(top)
        root = tk.Toplevel()
        root.geometry('1920x1080')
        path = 'C:/Politeness/game picture/Task.jpg'
        img = ImageTk.PhotoImage(Image.open(path))
        msg = Label(root, image=img)
        msg.image = img
        msg.pack()
        root.update()
        obj2=MoveRobot
        if (scenario==1):
            if(choice==1):
                obj2.oranagebox()
                bk=1
            elif(choice==2):
                obj2.blackbox()
                o=1
            elif(choice==3):
                obj2.purplebox()
                wh=1
            elif(choice==4):
                obj2.greenbox()
                gr=1
            elif(choice==5):
                obj2.yellowbox()
                ye=1
            else:
                obj2.whitebox()                
                pu=1
        elif(scenario==2):
            if(choice==1):
                obj2.blackbox()
                
                bk=1
            elif(choice==2):
                obj2.oranagebox()
                o=1
            elif(choice==3):
                obj2.whitebox()
                wh=1
            elif(choice==4):
                obj2.greenbox()
                gr=1
            elif(choice==5):
                obj2.yellowbox()
                ye=1
            else:
                obj2.purplebox()
                pu=1
        obj.redtimeGUI(root,count,bk,o,wh,gr,ye,pu,scenario)
        
    def redtimeGUI(top,count,bk,o,wh,gr,ye,pu,scenario):
        count=count+1
        obj = redfun
        obj_green=greenfun
        if (count>6):
            obj.finish(top)
        else:
            obj.destroy_window(top)
            root = tk.Toplevel()
            root.geometry('1920x1080')
            root.config(bg='azure')
            path = 'C:/Politeness/game picture/Option button.jpg'
            img = ImageTk.PhotoImage(Image.open(path))
            pannel = Label(root, image=img)
            pannel.image = img
            pannel.pack()
            # msg1=Label(root,text="When do you want me to \n setup the table ?",bg='azure',font=('times',80,'bold'))
            # img1=ImageTk.PhotoImage(Image.open('C:/Politeness/game picture/Black.jpg'))
            # img2 = ImageTk.PhotoImage(Image.open('C:/Politeness/game picture/orange.jpg'))
            # img3 = ImageTk.PhotoImage(Image.open('C:/Politeness/game picture/green.jpg'))
            # img4 = ImageTk.PhotoImage(Image.open('C:/Politeness/game picture/Yellow.jpg'))
            # img5 = ImageTk.PhotoImage(Image.open('C:/Politeness/game picture/Purple.jpg'))
            opt_black = tk.Button(root,bg='black', padx=1.0, pady=1.0, height=13, width=38,
                                command=lambda: obj.redtask(root,1,count,bk,o,wh,gr,ye,pu,scenario))
            opt_orange= tk.Button(root, bg='red',padx=1.0, pady=1.0, height=13, width=38,
                                  command=lambda: obj.redtask(root, 2,count,bk,o,wh,gr,ye,pu,scenario))
            opt_white = tk.Button(root, padx=1.0, pady=1.0, height=13, width=38, bg='white',
                                   command=lambda: obj.redtask(root, 3,count,bk,o,wh,gr,ye,pu,scenario))
            opt_green = tk.Button(root, padx=1.0,bg='green', pady=1.0, height=13, width=38,
                                   command=lambda: obj.redtask(root, 4,count,bk,o,wh,gr,ye,pu,scenario))
            opt_yellow = tk.Button(root, padx=1.0, pady=1.0,bg='yellow', height=13, width=38,
                                   command=lambda: obj.redtask(root, 5,count,bk,o,wh,gr,ye,pu,scenario))
            opt_purple = tk.Button(root,bg='purple', padx=1.0, pady=1.0, height=13, width=38,
                                   command=lambda: obj.redtask(root, 6,count,bk,o,wh,gr,ye,pu,scenario))
            # opt_twomi=tk.Button(root,padx=1.0,pady=1.0,height=2,width=25,bg='white',text='In two minutes',command=lambda: obj.red_timer(2),font=('times',34,'bold'))

            # msg1.grid()
            # opt_yes.grid()
            # opt_onemi.grid()
            # opt_twomi.grid()
            # pannel.grid()
            # msg1.place(relx=0,rely=0,anchor=NW)
            # pannel.place(relx=0.2,rely=0.6,anchor=CENTER)
            # opt_black.image=img1
            # opt_orange.image=img2
            # opt_green.image=img3
            # opt_yellow.image=img4
            # opt_purple.image=img5
            if (bk==0):
                opt_black.place(relx=0.1, rely=0.42, anchor=CENTER)
            if (o==0):
                opt_orange.place(relx=0.3, rely=0.42, anchor=CENTER)
            if (wh==0):
                opt_white.place(relx=0.52, rely=0.42, anchor=CENTER)
            if(gr==0):
                opt_green.place(relx=0.1, rely=0.71, anchor=CENTER)
            if(ye==0):
                opt_yellow.place(relx=0.3 , rely=0.71, anchor=CENTER)
            if(pu==0):
                opt_purple.place(relx=0.52, rely=0.7, anchor=CENTER)
            # opt_twomi.place(relx=0.7,rely=0.8,anchor=CENTER)
            # root.mainloop()

    def redstart(tp,scenario):
        obj = redfun
        obj.destroy_window(tp)
        root = tk.Toplevel()
        root.config(bg='azure')
        root.geometry('1920x1080')
        path = 'c:/Politeness/game picture/Welcome.png'
        img = ImageTk.PhotoImage(Image.open(path))
        pannel = Label(root, image=img)
        pannel.image = img
        pannel.pack()
        count=0    
        nxt = tk.Button(root, padx=10, pady=10, height=1, width=25, bg='azure', text='Next', font=('times', 32, 'bold'))
        nxt.config(command=lambda button=nxt: obj.redtimeGUI(root,count,0,0,0,0,0,0,scenario))
        # label.grid()
        # label.place(relx=0.5,rely=0.5,anchor=CENTER)
        # nxt.grid()
        nxt.place(relx=0.7, rely=0.8, anchor=CENTER)
        root.update()

    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    class ROBOT move
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


class MoveRobot:
    def oranagebox():
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
            # Plates
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 186.8912, 39.9336, -5.004, 1.9758, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 157,-229,59, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 16, -263, 65, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 22.64,-205.1410,26,-80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 22.64, -205.1410, -26, -80, 1)
            enableCtrl = 1
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 22.64, -205.1410, 26, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 157, -229, 59, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239, 143, 26, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239, 143, -26, -80, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239, 143, 26, -80, 1)
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

    def greenbox():
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
            # Plates
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 186.8912, 39.9336, -5.004, 1.9758, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 157, -229, 59, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 16, -263, 65, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -39.27, -205.1410, 26, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -39.64, -205.1410, -26, -80, 1)
            enableCtrl = 1
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -39.64, -205.1410, 26, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 157, -229, 59, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239, 143, 26, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239, 143, -26, -80, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239, 143, 26, -80, 1)
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
    def whitebox():
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
            # Plates
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 186.8912, 39.9336, -5.004, 1.9758, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 157, -229, 59, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 16, -263, 65, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -102, -205.1410, 26, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -102, -205.1410, -26, -80, 1)
            enableCtrl = 1
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -102, -205.1410, 26, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 157, -229, 59, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239, 143, 26, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239, 143, -26, -80, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239, 143, 26, -80, 1)
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
    def blackbox():
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
            # Plates
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 186.8912, 39.9336, -5.004, 1.9758, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 157, -229, 59, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 16, -263, 65, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -105, -287, 26, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -105, -287, -26, -80, 1)
            enableCtrl = 1
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -105, -287, 26, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 157, -229, 59, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239, 143, 26, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239, 143, -26, -80, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239, 143, 26, -80, 1)
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
    def yellowbox():
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
            # Plates
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 186.8912, 39.9336, -5.004, 1.9758, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 157, -229, 59, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 16, -263, 65, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -40, -287, 26, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -40, -287, -26, -80, 1)
            enableCtrl = 1
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -40, -287, 26, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 157, -229, 59, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239, 143, 26, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239, 143, -26, -80, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239, 143, 26, -80, 1)
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
    def purplebox():
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
            # Plates
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 186.8912, 39.9336, -5.004, 1.9758, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 157, -229, 59, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 16, -263, 65, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 25, -294, 26, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 25, -294, -28, -80, 1)
            enableCtrl = 1
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 25, -294, 26, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 157, -229, 59, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239, 143, 26, -80, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239, 143, -26, -80, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239, 143, 26, -80, 1)
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
class blankscreen:
    def blnkscr():
        root = Toplevel()
        root.title('Table setting experiment')
        root.geometry('1920x1080')
        root.config(bg='grey80')
        obj_green = greenfun

        obj_red = redfun
        green_low_polite = tk.Button(root, padx=1.0, pady=1.0, height=4, width=8, bg='skyblue', text='Left',
                                     font=('times', 32, 'bold'), command=lambda: obj_green.Greenlevel(root,1))
        left_middle=tk.Button(root, padx=1.0, pady=1.0, height=4, width=8, bg='skyblue', text='Left \n Middle',
                                     font=('times', 32, 'bold'), command=lambda: obj_green.Greenlevel(root,2))
        right_middle=tk.Button(root, padx=1.0, pady=1.0, height=4, width=8, bg='skyblue', text='Right \n Middle',
                                     font=('times', 32, 'bold'), command=lambda: obj_red.redstart(root,1))

        red_medium_polite = tk.Button(root, height=4, width=8, bg='skyblue', text='Right', font=('times', 32, 'bold'),
                                      command=lambda: obj_red.redstart(root,2))
        green_low_polite.grid(row=500, column=3, padx=10, pady=10)

        red_medium_polite.grid(row=500, column=8, padx=10, pady=10)
        green_low_polite.place(relx=0.2, rely=0.5, anchor=CENTER)
        left_middle.place(relx=0.4, rely=0.5, anchor=CENTER)
        right_middle.place(relx=0.6, rely=0.5, anchor=CENTER)
        red_medium_polite.place(relx=0.8, rely=0.5, anchor=CENTER)
        root.update()


class gui_main:

    def main():
        top = tk.Tk()
        top.title('Table setting experiment')
        top.geometry('1920x1080')
        top.config(bg='grey80')
        obj = blankscreen
        obj_green = greenfun

        obj_red = redfun
        path = 'C:\Politeness\Picture\Blankscreen.png'
        img = ImageTk.PhotoImage(Image.open(path))
        msg = Label(top, image=img)
        msg.image = img
        msg.pack(side='right')
        obj.blnkscr()
        top.mainloop()

    if __name__ == "__main__":
        main()








#!/usr/bin/python
import threading
import DobotDllType as dType
import tkinter as tk
from tkinter import *
import time
import os
import webbrowser 
from PIL import ImageTk, Image, ImageGrab, ImageOps
import pyautogui
import numpy as np
import sounddevice as sd
import soundfile as sf

#Green Function
class greenfun:
    def news(a):
        url='https://www.news.google.com'
        webbrowser.open_new(url)
    def finish():
        root=Toplevel()
        root.geometry('1920x1080')
        root.config(bg='azure')
        msg=Label(root,text="סיום")
        msg.config(bg='azure',font=('tahoma',80,'bold'))
        msg.pack()
        msg.place(relx=0.5,rely=0.5,anchor=CENTER)
        root.update()
        filename = r"C:\Users\Owner\Documents\Sound recordings\finish1576405544.wav"
        data, fs = sf.read(filename, dtype='float')
        sd.play(data, fs)
        sd.wait()
    def GreenGUI():
         root=Toplevel()
         root.geometry('1920x1080')
         root.config(bg='azure')
         obj=greenfun()
         msg=Label(root,text="עורך את השולחן")
         msg.config(bg='azure',font=('tahoma',80,'bold'))
         button=tk.Button(root,text="Please click here to get news",bg='white',font=('tahoma',40,'bold'),command=obj.news)
         msg.pack()
         button.pack()
         msg.place(relx=0.5,rely=0.5,anchor=CENTER)
         button.place(relx=0.5,rely=0.8,anchor=CENTER)
         root.update()
         filename = r"C:\Users\Owner\Documents\Sound recordings\i-am-setting-the-table1576402758.wav"
         data, fs = sf.read(filename, dtype='float')
         sd.play(data, fs)
         sd.wait()
    
    def Greenlevel():            
        obj1=greenfun
        obj2=MoveRobot
        a=threading.Thread(target=obj1.GreenGUI())
        a.start()
        obj2.movedairy()
        obj2.movespoon()
        obj2.movefork()
        obj2.moveteaspoon()
               
        obj1.finish()
#BLUE FUNCTION
class bluefun:
    def __init__():
        self.countdown=5
        
    def blue_timer():
        countdown=10
        root=tk.Toplevel()
        root.config(bg='azure')
        print(countdown)
        label=Label(root,text="",height=100,width=50)
        while(countdown!=-1):
            
            
            if (countdown==0):
                print("סיום")
                countdown=countdown-1
                root.destroy()
            else:
                label.configure(bg='azure',text="זמן שנותר: %d" %countdown + 'sec',font=('tahoma',60,'bold'))
                label.pack()
                root.update() 
                time.sleep(1)
                countdown=countdown-1                
                print(countdown)   
           
    def change_plate(a):
        obj_gre=greenfun
        obj_rob=MoveRobot
        obj_blu=bluefun
        obj_gre.GreenGUI()
        obj_rob.changeplate(a)
        obj_gre.finish()
    def blue_set_table(a):
        obj_gre=greenfun
        obj_gre.GreenGUI()
        obj_rob=MoveRobot
        obj_blu=bluefun
        if(a==1):
            obj_rob.movedairy()
            obj_rob.movespoon()
            obj_rob.movefork()
            obj_rob.moveteaspoon()
        else:
            obj_rob.movemeat()
            obj_rob.movespoon()
            obj_rob.movefork()
            obj_rob.moveteaspoon()
        root=tk.Toplevel()
        root.geometry('1920x1080')
        root.config(bg='azure')
        msg1=Label(root,text="?האם הנך מרוצה עריכת השולחן",bg='azure',font=('tahoma',80,'bold'))              
        opt_yes=tk.Button(root,padx=1.0,pady=1.0,height=2,width=25,bg='white',text='כן',font=('tahoma',34,'bold'))
        opt_yes.config(command=obj_gre.finish)
        opt_no=tk.Button(root,padx=1.0,pady=1.0,height=2,width=25,bg='white',text='לא',font=('tahoma',34,'bold'))
        opt_no.config(command=lambda button=opt_no : obj_blu.change_plate(a))
        root.config(bg='azure')
        path='C:/Users/Owner/eclipse-workspace/thePoliteRobot/thePoliteRobot/img/setTable.jpg'
        img = ImageTk.PhotoImage(Image.open(path))
        pannel=Label(root,image=img)
        msg1.grid()
        opt_yes.grid()
        opt_no.grid()
        msg1.place(relx=0.2,rely=0,anchor=NW)
        opt_yes.place(relx=0.7,rely=0.6,anchor=CENTER)
        opt_no.place(relx=0.7,rely=0.8,anchor=CENTER)
        pannel.place(relx=0.2,rely=0.6,anchor=CENTER)
        root.mainloop() 
        #obj_gre.finish()
    def blue_meal():
        root=tk.Toplevel()
        root.geometry('1920x1080')
        obj_gr=greenfun
        obj_blu=bluefun
        root.config(bg='azure')
        label=Label(root,text="האם ברצונך לערוך את \n?השולחן עם כלים לארוחה חלבית",bg='azure',font=('tahoma',80,'bold'))
        opt_yes=tk.Button(root,padx=1.0,pady=1.0,height=2,width=25,bg='white',text='כן',command=lambda: obj_blu.blue_set_table(1),font=('tahoma',34,'bold'))
        opt_no=tk.Button(root,padx=1.0,pady=1.0,height=2,width=25,bg='white',text='לא',command=lambda: obj_blu.blue_set_table(2),font=('tahoma',34,'bold'))
        label.grid()
        opt_yes.grid()
        opt_no.grid()
        path='C:/Users/Owner/eclipse-workspace/thePoliteRobot/thePoliteRobot/img/setTable.jpg'
        img = ImageTk.PhotoImage(Image.open(path))
        pannel=Label(root,image=img)
        label.place(relx=0.2,rely=0)                                                                                            
        opt_yes.place(relx=0.7,rely=0.6,anchor=CENTER)
        opt_no.place(relx=0.7,rely=0.8,anchor=CENTER)
        pannel.place(relx=0.2,rely=0.6,anchor=CENTER)
        root.mainloop() 
    def Bluestart():
        obj=bluefun
        root=tk.Toplevel()
        root.geometry('1920x1080')
        root.config(bg='azure')
        path='C:/Users/Owner/eclipse-workspace/thePoliteRobot/thePoliteRobot/img/setTable.jpg'
        img = ImageTk.PhotoImage(Image.open(path))
        pannel=Label(root,image=img)
        msg1=Label(root,text="האם ברצונך לערוך את\n? השולחן עכשיו",bg='azure',font=('tahoma',80,'bold'))               
        opt_yes=tk.Button(root,padx=1.0,pady=1.0,height=2,width=25,bg='white',text='כן',font=('tahoma',34,'bold'),command=obj.blue_meal)
        opt_no=tk.Button(root,padx=1.0,pady=1.0,height=2,width=25,bg='white',text='לא',font=('tahoma',34,'bold'),command=obj.blue_timer)
        msg1.grid()
        opt_yes.grid()
        opt_no.grid()
        msg1.place(relx=0.4,rely=0,anchor=NW)
        opt_yes.place(relx=0.7,rely=0.6,anchor=CENTER)
        opt_no.place(relx=0.7,rely=0.8,anchor=CENTER)
        pannel.place(relx=0.2,rely=0.6,anchor=CENTER)
        root.mainloop()
#GREEN LEVEL   
class redfun:
    
    def red_timer(a):
        countdown=60*a
        root=tk.Toplevel()
        obj_red=redfun
        root.geometry('1920x1080')
        root.config(bg='azure')
        label=Label(root,text="",height=100,width=50)
        close_but=tk.Button(root,bg='white',height=2,width=25,text="לסגירת החלון לחץ כאן",font=('tahoma',34,'bold'))
        while(countdown!=-1):
            
            
            if (countdown==0):
                print("finish")
                countdown=countdown-1
                root.destroy()
            else:
                label.configure(text="הזמן שנותר: %d" %countdown,bg='azure',font=('tahoma',40))
                label.pack()
                root.update()
                close_but.config(command=root.destroy)
                close_but.pack()
                close_but.place(relx=0.5,rely=0.8,anchor=CENTER)
                root.update()
                time.sleep(1)
                countdown=countdown-1
    def finish():
        root=Toplevel()
        root.geometry('1920x1080')
        root.config(bg='azure')
        #path='C:/Users/Owner/eclipse-workspace/thePoliteRobot/thePoliteRobot/img/bonape.gif'
        #img = ImageTk.PhotoImage(Image.open(path))
        #pannel=Label(root,image=img)
        msg=Label(root,text="תודה רבה ובתאבון",bg='azure')
        msg.config(font=('tahoma',80,'bold'))
        msg.pack()
        msg.place(relx=0.5,rely=0.5,anchor=CENTER)
        #pannel.place(relx=0.5,rely=0.5,anchor=CENTER)
        root.update()
        filename = r"C:\Users\Owner\Documents\Sound recordings\thank-you-very-much-bon1576406177.wav"
        data, fs = sf.read(filename, dtype='float')
        sd.play(data, fs)
        sd.wait()
    def change_plate(a):
        obj_rob=MoveRobot
        obj_gre=greenfun
        obj_red=redfun
        obj_gre.GreenGUI()
        obj_rob.changeplate(a)
        obj_red.finish()
    def red_set_table(a):
        obj_gre=greenfun
        obj_gre.GreenGUI()
        obj_rob=MoveRobot
        obj_red=redfun
        obj_blu=bluefun
        if(a==1):
            obj_rob.movedairy()
            obj_rob.movespoon()
            obj_rob.movefork()
            obj_rob.moveteaspoon()
        else:
            obj_rob.movemeat()
            obj_rob.movespoon()
            obj_rob.movefork()
            obj_rob.moveteaspoon()
        root=tk.Toplevel()
        root.geometry('1920x1080')
        root.config(bg='azure')
        msg1=Label(root,text="האם הנך מרוצה\n ?מעריכת השולחן",bg='azure',font=('tahoma',80,'bold'))              
        path='C:/Users/Owner/eclipse-workspace/thePoliteRobot/thePoliteRobot/img/setTable.jpg'
        img = ImageTk.PhotoImage(Image.open(path))
        pannel=Label(root,image=img)
        opt_yes=tk.Button(root,padx=1.0,pady=1.0,height=2,width=25,bg='white',text='כן',font=('tahoma',32,'bold'))
        opt_yes.config(command=obj_red.finish)
        opt_no=tk.Button(root,padx=1.0,pady=1.0,height=2,width=25,bg='white',text='לא, אני מעדיף לשנות צלחת',font=('tahoma',32,'bold'))
        opt_no.config(command=lambda button=opt_no : obj_red.change_plate(a))        
        path1='C:/Users/Owner/eclipse-workspace/thePoliteRobot/thePoliteRobot/img/goodsmily.png'
        path2='C:/Users/Owner/eclipse-workspace/thePoliteRobot/thePoliteRobot/img/badSmily.jpg'
        img1=ImageTk.PhotoImage(Image.open(path1))
        img2=ImageTk.PhotoImage(Image.open(path2))
        pannel1=Label(root,image=img1)
        pannel2=Label(root,image=img2)
        msg1.grid()
        opt_yes.grid()
        opt_no.grid()
        pannel.grid()
        pannel.place(relx=0.2,rely=0.6,anchor=CENTER)
        msg1.place(relx=0.4,rely=0,anchor=NW)
        opt_yes.place(relx=0.65,rely=0.55,anchor=CENTER)
        opt_no.place(relx=0.65,rely=0.75,anchor=CENTER)
        pannel1.place(relx=0.9,rely=0.55,anchor=CENTER)
        pannel2.place(relx=0.9,rely=0.75,anchor=CENTER)
        root.mainloop()
    def redmeal():
        root=tk.Toplevel()
        root.geometry('1920x1080')
        obj_gr=greenfun
        obj_red=redfun
        root.config(bg='azure')
        path='C:/Users/Owner/eclipse-workspace/thePoliteRobot/thePoliteRobot/img/setTable.jpg'
        img = ImageTk.PhotoImage(Image.open(path))
        pannel=Label(root,image=img)
        label=Label(root,text="באילו כלים \n ?לערוך את השולחן",bg='azure',font=('tahoma',78,'bold'))
        opt_dairy=tk.Button(root,padx=1.0,pady=1.0,height=2,width=25,bg='white',text='חלבי',command=lambda: obj_red.red_set_table(1),font=('tahoma',34,'bold'))
        opt_meat=tk.Button(root,padx=1.0,pady=1.0,height=2,width=25,bg='white',text='בשרי',command=lambda: obj_red.red_set_table(2),font=('tahoma',34,'bold'))
        opt_indiff=tk.Button(root,padx=1.0,pady=1.0,height=2,width=25,bg='white',text='לא משנה לי',command=lambda: obj_red.red_set_table(1),font=('tahoma',34,'bold'))
        annel=Label(root,image=img)
        label.grid()
        opt_dairy.grid()
        opt_meat.grid()
        opt_indiff.grid()
        pannel.place(relx=0.2,rely=0.6,anchor=CENTER)
        label.place(relx=0.4,rely=0,anchor=NW)
        opt_dairy.place(relx=0.7,rely=0.4,anchor=CENTER)
        opt_meat.place(relx=0.7,rely=0.6,anchor=CENTER)
        opt_indiff.place(relx=0.7,rely=0.8,anchor=CENTER)
        root.mainloop() 
    def redtimeGUI():
        obj=redfun
        root=tk.Toplevel()
        root.geometry('1920x1080')
        root.config(bg='azure')
        path='C:/Users/Owner/eclipse-workspace/thePoliteRobot/thePoliteRobot/img/setTable.jpg'
        img = ImageTk.PhotoImage(Image.open(path))
        msg1=Label(root,text="מתי תרצו שאתחיל\n ?לערוך את השולחן",bg='azure',font=('tahoma',80,'bold'))               
        opt_yes=tk.Button(root,padx=1.0,pady=1.0,height=2,width=25,bg='white',text='עכשיו',command=obj.redmeal,font=('tahoma',34,'bold'))
        opt_onemi=tk.Button(root,padx=1.0,pady=1.0,height=2,width=25,bg='white',text='בעוד דקה',command=lambda: obj.red_timer(1),font=('tahoma',34,'bold'))
        opt_twomi=tk.Button(root,padx=1.0,pady=1.0,height=2,width=25,bg='white',text='בעוד שתי דקות',command=lambda: obj.red_timer(2),font=('tahoma',34,'bold'))
        pannel=Label(root,image=img)
        msg1.grid()
        opt_yes.grid()
        opt_onemi.grid()
        opt_twomi.grid()
        pannel.grid()
        msg1.place(relx=0.4,rely=0,anchor=NW)
        pannel.place(relx=0.2,rely=0.6,anchor=CENTER)
        opt_yes.place(relx=0.7,rely=0.4,anchor=CENTER)
        opt_onemi.place(relx=0.7,rely=0.6,anchor=CENTER)
        opt_twomi.place(relx=0.7,rely=0.8,anchor=CENTER)
        root.mainloop()
    def redstart():
        obj=redfun
        root=tk.Toplevel()
        root.config(bg='azure')
        root.geometry('1920x1080')
        label=Label(root,text="!שלום וברוכים הבאים\n אני הרובוט קוקי\n תפקידי הוא לעזור לך בעריכת השולחן\n נא ללחוץ על כפתור \"התחל\" כדי להתחיל",bg='azure',font=('tahoma',70,'bold'))
        nxt=tk.Button(root,padx=10,pady=10,height=1,width=25,bg='white',text='התחל',font=('tahoma',32,'bold'),command=obj.redtimeGUI)
        label.grid()
        label.place(relx=0.5,rely=0.4,anchor=CENTER)
        nxt.grid()
        nxt.place(relx=0.5,rely=0.8,anchor=CENTER)
        root.update()
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    class ROBOT move
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''                    
class MoveRobot:
    def movedairy():
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
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
            dairy_above_x=21.6888
            dairy_above_y=-194.8045
            dairy_above_z=2.4489
            dairy_above_r=-194.8045
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,dairy_above_x,dairy_above_y,dairy_above_z,dairy_above_r,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-6.6001,-178.4935,-64.4683,-102.4588,1)
            enableCtrl=1
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
            dType.dSleep(4000)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,dairy_above_x,dairy_above_y,dairy_above_z,dairy_above_r,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,278.2912,9.7754,-17.5948,-109.0133,1)
            dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,318.0556,23.8490,-68.0394,-107.5309,1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
            que_sts=dType.GetQueuedCmdCurrentIndex(api)
            chk=0
            a=1
            strt=time.time()
            while (chk==0):
                strt=time.time()
                while(time.time()-strt<2):
                    pass
                if(que_sts!=dType.GetQueuedCmdCurrentIndex(api)):
                    que_sts=dType.GetQueuedCmdCurrentIndex(api)
                else:
                    break
            dType.DisconnectDobot(api)

    def movemeat():
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
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-2.9487,227.9338,-3.3685,84.9013,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-4.8533,228.3373,-67.732,86.6600,1)
            enableCtrl=1
            dType.dSleep(4000)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-2.9487,227.9338,-3.3685,84.9013,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,278.2912,9.7754,-17.5948,-109.0133,1)
            dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,318.0556,23.8490,-68.0394,-107.5309,1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
            que_sts=dType.GetQueuedCmdCurrentIndex(api)
            chk=0
            a=1
            strt=time.time()
            while (chk==0):
                strt=time.time()
                while(time.time()-strt<2):
                    pass
                if(que_sts!=dType.GetQueuedCmdCurrentIndex(api)):
                    que_sts=dType.GetQueuedCmdCurrentIndex(api)
                else:
                    break
            dType.DisconnectDobot(api)
    def movespoon():
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
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,13.9776,-272.3264,10.6812,-97.4030,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-74.9732,-266.3075,-65.0712,-88.7824,1)            
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
            dType.dSleep(5000)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,13.9776,-272.3264,10.6812,-97.4030,1)            
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,266.1983,151.1855,22.6635,-97.4030,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,266.1983,151.1855,-62.6635,-97.4030,1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,266.1983,151.1855,22.6635,1.9758,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
            que_sts=dType.GetQueuedCmdCurrentIndex(api)
            chk=0
            a=1
            strt=time.time()
            while (chk==0):
                strt=time.time()
                while(time.time()-strt<2):
                    pass
                if(que_sts!=dType.GetQueuedCmdCurrentIndex(api)):
                    que_sts=dType.GetQueuedCmdCurrentIndex(api)
                else:
                    break
            dType.DisconnectDobot(api)
    def movefork():
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
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,90.3679,-291.3491,68.2888,1.9758,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-52.9694,-301.0371,-65.3108,1.9758,1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
            dType.dSleep(5000)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,90.3679,-291.3491,68.2888,1.9758,1)            
            
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,261.2765,-169.0464,16.2014,1.9758,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,263.2043,-101.3576,-61.8008,1.9758,1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,263.2043,-101.3576,35.0919,-88.7824,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
            que_sts=dType.GetQueuedCmdCurrentIndex(api)
            chk=0
            a=1
            strt=time.time()
            while (chk==0):
                strt=time.time()
                while(time.time()-strt<2):
                    pass
                if(que_sts!=dType.GetQueuedCmdCurrentIndex(api)):
                    que_sts=dType.GetQueuedCmdCurrentIndex(api)
                else:
                    break
            dType.DisconnectDobot(api)
    def moveteaspoon():
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
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-53.5309,172.8677,-30.4244,96.8647,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-53.5309,172.8677,-64.4244,96.8647,1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
            dType.dSleep(5000)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-53.5309,172.8677,-30.4244,96.8647,1)            
            
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,262.2253,191.8166,-23.3965,103.3085,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,262.2253,191.8166,-43.3965,103.3085,1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,262.2253,191.8166,-23.3965,103.3085,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
            que_sts=dType.GetQueuedCmdCurrentIndex(api)
            chk=0
            a=1
            strt=time.time()
            while (chk==0):
                strt=time.time()
                while(time.time()-strt<4):
                    pass
                if(que_sts!=dType.GetQueuedCmdCurrentIndex(api)):
                    que_sts=dType.GetQueuedCmdCurrentIndex(api)
                else:
                    break
            dType.DisconnectDobot(api)
    def changeplate(a):
        
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
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,278.2912,9.7754,-17.5948,-109.0133,1)
            dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,318.0556,23.8490,-68.0394,-107.5309,1)
            enableCtrl=1
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
            dairy_above_x=21.6888
            dType.dSleep(3000)
            dairy_above_y=-194.8045
            dairy_above_z=2.4489
            dairy_above_r=-194.8045
            #a==1 for changing with the dairy plate with meat plate
            if (a==1):                     
                dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,dairy_above_x,dairy_above_y,dairy_above_z,dairy_above_r,1)
                dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,15.2427,-201.8519,-62.7202,-196.8427,1)    
                dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
                dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,dairy_above_x,dairy_above_y,dairy_above_z,dairy_above_r,1)
                dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
                dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-2.9487,227.9338,-3.3685,84.9013,1)
                dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-4.8533,228.3373,-65.732,86.6600,1)
                time.sleep(1)
                dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
                dType.dSleep(3000)
                dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-2.9487,227.9338,-3.3685,84.9013,1)
                dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,278.2912,9.7754,-17.5948,-109.0133,1)
                dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,318.0556,23.8490,-68.0394,-107.5309,1)
                dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
                dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
            else:
                dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-2.9487,227.9338,-3.3685,84.9013,1)
                dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-4.8533,228.3373,-67.732,86.6600,1)
                time.sleep(2)
                dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
                dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-2.9487,227.9338,-3.3685,84.9013,1)
                dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
                dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,dairy_above_x,dairy_above_y,dairy_above_z,dairy_above_r,1)
                dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,15.2427,-201.8519,-62.7202,-196.8427,1)    
                dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
                dType.dSleep(3000)
                dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,dairy_above_x,dairy_above_y,dairy_above_z,dairy_above_r,1)
                dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,278.2912,9.7754,-17.5948,-109.0133,1)
                dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,318.0556,23.8490,-68.0394,-107.5309,1)
                dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
                dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
            que_sts=dType.GetQueuedCmdCurrentIndex(api)
            chk=0
            a=1
            strt=time.time()
            while (chk==0):
                strt=time.time()
                while(time.time()-strt<4):
                    pass
                if(que_sts!=dType.GetQueuedCmdCurrentIndex(api)):
                    que_sts=dType.GetQueuedCmdCurrentIndex(api)
                else:
                    break
            dType.DisconnectDobot(api)  
   
class gui_main:
    def main():
        top = tk.Tk()
        top.title('Table setting experiment')
        top.geometry('1920x1080')
        top.config(bg='azure')
        obj_green=greenfun
        obj_blue=bluefun
        obj_red=redfun
        green_low_polite=tk.Button(top,padx=1.0,pady=1.0,height=4,width=8,bg='SeaGreen1',text='א',font=('tahoma',32,'bold'),command=obj_green.Greenlevel)        
        blue_medium_polite=tk.Button(top,height=4,width=8,bg='SteelBlue1',text='ב',font=('tahoma',32,'bold'),command=obj_blue.Bluestart)
        red_medium_polite=tk.Button(top,height=4,width=8,bg='OrangeRed2',text='ג',font=('tahoma',32,'bold'),command=obj_red.redstart)
        green_low_polite.grid(row=500,column=3,padx=10,pady=10)
        blue_medium_polite.grid(row=500,column=5,padx=10,pady=10)
        red_medium_polite.grid(row=500,column=8,padx=10,pady=10)
        green_low_polite.place(relx=0.7,rely=0.5,anchor=CENTER)
        blue_medium_polite.place(relx=0.5,rely=0.5,anchor=CENTER)
        red_medium_polite.place(relx=0.3,rely=0.5,anchor=CENTER)
        top.mainloop()
    if __name__== "__main__":
        main()
    







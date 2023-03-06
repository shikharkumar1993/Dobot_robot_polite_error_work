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
#Green Function
class greenfun:
    
    def destroy_window(top):
        top.destroy()
    def finish(top):
        obj_gr=greenfun       
        obj_gr.destroy_window(top)
        root=Toplevel()
        root.geometry('1920x1080')
        path='C:\Politeness\picture_hebrew\Finish.png'
        img = ImageTk.PhotoImage(Image.open(path))
        msg=Label(root,image=img)
        msg.image=img
        msg.pack(side='right')
        
        root.update()
        
        filename = r"C:\Users\Owner\Documents\Sound recordings\finish1576405544.wav"
        data, fs = sf.read(filename, dtype='float')
        sd.play(data, fs)
        sd.wait()
    def GreenGUI():
         root=tk.Toplevel()              
         root.geometry('1920x1080')
         root.config(bg='azure')
         path='C:\Politeness\picture_hebrew\settingtable.png'
         img = ImageTk.PhotoImage(Image.open(path))
         msg=Label(root,image=img)
         msg.image=img
         msg.pack()
         
         root.update()
         
         
         filename = r"C:\Users\Owner\Documents\Sound recordings\i-am-setting-the-table1576402758.wav"
         data, fs = sf.read(filename, dtype='float')
         sd.play(data, fs)
         sd.wait()
         return(root)
    def removeGUI():
         root=tk.Toplevel()              
         root.geometry('1920x1080')
         root.config(bg='azure')
         path='C:\Politeness\picture_hebrew/removeutensil.png'
         img = ImageTk.PhotoImage(Image.open(path))
         msg=Label(root,image=img)
         msg.image=img
         msg.pack()
         
         root.update()
         
         
         filename = r"C:\Users\Owner\Documents\Sound recordings\i-am-setting-the-table1576402758.wav"
         data, fs = sf.read(filename, dtype='float')
         sd.play(data, fs)
         sd.wait()
         return(root)
    def waitremove():
        countdown=10
        root=tk.Toplevel()
        root.config(bg='azure')
        print(countdown)
        label=Label(root,text="",height=100,width=50)
        while(countdown!=-1):
            
            
            if (countdown==0):
                print("finish")
                countdown=countdown-1
                root.destroy()
            else:
                label.configure(bg='azure',text="%d מפנה את כלי הארוחה  בעוד" %countdown,font=('times',60,'bold'))
                label.pack()
                root.update() 
                time.sleep(1)
                countdown=countdown-1                
                print(countdown)  
        
         
    def Greenlevel(tp):        
        obj1=greenfun
        obj2=MoveRobot
        obj1.destroy_window(tp)
        top=obj1.GreenGUI()
        obj2.regularsetting()
        obj1.destroy_window(top)
        obj1.waitremove()
        top1=obj1.removeGUI()
        obj2.removeregular()
        obj1.finish(top1)
#BLUE FUNCTION
class bluefun:

    def destroy_window(top):
        top.destroy()
        
    def blue_timer(top):
        countdown=10
        root=tk.Toplevel()
        root.config(bg='azure')
        print(countdown)
        label=Label(root,text="",height=100,width=50)
        top.destroy()
        obj_blue=bluefun
        while(countdown!=-1):
            
            
            if (countdown==0):
                print("finish")
                countdown=countdown-1
                obj_blue.blue_set_table(root)
            else:
                label.configure(bg='azure',text=" %d הזמן שנשאר" %countdown,font=('times',60,'bold'))
                label.pack()
                root.update() 
                time.sleep(1)
                countdown=countdown-1                
                print(countdown)   
           
    
    def blue_set_table(top):
        obj_gre=greenfun
        obj_blu=bluefun
        obj_blu.destroy_window(top)
        top=obj_gre.GreenGUI()
        obj_rob=MoveRobot
                
        obj_rob.regularsetting()
        obj_blu.destroy_window(top)
        root=tk.Toplevel()
        root.geometry('1920x1080')
        root.config(bg='azure')
        #msg1=Label(root,text="Are you satisfied with \n the table setting ?",bg='azure',font=('times',80,'bold'))
        path='c:/Politeness/picture_hebrew/blueremove.png'
        img = ImageTk.PhotoImage(Image.open(path))
        pannel=Label(root,image=img)
        pannel.image=img
        pannel.pack()
        opt_yes=tk.Button(root,padx=1.0,pady=1.0,height=2,width=25,bg='white',text='כן',font=('times',34,'bold'))
        opt_yes.config(command= lambda button=opt_yes :obj_blu.blue_remove(root))
        opt_no=tk.Button(root,padx=1.0,pady=1.0,height=2,width=25,bg='white',text='לא',font=('times',34,'bold'))
        opt_no.config(command=lambda button=opt_no : obj_gre.finish(root))
        #root.config(bg='azure')
        
        #msg1.grid()
        #opt_yes.grid()
        #opt_no.grid()
        #msg1.place(relx=0.1,rely=0,anchor=NW)
        opt_yes.place(relx=0.7,rely=0.6,anchor=CENTER)
        opt_no.place(relx=0.7,rely=0.8,anchor=CENTER)
        #pannel.place(relx=0.2,rely=0.6,anchor=CENTER)
        #root.mainloop() 
        #obj_gre.finish()
        
    def blue_remove(top):
        obj_rob=MoveRobot
        obj_gr=greenfun
        obj_blu=bluefun
        obj_blu.destroy_window(top)
        top=obj_gr.removeGUI()
        obj_rob.removeregular()
        obj_gr.finish(top)       
         
    def Bluestart(tp):
        obj=bluefun
        obj.destroy_window(tp)
        root=tk.Toplevel()
        root.geometry('1920x1080')
        root.config(bg='azure')
        path='c:/Politeness/picture_hebrew/bluequestion.png'
        img = ImageTk.PhotoImage(Image.open(path))
        pannel=Label(root,image=img)
        pannel.image=img
        pannel.pack()
        #msg1=Label(root,text="Do you want me to\n setup the table now ?",bg='azure',font=('times',80,'bold'))               
        opt_yes=tk.Button(root,padx=1.0,pady=1.0,height=2,width=25,bg='white',text='כן',font=('times',34,'bold'))
        opt_yes.config(command= lambda button=opt_yes: obj.blue_set_table(root))
        opt_no=tk.Button(root,padx=1.0,pady=1.0,height=2,width=25,bg='white',text='לא עכשיו',font=('times',34,'bold'),command=lambda: obj.blue_timer(root))
        #msg1.grid()
        #opt_yes.grid()
        #opt_no.grid()
        #msg1.place(relx=0.1,rely=0,anchor=NW)
        opt_yes.place(relx=0.7,rely=0.6,anchor=CENTER)
        opt_no.place(relx=0.7,rely=0.8,anchor=CENTER)
        #pannel.place(relx=0.2,rely=0.6,anchor=CENTER)
        #root.mainloop()
#GREEN LEVEL   
class redfun:

    def destroy_window(top):
        top.destroy()
    def fancysetting():
         root=tk.Toplevel()              
         root.geometry('1920x1080')
         root.config(bg='azure')
         path=r'c:\Politeness\picture_hebrew\fancysetting.png'
         img = ImageTk.PhotoImage(Image.open(path))
         msg=Label(root,image=img)
         msg.image=img
         msg.pack()
         
         root.update()
         
         
         filename = r"C:\Users\Owner\Documents\Sound recordings\i-am-setting-the-table1576402758.wav"
         data, fs = sf.read(filename, dtype='float')
         sd.play(data, fs)
         sd.wait()
         return(root)
    
    def red_timer(top,a):
        countdown=10*a
        root=tk.Toplevel()
        root.geometry('1920x1080')
        obj_red=redfun
        obj_red.destroy_window(top)
        root.config(bg='azure')
        label=Label(root,text="",height=100,width=50)
        
        while(countdown!=-1):
            
            
            if (countdown==0):
                print("finish")
                countdown=countdown-1
                obj_red.redmeal(root)
                #root.destroy()
            else:
                label.configure(text=" %d הזמן שנשאר" %countdown,bg='azure',font=('times',40))
                label.pack()
                root.update()                
                close_but=tk.Button(root,bg='white',height=2,width=45,text="ערוך את השולחן כעת",font=('times',34,'bold'),command=lambda: obj_red.redmeal(root))
                close_but.pack()
                close_but.place(relx=0.5,rely=0.8,anchor=CENTER)
                root.update()
                time.sleep(1)
                countdown=countdown-1
        
    def finish(top):
        obj=redfun
        obj.destroy_window(top)
        root=Toplevel()
        root.geometry('1920x1080')
        root.config(bg='azure')
        #path=r"C:/Users/Owner/eclipse-workspace/thePoliteRobot/thePoliteRobot/img/bonape.gif"
        #img = ImageTk.PhotoImage(Image.open(path))
        #pannel=Label(root,image=img)
        #pannel.image=img
        msg=Label(root,text="תודה רבה",bg='azure')
        msg.config(font=('times',80,'bold'))
        msg.pack()
        msg.place(relx=0.5,rely=0.2,anchor=CENTER)
        #pannel.place(relx=0.5,rely=0.5,anchor=CENTER)
        root.update()
        #filename = r"C:\Users\Owner\Documents\Sound recordings\thank-you-very-much-bon1576406177.wav"
        #data, fs = sf.read(filename, dtype='float')
        #sd.play(data, fs)
        #sd.wait()
    def red_utensils(top,a):
        obj_rob=MoveRobot
        obj_red=redfun
        obj_gr=greenfun
        obj_blu=bluefun
        obj_red.destroy_window(top)

        if (a == 1):

            top = obj_gr.removeGUI()
            obj_rob.removeregular()
            # obj_red.destroy_window(top)
        elif (a == 2):
            top=obj_red.fancysetting()
            obj_rob.removefancy()

        obj_red.finish(top)
    def red_remove(top,a):
        obj_red=redfun
        obj_red.destroy_window(top)
        root=Toplevel()
        root.geometry('1920x1080')
        root.config(bg='azure')
        #msg1=Label(root,text="Are you satisfied with \n the table setting ?",bg='azure',font=('times',80,'bold'))
        path='c:/Politeness/picture_hebrew/blueremove.png'
        img = ImageTk.PhotoImage(Image.open(path))
        pannel=Label(root,image=img)
        pannel.image=img
        pannel.pack()
        opt_yes=tk.Button(root,padx=1.0,pady=1.0,height=2,width=25,bg='white',text='כן',font=('times',34,'bold'))
        opt_yes.config(command=lambda button=opt_yes : obj_red.red_utensils(root,a))
        
        opt_no=tk.Button(root,padx=1.0,pady=1.0,height=2,width=25,bg='white',text='לא',font=('times',34,'bold'))
        opt_no.config(command= lambda:obj_red.finish(root))  
        opt_yes.place(relx=0.7,rely=0.6,anchor=CENTER)
        opt_no.place(relx=0.7,rely=0.8,anchor=CENTER)  
        
        
          
    def change_plate(top,a):
        obj_rob=MoveRobot
        obj_gre=greenfun
        obj_red=redfun
        obj_red.destroy_window(top)
        if (a == 1):
            top = obj_gre.GreenGUI()
            obj_rob.removeregular()
            obj_rob.fancysetting()
            #obj_red.destroy_window(top)
        elif (a == 2):
            top = obj_red.fancysetting()
            obj_rob.removefancy()
            obj_rob.regularsetting()
            #obj_red.destroy_window(top)
        a=3-a
        obj_red.red_remove(top,a)
    def red_set_table(top,a):
        obj_gre=greenfun
        
        obj_rob=MoveRobot
        obj_red=redfun
        obj_red.destroy_window(top)
        obj_blu=bluefun
        if(a==1):
            top=obj_gre.GreenGUI()
            obj_rob.regularsetting()
            obj_red.destroy_window(top)
        elif(a==2):
            top = obj_red.fancysetting()
            obj_rob.fancysetting()
            obj_red.destroy_window(top)
        root=tk.Toplevel()
        root.geometry('1920x1080')
        root.config(bg='azure')
        #msg1=Label(root,text="Are you satisfied \n with the table setting ?",bg='azure',font=('times',80,'bold'))              
        path='C:/Politeness/picture_hebrew/feedback.png'
        img = ImageTk.PhotoImage(Image.open(path))
        pannel=Label(root,image=img)
        pannel.image=img
        pannel.pack()
        path1='C:/Politeness/picture_hebrew/Yes.jpg'
        if (a==1):
            path2='C:/Politeness/picture_hebrew/feedback_fancy.jpg'
        else:
            path2='C:/Politeness/picture_hebrew/feedback_regular.jpg'        
        img1=ImageTk.PhotoImage(Image.open(path1))
        img2=ImageTk.PhotoImage(Image.open(path2))
        pannel1=Label(root,image=img1)
        pannel2=Label(root,image=img2)
        opt_yes=tk.Button(root,image=img1,height=500,width=500)
        opt_yes.config(command= lambda button=opt_yes: obj_red.red_remove(root,a))
        opt_yes.image=img1
        opt_yes.place(relx=0.15,rely=0.55,anchor=CENTER)
        opt_no=tk.Button(root,image=img2,height=700,width=500)
        opt_no.config(command=lambda button=opt_no : obj_red.change_plate(root,a))        
        opt_no.image=img2
        #msg1.grid()
        #opt_yes.grid()
        #opt_no.grid()
        #pannel.grid()
        #pannel.place(relx=0.2,rely=0.6,anchor=CENTER)
        #msg1.place(relx=0.1,rely=0,anchor=NW)
        
        opt_no.place(relx=0.7,rely=0.55,anchor=CENTER)
        
        #pannel1.place(relx=0.92,rely=0.6,anchor=CENTER)
        #pannel2.place(relx=0.92,rely=0.8,anchor=CENTER)
        #root.mainloop()
    def redmeal(top):
        root=tk.Toplevel()
        root.geometry('1920x1080')
        obj_gr=greenfun
        obj_red=redfun
        obj_red.destroy_window(top)
        root.config(bg='azure')
        path='c:/Politeness/picture_hebrew/red meal.png'
        path1='c:/Politeness/picture_hebrew/setTable.jpg'
        path2='c:/Politeness/picture_hebrew/image002.jpg'
        path3='c:/Politeness/picture_hebrew/indifferent.png'
        img = ImageTk.PhotoImage(Image.open(path))
        pannel=Label(root,image=img)
        pannel.image=img
        pannel.pack()
        img_reg=ImageTk.PhotoImage(Image.open(path1))
        img_fan=ImageTk.PhotoImage(Image.open(path2))
        img_ind=ImageTk.PhotoImage(Image.open(path3))
        #label=Label(root,text="How would you like me to set the table ?",bg='azure',font=('times',78,'bold'))
        opt_reg=tk.Button(root,image=img_reg,height=400,width=500,command=lambda: obj_red.red_set_table(root,1),font=('times',34,'bold'))
        opt_reg.image=img_reg
        opt_reg.place(relx=0.15,rely=0.5,anchor=CENTER)
        opt_fan=tk.Button(root,image=img_fan,height=400,width=500,command=lambda: obj_red.red_set_table(root,2),font=('times',34,'bold'))
        opt_fan.image=img_fan
        opt_fan.place(relx=0.48,rely=0.5,anchor=CENTER)
        opt_indiff=tk.Button(root,image=img_ind,height=400,width=500,command=lambda: obj_red.red_set_table(root,1),font=('times',34,'bold'))
        opt_indiff.image=img_ind
        opt_indiff.place(relx=0.8,rely=0.5,anchor=CENTER)
        #annel=Label(root,image=img)
        #label.grid()
        #opt_dairy.grid()
        #opt_meat.grid()
        #opt_indiff.grid()
        #pannel.place(relx=0.2,rely=0.6,anchor=CENTER)
        #label.place(relx=0,rely=0,anchor=NW)
            
        #root.mainloop() 
    def redtimeGUI(top):
        obj=redfun
        obj.destroy_window(top)
        root=tk.Toplevel()
        root.geometry('1920x1080')
        root.config(bg='azure')
        path='C:/Politeness/picture_hebrew/redtime.png'
        img = ImageTk.PhotoImage(Image.open(path))
        pannel=Label(root,image=img)
        pannel.image=img
        pannel.pack()
        #msg1=Label(root,text="When do you want me to \n setup the table ?",bg='azure',font=('times',80,'bold'))               
        opt_yes=tk.Button(root,padx=1.0,pady=1.0,height=2,width=25,bg='white',text='כעת',command=lambda:obj.redmeal(root),font=('times',34,'bold'))
        opt_onemi=tk.Button(root,padx=1.0,pady=1.0,height=2,width=25,bg='white',text='מאוחר יותר',command=lambda: obj.red_timer(root,1),font=('times',34,'bold'))
        #opt_twomi=tk.Button(root,padx=1.0,pady=1.0,height=2,width=25,bg='white',text='In two minutes',command=lambda: obj.red_timer(2),font=('times',34,'bold'))
        
        #msg1.grid()
        #opt_yes.grid()
        #opt_onemi.grid()
        #opt_twomi.grid()
        #pannel.grid()
        #msg1.place(relx=0,rely=0,anchor=NW)
        #pannel.place(relx=0.2,rely=0.6,anchor=CENTER)
        opt_yes.place(relx=0.7,rely=0.4,anchor=CENTER)
        opt_onemi.place(relx=0.7,rely=0.6,anchor=CENTER)
        #opt_twomi.place(relx=0.7,rely=0.8,anchor=CENTER)
        #root.mainloop()
    def redstart(tp):
        obj=redfun
        obj.destroy_window(tp)
        root=tk.Toplevel()
        root.config(bg='azure')
        root.geometry('1920x1080')
        path='c:/Politeness/picture_hebrew/Welcome.png'
        img = ImageTk.PhotoImage(Image.open(path))
        pannel=Label(root,image=img)
        pannel.image=img
        pannel.pack()
        nxt=tk.Button(root,padx=10,pady=10,height=1,width=25,bg='azure',text='המשך',font=('times',32,'bold'))
        nxt.config(command= lambda button=nxt:obj.redtimeGUI(root))
        #label.grid()
        #label.place(relx=0.5,rely=0.5,anchor=CENTER)
        #nxt.grid()
        nxt.place(relx=0.7,rely=0.8,anchor=CENTER)
        root.update()
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    class ROBOT move
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''                    
class MoveRobot:
    def fancysetting():
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
            #dType.SetPTPCoordinateParams(api, 200, 200, 200, 200)
            #dType.SetPTPJumpParams(api, 10, 200)
            #dType.SetPTPCommonParams(api, 100, 100)
            #Plates
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 186.8912, 39.9336, -5.004, 1.9758, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 125.0959, -221.2122, 34.7154, -64.8694, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -19.9620,-309.8604,32.0835,-98.0370, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -19.9620,-309.8604,-62.0835,-98.0370, 1)
            enableCtrl = 1
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -19.9620, -309.8604, 32.0835, -98.0370, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 125.0959, -221.2122, 64.7154, -64.8694, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 223.4960, -0.2065, 62.0835, -4.4106, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 223.4960, -0.2065, -64.1221, -4.4106, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 223.4960, -0.2065, 32.0835, -4.4106, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,35.004,1.9758,1)
            #Fork
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 186.8912, 39.9336, -5.004, 1.9758, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 125.0959, -221.2122, 34.7154, -64.8694, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-48.3145,-250.1328,30.7960,-108.7090, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -48.3145,-250.1328,-60.7960,-108.7090, 1)
            enableCtrl = 1
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -48.3145,-250.1328,30.7960,-108.7090, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 125.0959, -221.2122, 54.7154, -64.8694, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 242.3118,-121.3563,40.8418,-105.2900, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 242.3118,-121.3563,-60.8418,-105.2900, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 242.3118,-121.3563,30.8418,-105.29006, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
            #knife
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 186.8912, 39.9336, -5.004, 1.9758, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 125.0959, -221.2122, 54.7154, -64.8694, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-17.2140,-222.6702,48.4182,-94.4206, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -17.2140,-222.6702,-58.4182,-94.4206, 1)
            enableCtrl = 1
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -17.2140,-222.6702,38.4182,-94.4206, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 125.0959, -221.2122, 34.7154, -64.8694, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,35.004,-94.4206,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 252.1628,142.5985,36.5096,-89.8125, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 252.1628,142.5985,-58.5096,-89.8125, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 252.1628,142.5985,36.5096,-89.8125, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
            #Glass
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 186.8912, 39.9336, -5.004, 1.9758, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 125.0959, -221.2122, 64.7154, -64.8694, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-39.8103,-259.0938,68.4182,-94.4206, 1)

            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-100,-180.4377,66.9551,30.6419, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -100,-180.4377,38.9551,30.6419, 1)
            enableCtrl = 1
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-100,-180.4377,66.9551,30.6419, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 125.0959, -221.2122, 66.7154, 30.6419, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 223.4960, -0.2065, 66.0835, 30.6419, 1)
            #dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,46.5497,-94.4206,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 145.7806, 181.7918, 66.6431,30.6419, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,145.7806,181.7918, 38.0901, 30.6419, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,145.7806,181.7918, 67.6431, 30.9651, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,41.9758,1)
            #spoon
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 186.8912, 39.9336, -5.004, 1.9758, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 125.0959, -221.2122, 34.7154, -64.8694, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-39.1950,-192.1502,31.5350,-220.9505, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -39.1950,-192.1502,-61.5350,-220.9505, 1)
            enableCtrl = 1
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -39.1950,-192.1502,31.5350,-220.9505, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 125.0959, -221.2122, 54.7154, -64.8694, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,35.004,-94.4206,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239.3071,182.9795,33.4736,128.9525, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239.3071,182.9795,-63.4736,128.9525, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239.3071,182.9795,33.4736,128.9525, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
            
            #Napkin
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 186.8912, 39.9336, -5.004, 1.9758, 1)
            #dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 125.0959, -221.2122, 34.7154, -64.8694, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,153.6523,-264.8134,61.1512,-64.8694, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 153.6523,-264.8134,-61.1512,-64.8694, 1)
            enableCtrl = 1
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 206.6288,-250.2418,39.8620,42.10375, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 125.0959, -221.2122, 34.7154, -64.8694, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,-94.4206,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 269.7150,16.8439,30.9441,96.1301, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 269.7150,16.8439,-60.9441,96.1301, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 269.7150,16.8439,30.9441,96.1301, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,15.004,1.9758,1)
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
    def removefancy():
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
            #Napkin
            enableCtrl = 1
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,-94.4206,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 269.7150,16.8439,30.9441,96.1301, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 269.7150,16.8439,-60.9441,96.1301, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 269.7150,16.8439,30.9441,96.1301, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,153.6523,-264.8134,61.1512,-64.8694, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 153.6523,-264.8134,-61.1512,-64.8694, 1)
            enableCtrl = 1
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,153.6523,-264.8134,61.1512,-64.8694, 1)            
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 206.6288,-250.2418,39.8620,42.10375, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 125.0959, -221.2122, 34.7154, -64.8694, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,-94.4206,1)
            # Plates
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 186.8912, 39.9336, -5.004, 1.9758, 1)
            enableCtrl = 1
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 223.4960, -0.2065, 62.0835, -4.4106, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 223.4960, -0.2065, -64.1221, -4.4106, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 223.4960, -0.2065, 32.0835, -4.4106, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 125.0959, -221.2122, 34.7154, -64.8694, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -19.9620,-309.8604,32.0835,-98.0370, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -19.9620,-309.8604,-62.0835,-98.0370, 1)
            enableCtrl = 1
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -19.9620, -309.8604, 32.0835, -98.0370, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 125.0959, -221.2122, 64.7154, -64.8694, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 186.8912, 39.9336, -5.004, 1.9758, 1)
            #knife
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,35.004,-94.4206,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 252.1628,142.5985,36.5096,-89.8125, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 252.1628,142.5985,-60.5096,-89.8125, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 252.1628,142.5985,36.5096,-89.8125, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,35.004,-94.4206,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 125.0959, -221.2122, 34.7154, -64.8694, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-17.2140,-222.6702,48.4182,-94.4206, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -17.2140,-222.6702,-58.4182,-94.4206, 1)
            enableCtrl = 1
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -17.2140,-222.6702,38.4182,-94.4206, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 125.0959, -221.2122, 34.7154, -64.8694, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,35.004,-94.4206,1)
            #Fork
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 186.8912, 39.9336, -5.004, 1.9758, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 242.3118,-121.3563,40.8418,-105.2900, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 242.3118,-121.3563,-60.8418,-105.2900, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 242.3118,-121.3563,30.8418,-105.29006, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 125.0959, -221.2122, 34.7154, -64.8694, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-48.3145,-250.1328,30.7960,-108.7090, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -48.3145,-250.1328,-60.7960,-108.7090, 1)
            enableCtrl = 1
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -48.3145,-250.1328,30.7960,-108.7090, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 125.0959, -221.2122, 34.7154, -64.8694, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 186.8912, 39.9336, -5.004, 1.9758, 1)
            #glass
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,35.004,-94.4206,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 145.7806, 191.7918, 66.6431, 30.9651, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,145.7806,191.7918, 38.0901, 30.9651, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,145.7806,191.7918, 67.6431, 30.9651, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 223.4960, -0.2065, 66.0835, 30.6419, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 125.0959, -221.2122, 64.7154, 30.6419, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-17.2140,-222.6702,68.4182,30.6419, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-100,-180.4377,66.9551,30.6419, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -100,-180.4377,38.9551,30.6419, 1)
            enableCtrl = 1
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -100,-180.4377,66.9551,30.6419, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 125.0959, -221.2122, 66.7154, -64.8694, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,35.004,-94.4206,1)
            #Spoon
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,35.004,-94.4206,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239.3071,182.9795,33.4736,128.9525, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239.3071,182.9795,-63.4736,128.9525, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239.3071,182.9795,33.4736,128.9525, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,35.004,-94.4206,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 125.0959, -221.2122, 34.7154, -64.8694, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-39.1950,-192.1502,31.5350,-220.9505, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -39.1950,-192.1502,-61.5350,-220.9505, 1)
            enableCtrl = 1
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -39.1950,-192.1502,31.5350,-220.9505, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 125.0959, -221.2122, 54.7154, -64.8694, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,35.004,-94.4206,1)
            
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

    def regularsetting():
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
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 204.6735, 196.1538, 51.0921, 39.4247, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -16.5221, 313.4125, 39.8368, 85.2441, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -16.5221, 313.4125, -66.8368, 85.2441, 1)
            enableCtrl = 1
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -16.5221, 313.4125, 39.8368, 85.2441, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 223.4960, -0.2065, 62.0835, -4.4106, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 223.4960, -0.2065, -64.1221, -4.4106, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 223.4960, -0.2065, 32.0835, -4.4106, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 182.8912, 39.9336, 35.004, 1.9758, 1)
            #FORK
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -18.5335, 253.4467, 35.2350, 89.8247, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-18.5335,253.4467,-68.2350,89.8247,1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
            dType.dSleep(5000)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-18.5335,253.4467,35.2350,89.8247,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,40.004,87.707,1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 242.3118, -121.3563, 40.8418, 87.707, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 242.3118, -121.3563, -68.8418, 87.707, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 242.3118, -121.3563, 30.8418,87.707, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 182.8912, 39.9336, -5.004, 1.9758, 1)
            #kNIFE
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 182.8912, 39.9336, -5.004, 1.9758, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -25.5099, 224.4094, 32.0154, 92.1277, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -25.5099, 224.4094, -68.0154, 92.1277, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -25.5099, 224.4094, 32.0154, 92.1277, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -25.5099, 224.4094, 32.0154, 92.1277, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 252.1628, 142.5985, 36.5096, 92.1277, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 252.1628, 142.5985, -68.5096, 92.1277, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 252.1628, 142.5985, 36.5096, 92.1277, 1)
            #Spoom
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -12.1231, 187.1717, 35.6251, 83.3647, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -12.1231, 187.1717, -65.6251, 83.3647, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -12.1231, 187.1717, 35.6251, 83.3647, 1)            
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239.3071,182.9795,33.4736,83.3647, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239.3071,182.9795,-66.4736,83.3647, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239.3071,182.9795,33.4736,83.3647, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 182.8912, 39.9336, -5.004, 1.9758, 1)
            #Glass
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 182.8912, 39.9336, -5.004, 1.9758, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 37,241.6004,81.3297,76.7218, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -94.3592,190.3797,67.1485,112.0081, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -94.3592,190.3797,17.1485,112.0081, 1)

            dType.SetEndEffectorSuctionCup(api, enableCtrl, 1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,  -94.3592,190.3797,67.1485,112.0081, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 37, 241.6004, 81.3297, 76.7218, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 145.7806, 181.7918, 66.6431, 30.9651, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,145.7806,181.7918, 15.28671, 30.9651, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,145.7806,181.7918, 67.6431, 30.9651, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 182.8912, 39.9336, -5.004, 1.9758, 1)
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
    def removeregular():
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
            enableCtrl = 1
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 186.8912, 39.9336, -5.004, 1.9758, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 223.4960, -0.2065, 62.0835, -4.4106, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 223.4960, -0.2065, -64.1221, -4.4106, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 223.4960, -0.2065, 32.0835, -4.4106, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 204.6735, 196.1538, 51.0921, 39.4247, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -16.5221, 313.4125, 39.8368, 85.2441, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -16.5221, 313.4125, -66.8368, 85.2441, 1)
            enableCtrl = 1
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -16.5221, 313.4125, 39.8368, 85.2441, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 204.6735, 196.1538, 51.0921, 39.4247, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 186.8912, 39.9336, -5.004, 1.9758, 1)
            #Glass
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 182.8912, 39.9336, -5.004, 1.9758, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 145.7806, 181.7918, 66.6431, 30.9651, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 145.7806, 181.7918, 15.2867, 30.9651, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 145.7806, 181.7918, 67.6431, 30.9651, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 37, 241.6004, 81.3297, 76.7218, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -94.3592, 190.3797, 67.1485, 112.0081, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -94.3592, 190.3797, 17.1485, 112.0081, 1)

            dType.SetEndEffectorSuctionCup(api, enableCtrl, 0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -94.3592, 190.3797, 67.1485, 112.0081, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 37, 241.6004, 81.3297, 76.7218, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 182.8912, 39.9336, -5.004, 1.9758, 1)
            #FORK
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 182.8912, 39.9336, -5.004, 87.707, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 242.3118, -121.3563, 40.8418, 87.707, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 242.3118, -121.3563, -65.8418, 87.707, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 242.3118, -121.3563, 30.8418, 87.707, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 182.8912, 39.9336, 55.004, 87.707, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 204.6735, 196.1538, 51.0921, 39.4247, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -18.5335, 253.4467, 55.2350, 89.8247, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -18.5335, 253.4467, -68.2350, 89.8247, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 0, isQueued=1)
            dType.dSleep(5000)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -18.5335, 253.4467, 55.2350, 89.8247, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 204.6735, 196.1538, 51.0921, 39.4247, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 182.8912, 39.9336, 35.004, 87.707, 1)
            #Knife
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 182.8912, 39.9336, 45.004, 1.9758, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 252.1628, 142.5985, 36.5096, 92.1277, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 252.1628, 142.5985, -68.5096, 92.1277, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 252.1628, 142.5985, 36.5096, 92.1277, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -25.5099, 224.4094, 32.0154, 92.1277, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -25.5099, 224.4094, -65.0154, 92.1277, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -25.5099, 224.4094, 32.0154, 92.1277, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -25.5099, 224.4094, 32.0154, 92.1277, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 182.8912, 39.9336, -5.004, 1.9758, 1)

            
            #Spoon
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 182.8912, 39.9336, -5.004, 1.9758, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239.3071, 182.9795, 33.4736, 83.3647, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239.3071, 182.9795, -63.4736, 83.3647, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 1, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 239.3071, 182.9795, 33.4736, 83.3647, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -12.1231, 187.1717, 35.6251, 83.3647, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -12.1231, 187.1717, -65.6251, 83.3647, 1)
            dType.SetEndEffectorSuctionCup(api, enableCtrl, 0, isQueued=1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -12.1231, 187.1717, 35.6251, 83.3647, 1)
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 182.8912, 39.9336, -5.004, 1.9758, 1)
            que_sts = dType.GetQueuedCmdCurrentIndex(api)
            chk = 0
            a = 1
            strt = time.time()
            while (chk == 0):
                strt = time.time()
                while (time.time() - strt < 3):
                    pass
                if (que_sts != dType.GetQueuedCmdCurrentIndex(api)):
                    que_sts = dType.GetQueuedCmdCurrentIndex(api)
                else:
                    break
            dType.DisconnectDobot(api)

    

    # def moveplate1():
    #     CON_STR = {
    #     dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    #     dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    #     dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}
    #     #Load Dll
    #     api = dType.load()
    #     #Connect Dobot
    #     state = dType.ConnectDobot(api, "", 115200)[0]
    #     print("Connect status:",CON_STR[state])
    #     if (state == dType.DobotConnect.DobotConnect_NoError):
    #         dType.SetPTPJointParams(api,200,200,200,200,200,200,200,200)
    #         dType.SetPTPCoordinateParams(api,200,200,200,200)
    #         dType.SetPTPJumpParams(api, 10, 200)
    #         dType.SetPTPCommonParams(api, 100, 100)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,186.8912,39.9336,-5.004,1.9758,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,125.0959,-221.2122,34.7154,-64.8694,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,10.5221,-299.5519,30.7303,-92.3458,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,10.5221,-299.5519,-64.8675,-92.3458,1)
    #         enableCtrl=1
    #         dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,10.5221,-299.5519,30.7303,-92.3458,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,306.5724,-11.6725,38.3710,-45.45,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,306.5724,-11.6725,-68.3710,-45.45,1)
    #         dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,306.5724,-11.6725,38.3710,-45.45,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
    #         que_sts=dType.GetQueuedCmdCurrentIndex(api)
    #         chk=0
    #         a=1
    #         strt=time.time()
    #         while (chk==0):
    #             strt=time.time()
    #             while(time.time()-strt<2):
    #                 pass
    #             if(que_sts!=dType.GetQueuedCmdCurrentIndex(api)):
    #                 que_sts=dType.GetQueuedCmdCurrentIndex(api)
    #             else:
    #                 break
    #         dType.DisconnectDobot(api)
    #
    # def removeplate1():
    #     CON_STR = {
    #     dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    #     dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    #     dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}
    #     #Load Dll
    #     api = dType.load()
    #     #Connect Dobot
    #     state = dType.ConnectDobot(api, "", 115200)[0]
    #     print("Connect status:",CON_STR[state])
    #     if (state == dType.DobotConnect.DobotConnect_NoError):
    #         dType.SetPTPJointParams(api,200,200,200,200,200,200,200,200)
    #         dType.SetPTPCoordinateParams(api,200,200,200,200)
    #         dType.SetPTPJumpParams(api, 10, 200)
    #         dType.SetPTPCommonParams(api, 100, 100)
    #         enableCtrl=1
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,306.5724,-11.6725,38.3710,-45.45,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,306.5724,-11.6725,-68.3710,-45.45,1)
    #         dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,306.5724,-11.6725,38.3710,-45.45,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,125.0959,-221.2122,34.7154,-64.8694,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,10.5221,-299.5519,30.7303,-92.3458,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,10.5221,-299.5519,-64.8675,-92.3458,1)
    #         dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,10.5221,-299.5519,30.7303,-92.3458,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,125.0959,-221.2122,34.7154,-64.8694,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
    #         que_sts=dType.GetQueuedCmdCurrentIndex(api)
    #         chk=0
    #         a=1
    #         strt=time.time()
    #         while (chk==0):
    #             strt=time.time()
    #             while(time.time()-strt<2):
    #                 pass
    #             if(que_sts!=dType.GetQueuedCmdCurrentIndex(api)):
    #                 que_sts=dType.GetQueuedCmdCurrentIndex(api)
    #             else:
    #                 break
    #         dType.DisconnectDobot(api)
    # def movefork(opt):
    #     CON_STR = {
    #     dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    #     dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    #     dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}
    #     #Load Dll
    #     api = dType.load()
    #     #Connect Dobot
    #     state = dType.ConnectDobot(api, "", 115200)[0]
    #     print("Connect status:",CON_STR[state])
    #     if (state == dType.DobotConnect.DobotConnect_NoError):
    #         dType.SetPTPJointParams(api,200,200,200,200,200,200,200,200)
    #         dType.SetPTPCoordinateParams(api,200,200,200,200)
    #         dType.SetPTPJumpParams(api, 10, 200)
    #         dType.SetPTPCommonParams(api, 100, 100)
    #         enableCtrl=1
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-18.5335,253.4467,35.2350,89.8247,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-18.5335,253.4467,-68.2350,89.8247,1)
    #         dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #         dType.dSleep(5000)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-18.5335,253.4467,35.2350,89.8247,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,87.707,1)
    #         if(opt==1):
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,270.9802,-152.083,34.0257,87.707,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,270.9802,-152.083,-64.0257,87.707,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,270.9802,-152.083,34.0257,87.707, 1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
    #         elif(opt==2):
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,270.9802,-152.083,34.0257,87.707,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,270.9802,-152.083,-64.0257,87.707,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,270.9802,-152.083,34.0257,87.707, 1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
    #
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,127.7938,-244.6304,34.6886,-72.7589,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,127.7938,-244.6304,-65.6886,-72.7589,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,127.7938,-244.6304,34.6886,-72.7589,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,242.3140,-179.3222,34.4296,10.5278,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,242.3140,-179.3222,-64.4296,10.5278,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,242.3140,-179.3222,34.4296,10.5278,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
    #         que_sts=dType.GetQueuedCmdCurrentIndex(api)
    #         chk=0
    #         a=1
    #         strt=time.time()
    #         while (chk==0):
    #             strt=time.time()
    #             while(time.time()-strt<2):
    #                 pass
    #             if(que_sts!=dType.GetQueuedCmdCurrentIndex(api)):
    #                 que_sts=dType.GetQueuedCmdCurrentIndex(api)
    #             else:
    #                 break
    #         dType.DisconnectDobot(api)
    # def removefork(opt):
    #     CON_STR = {
    #     dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    #     dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    #     dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}
    #     #Load Dll
    #     api = dType.load()
    #     #Connect Dobot
    #     state = dType.ConnectDobot(api, "", 115200)[0]
    #     print("Connect status:",CON_STR[state])
    #     if (state == dType.DobotConnect.DobotConnect_NoError):
    #         dType.SetPTPJointParams(api,200,200,200,200,200,200,200,200)
    #         dType.SetPTPCoordinateParams(api,200,200,200,200)
    #         dType.SetPTPJumpParams(api, 10, 200)
    #         dType.SetPTPCommonParams(api, 100, 100)
    #         enableCtrl=1
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
    #         if(opt==1):
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,270.9802,-152.083,34.0257,87.707,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,270.9802,-152.083,-64.0257,87.707,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,270.9802,-152.083,34.0257,87.707, 1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-18.5335,253.4467,35.2350,89.8247,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-18.5335,253.4467,-68.2350,89.8247,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #             dType.dSleep(5000)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-18.5335,253.4467,35.2350,89.8247,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,87.707,1)
    #         elif(opt==2):
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,242.3140,-179.3222,34.4296,10.5278,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,242.3140,-179.3222,-64.4296,10.5278,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,242.3140,-179.3222,34.4296,10.5278,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,127.7938,-244.6304,34.6886,-72.7589,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,127.7938,-244.6304,-65.6886,-72.7589,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,127.7938,-244.6304,34.6886,-72.7589,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,271.0764,-136.0758,54.0257,87.707,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,271.0764,-136.0758,-64.0257,87.707,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,271.0764,-136.0758,54.0257,87.707,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
    #
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-18.5335,253.4467,35.2350,89.8247,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-18.5335,253.4467,-68.2350,89.8247,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-18.5335,253.4467,35.2350,89.8247,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,87.707,1)
    #         que_sts=dType.GetQueuedCmdCurrentIndex(api)
    #         chk=0
    #         a=1
    #         strt=time.time()
    #         while (chk==0):
    #             strt=time.time()
    #             while(time.time()-strt<2):
    #                 pass
    #             if(que_sts!=dType.GetQueuedCmdCurrentIndex(api)):
    #                 que_sts=dType.GetQueuedCmdCurrentIndex(api)
    #             else:
    #                 break
    #         dType.DisconnectDobot(api)
    # def moveknife(opt):
    #     CON_STR = {
    #     dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    #     dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    #     dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}
    #     #Load Dll
    #     api = dType.load()
    #     #Connect Dobot
    #     state = dType.ConnectDobot(api, "", 115200)[0]
    #     print("Connect status:",CON_STR[state])
    #     if (state == dType.DobotConnect.DobotConnect_NoError):
    #         dType.SetPTPJointParams(api,200,200,200,200,200,200,200,200)
    #         dType.SetPTPCoordinateParams(api,200,200,200,200)
    #         dType.SetPTPJumpParams(api, 10, 200)
    #         dType.SetPTPCommonParams(api, 100, 100)
    #         enableCtrl=1
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-25.5099,224.4094,32.0154,92.1277,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-25.5099,224.4094,-65.0154,92.1277,1)
    #         dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #         time.sleep(3)
    #         if (opt==1):
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-25.5099,224.4094,32.0154,92.1277,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,285.4430,93.1836,30.3683,92.1277,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,285.4430,93.1836,-68.6680,92.1277,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 285.4430,93.1836,48.6680,92.1277, 1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
    #         elif(opt==2):
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-25.5099,224.4094,32.0154,92.1277,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,285.4430,93.1836,30.3683,92.1277,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,285.4430,93.1836,-68.6680,92.1277,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 285.4430,93.1836,48.6680,92.1277, 1)
    #
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-12.1231,187.1717,35.6251,83.3647,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-12.1231,187.1717,-65.6251,83.3647,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-12.1231,187.1717,35.6251,83.3647,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,286.3798,122.3599,34.6310,83.3647,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,286.3798,122.3599,-64.6310,83.3647,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,286.3798,122.3599,34.6310,83.3647,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
    #         que_sts=dType.GetQueuedCmdCurrentIndex(api)
    #         chk=0
    #         a=1
    #         strt=time.time()
    #         while (chk==0):
    #             strt=time.time()
    #             while(time.time()-strt<2):
    #                 pass
    #             if(que_sts!=dType.GetQueuedCmdCurrentIndex(api)):
    #                 que_sts=dType.GetQueuedCmdCurrentIndex(api)
    #             else:
    #                 break
    #         dType.DisconnectDobot(api)
    # def removeknife(opt):
    #     CON_STR = {
    #     dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    #     dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    #     dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}
    #     #Load Dll
    #     api = dType.load()
    #     #Connect Dobot
    #     state = dType.ConnectDobot(api, "", 115200)[0]
    #     print("Connect status:",CON_STR[state])
    #     if (state == dType.DobotConnect.DobotConnect_NoError):
    #         dType.SetPTPJointParams(api,200,200,200,200,200,200,200,200)
    #         dType.SetPTPCoordinateParams(api,200,200,200,200)
    #         dType.SetPTPJumpParams(api, 10, 200)
    #         dType.SetPTPCommonParams(api, 100, 100)
    #         enableCtrl=1
    #         if (opt==1):
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,285.4430,93.1836,30.3683,92.1277,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,285.4430,93.1836,-68.6680,92.1277,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 285.4430,93.1836,48.6680,92.1277, 1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
    #         elif(opt==2):
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,286.3798,122.3599,34.6310,83.3647,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,286.3798,122.3599,-64.6310,83.3647,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,286.3798,122.3599,34.6310,83.3647,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-12.1231,187.1717,35.6251,83.3647,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-12.1231,187.1717,-65.6251,83.3647,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-12.1231,187.1717,35.6251,83.3647,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
    #             #knife1
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-25.5099,224.4094,32.0154,92.1277,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,285.4430,93.1836,30.3683,92.1277,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,285.4430,93.1836,-68.6680,92.1277,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 285.4430,93.1836,48.6680,92.1277, 1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-25.5099,224.4094,32.0154,92.1277,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-25.5099,224.4094,-65.0154,92.1277,1)
    #         dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-25.5099,224.4094,32.0154,92.1277,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
    #         que_sts=dType.GetQueuedCmdCurrentIndex(api)
    #         chk=0
    #         a=1
    #         strt=time.time()
    #         while (chk==0):
    #             strt=time.time()
    #             while(time.time()-strt<2):
    #                 pass
    #             if(que_sts!=dType.GetQueuedCmdCurrentIndex(api)):
    #                 que_sts=dType.GetQueuedCmdCurrentIndex(api)
    #             else:
    #                 break
    #         dType.DisconnectDobot(api)
    # def moveglass(opt):
    #     CON_STR = {
    #         dType.DobotConnect.DobotConnect_NoError: "DobotConnect_NoError",
    #         dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    #         dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}
    #     # Load Dll
    #     api = dType.load()
    #     # Connect Dobot
    #     state = dType.ConnectDobot(api, "", 115200)[0]
    #     print("Connect status:", CON_STR[state])
    #     if (state == dType.DobotConnect.DobotConnect_NoError):
    #         dType.SetPTPJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200)
    #         dType.SetPTPCoordinateParams(api, 200, 200, 200, 200)
    #         dType.SetPTPJumpParams(api, 10, 200)
    #         dType.SetPTPCommonParams(api, 100, 100)
    #         enableCtrl = 1
    #
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 182.8912, 39.9336, -5.004, 1.9758, 1)
    #
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 100.7043,295.9164,50.2867,66.0012, 1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,100.7043,295.9164,17.2867,66.0012, 1)
    #
    #         dType.SetEndEffectorSuctionCup(api, enableCtrl, 1, isQueued=1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,100.7043,295.9164,50.2867,66.0012, 1)
    # #         #if (opt==1 ):
    # #
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,247.9750,179.4652,47.6431,30.9651, 1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 247.9750,179.4652,20.0901,30.9651, 1)
    #         dType.SetEndEffectorSuctionCup(api, enableCtrl, 0, isQueued=1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 247.9750,179.4652,47.6431,30.9651, 1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 182.8912, 39.9336, -5.004, 1.9758, 1)
    #         #elif(opt==2):
    #         #   dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 183.9863,260.5047,70.4531,44.4264, 1)
    #         #   dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 183.9863,260.5047,20.4531,44.4264, 1)
    #         #   dType.SetEndEffectorSuctionCup(api, enableCtrl, 0, isQueued=1)
    #          #  dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 183.9863,260.5047,70.4531,44.4264, 1)
    #          #  dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 182.8912, 39.9336, -5.004, 1.9758, 1)
    #         que_sts = dType.GetQueuedCmdCurrentIndex(api)
    #         chk = 0
    #         a = 1
    #         strt = time.time()
    #         while (chk == 0):
    #             strt = time.time()
    #             while (time.time() - strt < 4):
    #                 pass
    #             if (que_sts != dType.GetQueuedCmdCurrentIndex(api)):
    #                 que_sts = dType.GetQueuedCmdCurrentIndex(api)
    #             else:
    #                 break
    #         dType.DisconnectDobot(api)
    # def removeglass():
    #     CON_STR = {
    #         dType.DobotConnect.DobotConnect_NoError: "DobotConnect_NoError",
    #         dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    #         dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}
    #     # Load Dll
    #     api = dType.load()
    #     # Connect Dobot
    #     state = dType.ConnectDobot(api, "", 115200)[0]
    #     print("Connect status:", CON_STR[state])
    #     if (state == dType.DobotConnect.DobotConnect_NoError):
    #         dType.SetPTPJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200)
    #         dType.SetPTPCoordinateParams(api, 200, 200, 200, 200)
    #         dType.SetPTPJumpParams(api, 10, 200)
    #         dType.SetPTPCommonParams(api, 100, 100)
    #         enableCtrl = 1
    #
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 182.8912, 39.9336, -5.004, 1.9758, 1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,247.9750,179.4652,47.6431,30.9651, 1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 247.9750,179.4652,17.2901,30.9651, 1)
    #         dType.SetEndEffectorSuctionCup(api, enableCtrl, 1, isQueued=1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 247.9750,179.4652,47.6431,30.9651, 1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 100.7043,295.9164,50.2867,66.0012, 1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,100.7043,295.9164,17.2867,66.0012, 1)
    #
    #         dType.SetEndEffectorSuctionCup(api, enableCtrl, 0, isQueued=1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,100.7043,295.9164,50.2867,66.0012, 1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 182.8912, 39.9336, -5.004, 1.9758, 1)
    #         que_sts = dType.GetQueuedCmdCurrentIndex(api)
    #         chk = 0
    #         a = 1
    #         strt = time.time()
    #         while (chk == 0):
    #             strt = time.time()
    #             while (time.time() - strt < 4):
    #                 pass
    #             if (que_sts != dType.GetQueuedCmdCurrentIndex(api)):
    #                 que_sts = dType.GetQueuedCmdCurrentIndex(api)
    #             else:
    #                 break
    #         dType.DisconnectDobot(api)
    #
    # def fancyplate1():
    #     CON_STR = {
    #     dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    #     dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    #     dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}
    #     #Load Dll
    #     api = dType.load()
    #     #Connect Dobot
    #     state = dType.ConnectDobot(api, "", 115200)[0]
    #     print("Connect status:",CON_STR[state])
    #     if (state == dType.DobotConnect.DobotConnect_NoError):
    #         dType.SetPTPJointParams(api,200,200,200,200,200,200,200,200)
    #         dType.SetPTPCoordinateParams(api,200,200,200,200)
    #         dType.SetPTPJumpParams(api, 10, 200)
    #         dType.SetPTPCommonParams(api, 100, 100)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,186.8912,39.9336,-5.004,1.9758,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,125.0959,-221.2122,34.7154,-64.8694,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,3.6097,-300.50,33.8218,-90.8900,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,3.6097,-300.50,-64.9357,-90.8900,1)
    #         enableCtrl=1
    #         dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,3.6097,-300.50,33.8218,-90.8900,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,125.0959,-221.2122,34.7154,-64.8694,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,186.8912,39.9336,-5.004,1.9758,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,306.5724,-11.6725,38.3710,-45.45,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,306.5724,-11.6725,-68.3710,-45.45,1)
    #         dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,306.5724,-11.6725,38.3710,-45.45,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,186.8912,39.9336,-5.004,1.9758,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,125.0959,-221.2122,34.7154,-64.8694,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,26.9190,-179.0504,39.8368,-125.5500,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,26.9190,-179.0504,-62.8368,-125.5500,1)
    #         enableCtrl=1
    #         dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,26.9190,-179.0504,39.8368,-125.5500,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,125.0959,-221.2122,34.7154,-125.5500,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,193.2952,-73.1423,31.9324,-125.5500,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,193.2952,-73.1423,-61.9324,-80.7089,1)
    #         dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,193.2952,-73.1423,31.9324,-125.5500,1)
           # dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,204.6735,196.1538,51.0921,39.4247,1)
            #dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-16.5221,313.4125,39.8368,85.2441,1)
            #dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-16.5221,313.4125,-66.8368,85.2441,1)
            #enableCtrl=1
            #dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
            #dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-16.5221,313.4125,39.8368,85.2441,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,309.6652,-65.9211,31.9324,85.2441,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,309.6652,-65.9211,-63.9324,85.2441,1)
    #         dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,309.6652,-65.9211,31.9324,85.2441,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,159.3461,224.9547,35.0439,6.2754,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,159.3461,224.9547,-65.0439,6.2754,1)
    #         enableCtrl=1
    #         dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,159.3461,224.9547,35.0439,6.2754,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,315.7741,-35.6003,31.9324,-16.7736,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,315.7741,-35.6003,-63.9324,-16.7736,1)
    #         dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,315.7741,-35.6003,31.9324,-16.7736,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,186.8912,39.9336,-5.004,1.9758,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,168.4479,-243.9648,35.0439,-14.3523,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,168.4479,-243.9648,-65.0439,-14.3523,1)
    #         enableCtrl=1
    #         dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,168.4479,-243.9648,35.0439,-14.3523,1)
    #
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,162.72381,124.4359,34,-29.1363,1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,162.72381,124.4359,-64,-29.1363,1)
    #         enableCtrl=1
    #         dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #         dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,162.72381,124.4359,34,-29.1363,1)
    #         que_sts = dType.GetQueuedCmdCurrentIndex(api)
    #         chk = 0
    #         a = 1
    #         strt = time.time()
    #         while (chk == 0):
    #             strt = time.time()
    #             while (time.time() - strt < 4):
    #                 pass
    #             if (que_sts != dType.GetQueuedCmdCurrentIndex(api)):
    #                 que_sts = dType.GetQueuedCmdCurrentIndex(api)
    #             else:
    #                 break
    #         dType.DisconnectDobot(api)
    # def changesetting(opt):
    #     CON_STR = {
    #     dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    #     dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    #     dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}
    #     #Load Dll
    #     api = dType.load()
    #     #Connect Dobot
    #     state = dType.ConnectDobot(api, "", 115200)[0]
    #     print("Connect status:",CON_STR[state])
    #     if (state == dType.DobotConnect.DobotConnect_NoError):
    #         dType.SetPTPJointParams(api,200,200,200,200,200,200,200,200)
    #         dType.SetPTPCoordinateParams(api,200,200,200,200)
    #         dType.SetPTPJumpParams(api, 10, 200)
    #         dType.SetPTPCommonParams(api, 100, 100)
    #         enableCtrl=1
    #         if (opt==1):
    #
    #             #move knife 2
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 285.4430,93.1836,48.6680,92.1277, 1)
    #
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-12.1231,187.1717,35.6251,83.3647,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-12.1231,187.1717,-65.6251,83.3647,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-12.1231,187.1717,35.6251,83.3647,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,286.3798,122.3599,34.6310,83.3647,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,286.3798,122.3599,-64.6310,83.3647,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,286.3798,122.3599,34.6310,83.3647,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
    #             #move fork 2
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,127.7938,-244.6304,34.6886,-72.7589,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,127.7938,-244.6304,-65.6886,-72.7589,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,127.7938,-244.6304,34.6886,-72.7589,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,242.3140,-179.3222,34.4296,10.5278,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,242.3140,-179.3222,-64.4296,10.5278,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,242.3140,-179.3222,34.4296,10.5278,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
    #             #move plate
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,125.0959,-221.2122,34.7154,-64.8694,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,26.9190,-179.0504,39.8368,-125.5500,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,26.9190,-179.0504,-62.8368,-125.5500,1)
    #             enableCtrl=1
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,26.9190,-179.0504,39.8368,-125.5500,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,125.0959,-221.2122,34.7154,-125.5500,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,193.2952,-73.1423,31.9324,-125.5500,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,193.2952,-73.1423,-61.9324,-80.7089,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,193.2952,-73.1423,31.9324,-125.5500,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,204.6735,196.1538,51.0921,39.4247,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-16.5221,313.4125,39.8368,85.2441,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-16.5221,313.4125,-66.8368,85.2441,1)
    #             enableCtrl=1
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-16.5221,313.4125,39.8368,85.2441,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,309.6652,-65.9211,31.9324,85.2441,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,309.6652,-65.9211,-63.9324,85.2441,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,309.6652,-65.9211,31.9324,85.2441,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,186.8912,39.9336,-5.004,1.9758,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,159.3461,224.9547,35.0439,6.2754,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,159.3461,224.9547,-65.0439,6.2754,1)
    #             enableCtrl=1
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,159.3461,224.9547,45.0439,6.2754,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,315.7741,-35.6003,44.9324,-16.7736,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,315.7741,-35.6003,-63.9324,-16.7736,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,315.7741,-35.6003,31.9324,-16.7736,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,186.8912,39.9336,-5.004,1.9758,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,168.4479,-243.9648,35.0439,-14.3523,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,168.4479,-243.9648,-65.0439,-14.3523,1)
    #             enableCtrl=1
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,168.4479,-243.9648,35.0439,-14.3523,1)
    #
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,162.72381,124.4359,34,-29.1363,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,162.72381,124.4359,-64,-29.1363,1)
    #             enableCtrl=1
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,162.72381,124.4359,34,-29.1363,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
    #         elif(opt==2):
    #             #move plate
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,193.2952,-73.1423,31.9324,-125.5500,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,193.2952,-73.1423,-64.9324,-80.7089,1)
    #             enableCtrl=1
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,193.2952,-73.1423,31.9324,-125.5500,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,125.0959,-221.2122,34.7154,-125.5500,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,26.9190,-179.0504,39.8368,-125.5500,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,26.9190,-179.0504,-62.8368,-125.5500,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,26.9190,-179.0504,39.8368,-125.5500,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,125.0959,-221.2122,44.7154,-125.5500,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,315.7741,-35.6003,41.9324,-16.7736,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,315.7741,-35.6003,-63.9324,-16.7736,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,315.7741,-35.6003,64.9324,-16.7736,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,159.3461,224.9547,65.0439,6.2754,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,159.3461,224.9547,-65.0439,6.2754,1)
    #             enableCtrl=1
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,159.3461,224.9547,45.0439,6.2754,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,309.6652,-65.9211,31.9324,85.2441,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,309.6652,-65.9211,-63.9324,85.2441,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,309.6652,-65.9211,31.9324,85.2441,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,204.6735,196.1538,51.0921,39.4247,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-16.5221,313.4125,39.8368,85.2441,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-16.5221,313.4125,-66.8368,85.2441,1)
    #             enableCtrl=1
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-16.5221,313.4125,39.8368,85.2441,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,204.6735,196.1538,51.0921,39.4247,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,162.72381,124.4359,34,-29.1363,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,162.72381,124.4359,-64,-29.1363,1)
    #             enableCtrl=1
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,162.72381,124.4359,34,-29.1363,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,168.4479,-243.9648,35.0439,-14.3523,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,168.4479,-243.9648,-65.0439,-14.3523,1)
    #             enableCtrl=1
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,168.4479,-243.9648,35.0439,-14.3523,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
    #             #movefork
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,242.3140,-179.3222,34.4296,10.5278,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,242.3140,-179.3222,-64.4296,10.5278,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,242.3140,-179.3222,34.4296,10.5278,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,127.7938,-244.6304,34.6886,-72.7589,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,127.7938,-244.6304,-65.6886,-72.7589,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,127.7938,-244.6304,34.6886,-72.7589,1)
    #             #moveknife
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,286.3798,122.3599,34.6310,83.3647,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,286.3798,122.3599,-65.6310,83.3647,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  1, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,286.3798,122.3599,34.6310,83.3647,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 285.4430,93.1836,48.6680,92.1277, 1)
    #
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-12.1231,187.1717,35.6251,83.3647,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-12.1231,187.1717,-65.6251,83.3647,1)
    #             dType.SetEndEffectorSuctionCup(api, enableCtrl,  0, isQueued=1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,-12.1231,187.1717,35.6251,83.3647,1)
    #             dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,182.8912,39.9336,-5.004,1.9758,1)
    #         que_sts = dType.GetQueuedCmdCurrentIndex(api)
    #         chk = 0
    #         a = 1ד
    #         strt = time.time()
    #         while (chk == 0):
    #             strt = time.time()
    #             while (time.time() - strt < 4):
    #                 pass
    #             if (que_sts != dType.GetQueuedCmdCurrentIndex(api)):
    #                 que_sts = dType.GetQueuedCmdCurrentIndex(api)
    #             else:
    #                 break
    #         dType.DisconnectDobot(api)
    #
class blankscreen:
    def blnkscr():
        root=Toplevel()
        root.title('Table setting experiment')
        root.geometry('1920x1080')
        root.config(bg='azure')
        obj_green=greenfun
        obj_blue=bluefun
        obj_red=redfun
        green_low_polite=tk.Button(root,padx=1.0,pady=1.0,height=4,width=8,bg='aquamarine',text='ירוק',font=('times',32,'bold'),command=lambda :obj_green.Greenlevel(root))
        blue_medium_polite=tk.Button(root,height=4,width=8,bg='skyblue',text='כחול',font=('times',32,'bold'),command=lambda :obj_blue.Bluestart(root))
        red_medium_polite=tk.Button(root,height=4,width=8,bg='plum1',text='סגול',font=('times',32,'bold'),command=lambda :obj_red.redstart(root))
        green_low_polite.grid(row=500,column=3,padx=10,pady=10)
        blue_medium_polite.grid(row=500,column=5,padx=10,pady=10)
        red_medium_polite.grid(row=500,column=8,padx=10,pady=10)
        green_low_polite.place(relx=0.3,rely=0.5,anchor=CENTER)
        blue_medium_polite.place(relx=0.5,rely=0.5,anchor=CENTER)
        red_medium_polite.place(relx=0.7,rely=0.5,anchor=CENTER)        
        root.update()
        
        
        
class gui_main:
    
        
    def main():
        top = tk.Tk()
        top.title('Table setting experiment')
        top.geometry('1920x1080')
        top.config(bg='azure')
        obj=blankscreen
        obj_green=greenfun
        obj_blue=bluefun
        obj_red=redfun
        path='C:\Politeness\picture_hebrew\Blankscreen.png'
        img = ImageTk.PhotoImage(Image.open(path))
        msg=Label(top,image=img)
        msg.image=img
        msg.pack(side='right')
        obj.blnkscr()
        top.mainloop()
    if __name__== "__main__":
        main()
    







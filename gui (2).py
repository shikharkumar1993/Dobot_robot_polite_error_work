#!/usr/bin/python
# -*- coding: utf-8 -*-
import DobotDllType as dType
from tkinter import *
from tkinter import ttk
import sys
import time
import os
from threading import Thread, Lock
import math

'''dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 199, 0, 20, 1) #go home
dType.dSleep(3000)
dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 178, -134, -16, 1) #go home
dType.dSleep(3000)
enableCtrl = True
on = True
dType.SetEndEffectorSuctionCup(api, enableCtrl,  on, isQueued=0)
dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 199, 0, 20, 1) #go home
dType.dSleep(3000)
enableCtrl = False
dType.SetEndEffectorSuctionCup(api, enableCtrl,  on, isQueued=0)'''

objects = ["Yellow", "Red", "Blue", "Pink", "Green", "orange", "Purple"]
suc = False
counter = 0
move = False
num_suc = 0
start = False
finish = False
Yellow = True
lego = False
Task = True
cup = True
knife = True
spoon = True
answer = " "
flag = False

current_path = os.path.dirname(__file__)
print(current_path)



def time(lbl):
	string = strftime('%H:%M:%S %p')
	lbl.config(text=string)
	lbl.after(1000, time)


class MoveRobot:
	def move_robot(self):
		import time
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
			# Clean Command Queued
			dType.SetQueuedCmdClear(api)
			# Async Motion Params Setting
			#dType.SetHOMEParams(api, 250, 0, 50, 0, isQueued=1)
			#dType.SetPTPJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200, isQueued=1)
			#dType.SetPTPCommonParams(api, 100, 100, isQueued=1)
			# Async Home
			dType.SetHOMECmd(api, temp=0, isQueued=1)
			# Async PTP Motion
			dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, -29, -230, -11.5, -67, isQueued=1)
			#dType.SetWAITCmd(api, 1000, isQueued=1)

			enableCtrl = 1
			dType.SetEndEffectorSuctionCup(api, enableCtrl, 1, isQueued=1)
			dType.dSleep(3000)
			dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 150, -150, 55, -65, isQueued=1)
			dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 200, 0, 115, -46, isQueued=1)
			dType.dSleep(7000)
			#dType.SetWAITCmd(api, 1000, isQueued=1)
			dType.SetEndEffectorSuctionCup(api, enableCtrl, 0, isQueued=1)
			#dType.SetQueuedCmdStartExec(api)
			que_sts = dType.GetQueuedCmdCurrentIndex(api)
			chk = 0
			a = 1
			dType.dSleep(3000)
			dType.DisconnectDobot(api)
			'''strt = time.time()
				while (time.time() - strt < 2):
					pass
				if (que_sts != dType.GetQueuedCmdCurrentIndex(api)):
					que_sts = dType.GetQueuedCmdCurrentIndex(api)
				else:
					break
			dType.DisconnectDobot(api)'''


			'''dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 199, 0, 20, 1)  # go home
			dType.dSleep(3000)
			dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 178, -134, -16, 1)  # go home
			dType.dSleep(3000)
			enableCtrl = True
			on = True
			dType.SetEndEffectorSuctionCup(api, enableCtrl, on, isQueued=0)
			dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 199, 0, 20, 1)  # go home
			dType.dSleep(3000)
			enableCtrl = False
			dType.SetEndEffectorSuctionCup(api, enableCtrl, on, isQueued=0)'''

			'''for i in range(0, 5):
				if i % 2 == 0:
					offset = 50
				else:
					offset = -50
				lastIndex = \
				dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 200 + offset, offset, offset, offset, isQueued=1)[0]
			# Start to Execute Command Queued
			dType.SetQueuedCmdStartExec(api)
			# Wait for Executing Last Command
			while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
				dType.dSleep(100)
			# Stop to Execute Command Queued
			dType.SetQueuedCmdStopExec(api)'''

		# Disconnect Dobot
		dType.DisconnectDobot(api)



class MyApp(Tk):

	def __init__(self):
		global flag
		Tk.__init__(self)
		# rospy.Subscriber("robot_state", String, self.callback)
		container = ttk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		self.frames = {}
		for F in (OpenPage, YellowPage, TaskPage, StopPage):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky=NSEW)
		flag = True
		self.show_frame(OpenPage)

	def suction_response(self):
		print("i am suction")
		global suc
		global counter
		global move
		print(counter)
		if move and suc:
			objectName = objects[counter - 1]
			print("bring know", objectName)
			cur_str = objectName + "Page"
			print(cur_str)
			cur_str = MyApp.str_to_class(cur_str)
			self.show_frame(cur_str)

	# response for moving client
	def moving_response(self):
		print("i am moving")
		global move
		global counter
		global num_suc
		global suc
		global finish
		if num_suc == 5:  # fished to set all the object
			if not move and not suc:  # stop moving
				finish = True
				time.sleep(1)
				#self.show_frame(FinishPage)

	def show_frame(self, cont):
		global counter
		print(cont)
		global start
		frame = self.frames[cont]
		counter += 1
		print(counter)
		frame.tkraise()

	def starting(self):
		print("startinggg")
		#self.show_frame(StartPage)

	def stopping(self):
		global counter
		counter = -1
		print(counter)
		# dana-robot stop
		self.show_frame(StopPage)

	@staticmethod
	def str_to_class(str):
		return getattr(sys.modules[__name__], str)

	def choose_item(self, item):
		global answer
		global Yellow
		global Task
		global cup
		global knife
		global spoon
		answer = item
		if answer == "Yellow" and Yellow:
			plate = False
			cur_str = answer + "Page"
			print(cur_str)
			cur_str = MyApp.str_to_class(cur_str)
			self.show_frame(cur_str)

		elif answer == "Task" and Task:
			knife = False
			cur_str = answer + "Page"
			print(cur_str)
			cur_str = MyApp.str_to_class(cur_str)
			obj2 = MoveRobot
			self.show_frame(cur_str)
			obj2.move_robot(self)

		elif answer == "Cup" and cup:
			cup = False
			cur_str = answer + "Page"
			print(cur_str)
			cur_str = MyApp.str_to_class(cur_str)
			self.show_frame(cur_str)
		elif answer == "Spoon" and spoon:
			spoon = False
			cur_str = answer + "Page"
			print(cur_str)
			cur_str = MyApp.str_to_class(cur_str)
			self.show_frame(cur_str)
		elif answer == "Fork":
			fork = False
			cur_str = answer + "Page"
			print(cur_str)
			cur_str = MyApp.str_to_class(cur_str)
			self.show_frame(cur_str)


class OpenPage(ttk.Frame):
	def __init__(self, parent, controller):
		ttk.Frame.__init__(self, parent)
		self.make_widget(controller)

	def make_widget(self, controller):
		global move
		global start
		print("open page")
		main_label = ttk.Label(self, text='ברוכים הבאים לניסוי', font=("Arial Bold", 70))
		main_label.grid(row=0, column=10, padx=(100, 5), pady=(30, 30))
		photo = PhotoImage(file=current_path + "/dobot.png")
		photo = photo.subsample(2, 2)
		photolabel = Label(self, image=photo)
		photolabel.image = photo
		photolabel.grid(row=3, column=10, padx=(30, 10), pady=(10, 10))
		start_button = Button(self, text='התחל', fg="black", bg="light blue", font=('Arial bold', 20),
							  command=lambda: controller.choose_item("Task"))  # call the fun show_frame
		start_button.grid(row=5, column=10, padx=(30, 30), pady=(30, 30))


class StopPage(ttk.Frame):
	def __init__(self, parent, controller):
		ttk.Frame.__init__(self, parent)
		stop_main_label = Label(self, text='תעצבמ תכרעמה', font=("Arial Bold", 100))
		stop_main_label.grid(row=0, column=15, padx=(250, 5))
		stop_sub_label = Label(self, text='הריצע', fg="dark red", font=("Arial Bold", 150))
		stop_sub_label.grid(row=1, column=15, padx=(250, 5))
		stop_photo = PhotoImage(file=current_path + "/stopsign.png")
		stop_photo = stop_photo.subsample(1, 1)
		stopphotolabel = Label(self, image=stop_photo)
		stopphotolabel.image = stop_photo
		stopphotolabel.grid(row=3, column=15, padx=(250, 5), pady=(30, 30))


class YellowPage(ttk.Frame):
	def __init__(self, parent, controller):
		ttk.Frame.__init__(self, parent)
		main_label1 = Label(self, text=':ה תא תעכ איבמ', font=("Arial Bold", 70))
		main_label1.grid(row=0, column=7, padx=(250, 30))
		sub_label1 = Label(self, text='תחלצ', font=("Arial Bold", 120))
		sub_label1.grid(row=1, column=7, padx=(250, 20))
		sub_label2 = Label(self, text='תעכ איבי טובורהש תרחב התאש ילכה הז יכ', font=("Arial Bold", 50))
		sub_label2.grid(row=2, column=7, padx=(250, 20))
		photo1 = PhotoImage(file=current_path + "/color.png")
		photo1 = photo1.subsample(1, 1)
		photolabel = Label(self, image=photo1)
		photolabel.image = photo1
		photolabel.grid(row=4, column=7, padx=(250, 30), pady=(10, 10))
	# if num_suc==2:
	#	app.show_frame(ForkPage)

class TaskPage(ttk.Frame):

	def __init__(self, parent, controller):
		global answer
		global lego
		ttk.Frame.__init__(self, parent)
		print("2 answer", answer)
		main_label = Label(self, text=':הצורה אותה את/ה אמור/ה להרכיב', font=("Arial Bold", 40))  # name label
		main_label.grid(row=0, column=5, padx=(100, 100), pady=(30, 30))
		photo1 = PhotoImage(file=current_path + "/color.png")
		photo1 = photo1.subsample(1, 1)
		photolabel = Label(self, image=photo1)
		photolabel.image = photo1
		photolabel.grid(row=4, column=5, padx=(100, 100), pady=(30, 30))

		# Styling the label widget so that clock
		# will look more attractive
		'''root = Tk()
		root.title('Clock')
		lbl = Label(root, font=('calibri', 40, 'bold'),
					background='purple',
					foreground='white')

		# Placing clock at the centre
		# of the tkinter window
		lbl.pack(anchor='center')
		time(lbl)'''


# create instanse
app = MyApp()
app.title('setting a table Application')
# app.maxsize(1100, 1000)
app.geometry("1000x700")


def main():
	app.mainloop()


if __name__ == '__main__':
	main()
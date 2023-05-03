#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import pyperclip
from tkinter import filedialog
# from Commands import UnitCommand
from PCE_Dialog import PrintDialog,WhileDialog,DefDialog,ForDialog,WaitDialog,TemplateDialog,TemplatePositonDialog,LINEtextDialog,LINEimageDialog,CommentDialog,NewFileDialog
from logging import getLogger, DEBUG, NullHandler



class Pokecon_Code_Editor:
	def __init__(self, root,ser):
		self._logger = getLogger(__name__)
		self._logger.addHandler(NullHandler())
		self._logger.setLevel(DEBUG)
		self.root = root
		self.listener = None
		self.printD = None
		self.WhileD = None
		self.DefD = None 
		self.ForD = None 
		self.WaitD = None 
		self.TemplateD = None 
		self.TemplatePD = None
		self.LINEtextD = None
		self.LINEimageD = None
		self.CommentD = None 
		self.NewFileD = None 
		self.Default_Value = "0.1"
		# build ui
		self.Body = tk.Toplevel(root)
		self.Body.configure(height=900, width=1000)
		# self.Body.maxsize(900, 900)
		# self.Body.minsize(900, 900)
		self.Body.title("Pokecon_Code_Editor")


		# print(self.Body)

		self.Code_Frame = ttk.Labelframe(self.Body)
		self.Code_Frame.configure(text='Code', width=0)

		self.Text_Edit = tk.Text(self.Code_Frame)
		# self.Text_Edit.insert(tk.END, self.val)
		# self.Text_Edit.bind('<Button-Key-Tab>',self.KeyBind())
		self.Text_Edit.configure(height=10, width=50)
		self.Text_Edit.place(anchor="nw", relheight=0.97,relwidth=0.97, relx=0.01, rely=0.01, x=0, y=0)
# ===================================================================================================================== #
		self.Code_Frame.place(anchor="nw",relheight=0.78,relwidth=0.4,relx=0.01,rely=0.01,x=0,y=0)

		self.Setting_Frame = ttk.Labelframe(self.Body)
		self.Setting_Frame.configure(height=200, text='Setting', width=200)
		self.PY_While = ttk.Button(self.Setting_Frame)
		self.PY_While.configure(text='while',command=self.OpenWhileDialog)
		self.PY_While.place(anchor="nw",relheight=0.2,relwidth=0.2,relx=0.025,rely=0.1,x=0,y=0)

		self.PY_For = ttk.Button(self.Setting_Frame)
		self.PY_For.configure(text='for',command=self.OpenForDialog)
		self.PY_For.place(anchor="nw",relheight=0.2,relwidth=0.2,relx=0.275,rely=0.1,x=0,y=0)
		
		self.PY_IF = ttk.Button(self.Setting_Frame)
		self.PY_IF.configure(text='if', state="disabled")
		self.PY_IF.place(anchor="nw",relheight=0.2,relwidth=0.2,relx=0.525,rely=0.1,x=0,y=0)
		
		self.PY_def = ttk.Button(self.Setting_Frame)
		self.PY_def.configure(text='def',command=self.OpenDefDialog)
		self.PY_def.place(anchor="nw",relheight=0.2,relwidth=0.2,relx=0.775,rely=0.1,x=0,y=0)

		self.PY_Print = ttk.Button(self.Setting_Frame)
		self.PY_Print.configure(text='print',command=self.OpenPrintDialog)
		
		self.PY_Print.place(anchor="nw",relheight=0.2,relwidth=0.2,relx=0.025,rely=0.4,x=0,y=0)

		self.PY_Template = ttk.Button(self.Setting_Frame)
		self.PY_Template.configure(text='画像認識',command=self.OpenTemplateDialog)
		self.PY_Template.place(anchor="nw",relheight=0.2,relwidth=0.2,relx=0.275,rely=0.4,x=0,y=0)

		self.PY_LINE_txt = ttk.Button(self.Setting_Frame)
		self.PY_LINE_txt.configure(text='LINE_text',command=self.OpenLINEtextDialog)
		self.PY_LINE_txt.place(anchor="nw",relheight=0.2,relwidth=0.2,relx=0.525,rely=0.4,x=0,y=0)

		self.PY_LINE_Image = ttk.Button(self.Setting_Frame)
		self.PY_LINE_Image.configure(text='LINE_image',command=self.OpenLINEimageDialog)
		self.PY_LINE_Image.place(anchor="nw",relheight=0.2,relwidth=0.2,relx=0.775,rely=0.4,x=0,y=0)
		
		self.PY_Wait = ttk.Button(self.Setting_Frame)
		self.PY_Wait.configure(text='wait',command=self.OpenWaitDialog)
		self.PY_Wait.place(anchor="nw",relheight=0.2,relwidth=0.2,relx=0.025,rely=0.7,x=0,y=0)

		self.PY_saveCapture = ttk.Button(self.Setting_Frame)
		self.PY_saveCapture.configure(text='saveCapture', command=self.saveCapture_Button)
		self.PY_saveCapture.place(anchor="nw", relheight=0.2,relwidth=0.2, relx=0.275, rely=0.7, x=0, y=0)

		self.PY_IFAlive = ttk.Button(self.Setting_Frame)
		self.PY_IFAlive.configure(text='checkIfAlive',command=self.checkIfAlive_Button)
		self.PY_IFAlive.place(anchor="nw",relheight=0.2,relwidth=0.2,relx=0.525,rely=0.7,x=0,y=0)

		self.PY_Finish = ttk.Button(self.Setting_Frame)
		self.PY_Finish.configure(text='Finish',command=self.Finish_Button)
		self.PY_Finish.place(anchor="nw",relheight=0.2,relwidth=0.2,relx=0.775,rely=0.7,x=0,y=0)

		self.PY_Label_For = ttk.Label(self.Setting_Frame)
		self.PY_Label_For.configure(text='繰り返し回数指定あり')
		self.PY_Label_For.place(anchor="nw",relwidth=0.25,relx=0.275,x=0,y=0)

		self.PY_Label_IF = ttk.Label(self.Setting_Frame)
		self.PY_Label_IF.configure(anchor="center", text='条件分岐')
		self.PY_Label_IF.place(anchor="nw", relwidth=0.2, relx=0.525, x=0, y=0)

		self.PY_Label_Def = ttk.Label(self.Setting_Frame)
		self.PY_Label_Def.configure(anchor="center", text='関数作成')
		self.PY_Label_Def.place(anchor="nw",relwidth=0.2,relx=0.775,x=0,y=0)

		self.PY_Label_While = ttk.Label(self.Setting_Frame)
		self.PY_Label_While.configure(anchor="center", text='繰り返し回数指定なし')
		self.PY_Label_While.place(anchor="nw", relwidth=0.25, relx=0.025, x=0, y=0)


		self.Setting_Frame.place(anchor="nw",relheight=0.25,relwidth=0.57,relx=0.42,rely=0.01,x=0,y=0)
		# ===================================================================================================================== #

		
		self.Controller_Frame = ttk.Labelframe(self.Body)
		self.Controller_Frame.configure(height=200, text='Controller', width=200)

		# self.Check_Text = ttk.Checkbutton(self.Controller_Frame)
		# self.Check_Text.configure(text='Text')
		# self.Check_Text.place(anchor="nw",relheight=0.075,relwidth=0.2,relx=0.1,x=0,y=0)

		# self.Check_Repeat = ttk.Checkbutton(self.Controller_Frame)
		# self.Check_Repeat.configure(text='Repeat')
		# self.Check_Repeat.place(anchor="nw",relheight=0.075,relwidth=0.2,relx=0.3,x=0,y=0)

		# self.Check_Hold = ttk.Checkbutton(self.Controller_Frame)
		# self.Check_Hold.configure(text='Hold')
		# self.Check_Hold.place(anchor="nw",relheight=0.075,relwidth=0.2,relx=0.5,x=0,y=0)

		self.Check_Controller = ttk.Checkbutton(self.Controller_Frame)
		self.Check_Controller_value = tk.BooleanVar(value=True)
		self.Check_Controller.configure(variable=self.Check_Controller_value,text='Controller')
		self.Check_Controller.place(anchor="nw",relheight=0.075,relwidth=0.2,relx=0.7,x=0,y=0)

		self.Button_ZL = ttk.Button(self.Controller_Frame)
		self.Button_ZL.configure(text='ZL',command=self.PressButton_ZL)
		self.Button_ZL.place(anchor="nw",relheight=0.075,relwidth=0.1,relx=0.05,rely=0.1,x=0,y=0)

		self.Button_L = ttk.Button(self.Controller_Frame)
		self.Button_L.configure(text='L', command=self.PressButton_L)
		self.Button_L.place(anchor="nw",relheight=0.075,relwidth=0.1,relx=0.15,rely=0.1,x=0,y=0)

		self.Button_MINUS = ttk.Button(self.Controller_Frame)
		self.Button_MINUS.configure(text='-', command=self.PressButton_MINUS)
		self.Button_MINUS.place(anchor="nw",relheight=0.075,relwidth=0.1,relx=0.35,rely=0.1,x=0,y=0)

		self.Button_PLUS = ttk.Button(self.Controller_Frame)
		self.Button_PLUS.configure(text='+',command=self.PressButton_PLUS)
		self.Button_PLUS.place(anchor="nw",relheight=0.075,relwidth=0.1,relx=0.55,rely=0.1,x=0,y=0)

		self.Button_R = ttk.Button(self.Controller_Frame)
		self.Button_R.configure(text='R', command=self.PressButton_R)
		self.Button_R.place(anchor="nw",relheight=0.075,relwidth=0.1,relx=0.75,rely=0.1,x=0,y=0)

		self.Button_ZR = ttk.Button(self.Controller_Frame)
		self.Button_ZR.configure(text='ZR', command=self.PressButton_ZR)
		self.Button_ZR.place(anchor="nw",relheight=0.075,relwidth=0.1,relx=0.85,rely=0.1,x=0,y=0)

		self.LEFT_Stick_UP_LEFT = ttk.Button(self.Controller_Frame)
		self.LEFT_Stick_UP_LEFT.configure(text='↖',command=self.PressDirection_LS_UL)
		self.LEFT_Stick_UP_LEFT.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.1,rely=0.2,x=0,y=0)

		self.LEFT_Stick_UP = ttk.Button(self.Controller_Frame)
		self.LEFT_Stick_UP.configure(text='↑', command=self.PressDirection_LS_U)
		self.LEFT_Stick_UP.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.2,rely=0.2,x=0,y=0)

		self.LEFT_Stick_UP_RIGHT = ttk.Button(self.Controller_Frame)
		self.LEFT_Stick_UP_RIGHT.configure(text='↗', command=self.PressDirection_LS_UR)
		self.LEFT_Stick_UP_RIGHT.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.3,rely=0.2,x=0,y=0)

		self.LEFT_Stick_LEFT = ttk.Button(self.Controller_Frame)
		self.LEFT_Stick_LEFT.configure(text='←', command=self.PressDirection_LS_L)
		self.LEFT_Stick_LEFT.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.1,rely=0.3,x=0,y=0)

		self.LEFT_Stick_L3 = ttk.Button(self.Controller_Frame)
		self.LEFT_Stick_L3.configure(text='■', command=self.PressButton_LCLICK)
		self.LEFT_Stick_L3.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.2,rely=0.3,x=0,y=0)

		self.LEFT_Stick_RIGHT = ttk.Button(self.Controller_Frame)
		self.LEFT_Stick_RIGHT.configure(text='→', command=self.PressDirection_LS_R)
		self.LEFT_Stick_RIGHT.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.3,rely=0.3,x=0,y=0)

		self.LEFT_Stick_DOWN_LEFT = ttk.Button(self.Controller_Frame)
		self.LEFT_Stick_DOWN_LEFT.configure(text='↙', command=self.PressDirection_LS_DL)
		self.LEFT_Stick_DOWN_LEFT.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.1,rely=0.4,x=0,y=0)

		self.LEFT_Stick_DOWN = ttk.Button(self.Controller_Frame)
		self.LEFT_Stick_DOWN.configure(text='↓',  command=self.PressDirection_LS_D)
		self.LEFT_Stick_DOWN.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.2,rely=0.4,x=0,y=0)

		self.LEFT_Stick_DOWN_RIGHT = ttk.Button(self.Controller_Frame)
		self.LEFT_Stick_DOWN_RIGHT.configure(text='↘', command=self.PressDirection_LS_DR)
		self.LEFT_Stick_DOWN_RIGHT.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.3,rely=0.4,x=0,y=0)

		self.Button_X = ttk.Button(self.Controller_Frame)
		self.Button_X.configure(text='X', command=self.PressButton_X)
		self.Button_X.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.7,rely=0.2,x=0,y=0)

		self.Button_Y = ttk.Button(self.Controller_Frame)
		self.Button_Y.configure(text='Y', command=self.PressButton_Y)
		self.Button_Y.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.6,rely=0.3,x=0,y=0)

		self.Button_A = ttk.Button(self.Controller_Frame)
		self.Button_A.configure(text='A', command=self.PressButton_A)
		self.Button_A.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.8,rely=0.3,x=0,y=0)

		self.Button_B = ttk.Button(self.Controller_Frame)
		self.Button_B.configure(text='B', command=self.PressButton_B)
		self.Button_B.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.7,rely=0.4,x=0,y=0)

		self.Button_Hat_LEFT_TOP = ttk.Button(self.Controller_Frame)
		self.Button_Hat_LEFT_TOP.configure(text='↖',command=self.PressHat_TL)
		self.Button_Hat_LEFT_TOP.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.1,rely=0.6,x=0,y=0)

		self.Button_Hat_TOP = ttk.Button(self.Controller_Frame)
		self.Button_Hat_TOP.configure(text='↑', command=self.PressHat_T)
		self.Button_Hat_TOP.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.2,rely=0.6,x=0,y=0)

		self.Button_Hat_RIGHT_TOP = ttk.Button(self.Controller_Frame)
		self.Button_Hat_RIGHT_TOP.configure(text='↗', command=self.PressHat_TR)
		self.Button_Hat_RIGHT_TOP.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.3,rely=0.6,x=0,y=0)

		self.Button_Hat_LEFT = ttk.Button(self.Controller_Frame)
		self.Button_Hat_LEFT.configure(text='←', command=self.PressHat_L)
		self.Button_Hat_LEFT.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.1,rely=0.7,x=0,y=0)

		self.Button_Hat_RIGHT = ttk.Button(self.Controller_Frame)
		self.Button_Hat_RIGHT.configure(text='→', command=self.PressHat_R)
		self.Button_Hat_RIGHT.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.3,rely=0.7,x=0,y=0)

		self.Button_Hat_BTM_LEFT = ttk.Button(self.Controller_Frame)
		self.Button_Hat_BTM_LEFT.configure(text='↙', command=self.PressHat_BL)
		self.Button_Hat_BTM_LEFT.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.1,rely=0.8,x=0,y=0)

		self.Button_Hat_BTM = ttk.Button(self.Controller_Frame)
		self.Button_Hat_BTM.configure(text='↓', command=self.PressHat_B)
		self.Button_Hat_BTM.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.2,rely=0.8,x=0,y=0)

		self.Button_Hat_BTM_RIGHT = ttk.Button(self.Controller_Frame)
		self.Button_Hat_BTM_RIGHT.configure(text='↘', command=self.PressHat_BR)
		self.Button_Hat_BTM_RIGHT.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.3,rely=0.8,x=0,y=0)

		self.RIGHT_Stick_UP_LEFT = ttk.Button(self.Controller_Frame)
		self.RIGHT_Stick_UP_LEFT.configure(text='↖',command=self.PressDirection_RS_UL)
		self.RIGHT_Stick_UP_LEFT.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.6,rely=0.6,x=0,y=0)

		self.RIGHT_Stick_UP = ttk.Button(self.Controller_Frame)
		self.RIGHT_Stick_UP.configure(text='↑', command=self.PressDirection_RS_U)
		self.RIGHT_Stick_UP.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.7,rely=0.6,x=0,y=0)

		self.RIGHT_Stick_UP_RIGHT = ttk.Button(self.Controller_Frame)
		self.RIGHT_Stick_UP_RIGHT.configure(text='↗', command=self.PressDirection_RS_UR)
		self.RIGHT_Stick_UP_RIGHT.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.8,rely=0.6,x=0,y=0)

		self.RIGHT_Stick_LEFT = ttk.Button(self.Controller_Frame)
		self.RIGHT_Stick_LEFT.configure(text='←', command=self.PressDirection_RS_L)
		self.RIGHT_Stick_LEFT.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.6,rely=0.7,x=0,y=0)

		self.RIGHT_Stick_R3 = ttk.Button(self.Controller_Frame)
		self.RIGHT_Stick_R3.configure(text='■', command=self.PressButton_RCLICK)
		self.RIGHT_Stick_R3.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.7,rely=0.7,x=0,y=0)

		self.RIGHT_Stick_RIGHT = ttk.Button(self.Controller_Frame)
		self.RIGHT_Stick_RIGHT.configure(text='→', command=self.PressDirection_RS_R)
		self.RIGHT_Stick_RIGHT.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.8,rely=0.7,x=0,y=0)

		self.RIGHT_Stick_DOWN_LEFT = ttk.Button(self.Controller_Frame)
		self.RIGHT_Stick_DOWN_LEFT.configure(text='↙', command=self.PressDirection_RS_DL)
		self.RIGHT_Stick_DOWN_LEFT.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.6,rely=0.8,x=0,y=0)

		self.RIGHT_Stick_DOWN = ttk.Button(self.Controller_Frame)
		self.RIGHT_Stick_DOWN.configure(text='↓', command=self.PressDirection_RS_D)
		self.RIGHT_Stick_DOWN.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.7,rely=0.8,x=0,y=0)

		self.RIGHT_Stick_DOWN_RIGHT = ttk.Button(self.Controller_Frame)
		self.RIGHT_Stick_DOWN_RIGHT.configure(text='↘', command=self.PressDirection_RS_DR)
		self.RIGHT_Stick_DOWN_RIGHT.place(anchor="nw",relheight=0.075,relwidth=0.075,relx=0.8,rely=0.8,x=0,y=0)

		self.Button_CAPTURE = ttk.Button(self.Controller_Frame)
		self.Button_CAPTURE.configure(text='CAP', command=self.PressButton_CAPTURE)
		self.Button_CAPTURE.place(anchor="nw",relheight=0.075,relwidth=0.1,relx=0.35,rely=0.9,x=0,y=0)

		self.Button_HOME = ttk.Button(self.Controller_Frame)
		self.Button_HOME.configure(text='HOME', command=self.PressButton_HOME)
		self.Button_HOME.place(anchor="nw",relheight=0.075,relwidth=0.1,relx=0.55,rely=0.9,x=0,y=0)

		

		# ===================================================================================================================== #

		self.Controller_Frame.place(anchor="nw",relheight=0.5175,relwidth=0.57,relx=0.42,rely=0.271,x=0,y=0)

		self.ETC_Frame = ttk.Labelframe(self.Body)
		self.ETC_Frame.configure(height=200, text='etc', width=200)
		# self.ETC_Label_Threshold = ttk.Label(self.ETC_Frame)
		# self.ETC_Label_Threshold.configure(anchor="center", text='threshold')
		# self.ETC_Label_Threshold.place(relheight=0.2, relwidth=0.1, rely=0.0, x=0, y=0)

		# self.ETC_Label_show_gray = ttk.Label(self.ETC_Frame)
		# self.ETC_Label_show_gray.configure(anchor="center", text='show_gray')
		# self.ETC_Label_show_gray.place(relheight=0.2, relwidth=0.1, rely=0.25, x=0, y=0)

		# self.ETC_Label_Position = ttk.Label(self.ETC_Frame)
		# self.ETC_Label_Position.configure(anchor="center", text='position')
		# self.ETC_Label_Position.place(relheight=0.2, relwidth=0.1, rely=0.5, x=0, y=0)

		# self.ETC_Label_KeyBoard = ttk.Label(self.ETC_Frame)
		# self.ETC_Label_KeyBoard.configure(anchor="center", text='KeyBoard')
		# self.ETC_Label_KeyBoard.place(relheight=0.2, relwidth=0.1, rely=0.75, x=0, y=0)

		self.ETC_Label_Duration = ttk.Label(self.ETC_Frame)
		self.ETC_Label_Duration.configure(anchor="center", text='duration')
		self.ETC_Label_Duration.place(relheight=0.2,relwidth=0.1,relx=0.15,rely=0.0,x=0,y=0)

		# self.ETC_Label_Repeat = ttk.Label(self.ETC_Frame)
		# self.ETC_Label_Repeat.configure(anchor="center", text='repeat')
		# self.ETC_Label_Repeat.place(relheight=0.2,relwidth=0.1,relx=0.15,rely=0.25,x=0,y=0)

		self.ETC_Label_Wait = ttk.Label(self.ETC_Frame)
		self.ETC_Label_Wait.configure(anchor="center", text='wait')
		self.ETC_Label_Wait.place(relheight=0.2,relwidth=0.1,relx=0.15,rely=0.5,x=0,y=0)

		# self.ETC_Label_Print = ttk.Label(self.ETC_Frame)
		# self.ETC_Label_Print.configure(anchor="center", text='print')
		# self.ETC_Label_Print.place(relheight=0.2,relwidth=0.05,relx=0.3,rely=0.0,x=0,y=0)

		# self.ETC_Label_X1 = ttk.Label(self.ETC_Frame)
		# self.ETC_Label_X1.configure(anchor="center", text='x1')
		# self.ETC_Label_X1.place(relheight=0.2,relwidth=0.025,relx=0.5,rely=0.0,x=0,y=0)

		# self.ETC_Label_X2 = ttk.Label(self.ETC_Frame)
		# self.ETC_Label_X2.configure(anchor="center", text='x2')
		# self.ETC_Label_X2.place(relheight=0.2,relwidth=0.025,relx=0.5,rely=0.25,x=0,y=0)

		# self.ETC_Label_Y1 = ttk.Label(self.ETC_Frame)
		# self.ETC_Label_Y1.configure(anchor="center", text='y1')
		# self.ETC_Label_Y1.place(relheight=0.2,relwidth=0.025,relx=0.5,rely=0.5,x=0,y=0)

		# self.ETC_Label_Y2 = ttk.Label(self.ETC_Frame)
		# self.ETC_Label_Y2.configure(anchor="center", text='y2')
		# self.ETC_Label_Y2.place(relheight=0.2,relwidth=0.025,relx=0.5,rely=0.75,x=0,y=0)

		# self.ETC_Entry_Threshold = ttk.Entry(self.ETC_Frame)
		# self.ETC_Entry_Threshold.configure(justify="center")
		# self.ETC_Entry_Threshold.place(anchor="nw",relheight=0.2,relwidth=0.05,relx=0.1,rely=0.0,x=0,y=0)

		# self.ETC_Check_Show_Gray = ttk.Checkbutton(self.ETC_Frame)
		# self.ETC_Check_Show_Gray.place(anchor="nw",relheight=0.2,relwidth=0.05,relx=0.1,rely=0.25,x=0,y=0)

		# self.ETC_Check_Postion = ttk.Checkbutton(self.ETC_Frame)
		# self.ETC_Check_Postion.place(anchor="nw",relheight=0.2,relwidth=0.05,relx=0.1,rely=0.5,x=0,y=0)

		# self.ETC_Button_PushOnce = ttk.Button(self.ETC_Frame)
		# self.ETC_Button_PushOnce.configure(text='初めに一回')
		# self.ETC_Button_PushOnce.place(anchor="nw",relheight=0.2,relwidth=0.1,relx=0.1,rely=0.75,x=0,y=0)

		# self.ETC_Button_KeyBoard_Input = ttk.Button(self.ETC_Frame)
		# self.ETC_Button_KeyBoard_Input.configure(text='入力')
		# self.ETC_Button_KeyBoard_Input.place(anchor="nw",relheight=0.2,relwidth=0.05,relx=0.2,rely=0.75,x=0,y=0)

		self.ETC_Entry_Duration = ttk.Entry(self.ETC_Frame)
		self.ETC_Entry_Duration_value = tk.StringVar()
		self.ETC_Entry_Duration.configure(justify="center",textvariable=self.ETC_Entry_Duration_value)
		self.ETC_Entry_Duration.delete("0", "end")
		self.ETC_Entry_Duration.insert(tk.END, "0.1")	
		self.ETC_Entry_Duration.place(anchor="nw",relheight=0.2,relwidth=0.05,relx=0.25,rely=0.0,x=0,y=0)

		# self.ETC_Entry_Repeat = ttk.Entry(self.ETC_Frame)
		# self.ETC_Entry_Repeat.configure(justify="center")
		# self.ETC_Entry_Repeat.place(anchor="nw",relheight=0.2,relwidth=0.05,relx=0.25,rely=0.25,x=0,y=0)

		self.ETC_Entry_Wait = ttk.Entry(self.ETC_Frame)
		self.ETC_Entry_Wait_value = tk.StringVar()
		self.ETC_Entry_Wait.configure(justify="center",textvariable=self.ETC_Entry_Wait_value)
		self.ETC_Entry_Wait.delete("0", "end")
		self.ETC_Entry_Wait.insert(tk.END, "0.1")
		self.ETC_Entry_Wait.place(anchor="nw",relheight=0.2,relwidth=0.05,relx=0.25,rely=0.5,x=0,y=0)

		# self.ETC_Entry_KeyBoard = ttk.Entry(self.ETC_Frame)
		# self.ETC_Entry_KeyBoard.configure(justify="center")
		# self.ETC_Entry_KeyBoard.place(anchor="nw",relheight=0.2,relwidth=0.25,relx=0.25,rely=0.75,x=0,y=0)

		# self.ETC_Entry_Print = ttk.Entry(self.ETC_Frame)
		# self.ETC_Entry_Print.configure(justify="center")
		# self.ETC_Entry_Print.place(anchor="nw",relheight=0.2,relwidth=0.15,relx=0.35,rely=0.0,x=0,y=0)

		# self.ETC_Button_Print_Input = ttk.Button(self.ETC_Frame)
		# self.ETC_Button_Print_Input.configure(text='入力')
		# self.ETC_Button_Print_Input.place(anchor="nw",relheight=0.2,relwidth=0.2,relx=0.3,rely=0.25,x=0,y=0)

		# self.ETC_Entry_X1 = ttk.Entry(self.ETC_Frame)
		# self.ETC_Entry_X1.configure(justify="center")
		# self.ETC_Entry_X1.place(anchor="nw",relheight=0.2,relwidth=0.05,relx=0.525,rely=0.0,x=0,y=0)

		# self.ETC_Entry_X2 = ttk.Entry(self.ETC_Frame)
		# self.ETC_Entry_X2.configure(justify="center")
		# self.ETC_Entry_X2.place(anchor="nw",relheight=0.2,relwidth=0.05,relx=0.525,rely=0.25,x=0,y=0)

		# self.ETC_Entry_Y1 = ttk.Entry(self.ETC_Frame)
		# self.ETC_Entry_Y1.configure(justify="center")
		# self.ETC_Entry_Y1.place(anchor="nw",relheight=0.2,relwidth=0.05,relx=0.525,rely=0.5,x=0,y=0)

		# self.ETC_Entry_Y2 = ttk.Entry(self.ETC_Frame)
		# self.ETC_Entry_Y2.configure(justify="center")
		# self.ETC_Entry_Y2.place(anchor="nw",relheight=0.2,relwidth=0.05,relx=0.525,rely=0.75,x=0,y=0)

		self.ETC_Button_CommentOut_Value = ttk.Button(self.ETC_Frame)
		self.ETC_Button_CommentOut_Value.configure(text='コメント', command=self.OpenCommentOutPDialog)
		self.ETC_Button_CommentOut_Value.place(anchor="nw", relheight=0.5, relx=0.5, rely=0.0, x=0, y=0.5)

		self.ETC_Button_Format_Value = ttk.Button(self.ETC_Frame)
		self.ETC_Button_Format_Value.configure(text='format',command=self.Text_Format)
		self.ETC_Button_Format_Value.place(anchor="nw", relheight=0.5, relx=0.5, rely=0.5, x=0, y=0.5)

		self.ETC_Button_Template_Value = ttk.Button(self.ETC_Frame)
		self.ETC_Button_Template_Value.configure(text='座標指定\n＆\n画像認識',command=self.OpenTemplatePDialog)
		self.ETC_Button_Template_Value.place(anchor="nw", relheight=1.0, relx=0.6, rely=0.0, x=0, y=0)

		self.ETC_Button_Edit_PNG = ttk.Button(self.ETC_Frame)
		self.ETC_Button_Edit_PNG.configure(state="disabled", text='画像編集\n（未実装）')
		self.ETC_Button_Edit_PNG.place(anchor="nw", relheight=1, relx=0.7, rely=0.0, x=0, y=0)

		self.ETC_Button_OCR = ttk.Button(self.ETC_Frame)
		self.ETC_Button_OCR.configure(state="disabled", text='文字認識\n（未実装）')
		self.ETC_Button_OCR.place(anchor="nw",relheight=1,relx=0.8,rely=0,x=0,y=0)

		self.ETC_Button_NewFile = ttk.Button(self.ETC_Frame)
		self.ETC_Button_NewFile.configure(text='新規作成', command=self.OpenNeFileDialog)
		self.ETC_Button_NewFile.place(anchor="nw",relheight=0.25,relx=0.9,rely=0.0,x=0,y=0)

		self.ETC_Button_OpenFile = ttk.Button(self.ETC_Frame)
		self.ETC_Button_OpenFile.configure(text='開く',command=self.OpenFile_Button)
		self.ETC_Button_OpenFile.place(anchor="nw", relheight=0.25, relx=0.9, rely=0.25, x=0, y=0)

		self.ETC_Button_SaveFile = ttk.Button(self.ETC_Frame)
		self.ETC_Button_SaveFile.configure(text='保存', state="disabled")
		self.ETC_Button_SaveFile.place(anchor="nw", relheight=0.25, relx=0.9, rely=0.5, x=0, y=0)

		self.ETC_Button_NewFileSave = ttk.Button(self.ETC_Frame)
		self.ETC_Button_NewFileSave.configure(text='新規保存',command=self.SaveFile_Button)
		self.ETC_Button_NewFileSave.place(anchor="nw", relheight=0.25, relx=0.9, rely=0.75, x=0, y=0)

		# self.ETC_Button_Finish = ttk.Button(self.ETC_Frame)
		# self.ETC_Button_Finish.configure(
		# 	text='終了', command=menu.closingCodeDesigner)
		# self.ETC_Button_Finish.place(anchor="nw", relheight=1, relx=0.9, rely=0.0, x=0, y=0)

		self.ETC_Frame.place(anchor="nw",relheight=0.2,relwidth=0.98,relx=0.01,rely=0.79,x=0,y=0)
		# ===================================================================================================================== #

		self.Body.grid_propagate(0)

		# Main widget
		self.mainwindow = self.Body




	def bind(self, event, func):
		self.mainwindow.bind(event, func)

	def KeyBind(self,event,func):
		print("    ")

	def protocol(self, event, func):
		self.mainwindow.protocol(event, func)

	def focus_force(self):
		self.mainwindow.focus_force()

	def destroy(self):
		self.mainwindow.destroy()

	def ValueGet(self):
		self.ETC_Entry_Duration_value2 = self.ETC_Entry_Duration_value.get()
		self.ETC_Entry_Wait_value2 = self.ETC_Entry_Wait_value.get()


	def Clip_BoardPaste(self):
		self.val = pyperclip.paste()
		print(self.val)
		self.Text_Edit.insert(tk.INSERT,self.val)
		pyperclip.copy("")

	def saveCapture_Button(self):
		self.val = ('self.saveCapture("")\n')
		self.Text_Edit.insert(tk.INSERT, self.val)

	def checkIfAlive_Button(self):
		self.val = ("self.checkIfAlive():\n")
		self.Text_Edit.insert(tk.INSERT, self.val)
		
	def Finish_Button(self):
		self.val = ("self.finish():\n")
		self.Text_Edit.insert(tk.INSERT, self.val)


	# 将来的に別ファイルに分けたい。
	# PressButtonの所だけ。

	# self.Check_ControllerがTrueの時の動作も追加したい。

	def PressButton_A(self):
		# self.Check_Controller_value = self.Check_Controller_value.get()
		# if self.Check_Controller_value == True:
		# 	UnitCommand.A().start(ser)
		self.ValueGet()
		self.val = (f"        self.press(Button.A,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressButton_B(self):
		self.ValueGet()
		self.val = (f"        self.press(Button.B,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressButton_X(self):
			self.ETC_Entry_Duration_value2 = self.ETC_Entry_Duration_value.get()
			self.ETC_Entry_Wait_value2 = self.ETC_Entry_Wait_value.get()
			self.val = (f"        self.press(Button.X,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
			self.Text_Edit.insert(tk.INSERT, self.val)
		
	def PressButton_Y(self):
		self.ValueGet()
		self.val = (f"        self.press(Button.Y,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressButton_L(self):
		self.ValueGet()
		self.val = (f"        self.press(Button.L,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressButton_ZL(self):
		self.ValueGet()
		self.val = (f"        self.press(Button.ZL,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)
	
	def PressButton_R(self):
		self.ValueGet()
		self.val = (f"        self.press(Button.R,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressButton_ZR(self):
		self.ValueGet()
		self.val = (f"        self.press(Button.ZR,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressButton_PLUS(self):
		self.ValueGet()
		self.val = (f"        self.press(Button.PLUS,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)
	
	def PressButton_MINUS(self):
		self.ValueGet()
		self.val = (f"        self.press(Button.MINUS,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressButton_CAPTURE(self):
		self.ValueGet()
		self.val = (f"        self.press(Button.CAPTURE,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressButton_HOME(self):
		self.ValueGet()
		self.val = (f"        self.press(Button.HOME,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressButton_LCLICK(self):
		self.ValueGet()
		self.val = (f"        self.press(Button.LCLICK,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressButton_RCLICK(self):
		self.ValueGet()
		self.val = (
					f"        self.press(Button.RCLICK,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressDirection_LS_UL(self):
		self.ValueGet()
		self.val = (
					f"        self.press(Direction.L_UP_LEFT,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)
	
	def PressDirection_LS_U(self):
		self.ValueGet()
		self.val = (
					f"        self.press(Direction.L_UP,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressDirection_LS_UR(self):
		self.ValueGet()
		self.val = (
					f"        self.press(Direction.L_UP_RIGHT,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressDirection_LS_L(self):
		self.ValueGet()
		self.val = (
					f"        self.press(Direction.L_LEFT,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressDirection_LS_R(self):
		self.ValueGet()
		self.val = (
					f"        self.press(Direction.L_RIGHT,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressDirection_LS_DL(self):
		self.ValueGet()
		self.val = (f"        self.press(Direction.L_DOWN_LEFT,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)
	
	def PressDirection_LS_D(self):
		self.ValueGet()
		self.val = (f"        self.press(Direction.L_DOWN,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressDirection_LS_DR(self):
		self.ValueGet()
		self.val = (
					f"        self.press(Direction.L_DOWN_RIGHT,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressHat_TL(self):
		self.ValueGet()
		self.val = (
					f"        self.press(Hat.TOP_LEFT,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressHat_T(self):
		self.ValueGet()
		self.val = (
					f"        self.press(Hat.TOP,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressHat_TR(self):
		self.ValueGet()
		self.val = (
					f"        self.press(Hat.TOP_RIGHT,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressHat_L(self):
		self.ValueGet()
		self.val = (
					f"        self.press(Hat.LEFT,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressHat_R(self):
		self.ValueGet()
		self.val = (
					f"        self.press(Hat.RIGHT,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)
	
	def PressHat_BL(self):
		self.ValueGet()
		self.val = (f"        self.press(Hat.BTM_LEFT,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressHat_B(self):
		self.ValueGet()
		self.val = (f"        self.press(Hat.BTM,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressHat_BR(self):
		self.ValueGet()
		self.val = (f"        self.press(Hat.BTM_RIGHT,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressDirection_RS_UL(self):
		self.ValueGet()
		self.val = (f"        self.press(Direction.R_UP_LEFT,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressDirection_RS_U(self):
		self.ValueGet()
		self.val = (f"        self.press(Direction.R_UP,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressDirection_RS_UR(self):
		self.ValueGet()
		self.val = (f"        self.press(Direction.R_UP_RIGHT,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressDirection_RS_L(self):
		self.ValueGet()
		self.val = (f"        self.press(Direction.R_LEFT,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressDirection_RS_R(self):
		self.ValueGet()
		self.val = (f"        self.press(Direction.R_RIGHT,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressDirection_RS_DL(self):
		self.ValueGet()
		self.val = (f"        self.press(Direction.R_DOWN_LEFT,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressDirection_RS_D(self):
		self.ValueGet()
		self.val = (f"        self.press(Direction.R_DOWN,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)

	def PressDirection_RS_DR(self):
		self.ValueGet()
		self.val = (f"        self.press(Direction.R_DOWN_RIGHT,duration = {self.ETC_Entry_Duration_value2}, wait = {self.ETC_Entry_Wait_value2})\n")
		self.Text_Edit.insert(tk.INSERT, self.val)


	def OpenPrintDialog(self):
		self._logger.debug("Open print dialog")
		if self.printD is not None:
			self.printD.focus_force()
			return
		Print_Dialog_window = PrintDialog(self.root, self)
		Print_Dialog_window.protocol("WM_DELETE_WINDOW", self.closingPrintDialog)
		self.printD = Print_Dialog_window

	def closingPrintDialog(self):
		self._logger.debug("Close Print Dialog")
		self.printD.destroy()
		self.Clip_BoardPaste()
		self.printD = None

	def OpenWhileDialog(self):
		self._logger.debug("Open While dialog")
		if self.WhileD is not None:
			self.WhileD.focus_force()
			return
		While_Dialog_window = WhileDialog(self.root, self)
		While_Dialog_window.protocol("WM_DELETE_WINDOW", self.closingWhileDialog)
		self.WhileD = While_Dialog_window

	def closingWhileDialog(self):
		self._logger.debug("Close While Dialog")
		self.WhileD.destroy()
		self.Clip_BoardPaste()
		self.WhileD = None

	def OpenDefDialog(self):
		self._logger.debug("Open Def dialog")
		if self.DefD is not None:
			self.DefD.focus_force()
			return
		Def_Dialog_window = DefDialog(self.root, self)
		Def_Dialog_window.protocol("WM_DELETE_WINDOW", self.closingDefDialog)
		self.DefD = Def_Dialog_window

	def closingDefDialog(self):
		self._logger.debug("Close Def Dialog")
		self.DefD.destroy()
		self.Clip_BoardPaste()
		self.DefD = None

	def OpenForDialog(self):
		self._logger.debug("Open For dialog")
		if self.ForD is not None:
			self.ForD.focus_force()
			return
		For_Dialog_window = ForDialog(self.root, self)
		For_Dialog_window.protocol("WM_DELETE_WINDOW", self.closingForDialog)
		self.ForD = For_Dialog_window

	def closingForDialog(self):
		self._logger.debug("Close For Dialog")
		self.ForD.destroy()
		self.Clip_BoardPaste()
		self.ForD = None

	def OpenWaitDialog(self):
		self._logger.debug("Open Wait dialog")
		if self.WaitD is not None:
			self.WaitD.focus_force()
			return
		Wait_Dialog_window = WaitDialog(self.root, self)
		Wait_Dialog_window.protocol("WM_DELETE_WINDOW", self.closingWaitDialog)
		self.WaitD = Wait_Dialog_window

	def closingWaitDialog(self):
		self._logger.debug("Close Wait Dialog")
		self.WaitD.destroy()
		self.Clip_BoardPaste()
		self.WaitD = None

	def OpenTemplateDialog(self):
		self._logger.debug("Open Template dialog")
		if self.TemplateD is not None:
			self.TemplateD.focus_force()
			return
		Template_Dialog_window = TemplateDialog(self.root, self)
		Template_Dialog_window.protocol("WM_DELETE_WINDOW", self.closingTemplateDialog)
		self.TemplateD = Template_Dialog_window

	def closingTemplateDialog(self):
		self._logger.debug("Close Template Dialog")
		self.TemplateD.destroy()
		self.Clip_BoardPaste()
		self.TemplateD = None

	def OpenTemplatePDialog(self):
		self._logger.debug("Open Template dialog")
		if self.TemplatePD is not None:
			self.TemplatePD.focus_force()
			return
		TemplateP_Dialog_window = TemplatePositonDialog(self.root, self)
		TemplateP_Dialog_window.protocol(
			"WM_DELETE_WINDOW", self.closingTemplateDialog)
		self.TemplatePD = TemplateP_Dialog_window

	def closingTemplatePDialog(self):
		self._logger.debug("Close Template Dialog")
		self.TemplatePD.destroy()
		self.Clip_BoardPaste()
		self.TemplatePD = None

	def OpenLINEtextDialog(self):
		self._logger.debug("Open LINEtext dialog")
		if self.LINEtextD is not None:
			self.LINEtextD.focus_force()
			return
		LINEtextP_Dialog_window = LINEtextDialog(self.root, self)
		LINEtextP_Dialog_window.protocol(
			"WM_DELETE_WINDOW", self.closingLINEtextDialog)
		self.LINEtextD = LINEtextP_Dialog_window

	def closingLINEtextDialog(self):
		self._logger.debug("Close LINEtext Dialog")
		self.LINEtextD.destroy()
		self.Clip_BoardPaste()
		self.LINEtextD = None

	def OpenLINEimageDialog(self):
		self._logger.debug("Open LINEimage dialog")
		if self.LINEimageD is not None:
			self.LINEimageD.focus_force()
			return
		LINEimageP_Dialog_window = LINEimageDialog(self.root, self)
		LINEimageP_Dialog_window.protocol(
			"WM_DELETE_WINDOW", self.closingLINEimageDialog)
		self.LINEimageD = LINEimageP_Dialog_window

	def closingLINEimageDialog(self):
		self._logger.debug("Close LINEimage Dialog")
		self.LINEimageD.destroy()
		self.Clip_BoardPaste()
		self.LINEimageD = None

	def OpenCommentOutPDialog(self):
		self._logger.debug("Open Comment dialog")
		if self.CommentD is not None:
			self.CommentD.focus_force()
			return
		Comment_Dialog_window = CommentDialog(self.root, self)
		Comment_Dialog_window.protocol(
			"WM_DELETE_WINDOW", self.closingCommentOutDialog)
		self.CommentD = Comment_Dialog_window

	def closingCommentOutDialog(self):
		self._logger.debug("Close Comment Dialog")
		self.CommentD.destroy()
		self.Clip_BoardPaste()
		self.CommentD = None

	def OpenNeFileDialog(self):
		self._logger.debug("Open NewFile dialog")
		if self.NewFileD is not None:
			self.NewFileD.focus_force()
			return
		NewFile_Dialog_window = NewFileDialog(self.root, self)
		NewFile_Dialog_window.protocol(
			"WM_DELETE_WINDOW", self.closingNewFileOutDialog)
		self.NewFileD = NewFile_Dialog_window

	def closingNewFileOutDialog(self):
		self._logger.debug("Close NewFile Dialog")
		self.NewFileD.destroy()
		self.Text_Edit.delete("1.0", "end")
		self.Clip_BoardPaste()
		self.NewFileD = None

	def Text_Format(self):
		self.Text_Edit_value  = self.Text_Edit.get("1.0","end-1c")
		self.Text_Edit_value = self.Text_Edit_value.replace("	", "    ")
		self.Text_Edit.delete("1.0","end")
		self.Text_Edit.insert(tk.END,self.Text_Edit_value)

	def SaveFile_Button(self):
		self.Text_File_Save = filedialog.asksaveasfilename(
			title="名前を付けて保存", initialdir="./Commands/PythonCommands", defaultextension=".py", filetypes=[("Python", ".py"), ("Text", ".txt")])
		# print(filename)
		with open(self.Text_File_Save,'w',encoding='utf-8')as f:
			self.Text_Edit_value = self.Text_Edit.get("1.0", "end-1c")
			f.write(self.Text_Edit_value)
			f.close


	def OpenFile_Button(self):
		self.Template_Path_Entry_value = filedialog.askopenfilename(
			filetypes=[("Python File", "*.py")], initialdir="./Commands/PythonCommands")
		if not self.Template_Path_Entry_value:
			self.Template_Path_Entry_value = self.Template_Path_Entry_value.replace(
				"C:/PokeCon/Poke-Controller-Modified/SerialController/", "")
			with open(self.Template_Path_Entry_value,"r",encoding='utf-8')as f:
				self.Text_Edit_value = f.read()
				f.close()
			print(self.Template_Path_Entry_value)
			self.Text_Edit.delete("1.0", "end")
			self.Text_Edit.insert(tk.END,self.Text_Edit_value)


		

	


	def OpenCodeDesigner(self):
		self._logger.debug("Open code designer")
		if self.code_de is not None:
			self.code_de.focus_force()
			return
		CD_window = Pokecon_Code_Editor(self.root, self)
		CD_window.protocol("WM_DELETE_WINDOW", self.closingCodeDesigner)
		self.code_de = CD_window

	def closingCodeDesigner(self):
		self._logger.debug("Close Code Desinger window")
		self.code_de.destroy()
		self.code_de = None



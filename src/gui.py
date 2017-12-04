""" 
  Here the main body of the graphical user interface (GUI) is build and 
  configured. 
  
  Three tabs are defined, each in there own function. The init function 
  defines the different notebooks and tabs needed for the GUI. 
"""

try:
  from tkinter import *
  from tkinter import ttk
except ImportError:
  from Tkinter import *
  import ttk

import programmer  

import time
import csv

class GuiAR2():
  """
  The graphical interface of the robotic arm
  """
  
  def __init__(self):
    """ """
    self.root = Tk()
    self.root.wm_title("AR2 software 1.1")
    self.root.iconbitmap(r'icons/AR2.ico')
    self.root.resizable(width=True, height=True)
    
    self._screen_width = self.root.winfo_screenwidth() - 15
    self._screen_height = self.root.winfo_screenheight() - 40
        
    self.root.geometry(str(self._screen_width)+'x'+str(self._screen_height)+'+0+0')

    self.root.runTrue = 0

    self.nb = ttk.Notebook(self.root, width=self._screen_width+15, height=self._screen_height)
    self.nb.place(x=0, y=0)

    self.tab1 = ttk.Frame(self.nb)
    self.nb.add(self.tab1, text=' Main Controls ')

    self.tab2 = ttk.Frame(self.nb)
    self.nb.add(self.tab2, text='  Calibration  ')

    self.tab3 = ttk.Frame(self.nb)
    self.nb.add(self.tab3, text=' Inputs Outputs ')
    
    # TODO: split Main Controls in programming and robot status 
    
    self.currentAngleEntryField = {}
    self.jogDegreesEntryField   = {}
    
    self.currentPositionEntryField = {}
    self.jogPositionEntryField     = {}
    

  def start(self):
    self.tab1.mainloop()
    
  def CreateTab1(self):
  
    tab1 = self.tab1
  
    progName = "somefile"
    ProgEntryField = Entry(tab1,width=20)
    ProgEntryField.place(x=170, y=45)
    
    progframe=Frame(tab1)
    progframe.place(x=7,y=174)
    scrollbar = Scrollbar(progframe) 
    scrollbar.pack(side=RIGHT, fill=Y)
    tab1.progView = Listbox(progframe ,width=64,height=29, yscrollcommand=scrollbar.set)
       
    prog = programmer.Programmer(progName)
    
    tab1.progView.bind('<<ListboxSelect>>', prog.progViewselect)
    
    time.sleep(.2)
    for item in prog.Prog:
      tab1.progView.insert(END,item) 
    tab1.progView.pack()
    scrollbar.config(command=tab1.progView.yview)
    
    LabelsTab1 = {}
    
    fileID = open('../conf/conf_tab1_labels.csv')
    csvID  = csv.reader(fileID, delimiter=',')
    
    for row in csvID:     
      LabelsTab1[row[0]] = Label(self.tab1, text=row[1])
      LabelsTab1[row[0]].place(x=row[2],y=row[3])
      
      if row[4] != 'none':
        LabelsTab1[row[0]]['bg'] = row[4]
      
      if row[5] != 'default':
        LabelsTab1[row[0]]['font'] = row[5]+row[6]
 
    fileID.close()
 
    # Joint labels
    joint_label = {}
    for ii in range(1,7):
      joint_label[ii] = Label(tab1, font=("Arial", 18), text = "J" + str(ii))
      joint_label[ii].place(x=660+(ii-1)*90, y=5)


    ####STEPS LABELS BLUE######
    stepCol = "SteelBlue4"

    joint_step_label = {}
    joint_label2 = {}
    joint_str = [" X", " Y", " Z", "Rx", "Ry", "Rz"]
    for ii in range(1,7):
      joint_step_label[ii] = Label(tab1, font=("Arial", 8), fg=stepCol, text = "000")
      joint_step_label[ii].place(x=695+(ii-1)*90, y=40)
  
      joint_label2[ii] = Label(tab1, font=("Arial", 18), text = joint_str[ii-1])
      joint_label2[ii].place(x=660+(ii-1)*90, y=125)

 

    # register labels
    for ii in range(360, 521, 40):
      tmp = Label(tab1, text = "=")
      tmp.place(x=855, y=ii)

      tmp = Label(tab1, text = "=")
      tmp.place(x=1075, y=360)

    label_robot = {}
    
    for ii in range(1,9):
      
      label_robot[ii] = Label(tab1, text = "R" + str(ii))
      x = {}
      if ii < 5:
        label_robot[ii].place(x=1200, y=35+(ii-1)*40)
      else:
        label_robot[ii].place(x=1275, y=35+(ii-5)*40)


    ###BUTTONS################################################################
    ##########################################################################

    Buttons = {}
    
    foo = lambda: prog.manAddItem()
    Buttons['manEnt'] = Button(tab1, bg="grey85", text="Enter Text", height=1, width=14, command=prog.manAddItem)
    Buttons['manEnt'].place(x=795, y=641)
    
    Buttons['teachInsBut'] = Button(tab1, bg="grey85", text="Teach New Position", height=1, width=20, command = prog.teachInsertBelSelected)
    Buttons['teachInsBut'].place(x=540, y=440)

    Buttons['teachReplaceBut'] = Button(tab1, bg="grey85", text="Modify Position", height=1, width=20, command = prog.teachReplaceSelected)
    Buttons['teachReplaceBut'].place(x=540, y=480)

    Buttons['waitTimeBut'] = Button(tab1, bg="grey85", text="Wait Time (seconds)", height=1, width=20, command = prog.waitTime)
    Buttons['waitTimeBut'].place(x=700, y=360)

    Buttons['waitInputOnBut'] = Button(tab1, bg="grey85", text="Wait Input ON", height=1, width=20, command = prog.waitInputOn)
    Buttons['waitInputOnBut'].place(x=700, y=400)

    Buttons['waitInputOffBut'] = Button(tab1, bg="grey85", text="Wait Input OFF", height=1, width=20, command = prog.waitInputOff)
    Buttons['waitInputOffBut'].place(x=700, y=440)

    Buttons['setOutputOnBut'] = Button(tab1, bg="grey85", text="Set Output On", height=1, width=20, command = prog.setOutputOn)
    Buttons['setOutputOnBut'].place(x=700, y=480)

    Buttons['setOutputOffBut'] = Button(tab1, bg="grey85", text="Set Output OFF", height=1, width=20, command = prog.setOutputOff)
    Buttons['setOutputOffBut'].place(x=700, y=520)

    Buttons['tabNumBut'] = Button(tab1, bg="grey85", text="Create Tab Number", height=1, width=20, command = prog.tabNumber)
    Buttons['tabNumBut'].place(x=920, y=360)

    # jumpTabBut = Button(tab1, bg="grey85", text="Jump to Tab", height=1, width=20, command = jumpTab)
    # jumpTabBut.place(x=920, y=400)

    # IfOnjumpTabBut = Button(tab1, bg="grey85", text="If On Jump", height=1, width=20, command = IfOnjumpTab)
    # IfOnjumpTabBut.place(x=920, y=440)

    # IfOffjumpTabBut = Button(tab1, bg="grey85", text="If Off Jump", height=1, width=20, command = IfOffjumpTab)
    # IfOffjumpTabBut.place(x=920, y=480)

    # servoBut = Button(tab1, bg="grey85", text="Servo", height=1, width=20, command = Servo)
    # servoBut.place(x=920, y=520)

    # callBut = Button(tab1, bg="grey85", text="Call Program", height=1, width=20, command = insertCallProg)
    # callBut.place(x=540, y=560)
    pos = 1
    Buttons['returnBut'] = Button(tab1, bg="grey85", text="Return", height=1, width=20, command=lambda pos=pos: prog.insertReturn(pos))
    Buttons['returnBut'].place(x=540, y=600)

    # comPortBut = Button(tab1, bg="grey85", text="Set Com", height=0, width=7, command = setCom)
    # comPortBut.place(x=103, y=7)

    # ProgBut = Button(tab1, bg="grey85", text="Load Program", height=0, width=12, command = loadProg)
    # ProgBut.place(x=202, y=42)

    # deleteBut = Button(tab1, bg="grey85", text="Delete", height=1, width=20, command = deleteitem)
    # deleteBut.place(x=540, y=520)

    # runProgBut = Button(tab1, height=60, width=60, command = runProg)
    # playPhoto=PhotoImage(file="icons\play-icon.gif")
    # runProgBut.config(image=playPhoto,width="60",height="60")
    # runProgBut.place(x=20, y=80)

    # stopProgBut = Button(tab1, height=60, width=60, command = stopProg)
    # stopPhoto=PhotoImage(file="icons\stop-icon.gif")
    # stopProgBut.config(image=stopPhoto,width="60",height="60")
    # stopProgBut.place(x=200, y=80)

    # fwdBut = Button(tab1, bg="grey85", text="FWD", height=3, width=4, command = stepFwd)
    # fwdBut.place(x=100, y=80)

    # revBut = Button(tab1, bg="grey85", text="REV", height=3, width=4, command = stepRev)
    # revBut.place(x=150, y=80)

    # RegNumBut = Button(tab1, bg="grey85", text="Register", height=1, width=20, command = insertRegister)
    # RegNumBut.place(x=920, y=560)

    # RegJmpBut = Button(tab1, bg="grey85", text="If Register Jump", height=1, width=20, command = IfRegjumpTab)
    # RegJmpBut.place(x=920, y=600)

    # CalibrateBut = Button(tab1, bg="grey85", text="Auto Calibrate CMD", height=1, width=20, command = insCalibrate)
    # CalibrateBut.place(x=700, y=600)

    # J1jogNegBut = Button(tab1, bg="grey85", text="-", height=1, width=3, command = J1jogNeg)
    # J1jogNegBut.place(x=642, y=90)

    # J1jogPosBut = Button(tab1, bg="grey85",text="+", height=1, width=3, command = J1jogPos)
    # J1jogPosBut.place(x=680, y=90)

    # J2jogNegBut = Button(tab1, bg="grey85",text="-", height=1, width=3, command = J2jogNeg)
    # J2jogNegBut.place(x=732, y=90)

    # J2jogPosBut = Button(tab1, bg="grey85",text="+", height=1, width=3, command = J2jogPos)
    # J2jogPosBut.place(x=770, y=90)

    # J3jogNegBut = Button(tab1, bg="grey85",text="-", height=1, width=3, command = J3jogNeg)
    # J3jogNegBut.place(x=822, y=90)

    # J3jogPosBut = Button(tab1, bg="grey85",text="+", height=1, width=3, command = J3jogPos)
    # J3jogPosBut.place(x=860, y=90)

    # J4jogNegBut = Button(tab1, bg="grey85",text="-", height=1, width=3, command = J4jogNeg)
    # J4jogNegBut.place(x=912, y=90)

    # J4jogPosBut = Button(tab1, bg="grey85",text="+", height=1, width=3, command = J4jogPos)
    # J4jogPosBut.place(x=950, y=90)

    # J5jogNegBut = Button(tab1, bg="grey85",text="-", height=1, width=3, command = J5jogNeg)
    # J5jogNegBut.place(x=1002, y=90)

    # J5jogPosBut = Button(tab1, bg="grey85",text="+", height=1, width=3, command = J5jogPos)
    # J5jogPosBut.place(x=1040, y=90)

    # J6jogNegBut = Button(tab1, bg="grey85",text="-", height=1, width=3, command = J6jogNeg)
    # J6jogNegBut.place(x=1092, y=90)

    # J6jogPosBut = Button(tab1, bg="grey85",text="+", height=1, width=3, command = J6jogPos)
    # J6jogPosBut.place(x=1130, y=90)

    # XjogNegBut = Button(tab1, bg="grey85",text="-", height=1, width=3, command = XjogNeg)
    # XjogNegBut.place(x=642, y=210)

    # XjogPosBut = Button(tab1, bg="grey85",text="+", height=1, width=3, command = XjogPos)
    # XjogPosBut.place(x=680, y=210)

    # YjogNegBut = Button(tab1, bg="grey85",text="-", height=1, width=3, command = YjogNeg)
    # YjogNegBut.place(x=732, y=210)

    # YjogPosBut = Button(tab1, bg="grey85",text="+", height=1, width=3, command = YjogPos)
    # YjogPosBut.place(x=770, y=210)

    # ZjogNegBut = Button(tab1, bg="grey85",text="-", height=1, width=3, command = ZjogNeg)
    # ZjogNegBut.place(x=822, y=210)

    # ZjogPosBut = Button(tab1, bg="grey85",text="+", height=1, width=3, command = ZjogPos)
    # ZjogPosBut.place(x=860, y=210)

    # RxjogNegBut = Button(tab1, bg="grey85",text="-", height=1, width=3, command = RxjogNeg)
    # RxjogNegBut.place(x=912, y=210)

    # RxjogPosBut = Button(tab1, bg="grey85",text="+", height=1, width=3, command = RxjogPos)
    # RxjogPosBut.place(x=950, y=210)

    # RyjogNegBut = Button(tab1, bg="grey85",text="-", height=1, width=3, command = RyjogNeg)
    # RyjogNegBut.place(x=1002, y=210)

    # RyjogPosBut = Button(tab1, bg="grey85",text="+", height=1, width=3, command = RyjogPos)
    # RyjogPosBut.place(x=1040, y=210)

    # RzjogNegBut = Button(tab1, bg="grey85",text="-", height=1, width=3, command = RzjogNeg)
    # RzjogNegBut.place(x=1092, y=210)

    # RzjogPosBut = Button(tab1, bg="grey85",text="+", height=1, width=3, command = RzjogPos)
    # RzjogPosBut.place(x=1130, y=210)

    # JogStepsCbut = Checkbutton(tab1, text="Jog joints in steps",variable = JogStepsStat)
    # JogStepsCbut.place(x=1190, y=10)









    ####ENTRY FIELDS##########################################################
    ##########################################################################

    entryField = {}

    fileID = open('../conf/conf_tab1_entries.csv')
    csvID  = csv.reader(fileID, delimiter=',')
  
    
    for row in csvID:
      entryField[row[0]] = Entry(tab1, width=row[1])
      entryField[row[0]].place(x=row[2], y=row[3])
    
    fileID.close()

  
    joint_names = []
    for ii in range(1,7):
      joint_names.append('J' + str(ii))
    
    self.currentAngleEntryField = {}
    for ii, joint_name in enumerate(joint_names): 
      self.currentAngleEntryField[joint_name] = Entry(tab1, width=5)
      self.currentAngleEntryField[joint_name].place(x=660+(ii)*90, y=40)
      
      # self.jogDegreesEntryField[ii] = Entry(tab1,width=5)
      # self.jogDegreesEntryField[ii].place(x=660+(ii-1)*90, y=65)
 

      # self.currentPositionEntryField[ii] = Entry(tab1,width=5)
      # self.currentPositionEntryField[ii].place(x=660+(ii-1)*90, y=160)
      
      # self.jogPositionEntryField[ii] = Entry(tab1,width=5)
      # self.jogPositionEntryField[ii].place(x=660+(ii-1)*90, y=185)
      
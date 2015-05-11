from Tkinter import *
import string
import random
import tkMessageBox
import tkFileDialog
import datetime
import os
import time
import winsound
import pickle




class encryption:
    encrypted=True
    def encryptfile(self):
        if self.encrypted==False:
            infile1=open("Tasks.txt")
            infile2=open("Temp.txt","w")
            text=infile1.read()
            text=encrypt(text)
            infile2.write(text)
            infile1.close()
            infile2.close()
            os.remove("Tasks.txt")
            os.rename("Temp.txt","Tasks.txt")
            infile1=open("settings.txt")
            infile2=open("Temp.txt","w")
            text=infile1.read()
            text=encrypt(text)
            infile2.write(text)
            infile1.close()
            infile2.close()
            os.remove("settings.txt")
            os.rename("Temp.txt","settings.txt")
            self.encrypted=True
    def decryptfile(self):
        if self.encrypted==True:
            infile1=open("Tasks.txt")
            infile2=open("Temp.txt","w")
            text=infile1.read()
            text=decrypt(text)
            infile2.write(text)
            infile1.close()
            infile2.close()
            os.remove("Tasks.txt")
            os.rename("Temp.txt","Tasks.txt")
            infile1=open("settings.txt")
            infile2=open("Temp.txt","w")
            text=infile1.read()
            text=decrypt(text)
            infile2.write(text)
            infile1.close()
            infile2.close()
            os.remove("settings.txt")
            os.rename("Temp.txt","settings.txt")
            self.encrypted=False
            



     

def encrypt(text):
    password="Porunga"
    encrypted = []
    for i, c in enumerate(text):
        shift = password[i % len(password)]
        shift = ord(shift)
        encrypted.append((ord(c) + shift) % 256)
    return ''.join([chr(n) for n in encrypted])

def decrypt(text):
    password="Porunga"
    plain = []
    for i, c in enumerate(text):
        shift = password[i % len(password)]
        shift = ord(shift)
        plain.append((256 + ord(c) - shift) % 256)
    return ''.join([chr(n) for n in plain])




class Diary:
    def __init__(self):
        self.DateTime=01/01/0001
        self.Label=''
        self.Details=''
        self.cstatus="Pending"
    def NewID(self):
        NID=str(random.randrange(0,10))+str(random.randrange(0,10))+str(random.randrange(0,10))+str(random.randrange(0,10))
        return NID
    def Store(self,DateTime,Label,Details,Rating):
        self.ID=self.NewID()
        
        S=self.ID+" "+str(DateTime).replace(" ","_")+" "+str(Label).replace(" ","_")+" "+str(Details).replace(" ","_")+" "+str(self.cstatus)+" "+str(Rating)+"\n"
        infile=open("Tasks.txt",'a')
        infile.write(S)
        infile.close()
    def Delete(self,DID):
        DID=str(DID)
        infile1=open("Tasks.txt","r")
        infile2=open("Temp.txt","w")
        for j in infile1.readlines():
            T=j.split()
            if T[0]!=DID:
                S=T[0]+" "+T[1]+" "+T[2]+" "+T[3]+" "+str(T[4])+" "+str(T[5])+"\n"
                infile2.write(S)
        infile1.close()
        infile2.close()
        infile1=open("Tasks.txt","w")
        infile2=open("Temp.txt","r")
        for i in infile2.readlines():
            infile1.write(i)
        infile1.close()
        infile2.close()
        os.remove("Temp.txt")



    

class Controlwindow:
    def __init__(self, parent):

        self.smileypath=os.getcwd()+"/smiley.ico"

        self.myParent = parent
        self.mainframe = Frame(parent) 
        self.mainframe.pack()

        
       
        # Control Box
        self.controlbox= Frame(self.mainframe)
        self.controlbox.pack(side=TOP,ipadx="3m",ipady="2m",padx="3m",pady="2m",
            )

        # Task Selection Frame
        self.tsf=Frame(self.mainframe)
        self.tsf.pack(side=TOP,fill=BOTH,expand=YES)

        self.scroll=Scrollbar(self.tsf)
        self.scroll.pack(side=RIGHT, fill=Y)

        self.DF=Text(self.tsf,yscrollcommand=self.scroll.set,wrap=WORD,font='System',bg='black',fg='white')
        
        self.DF.pack(side=TOP,fill=BOTH,expand=1)
        self.scroll.config(command=self.DF.yview)
         
        self.reld()

        showtime=Label(self.tsf,bd=1)
        showtime.pack(side=RIGHT,padx="5m")
        def tick():
            T=datetime.datetime.today()
            DT=str(T.day)+"/"+str(T.month)+"/"+str(T.year)+"    "+str(T.hour)+":"+str(T.minute)
            showtime.configure(text=DT)
            time.sleep(1)
            showtime.after(60000, tick)
        tick()

        self.v=StringVar()
        self.textbox=Entry(self.tsf,textvariable=self.v,bd=2)
        self.textbox.bind("<Return>",self.Display)
        self.textbox.pack(side=RIGHT,padx="29m")
        # Extracted all tasks in file one by one and diplayed in scrollable textbox


        

        
        self.AlarmB=PhotoImage(file="clock.gif")
        self.QuitB=PhotoImage(file="quit.gif")
        self.AddB=PhotoImage(file="add.gif")
        self.EditB=PhotoImage(file="edit.gif")
        self.DeleteB=PhotoImage(file="delete.gif")
        self.CheckB=PhotoImage(file="check.gif")
        self.SettingsB=PhotoImage(file="settings.gif")
        # Control Buttons
        self.NT = Button(self.controlbox,command=self.NTF,width=50,height=50,image=self.AddB)
        self.NT.pack(side=LEFT)
        self.EET = Button(self.controlbox,command=self.EETF,width=50,height=50,image=self.EditB)
        self.EET.pack(side=LEFT)
        self.DT = Button(self.controlbox,command=self.DTF,width=50,height=50,image=self.DeleteB)
        self.DT.pack(side=LEFT)
        self.checkbutton=Button(self.controlbox,command=self.Checker,width=50,height=50,image=self.CheckB)
        self.checkbutton.pack(side=LEFT)
        self.closebutton3=Button(self.controlbox,command=parent.destroy,width=50,height=50,image=self.QuitB)
        self.closebutton3.pack(side=RIGHT)
        
        self.alarmbutton=Button(self.controlbox,width=50,height=50,image=self.AlarmB,command=self.alarmmode)
        self.alarmbutton.pack(side=RIGHT)
        self.settingsbutton=Button(self.controlbox,width=50,height=50,image=self.SettingsB,command=self.options)
        self.settingsbutton.pack(side=RIGHT)

    

    def options(self):
        self.opwin=Toplevel(self.controlbox)
        self.opwin.iconbitmap(self.smileypath)
        self.opframe1=Frame(self.opwin)
        self.opframe1.pack(side=TOP)
        self.opframe2=Frame(self.opwin)
        self.opframe2.pack(side=TOP)
        

        self.epass=StringVar()
        self.npass=StringVar()

        self.openB=PhotoImage(file="open.gif")
        self.playB=PhotoImage(file="play.gif")
        
        self.passchange=Label(self.opframe1,text="Change Your Password",pady="3m")
        self.passchange.pack(side=TOP)
        self.passchange1=Label(self.opframe1,text="Existing Password:")
        self.passchange1.pack(side=TOP)
        self.passbox1=Entry(self.opframe1,textvariable=self.epass,show="*")
        self.passbox1.pack(side=TOP)
        self.passchange2=Label(self.opframe1,text="New Password:")
        self.passchange2.pack(side=TOP)
        self.passbox2=Entry(self.opframe1,textvariable=self.npass,show="*")
        self.passbox2.pack(side=TOP)
        self.passchangeB=Button(self.opframe1,command=self.pchange,text="Ok")
        self.passchangeB.pack(side=BOTTOM)

        

        
        self.openfile=Button(self.opframe2,image=self.openB,command=self.opennew)
        self.openfile.pack(side=LEFT)
        
        self.play=Button(self.opframe2,image=self.playB,command=self.plays)
        self.play.pack(side=RIGHT)

        self.importsound2=Label(self.opframe2,text="Custom Alarm Sound",pady='5m')
        self.importsound2.pack(side=TOP)

        opf=open("settings.txt")
        oplist=pickle.load(opf)
        opf.close()

        

    def opennew(self):
        self.opwin.iconify()
        self.newsoundpath=tkFileDialog.askopenfilename()
        if self.newsoundpath[-3:]=='wav':
            opf=open("settings.txt")
            oplist=pickle.load(opf)
            opf.close()
            f=open("settings.txt",'w')
            pickle.dump(oplist,f)
            f.close()
        else:
            tkMessageBox.showwarning("Error","Please select a .wav sound file")
        
        self.opwin.deiconify()
    def plays(self):
        opf=open("settings.txt")
        oplist=pickle.load(opf)
        opf.close()
        spath=oplist[1]
        data=open(spath,"r").read()
        winsound.PlaySound(data, winsound.SND_MEMORY)
        
        

        
    def pchange(self):
        self.opwin.iconify()
        opf=open("settings.txt")
        oplist=pickle.load(opf)
        opf.close()
        if self.epass.get()==oplist[0]:
            oplist[0]=self.npass.get()
            f=open("settings.txt",'w')
            pickle.dump(oplist,f)
            f.close()
            tkMessageBox.showwarning("Success","Password has been changed")
        else:
            tkMessageBox.showwarning("Error","Incorrect Password")
        self.opwin.deiconify()
        self.passbox1.delete(0,END)
        self.passbox2.delete(0,END)
            
        
  
        
        

    def alarmmode(self):
        self.al=Toplevel(self.myParent)
        self.al.iconbitmap(self.smileypath)

        self.alDateYear=StringVar()
        self.alDateMonth=StringVar()
        self.alDateDay=StringVar()
        self.alTimeHour=StringVar()
        self.alTimeMinute=StringVar()
        
        self.all1=Label(self.al,text="Enter the Alarm Date [DD/MM/YY]:")
        self.all1.pack(side=LEFT)
        
        textbox1=Entry(self.al,textvariable=self.alDateDay,width=4)
        textbox1.pack(side=LEFT)
        textbox1_=Entry(self.al,textvariable=self.alDateMonth,width=4)
        textbox1_.pack(side=LEFT)
        textbox1__=Entry(self.al,textvariable=self.alDateYear,width=6)
        textbox1__.pack(side=LEFT)

        self.alb=Button(self.al,text="Set",command=self.alarmtime)
        self.alb.pack(side=RIGHT)

        textbox2_=Entry(self.al,textvariable=self.alTimeMinute,width=4)
        textbox2_.pack(side=RIGHT)
        textbox2=Entry(self.al,textvariable=self.alTimeHour,width=4)
        textbox2.pack(side=RIGHT)
        

        self.all2=Label(self.al,text="Enter the Alarm Time [24:00]:")
        self.all2.pack(side=RIGHT)

        

        
    def alarmtime(self):
        self.al.destroy()
        self.altime=Toplevel(self.myParent)
        self.altime.iconbitmap(self.smileypath)
        S="Alarm set for "+self.alDateDay.get()+"/"+self.alDateMonth.get()+"/"+self.alDateYear.get()+" "+self.alTimeHour.get()+":"+self.alTimeMinute.get()
        self.all12=Label(self.altime,text=S)
        self.all12.pack(side=LEFT)
        self.albb=Button(self.altime,text="Abort",command=self.altime.destroy)
        self.albb.pack(side=RIGHT)
        def tick():
            T=datetime.datetime.today()
            if T.year==eval(self.alDateYear.get()) and T.month==eval(self.alDateMonth.get()) and T.day==eval(self.alDateDay.get()) and T.hour==eval(self.alTimeHour.get()) and T.minute==eval(self.alTimeMinute.get()):

                opf=open("settings.txt")
                oplist=pickle.load(opf)
                opf.close()
                spath=oplist[1]
                data=open(spath,"r").read()
                
                winsound.PlaySound(data, winsound.SND_MEMORY)
            self.altime.after(1000, tick)
        tick()
        
        
         


    def Checker(self):
        
        self.cframe=Toplevel(self.controlbox,borderwidth=5,relief=RIDGE)
        self.cframe.iconbitmap(self.smileypath)

        self.ctxt=Label(self.cframe,text="Input the ID's of the tasks you have finished and hit Return:")
        self.ctxt.pack()
        
        
        self.varn=StringVar()
        self.textboxn1=Entry(self.cframe,textvariable=self.varn)
        self.textboxn1.bind("<Return>",self.Ch)
        self.textboxn1.pack(side=BOTTOM)

    def Ch(self,event):
        
        infile=open("Tasks.txt","r")       
        
        for j in infile.readlines():
            T=string.split(j)
            if T[0]==str(self.varn.get()):
                p=Diary()
                p.Delete(self.varn.get())
                f=open("Tasks.txt","a")
                S=T[0]+" "+T[1].replace(" ","_")+" "+T[2].replace(" ","_")+" "+T[3].replace(" ","_")+" "+"Done"+" "+T[5]+"\n"
                f.write(S)
                f.close()
        infile.close()
        self.textboxn1.delete(0,END)
        self.textboxn1.pack()
        self.reld()
            
        
        

    # Kept for Smart Search
    def Display(self,event):
        self.reld()
        self.DF.configure(state=NORMAL)
        self.DF.delete(1.0,END)
        infile=open("Tasks.txt","r")
        L=[]
        D={}
        for j in infile.readlines():
            T=string.split(j)
            T[1]=T[1].replace("_"," ")
            T[2]=T[2].replace("_"," ")
            T[3]=T[3].replace("_"," ")
            D1=T[1].split()
            AD=D1[0].split("/")
            AT=D1[1].split(":")
            
            Test=datetime.datetime(eval(AD[2]),eval(AD[1]),eval(AD[0]),eval(AT[0]),eval(AT[1]))
            try:
                D[Test].append(T)
            except KeyError:
                D[Test]=[T]
        Li=D.keys()
        Li.sort()
        for i in Li:
            L.extend(D[i])
        Term=self.v.get()
        if Term=="Today":
            curdate=datetime.datetime.now()
            Term=str(curdate.day)+"/"+str(curdate.month)+"/"+str(curdate.year)
                    
        for k in L:
            D=k[1].split()
            sinitial=eval(k[5])*"*"
            if Term in k[1] or self.v.get() in k[2]or self.v.get() in k[3] or self.v.get() in k[4]or self.v.get()==D[0] or self.v.get()==D[1]or self.v.get()==sinitial:
                s=eval(k[5])*"*"
                S="ID: %s\nDate: %s\nName: %s\nDetails: %s\nRating: %s\nStatus: %s\n\n"%(k[0],k[1],k[2],k[3],s,k[4])
                self.DF.insert(END,S)
        self.DF.pack(side=TOP,fill=BOTH)
        self.DF.configure(state=DISABLED)
                       
        infile.close()

        
# Edit Frame1
    def EETF(self):
        self.eframe=Toplevel(self.controlbox,borderwidth=5,relief=RIDGE)
        self.eframe.iconbitmap(self.smileypath)
               
        self.Etxt=Label(self.eframe,text="Input the Task ID you wish to Edit and hit Return:")
        self.Etxt.pack()
        self.var1=StringVar()
        textbox3=Entry(self.eframe,textvariable=self.var1)
        textbox3.bind("<Return>",self.Ed)
        textbox3.pack(side=BOTTOM)

    def Ed(self,event):
        self.eframe.destroy()
        self.neframe=Toplevel(self.controlbox,borderwidth=5,relief=RIDGE)
        self.neframe.iconbitmap(self.smileypath)

        c=0

        infile=open("Tasks.txt","r")
        for j in infile.readlines():
            T=string.split(j)
            if T[0]==str(self.var1.get()):
                self.ExistingID=T[0]
                c=1
                D=T[1].split("_")
                Date2=D[0].split("/")
                Time2=D[1].split(":")
                break
        infile.close()
        
        if c==1:
            self.DateYear1_=StringVar()
            self.DateMonth1_=StringVar()
            self.DateDay1_=StringVar()
            self.TimeHour1_=StringVar()
            self.TimeMinute1_=StringVar()
            self.Name1_=StringVar()
            self.Details1_=StringVar()
            
            self.l11=Label(self.neframe,text="Enter the task Date [DD/MM/YY]:")
            self.l11.pack(side=LEFT)
        
            textbox111=Entry(self.neframe,textvariable=self.DateDay1_,width=4)
            textbox111.insert(END,Date2[0])
            textbox111.pack(side=LEFT)
            textbox112_=Entry(self.neframe,textvariable=self.DateMonth1_,width=4)
            textbox112_.insert(END,Date2[1])
            textbox112_.pack(side=LEFT)
            textbox113__=Entry(self.neframe,textvariable=self.DateYear1_,width=6)
            textbox113__.insert(END,Date2[2])
            textbox113__.pack(side=LEFT)

            textbox21_=Entry(self.neframe,textvariable=self.TimeMinute1_,width=4)
            textbox21_.insert(END,Time2[1])
            textbox21_.pack(side=RIGHT)
        
            textbox211=Entry(self.neframe,textvariable=self.TimeHour1_,width=4)
            textbox211.insert(END,Time2[0])
            textbox211.pack(side=RIGHT)
        

            self.l2=Label(self.neframe,text="Enter the task Time [24:00]:")
            self.l2.pack(side=RIGHT)

            self.l322=Label(self.neframe,text="Enter the task Priority :")
            self.l322.pack(side=TOP)

            self.slider=Scale(self.neframe,from_=1,to=5,orient=HORIZONTAL)
            self.slider.set(eval(T[5]))
            self.slider.pack()

            self.l31=Label(self.neframe,text="Enter the task Name :")
            self.l31.pack(side=TOP)

            textbox31=Entry(self.neframe,textvariable=self.Name1_)
            textbox31.insert(END,T[2].replace("_"," "))
            textbox31.pack(side=TOP)
   
            self.l41=Label(self.neframe,text="Enter the task Details: ")
            self.l41.pack(side=TOP)
        
            textbox41=Entry(self.neframe,textvariable=self.Details1_,width=50)
            textbox41.insert(END,T[3].replace("_"," "))
            textbox41.pack(side=TOP)

            self.l51=Button(self.neframe,text="OK",command=self.Modify)
            self.l51.pack(side=TOP)
        else:
            tkMessageBox.showwarning("Error","Please Enter a Correct ID")
            self.neframe.destroy()

        
        
        

    def Modify(self):
        p=Diary()
        c=1
        try:
            Timetest=datetime.time(eval(self.TimeHour1_.get()),eval(self.TimeMinute1_.get()))
        except (NameError,ValueError,SyntaxError):
            tkMessageBox.showwarning("Error","Please Enter a Correct Time")
            c=0
        try:
            Datetest=datetime.date(eval(self.DateYear1_.get()),eval(self.DateMonth1_.get()),eval(self.DateDay1_.get()))
        except (NameError,ValueError,SyntaxError):
            tkMessageBox.showwarning("Error","Please Enter a Correct Date")
            c=0

        if c!=0:
            Now=datetime.datetime.now()
            Test=datetime.datetime(eval(self.DateYear1_.get()),eval(self.DateMonth1_.get()),eval(self.DateDay1_.get()),eval(self.TimeHour1_.get()),eval(self.TimeMinute1_.get()))
            if Now>Test:
                c=0
                tkMessageBox.showwarning("Error","You cannot set Date and Time in the Past")
        if c==1:
            
            DT=self.DateDay1_.get()+"/"+self.DateMonth1_.get()+"/"+self.DateYear1_.get()+" "+self.TimeHour1_.get()+":"+self.TimeMinute1_.get()
            
            p.Delete(self.var1.get())
            S=self.ExistingID+" "+str(DT).replace(" ","_")+" "+str(self.Name1_.get()).replace(" ","_")+" "+str(self.Details1_.get()).replace(" ","_")+" "+"Pending"+" "+str(self.slider.get())+"\n"
            infile=open("Tasks.txt",'a')
            infile.write(S)
            infile.close()
        
        self.reld()
        
                
        
        

    def NTF(self):
        self.NTframe=Toplevel(self.controlbox,borderwidth=5,relief=RIDGE)
        self.NTframe.iconbitmap(self.smileypath)


        self.DateYear_=StringVar()
        self.DateMonth_=StringVar()
        self.DateDay_=StringVar()
        self.TimeHour_=StringVar()
        self.TimeMinute_=StringVar()
        self.Name_=StringVar()
        self.Details_=StringVar()
        
        self.l1=Label(self.NTframe,text="Enter the task Date [DD/MM/YY]:")
        self.l1.pack(side=LEFT)
        
        textbox1=Entry(self.NTframe,textvariable=self.DateDay_,width=4)
        textbox1.pack(side=LEFT)
        textbox1_=Entry(self.NTframe,textvariable=self.DateMonth_,width=4)
        textbox1_.pack(side=LEFT)
        textbox1__=Entry(self.NTframe,textvariable=self.DateYear_,width=6)
        textbox1__.pack(side=LEFT)

        textbox2_=Entry(self.NTframe,textvariable=self.TimeMinute_,width=4)
        textbox2_.pack(side=RIGHT)
        textbox2=Entry(self.NTframe,textvariable=self.TimeHour_,width=4)
        textbox2.pack(side=RIGHT)
        

        self.l2=Label(self.NTframe,text="Enter the task Time [24:00]:")
        self.l2.pack(side=RIGHT)

        self.l322=Label(self.NTframe,text="Enter the task Priority :")
        self.l322.pack(side=TOP)

        self.slider1=Scale(self.NTframe,from_=1,to=5,orient=HORIZONTAL)
        self.slider1.pack()

        

        self.l3=Label(self.NTframe,text="Enter the task Name :")
        self.l3.pack(side=TOP)

        textbox3=Entry(self.NTframe,textvariable=self.Name_)
        textbox3.pack(side=TOP)

        self.l5=Button(self.NTframe,text="OK",command=self.Insert)
        self.l5.pack(side=BOTTOM)

        textbox4=Entry(self.NTframe,textvariable=self.Details_,width=50)
        textbox4.pack(side=BOTTOM)

        self.l4=Label(self.NTframe,text="Enter the task Details: ")
        self.l4.pack(side=BOTTOM)
        

    def Insert(self):
        p=Diary()
        c=1
        try:
            Timetest=datetime.time(eval(self.TimeHour_.get()),eval(self.TimeMinute_.get()))
        except (NameError,ValueError,SyntaxError):
            tkMessageBox.showwarning("Error","Please Enter a Correct Time")
            c=0
        try:
            Datetest=datetime.date(eval(self.DateYear_.get()),eval(self.DateMonth_.get()),eval(self.DateDay_.get()))
        except (NameError,ValueError,SyntaxError):
            tkMessageBox.showwarning("Error","Please Enter a Correct Date")
            c=0
        if c!=0:
            Now=datetime.datetime.now()
            Test=datetime.datetime(eval(self.DateYear_.get()),eval(self.DateMonth_.get()),eval(self.DateDay_.get()),eval(self.TimeHour_.get()),eval(self.TimeMinute_.get()))
            if Now>Test:
                c=0
                tkMessageBox.showwarning("Error","You cannot set Date and Time in the Past")
                
        if c==1:
            
            DT=self.DateDay1_.get()+"/"+self.DateMonth1_.get()+"/"+self.DateYear1_.get()+" "+self.TimeHour1_.get()+":"+self.TimeMinute1_.get()
            
            p.Delete(self.var1.get())
            S=self.ExistingID+" "+str(DT).replace(" ","_")+" "+str(self.Name1_.get()).replace(" ","_")+" "+str(self.Details1_.get()).replace(" ","_")+" "+"Pending"+" "+str(self.slider.get())+"\n"
            infile=open("Tasks.txt",'a')
            infile.write(S)
            infile.close()
        
        self.reld()

    def DTF(self):
        self.deleteframe=Toplevel(self.controlbox,borderwidth=5,relief=RIDGE,)
        self.deleteframe.iconbitmap(self.smileypath)

                      
        self.Deltxt=Label(self.deleteframe,text="Input the Task ID you wish to delete and hit Return:")
        self.Deltxt.pack()
        
        
        self.var=StringVar()
        self.textboxx=Entry(self.deleteframe,textvariable=self.var)
        self.textboxx.bind("<Return>",self.Del)
        self.textboxx.pack(side=BOTTOM)        
        
    def Del(self,event):
        p=Diary()
        p.Delete(self.var.get())
        self.textboxx.delete(0,END)
        self.textboxx.pack()
        self.reld()
    def reld(self):
        self.DF.configure(state=NORMAL)
        self.DF.delete(1.0,END)
        infile=open("Tasks.txt","r")
        L=[]
        Li=[]
        D={}
        for j in infile.readlines():
            T=string.split(j)
            T[1]=T[1].replace("_"," ")
            T[2]=T[2].replace("_"," ")
            T[3]=T[3].replace("_"," ")
            D1=T[1].split()
            AD=D1[0].split("/")
            AT=D1[1].split(":")
                       
            Test=datetime.datetime(eval(AD[2]),eval(AD[1]),eval(AD[0]),eval(AT[0]),eval(AT[1]))
            try:
                D[Test].append(T)
            except KeyError:
                D[Test]=[T]
            
        Li=D.keys()
        Li.sort()
        for i in Li:
            L.extend(D[i])
        for k in L:
            s=eval(k[5])*"*"
            S="ID: %s\nDate: %s\nName: %s\nDetails: %s\nRating: %s\nStatus: %s\n\n"%(k[0],k[1],k[2],k[3],s,k[4])
            self.DF.insert(END,S)
        self.DF.pack(side=TOP,fill=BOTH)
        self.DF.configure(state=DISABLED)
                       
        infile.close()

a=encryption()
a.decryptfile()
global oplist
opf=open("settings.txt")
oplist=pickle.load(opf)
opf.close()



global passcode
passcode=oplist[0]

def passcheck(event):
    global password
    global root1    
    if password.get()==passcode:
        root1.destroy()
        root=Tk()
        root.iconbitmap(smiley)
        root.title("Personal Planner")
        p=Diary()
        Main=Controlwindow(root)
        root.mainloop()

    
    

 
    

smiley=os.getcwd()+"/smiley.ico"

global root1
root1=Tk()
root1.title("Welcome to Personal Planner")
root1.iconbitmap(smiley)

f1=Frame(root1)
f1.pack(side=LEFT)

f2=Frame(root1)
f2.pack(side=RIGHT)

   
helptxt=Text(f2,wrap=WORD)
helptxt.pack(side=RIGHT,fill=BOTH,expand=1)
helptxt.configure(state=NORMAL)
helptxt.delete(1.0,END)
infile=open("help.txt")
S=infile.read()
helptxt.insert(END,S)
helptxt.configure(state=DISABLED)
infile.close()
  



cal=PhotoImage(file="calendar.gif")
L=Label(f2,image=cal,bd=0)
L.pack()

global password
password=StringVar()


passbox=Entry(f2,textvariable=password,show="*")
passbox.bind("<Return>",passcheck)
passbox.pack(side=BOTTOM)

root1.mainloop()

a.encryptfile()



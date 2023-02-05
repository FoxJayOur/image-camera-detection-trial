import datetime
from tkinter import *
import tkinter.messagebox as mb
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import filedialog
import sqlite3

class CrimInfo:
    def __init__(self, crimID, crimName, crimDoB, crimGen, crimDn):
        self.crimID = crimID
        self.crimName = crimName
        self.crimDoB = crimDoB
        self.crimGen = crimGen
        self.crimDn = crimDn

class mrdrHomi(CrimInfo):
    def __init__(self, crimID, crimName, crimDoB, crimGen, crimDn):
        super().__init__(crimID, crimName, crimDoB, crimGen, crimDn)
        self.__cdh = (crimDn.get() + " has been done. \n It is the ultimate crime and \nhas ripple effects that go far beyond \nthe original loss of human life")
    def sayCrm(self):
        print(self.__cdh)
        Label(center_frame, text=self.__cdh, bg="Orange").place(x = 180, y = 450, relheight=.15, relwidth=.6)
class sxlhrssr(CrimInfo):
    def __init__(self, crimID, crimName, crimDoB, crimGen, crimDn):
        super().__init__(crimID, crimName, crimDoB, crimGen, crimDn)
        self.__cds = (crimDn.get() + " has been done. \nIt is an act or a series of acts involving\n any unwelcome sexual advance, request or\n" 
        , " demand for a sexual favor\n, or other verbal or physical behavior\n of a sexual nature")
    def sayCrm(self):
        print(self.__cds)
        Label(center_frame, text=self.__cds, bg="Orange").place(x = 180, y = 450, relheight=.15, relwidth=.6)
class thft(CrimInfo):
    def __init__(self, crimID, crimName, crimDoB, crimGen, crimDn):
        super().__init__(crimID, crimName, crimDoB, crimGen, crimDn)
        self.__cdt = (crimDn.get() + " has been done. \nTaking a person's property involves\n taking possession or control of property\n that rightfully belongs to someone else")
    def sayCrm(self):
        print(self.__cdt)
        Label(center_frame, text=self.__cdt, bg="Orange").place(x = 180, y = 450, relheight=.15, relwidth=.6)
class cybr(CrimInfo):
    def __init__(self, crimID, crimName, crimDoB, crimGen, crimDn):
        super().__init__(crimID, crimName, crimDoB, crimGen, crimDn)
        self.__cdc = (crimDn.get() + " has been done. \nCriminal activities carried out by means of \ncomputers or the internet.")
    def sayCrm(self):
        print(self.__cdc)
        Label(center_frame, text=self.__cdc, bg="Orange").place(x = 180, y = 450, relheight=.15, relwidth=.6)

connector = sqlite3.connect('Criminal Profiler.db')
cursor = connector.cursor()
connector.execute(
"CREATE TABLE IF NOT EXISTS CRIMINAL_PROFILER (CRIMINAL_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, ID TEXT, NAME TEXT, DOB TEXT, GENDER TEXT, CRIME TEXT)"
)
# Functions
def emptyEntry():
   global crimID, crimName, crimDoB, crimGen, crimDn
   for i in ['crimID', 'crimName', 'crimGen', 'crimDn']:
       exec(f"{i}.set('')")
   crimDoB.set_date(datetime.datetime.now().date())
def resDb():
   global tree
   tree.delete(*tree.get_children())
   emptyEntry()
def display_records():
   tree.delete(*tree.get_children())
   curr = connector.execute('SELECT * FROM CRIMINAL_PROFILER')
   data = curr.fetchall()
   for records in data:
       tree.insert('', END, values=records)
def addData():
   global crimID, crimName, crimDoB, crimGen, crimDn
   ID = crimID.get()
   Name = crimName.get()
   Gender = crimGen.get()
   Crime = crimDn.get()
   DOB = crimDoB.get_date()
   if not ID or not Name or not Gender or not Crime or not DOB :
       mb.showerror('Error!', "Please fill all the missing fields!!")
   else:
       try:
           connector.execute(
           'INSERT INTO CRIMINAL_PROFILER (ID, Name, DoB, Gender, Crime) VALUES (?,?,?,?,?)', (ID, Name, DOB, Gender, Crime)
           )
           connector.commit()
           mb.showinfo('Record added', f"Record of {Name} was successfully added")
           emptyEntry()
           display_records()
           center_frame.update()
       except:
           mb.showerror('Wrong type', 'The type of the values entered is not accurate. Pls note that the contact field can only contain numbers')
def showCrm():
    if crimDn.get() == "Murder/Violence":
        showcrm = mrdrHomi(crimID, crimName, crimDoB, crimGen, crimDn)
        showcrm.sayCrm()
    elif crimDn.get() == "Sexual Harassment":
        showcrm = sxlhrssr(crimID, crimName, crimDoB, crimGen, crimDn)
        showcrm.sayCrm()
    elif crimDn.get() == "Theft":
        showcrm = thft(crimID, crimName, crimDoB, crimGen, crimDn)
        showcrm.sayCrm()
    else:
        showcrm = cybr(crimID, crimName, crimDoB, crimGen, crimDn)
        showcrm.sayCrm()
def remData():
   if not tree.selection():
       mb.showerror('Error!', 'Please select an item from the database')
   else:
       current_item = tree.focus()
       values = tree.item(current_item)
       selection = values["values"]
       tree.delete(current_item)
       connector.execute('DELETE FROM CRIMINAL_PROFILER WHERE STUDENT_ID=%d' % selection[0])
       connector.commit()
       mb.showinfo('Done', 'The record you wanted deleted was successfully deleted.')
       display_records()
def viewData():
   global crimID, crimName, crimDoB, crimGen, crimDn
   current_item = tree.focus()
   values = tree.item(current_item)
   selection = values["values"]
   date = datetime.date(int(selection[3][:4]), int(selection[3][5:7]), int(selection[3][8:]))
   crimID.set(selection[1]); crimName.set(selection[2]); crimDoB.set_date(date)
   crimGen.set(selection[4]); crimDn.set(selection[5])
   
main = Tk()
main.title('Criminal Profiler')
main.geometry('1420x780')
main.resizable(0, 0)

lf_bg = 'Gray' 
cf_bg = 'Dark Gray' 
labelfont = ('Arial', 9)

crimID = StringVar()
crimName = StringVar()
crimDoB = StringVar()
crimGen = StringVar()
crimDn = StringVar()
# Window
Label(main, text="Criminal DTBS", bg='Gray').pack(side=TOP, fill=X)
left_frame = Frame(main, bg=lf_bg)
left_frame.place(x=0, y=30, relheight=1, relwidth=0.1)
center_frame = Frame(main, bg=cf_bg)
center_frame.place(relx=0.1, y=30, relheight=1, relwidth=0.3)
right_frame = Frame(main, bg="Gray35")
right_frame.place(relx=0.4, y=30, relheight=1, relwidth=0.6)

Label(left_frame, text="Criminal ID: ", bg = 'Orange').place(
        x = 5, y = 15, relheight=.05, relwidth=.8)
Label(left_frame, text="Criminal Name: ", bg = 'Orange').place(
        x = 5, y = 115, relheight=.05, relwidth=.8)
Label(left_frame, text="Criminal DoB: ", bg = 'Orange').place(
        x = 5, y = 215, relheight=.05, relwidth=.8)
Label(left_frame, text="Criminal Gender: ", bg = 'Orange').place(
        x = 5, y = 315, relheight=.05, relwidth=.8)
Label(left_frame, text="Crime Done: ", bg = 'Orange').place(
        x = 5, y = 615, relheight=.05, relwidth=.8)        
Entry(center_frame, width=50, textvariable=crimID).place(
        x = 25, y = 15, relheight=.05, relwidth=.8)
Entry(center_frame, width=50, textvariable=crimName).place(
        x = 25, y = 115, relheight=.05, relwidth=.8)
Entry(center_frame, width=50, textvariable=crimGen).place(
        x = 25, y = 315, relheight=.05, relwidth=.8)
crimDoB = DateEntry(center_frame, font=("Arial", 12), width=15)
crimDoB.place(x=25, rely=0.29)
algmenu2 = ttk.Combobox(
    center_frame, textvariable=crimDn, values=["Murder/Violence", "Sexual Harassment", "Theft", "Cyberattack"])
algmenu2.place(x = 25, y = 615, relheight=.05, relwidth=.8)
algmenu2.current(0)

Button(center_frame, text='Input Data', font=labelfont, command=addData, width=18).place(relx=0.025, rely=0.85)
Button(center_frame, text='Delete Data', font=labelfont, command=remData, width=15).place(relx=0.1, rely=0.50)
Button(center_frame, text='View Data', font=labelfont, command=viewData, width=15).place(relx=0.1, rely=0.56)
Button(center_frame, text='Reset Fields', font=labelfont, command=emptyEntry, width=15).place(relx=0.1, rely=0.63)
Button(center_frame, text='Reset Form', font=labelfont, command=resDb, width=15).place(relx=0.1, rely=0.70)
Button(center_frame, text='Show Crime', font=labelfont, command=showCrm, width=15).place(relx=0.4, rely=0.50)
Label(right_frame, text='Criminal Records', font=labelfont, bg='DarkGreen', fg='LightCyan').pack(side=TOP, fill=X)
tree = ttk.Treeview(right_frame, height=100, selectmode=BROWSE,
                   columns=('No.', 'Criminal ID', "Criminal Name", "Date of Birth", "Gender", "Crime"))
X_scroller = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
Y_scroller = Scrollbar(tree, orient=VERTICAL, command=tree.yview)
X_scroller.pack(side=BOTTOM, fill=X)
Y_scroller.pack(side=RIGHT, fill=Y)
tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)
tree.heading('No.', text='No', anchor=CENTER)
tree.heading('Criminal ID', text='Criminal ID', anchor=CENTER)
tree.heading('Criminal Name', text='Name', anchor=CENTER)
tree.heading('Date of Birth', text='DOB', anchor=CENTER)
tree.heading('Gender', text='Gender', anchor=CENTER)
tree.heading('Crime', text='Crime', anchor=CENTER)
tree.column('#0', width=0, stretch=NO)
tree.column('#1', width=40, stretch=NO)
tree.column('#2', width=140, stretch=NO)
tree.column('#3', width=200, stretch=NO)
tree.column('#4', width=80, stretch=NO)
tree.column('#5', width=80, stretch=NO)
tree.place(y=30, relwidth=1, relheight=0.9, relx=0)
display_records()
# Finalize
main.update()
main.mainloop()



#File Transfer Project
#Functions of GUI & Database
#Author: Becky Blue
#Py 3.6.1
#Functions w/db record


from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter as ttk
from datetime import *
from datetime import timedelta
import shutil
import os
import sqlite3


import GUI_Master
import GUI_Main


#Center window
def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()

    x = int((screen_width/2)-(w/2))
    y = int((screen_height/2)-(h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo


#Exit'X'
def ask_quit(self):
    if messagebox.askokcancel("Exit Program", "Are you sure you want to exit?"):
        self.master.destroy()
        os._exit(0)


#From and To folders
def browse_folder_from(self):
    browse_dir = filedialog.askdirectory()
    self.entry_transfer_from.delete(0,END)
    self.entry_transfer_from.insert(0,browse_dir)

def browse_folder_to(self):
    browse_dir = filedialog.askdirectory()
    self.entry_transfer_to.delete(0,END)
    self.entry_transfer_to.insert(0,browse_dir)


#Get rrr done
def run_file_transfer(self):

    src = self.entry_transfer_from.get()#From entry
    dest = self.entry_transfer_to.get()#To entry

    if os.path.exists(src) and os.path.exists(dest) and src != dest:#files must be different
        currentTime = datetime.now()
        twentyFourHoursAgo = currentTime + timedelta(hours=-24)#pull files from last #24hrs
        files = [f for f in os.listdir(src) if os.path.isfile(os.path.join(src,f))]

        for f in files:
            src_file = src + '\\' + f
            lastModUnix = os.path.getmtime(src_file)
            lastMod = datetime.fromtimestamp(int(lastModUnix))
            if lastMod >= twentyFourHoursAgo:
                dest_file = dest + '\\' + f
                shutil.copy(src_file, dest_file)
        update_last_run_time(self,currentTime)#See when last transfer happened
        messagebox.showinfo("File Transfer Complete", "UPDATE Complete")
    else:
        if src == dest:
            messagebox.showerror("Invalid Entry", "'From' and 'To' folders can not be the same. ")
        else:
            messagebox.showerror("Invalid directory", "Invalid directory")

#Database Create/Update
def create_db(self):
    conn = sqlite3.connect('last_run_time.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_last_run( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_month INT, \
            col_day INT, \
            col_year INT, \
            col_hour INT, \
            col_min INT, \
            col_sec INT \
            );")
        conn.commit()
    conn.close()
    check_for_records(self)


def check_for_records(self):
    conn = sqlite3.connect('last_run_time.db')
    with conn:
        cur = conn.cursor()
        cur, count = count_records(cur)
        if count > 0:
            get_last_run(self,cur)

def count_records(cur):
    count = ""
    cur.execute("SELECT COUNT(*) FROM tbl_last_run")#last updated
    count = cur.fetchone()[0]
    return cur, count


def get_last_run(self,cur):
    cur.execute("SELECT *, MAX(ID) FROM tbl_last_run GROUP BY ID ORDER BY ID DESC")#organize table
    lr = cur.fetchall()[0]

    #fix time to 12hr clock
    amPm = 'AM'
    hour = int(lr[4])
    if hour > 12:
        hour = hour - 12
        amPm = 'PM'
    last_run = '{}-{}-{} {}:{}:{} {}'.format(str(lr[1]).zfill(2),str(lr[2]).zfill(2),lr[3],str(hour).zfill(2),str(lr[5]).zfill(2),str(lr[6]).zfill(2),amPm)
    self.lr_time.set(last_run)


def update_last_run_time(self,currentTime):
    conn = sqlite3.connect('last_run_time.db')
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_last_run (col_month,col_day,col_year,col_hour,col_min,col_sec)\
                    VALUES(?,?,?,?,?,?)",(currentTime.month,currentTime.day,currentTime.year,currentTime.hour,currentTime.minute,currentTime.second))
    create_db(self)





if __name__ == "__main__":
    pass

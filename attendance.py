from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x720+0+0")
        self.root.title("Student Details")

        # ==================== variables =================
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # Image 0
        img = Image.open("./assets/smart-attendance.jpg")
        img = img.resize((600, 200), Image.ADAPTIVE)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=600, height=200)

        # Image 1
        img1 = Image.open("./assets/stud.jpg")
        img1 = img1.resize((600, 200), Image.ADAPTIVE)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=600, y=0, width=600, height=200)

        # Background Image
        img3 = Image.open("./assets/background-img.jpg")
        img3 = img3.resize((1200, (720 - 130)), Image.ADAPTIVE)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1200, height=(720 - 130))

        # Software Title Text
        title_lbl = Label(
            bg_img,
            text="ATTENDANCE MANAGEMENT SYSTEM",
            font=("Times new roman", 28, "bold"),
            bg="white",
            fg="darkblue",
        )
        title_lbl.place(x=0, y=0, width=1200, height=40)

        # Making frame
        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=20, y=55, width=(1200 - 40), height=(600 - 100))

        # left lable frame
        Left_frame = LabelFrame(
            main_frame,
            bd=2,
            relief=RIDGE,
            text="Student Details",
            font=("Times new roman", 12, "bold"),
        )
        Left_frame.place(x=10, y=10, width=560, height=480)

        # Left frame image top
        img_left = Image.open("./assets/AdobeStock_303989091.jpeg")
        img_left = img_left.resize((545, 130), Image.ADAPTIVE)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=545, height=130)

        left_inside_frame = Frame(Left_frame, bd=2,relief=RIDGE)
        left_inside_frame.place(x=2, y=135, width=(550), height=(300))

        # Label and Entries
        # Attendance ID
        student_ID_label = Label(
            left_inside_frame, text="Student ID", font=("Times new roman", 12, "bold")
        )
        student_ID_label.grid(row=0, column=0, padx=5, sticky=W)

        student_id_entry = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_atten_id,
            width=17,
            font=("Times new roman", 12, "bold"),
        )
        student_id_entry.grid(row=0, column=1, padx=5, sticky=W)

        # Department
        department_label = Label(
            left_inside_frame,
            text="Department: ",
            font=("Times new roman", 12, "bold"),
        )
        department_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        atten_department = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_atten_roll,
            width=17,
            font=("Times new roman", 12, "bold"),
        )
        atten_department.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # Name
        nameLabel = Label(
            left_inside_frame, text="Name:", font=("Times new roman", 12, "bold")
        )
        nameLabel.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        atten_name = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_atten_name,
            width=17,
            font=("Times new roman", 12, "bold"),
        )
        atten_name.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Department
        courseLabel = Label(
            left_inside_frame, text="Course:", font=("Times new roman", 12, "bold")
        )
        courseLabel.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        atten_course = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_atten_dep,
            width=17,
            font=("Times new roman", 12, "bold"),
        )
        atten_course.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # Time
        timeLabel = Label(
            left_inside_frame, text="Time:", font=("Times new roman", 12, "bold")
        )
        timeLabel.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        atten_time = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_atten_time,
            width=17,
            font=("Times new roman", 12, "bold"),
        )
        atten_time.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        # Date
        dateLabel = Label(
            left_inside_frame, text="Date:", font=("Times new roman", 12, "bold")
        )
        dateLabel.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        atten_date = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_atten_date,
            width=17,
            font=("Times new roman", 12, "bold"),
        )
        atten_date.grid(row=2, column=3, padx=5, pady=5, sticky=W)
        
        # Attendance Status
        attendanceLabel = Label(
            left_inside_frame, text="Attendance Status", font=("Times new roman", 12, "bold")
        )
        attendanceLabel.grid(row=3, column=0)

        atten_status = ttk.Combobox(
            left_inside_frame,
            textvariable=self.var_atten_attendance,
            font=("Times new roman", 12, "bold"),
            width=17,
            state="readonly",
        )
        atten_status["values"] = (
            "Select Status",
            "Present",
            "Absent"
        )
        atten_status.current(0)
        atten_status.grid(row=3, column=1)

        # Button Frame
        btn_frame = Frame(left_inside_frame, bd=0, relief=RIDGE)
        btn_frame.place(x=5, y=140, width=535, height=50)

        button_width = 12

        # Import CSV
        update_btn = Button(
            btn_frame,
            text="Import CSV",
            command=self.importCsv,
            width=button_width,
            font=("Times new roman", 12, "bold"),
            bg="grey",
            fg="white",
        )
        update_btn.grid(row=0, column=1, padx=5, pady=5)

        # Export button
        reset_btn = Button(
            btn_frame,
            text="Export CSV",
            command=self.exportCsv,
            width=button_width,
            font=("Times new roman", 12, "bold"),
            bg="grey",
            fg="white",
        )
        reset_btn.grid(row=0, column=2, padx=5, pady=5)

        # Update button
        take_photo_btn = Button(
            btn_frame,
            text="Update",
            # command=self.generate_dataset,
            width=button_width,
            font=("Times new roman", 12, "bold"),
            bg="grey",
            fg="white",
        )
        take_photo_btn.grid(row=0, column=3, padx=5, pady=5)

        # Reset button
        take_sample_btn = Button(
            btn_frame,
            text="Reset",
            command=self.reset_data,
            width=button_width,
            font=("Times new roman", 12, "bold"),
            bg="grey",
            fg="white",
        )
        take_sample_btn.grid(row=0, column=4)


        # Right label frame
        Right_frame = LabelFrame(
            main_frame,
            bd=2,
            relief=RIDGE,
            text="Attendance Details",
            font=("Times new roman", 12, "bold"),
        )
        Right_frame.place(x=580, y=10, width=560, height=480)

        table_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=550,height=445)

        # ========= scroll bar table ========================
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,columns=("roll","department","name","course","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        # self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("course",text="Course")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"] = "headings"
        # self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("course",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)



    # =================== Fetch Data ========================
    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

     # =========== Import CSV ==================
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(
            initialdir = os.getcwd(),
            title="Open CSV", 
            filetypes=(("CSV File","*.csv"),("All File","*.*")),
            parent=self.root
            )
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    # =========== Export CSV ==================
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to export", parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Open CSV", 
                filetypes=(("CSV File","*.csv"),("All File","*.*")),
                parent=self.root
                )
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+ os.path.basename(fln)+" successfully.")
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parernt=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows [2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows [5])
        self.var_atten_attendance. set (rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance. set ("")
            


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()

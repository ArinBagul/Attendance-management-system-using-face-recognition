from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    # ===================== Add Data ========================
    def add_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_name == ""
            or self.var_std_id == ""
        ):
            messagebox.showerror("Error", "All fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="your_host_name",
                    username="your_mysql_username",
                    password="your_password",
                    database="your_database_name",
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_id.get(),
                        self.var_std_name.get(),
                        self.var_sec.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_radio1.get()
                    ),
                )

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success",
                    "Student details has been added successfully",
                    parent=self.root,
                )

            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)

    # ==================== Fetch Data =====================
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="1234",
            database="face_recognizer",
        )
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ============ get cursor ==============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_sec.set(data[6]),
        self.var_email.set(data[7]),
        self.var_phone.set(data[8]),
        self.var_radio1.set(data[9])

    # =============== Update Function ===============
    def update_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_name == ""
            or self.var_std_id == ""
        ):
                messagebox.showerror("Error", "All fields are Required", parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update", "Do you want to update students details", parent=self.root)
                if Update>0:
                        conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="1234",
                        database="face_recognizer",
                        )
                        my_cursor = conn.cursor()
                        my_cursor.execute("update student set Dep=%s,course=%s,year=%s,semester=%s,name=%s,sec=%s,email=%s,phone=%s,PhotoSample=%s where student_id=%s",(
                                self.var_dep.get(),
                                self.var_course.get(),
                                self.var_year.get(),
                                self.var_semester.get(),
                                self.var_std_name.get(),
                                self.var_sec.get(),
                                self.var_email.get(),
                                self.var_phone.get(),
                                self.var_radio1.get(),
                                self.var_std_id.get() # primary key
                        ))
                else:
                     if not Update:
                                return
                messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                 messagebox.showerror("Error", f"Due to:{str(es)}",parent=self.root)

    # ================= delete function ================
    def delete_data(self):
        if self.var_std_id.get()=="":
              messagebox.showerror("Error", "Student ID must required", parent=self.root)
        else:
             try:
                delete=messagebox.askyesno("Delete Student Details", "Do you want to delete this student", parent=self.root )
                if delete>0:
                        conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="1234",
                        database="face_recognizer",
                        )
                        my_cursor = conn.cursor()
                        sql="delete from student where student_id=%s"
                        val=(self.var_std_id.get(),)
                        my_cursor.execute(sql,val)
                else:
                       if not delete:
                            return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("delete", "Successfully deleted student detail", parent=self.root)
                       
                  
             except Exception as es:
                  messagebox.showerror("Error", f"Due to:{str(es)}",parent=self.root)

    # ========== Reset Data ===========
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_sec.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_radio1.set("")


    # ===================== GENERATE DATA SET - TAKE PHOTO SAMPLE ===================
    def generate_dataset(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_name == ""
            or self.var_std_id == ""
        ):
                messagebox.showerror("Error", "All fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="1234",
                        database="face_recognizer",
                )
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id=0
                dataset_id = self.var_std_id.get()
                for x in myresult:
                     id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,year=%s,semester=%s,name=%s,sec=%s,email=%s,phone=%s,PhotoSample=%s where student_id=%s",(
                                self.var_dep.get(),
                                self.var_course.get(),
                                self.var_year.get(),
                                self.var_semester.get(),
                                self.var_std_name.get(),
                                self.var_sec.get(),
                                self.var_email.get(),
                                self.var_phone.get(),
                                self.var_radio1.get(),
                                self.var_std_id.get() # primary key
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # =========== Load OpenCV Frontal face data ============

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor = 1.3
                    # minimum neighbour = 5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h, x:x+w]
                        return face_cropped
                    
                cap = cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret, my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="dataset/user."+str(dataset_id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed")

            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}",parent=self.root)

                    
                




    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x720+0+0")
        self.root.title("Student Details")

        # ============variables=================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_sec = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_radio1 = StringVar()

        # Image 0
        img = Image.open("./assets/face-recognition.png")
        img = img.resize((400, 130), Image.ADAPTIVE)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=400, height=130)

        # Image 1
        img1 = Image.open("./assets/facialrecognition.png")
        img1 = img1.resize((400, 130), Image.ADAPTIVE)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=400, y=0, width=400, height=130)

        # Image 2
        img2 = Image.open("./assets/facial-recognition_0.jpg")
        img2 = img2.resize((400, 130), Image.ADAPTIVE)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=800, y=0, width=400, height=130)

        # Background Image
        img3 = Image.open("./assets/background-img.jpg")
        img3 = img3.resize((1200, (720 - 130)), Image.ADAPTIVE)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1200, height=(720 - 130))

        # Software Title Text
        title_lbl = Label(
            bg_img,
            text="STUDENT MANAGEMENT SYSTEM",
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

        # current course
        current_course_frame = LabelFrame(
            Left_frame,
            bd=2,
            relief=RIDGE,
            text="Current Course Information",
            font=("Times new roman", 12, "bold"),
        )
        current_course_frame.place(x=5, y=135, width=550, height=100)

        # Department
        dep_label = Label(
            current_course_frame,
            text="Department",
            font=("Times new roman", 12, "bold"),
        )
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_dep,
            font=("Times new roman", 12, "bold"),
            width=17,
            state="readonly",
        )
        dep_combo["values"] = ("Select Department", "CSE", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Course
        course_label = Label(
            current_course_frame, text="Course", font=("Times new roman", 12, "bold")
        )
        course_label.grid(row=0, column=2, padx=5, sticky=W)

        course_combo = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_course,
            font=("Times new roman", 12, "bold"),
            width=17,
            state="readonly",
        )
        course_combo["values"] = (
            "Select Course",
            "B.E./B.Tech.",
            "BCA",
            "B. Sc.",
            "BBA",
            "M.E./M.Tech.",
            "MCA",
            "M.Sc.",
            "MBA",
        )
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # Year
        year_label = Label(
            current_course_frame, text="Year", font=("Times new roman", 12, "bold")
        )
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_year,
            font=("Times new roman", 12, "bold"),
            width=17,
            state="readonly",
        )
        year_combo["values"] = ("Select Year", "1st", "2nd", "3rd", "4th")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Semester
        semester_label = Label(
            current_course_frame, text="Semester", font=("Times new roman", 12, "bold")
        )
        semester_label.grid(row=1, column=2, padx=5, sticky=W)

        semester_combo = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_semester,
            font=("Times new roman", 12, "bold"),
            width=17,
            state="readonly",
        )
        semester_combo["values"] = (
            "Select Semester",
            "1st",
            "2nd",
            "3rd",
            "4th",
            "5th",
            "6th",
            "7th",
            "8th",
        )
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # Class Student Information
        class_student_frame = LabelFrame(
            Left_frame,
            bd=2,
            relief=RIDGE,
            text="Current Course Information",
            font=("Times new roman", 12, "bold"),
        )
        class_student_frame.place(x=5, y=240, width=550, height=215)

        # Student ID
        studentId_label = Label(
            class_student_frame, text="Student ID", font=("Times new roman", 12, "bold")
        )
        studentId_label.grid(row=0, column=0, padx=5, sticky=W)

        Student_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_std_id,
            width=17,
            font=("Times new roman", 12, "bold"),
        )
        Student_entry.grid(row=0, column=1, padx=5, sticky=W)

        # Student name
        studentName_label = Label(
            class_student_frame,
            text="Student Name",
            font=("Times new roman", 12, "bold"),
        )
        studentName_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        StudentName_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_std_name,
            width=17,
            font=("Times new roman", 12, "bold"),
        )
        StudentName_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # class Section
        section_label = Label(
            class_student_frame, text="Section", font=("Times new roman", 12, "bold")
        )
        section_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        section_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_sec,
            width=17,
            font=("Times new roman", 12, "bold"),
        )
        section_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Email
        email_label = Label(
            class_student_frame, text="Email", font=("Times new roman", 12, "bold")
        )
        email_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        email_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_email,
            width=17,
            font=("Times new roman", 12, "bold"),
        )
        email_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # Phone
        phone_label = Label(
            class_student_frame, text="Phone", font=("Times new roman", 12, "bold")
        )
        phone_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        phone_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_phone,
            width=17,
            font=("Times new roman", 12, "bold"),
        )
        phone_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        # radio buttons
        radiobtn1 = ttk.Radiobutton(
            class_student_frame,
            text="Take Sample",
            variable=self.var_radio1,
            value="Yes",
        )
        radiobtn1.grid(row=3, column=0, padx=5, pady=5)
        radiobtn2 = ttk.Radiobutton(
            class_student_frame, text="No Sample", variable=self.var_radio1, value="No"
        )
        radiobtn2.grid(row=3, column=1, padx=5, pady=5)

        # save button (add to database)
        save_btn = Button(
            class_student_frame,
            text="Save",
            command=self.add_data,
            width=10,
            font=("Times new roman", 12, "bold"),
            bg="green",
            fg="white",
        )
        save_btn.grid(row=3, column=2, padx=5, pady=5)

        # Delete button
        delete_btn = Button(
            class_student_frame,
            text="Delete",
            command=self.delete_data,
            width=10,
            font=("Times new roman", 12, "bold"),
            bg="red",
            fg="white",
        )
        delete_btn.grid(row=3, column=3, padx=5, pady=5)

        # Button Frame
        btn_frame = Frame(class_student_frame, bd=0, relief=RIDGE)
        btn_frame.place(x=5, y=140, width=535, height=50)

        # update button
        update_btn = Button(
            btn_frame,
            text="Update",
            command=self.update_data,
            width=10,
            font=("Times new roman", 12, "bold"),
            bg="grey",
            fg="white",
        )
        update_btn.grid(row=0, column=1, padx=5, pady=5)

        # Reset button
        reset_btn = Button(
            btn_frame,
            text="Reset",
            command=self.reset_data,
            width=10,
            font=("Times new roman", 12, "bold"),
            bg="grey",
            fg="white",
        )
        reset_btn.grid(row=0, column=2, padx=5, pady=5)

        # Take Photo Sample button
        take_photo_btn = Button(
            btn_frame,
            text="Take photo Sample",
            command=self.generate_dataset,
            width=15,
            font=("Times new roman", 12, "bold"),
            bg="grey",
            fg="white",
        )
        take_photo_btn.grid(row=0, column=3, padx=5, pady=5)
        # Update button
        take_sample_btn = Button(
            btn_frame,
            text="Update photo sample",
            width=16,
            font=("Times new roman", 12, "bold"),
            bg="grey",
            fg="white",
        )
        take_sample_btn.grid(row=0, column=4)

        # Right lable frame
        Right_frame = LabelFrame(
            main_frame,
            bd=2,
            relief=RIDGE,
            text="Student Details",
            font=("Times new roman", 12, "bold"),
        )
        Right_frame.place(x=580, y=10, width=560, height=480)

        img_right = Image.open("./assets/AdobeStock_303989091.jpeg")
        img_right = img_right.resize((545, 130), Image.ADAPTIVE)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=545, height=130)

        # ========== SEARCH SYSTEM ============
        search_frame = LabelFrame(
            Right_frame,
            bd=2,
            relief=RIDGE,
            text="Search System",
            font=("Times new roman", 12, "bold"),
        )
        search_frame.place(x=5, y=135, width=550, height=70)

        search_label = Label(
            search_frame, text="Search By:", font=("Times new roman", 12, "bold")
        )
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        search_combo = ttk.Combobox(
            search_frame,
            font=("Times new roman", 12, "bold"),
            width=17,
            state="readonly",
        )
        search_combo["values"] = ("Select", "Student ID", "Phone No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        search_entry = ttk.Entry(
            search_frame, width=17, font=("Times new roman", 12, "bold")
        )
        search_entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        # search button
        search_btn = Button(
            search_frame,
            text="Search",
            width=8,
            font=("Times new roman", 9, "bold"),
            bg="grey",
            fg="white",
        )
        search_btn.grid(row=0, column=3)

        # show all button
        showAll_btn = Button(
            search_frame,
            text="Show All",
            width=8,
            font=("Times new roman", 9, "bold"),
            bg="grey",
            fg="white",
        )
        showAll_btn.grid(row=0, column=4)

        # ============== Table Frame ===============
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=210, width=550, height=240)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame,
            columns=(
                "dep",
                "course",
                "year",
                "sem",
                "id",
                "name",
                "sec",
                "email",
                "phone",
                "photo",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="course")
        self.student_table.heading("year", text="year")
        self.student_table.heading("sem", text="semester")
        self.student_table.heading("id", text="student id")
        self.student_table.heading("name", text="name")
        self.student_table.heading("sec", text="section")
        self.student_table.heading("email", text="email")
        self.student_table.heading("phone", text="phone no.")
        self.student_table.heading("photo", text="photo status")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("sec", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()

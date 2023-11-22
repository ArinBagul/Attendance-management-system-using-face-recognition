from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os

from student import Student
from train import Train
from face_recognition import Face_Recognition


class Face_Recognition_System:
    def open_img(self):
        os.startfile("dataset")

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x720+0+0")
        self.root.title("Face Recognition System")

        # Image 0
        img = Image.open("./assets/BestFacialRecognition.jpg")
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
        img2 = Image.open("./assets/images.jpg")
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
            text="FACE RECOGNITION SYSTEM FOR ATTENDANCE",
            font=("Times new roman", 28, "bold"),
            bg="white",
            fg="red",
        )
        title_lbl.place(x=0, y=0, width=1200, height=40)

        # Adding Buttons
        # Top Buttons
        # Student button
        img4 = Image.open("./assets/student-btn1.jpg")
        img4 = img4.resize((150, 150), Image.ADAPTIVE)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(
            bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2"
        )
        b1.place(x=100, y=100, width=150, height=150)

        b1_1 = Button(
            bg_img,
            text="Student Details",
            command=self.student_details,
            font=("Times new roman", 14, "bold"),
            bg="darkblue",
            fg="white",
            cursor="hand2",
        )
        b1_1.place(x=100, y=260, width=150, height=30)

        # Detect face
        img5 = Image.open("./assets/face_detector1.jpg")
        img5 = img5.resize((150, 150), Image.ADAPTIVE)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.face_data)
        b2.place(x=350, y=100, width=150, height=150)

        b2_1 = Button(
            bg_img,
            text="Face Detector",
            font=("Times new roman", 14, "bold"),
            bg="darkblue",
            fg="white",
            cursor="hand2",
            command=self.face_data
        )
        b2_1.place(x=350, y=260, width=150, height=30)

        # Attendance button
        img6 = Image.open("./assets/report.jpg")
        img6 = img6.resize((150, 150), Image.ADAPTIVE)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b3.place(x=600, y=100, width=150, height=150)

        b3_1 = Button(
            bg_img,
            text="Attendance",
            font=("Times new roman", 14, "bold"),
            bg="darkblue",
            fg="white",
            cursor="hand2",
        )
        b3_1.place(x=600, y=260, width=150, height=30)

        # Help desk button
        img7 = Image.open("./assets/help-desk.jpg")
        img7 = img7.resize((150, 150), Image.ADAPTIVE)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b4 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b4.place(x=850, y=100, width=150, height=150)

        b4_1 = Button(
            bg_img,
            text="Help Desk",
            font=("Times new roman", 14, "bold"),
            bg="darkblue",
            fg="white",
            cursor="hand2",
        )
        b4_1.place(x=850, y=260, width=150, height=30)

        # Bottom Buttons
        # Train button
        img8 = Image.open("./assets/Train.jpg")
        img8 = img8.resize((150, 150), Image.ADAPTIVE)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.train_data)
        b5.place(x=100, y=350, width=150, height=150)

        b5_1 = Button(
            bg_img,
            text="Train Data",
            font=("Times new roman", 14, "bold"),
            bg="darkblue",
            fg="white",
            cursor="hand2",
            command=self.train_data
        )
        b5_1.place(x=100, y=510, width=150, height=30)

        # Photos face
        img9 = Image.open("./assets/photos.jpg")
        img9 = img9.resize((150, 150), Image.ADAPTIVE)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b6 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.open_img)
        b6.place(x=350, y=350, width=150, height=150)

        b6_1 = Button(
            bg_img,
            text="Face Photos",
            font=("Times new roman", 14, "bold"),
            bg="darkblue",
            fg="white",
            cursor="hand2",
            command=self.open_img
        )
        b6_1.place(x=350, y=510, width=150, height=30)

        # Developer button
        img10 = Image.open("./assets/dev.jpg")
        img10 = img10.resize((150, 150), Image.ADAPTIVE)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b7 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        b7.place(x=600, y=350, width=150, height=150)

        b7_1 = Button(
            bg_img,
            text="Developer",
            font=("Times new roman", 14, "bold"),
            bg="darkblue",
            fg="white",
            cursor="hand2",
        )
        b7_1.place(x=600, y=510, width=150, height=30)

        # Exit button
        img11 = Image.open("./assets/exit.jpg")
        img11 = img11.resize((150, 150), Image.ADAPTIVE)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b8 = Button(bg_img, image=self.photoimg11, cursor="hand2")
        b8.place(x=850, y=350, width=150, height=150)

        b8_1 = Button(
            bg_img,
            text="Exit",
            font=("Times new roman", 14, "bold"),
            bg="darkblue",
            fg="white",
            cursor="hand2",
        )
        b8_1.place(x=850, y=510, width=150, height=30)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()

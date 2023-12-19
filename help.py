from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

class Help:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1200x720+0+0")
        self.root.title("face Recogniton System")

        title_lbl = Label(
            self.root,
            text="Help Desk",
            font=("Times new roman", 28, "bold"),
            bg="white",
            fg="darkblue",
        )
        title_lbl.place(x=0, y=0, width=1200, height=40)

        # Image
        img_top=Image.open(r"assets\helpDesk.jpeg")
        img_top=img_top.resize((1200, (720-40)), Image.ADAPTIVE)
        self.photoimg_top=ImageTk. PhotoImage(img_top)

        f_lbl=Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0,y=40,width=1200,height=(720-40))

        # Making frame
        main_frame = Frame(f_lbl, bd=2)
        main_frame.place(x=600, y=50, width=500, height=450)

        Developer_1 = Label(
            main_frame,
            text="Welcome to our Face Recognition Software Help Desk\nReach us at any of the following Email:\n\nen20cs302008@medicaps.ac.in\n\nen20cs302015@medicaps.ac.in\n\nen20cs302019@medicaps.ac.in",
            font=("Times new roman",15,"bold"),
            fg="darkblue"
        )
        Developer_1.place(x=10, y=100)


if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
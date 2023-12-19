from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

class Developer:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1200x720+0+0")
        self.root.title("face Recogniton System")

        title_lbl = Label(
            self.root,
            text="Developers",
            font=("Times new roman", 28, "bold"),
            bg="white",
            fg="darkblue",
        )
        title_lbl.place(x=0, y=0, width=1200, height=40)

        # Image
        img_top=Image.open(r"assets\dev.jpg")
        img_top=img_top.resize((1200, (720-40)), Image.ADAPTIVE)
        self.photoimg_top=ImageTk. PhotoImage(img_top)

        f_lbl=Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0,y=40,width=1200,height=(720-40))

        # Making frame
        main_frame = Frame(f_lbl, bd=2)
        main_frame.place(x=600, y=50, width=500, height=450)

        Developer_1 = Label(
            main_frame,
            text="Arin Bagul - EN20CS302008 \nCSE-CTIS",
            font=("Times new roman",16,"bold"),
            fg="darkblue"
        )
        Developer_1.place(x=100, y=100)

        Developer_2 = Label(
            main_frame,
            text="Eshanchi Bajpai - EN20CS302015 \nCSE-CTIS",
            font=("Times new roman",16,"bold"),
            fg="darkblue"
        )
        Developer_2.place(x=80, y=200)

        Developer_3 = Label(
            main_frame,
            text="Kamakshi Sharma - EN20CS302019 \nCSE-CTIS",
            font=("Times new roman",16,"bold"),
            fg="darkblue"
        )
        Developer_3.place(x=60, y=300)


if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
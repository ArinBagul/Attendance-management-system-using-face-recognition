from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
# import tensorflow as tf
# from tensorflow.keras import layers, models

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x720+0+0")
        self.root.title("Train Dataset")

        title_lbl = Label(
            self.root,
            text="Train Dataset",
            font=("Times new roman", 28, "bold"),
            bg="white",
            fg="darkblue",
        )
        title_lbl.place(x=0, y=0, width=1200, height=40)

        # Image
        img_top=Image.open(r"assets\facial_recognition_action.jpg")
        img_top=img_top.resize((1200, 325), Image.ADAPTIVE)
        self.photoimg_top=ImageTk. PhotoImage(img_top)

        f_lbl=Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0,y=40,width=1200,height=325)

        # Button
        b1_1 = Button(
            self.root,
            text="Train Data",
            command=self.train_classifier,
            font=("Times new roman", 22, "bold"),
            bg="darkblue",
            fg="white",
            cursor="hand2",
        )
        b1_1.place(x=0, y=365, width=1200, height=35)

        # Image
        img_bottom=Image.open(r"assets\Facialrecognition.png")
        img_bottom=img_bottom. resize((1200, 325), Image.ADAPTIVE)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=410,width=1200,height=325)



    def train_classifier(self):
        data_dir=("dataset")
        path=[ os.path.join(data_dir, file) for file in os.listdir(data_dir) ]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # grey scale image
            imageNp = np.array(img,'uint8')
            filename = os.path.split(image)[1]
            parts = filename.split(".")
                    
            
            id_string = parts[1]  # Assuming ID is the second part
            # Extract the last two characters as the ID
            id_string = id_string[-2:]

            # Convert the ID string to an integer
            id_integer = int(id_string)
            
            faces.append(imageNp)
            ids.append(id_string)  # Store the ID as a string
            # print(id_string)
            print("Extracted ID:", id_string)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids, dtype=np.int32)


        # ================ TRAIN THE CLASSIFIER AND SAVE ==================

        clf=cv2.face.LBPHFaceRecognizer.create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed")

    # def train_classifier(self):
    #     data_dir = "dataset"
    #     path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

    #     faces = []
    #     ids = []

    #     for image in path:
    #         img = Image.open(image).convert('L')  # Convert to grayscale
    #         imageNp = np.array(img, 'uint8')

    #         # Extract the numeric ID from the filename
    #         filename = os.path.split(image)[1]
    #         parts = filename.split(".")
            
    #         if len(parts) >= 3 and parts[0].startswith("user."):
    #             numeric_id = parts[1]  # Assuming ID is the second part
    #             try:
    #                 numeric_id = int(numeric_id)
    #                 faces.append(imageNp)
    #                 ids.append(numeric_id)
    #             except ValueError:
    #                 print(f"Invalid ID format in filename: {filename}")

    #         cv2.imshow("Training", imageNp)
    #         cv2.waitKey(1) == 13  # This line doesn't seem to have any effect

    #     if len(faces) < 2:
    #         print("Error: Insufficient training data. You need at least two samples.")
    #         return

    #     ids = np.array(ids)

    #     # ================ TRAIN THE CLASSIFIER AND SAVE ==================

    #     clf = cv2.face_LBPHFaceRecognizer.create()
    #     clf.train(faces, ids)
    #     clf.save("classifier.xml")  # Use save() instead of write()
    #     cv2.destroyAllWindows()
    #     messagebox.showinfo("Result", "Training dataset completed")


        # model = models.Sequential([
        #     layers.Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 1)),
        #     layers.MaxPooling2D((2, 2)),
        #     layers.Conv2D(64, (3, 3), activation='relu'),
        #     layers.MaxPooling2D((2, 2)),
        #     layers.Flatten(),
        #     layers.Dense(128, activation='relu'),
        #     layers.Dense(ids, activation='softmax')  # 'num_classes' is the number of unique face IDs
        # ])

        # # Compile the model
        # model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

        # # Load and preprocess face images from your dataset
        # # Train the model with your dataset

        # # Save the trained model
        # model.save("face_recognition_model.h5")





if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()

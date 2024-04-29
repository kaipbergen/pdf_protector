from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox
from PyPDF2 import PdfFileWriter, PdfFileReader
import os
from PyPDF2 import PdfReader, PdfWriter

root = tk.Tk()
root.title("PDF protector")
root.geometry("600x430+300+100")
root.resizable(False, False)

def browse():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), 
                                          title="Select PDF File",
                                          filetypes=(("PDF File", "*.pdf"), ("All Files", "*.*")))  
    entry1.delete(0, tk.END) 
    entry1.insert(tk.END, filename)  
    
    
def Protect():
    mainfile = source.get()
    protectfile = target.get()
    code = password.get()
    
    if mainfile == "" or protectfile == "" or code == "":
        messagebox.showerror("Invalid", "Please fill in all fields.")
    else:
        try:
            out = PdfWriter()
            file = PdfReader(mainfile)
            
            for page in file.pages:
                out.add_page(page)
                
            out.encrypt(code)
            
            with open(protectfile, "wb") as f:
                out.write(f)
            
            # Clearing the entry fields after successful operation
            source.set("")
            target.set("")
            password.set("")
            
            messagebox.showinfo("Success", "The PDF was successfully protected.")
        except Exception as e:  # This catches any exception and prints it out
            print("An error occurred: ", e)
            messagebox.showerror("Error", f"An error occurred: {e}")


 


img = Image.open("images/main.png")

img = img.resize((580, 125), Image.Resampling.LANCZOS)


# Convert the image to PhotoImage
top_image = ImageTk.PhotoImage(img)

# Create a Label to display the image, with no padding
label = tk.Label(root, image=top_image, bd=0)
label.pack(side="top", fill="x", padx=0, pady=0)

# Create a Frame with a groove relief
frame = tk.Frame(root, width=580, height=290, bd=5, relief=tk.GROOVE)
frame.place(x=10, y=130)

# Define the StringVar for source PDF file
source = tk.StringVar()

# Create a Label for the source PDF file
source_label = tk.Label(frame, text="Source PDF File:", font="arial 10 bold", fg="#4c4542")
source_label.place(x=30, y=50)

# Create an Entry for the source PDF file
entry1 = tk.Entry(frame, width=30, textvariable=source, font="arial 15", bd=1)
entry1.place(x=150, y=48)

# Define the StringVar for target PDF file
target = tk.StringVar()

# Create a Label for the target PDF file
target_label = tk.Label(frame, text="Target PDF File:", font="arial 10 bold", fg="#4c4542")
target_label.place(x=30, y=100)

# Create an Entry for the target PDF file
entry2 = tk.Entry(frame, width=30, textvariable=target, font="arial 15", bd=1)
entry2.place(x=150, y=100)

# Define the StringVar for the password
password = tk.StringVar()

# Create a Label for the password
password_label = tk.Label(frame, text="Set User Password:", font="arial 10 bold", fg="#4c4542")
password_label.place(x=15, y=150)

# Create an Entry for the password
entry3 = tk.Entry(frame, width=30, textvariable=password, font="arial 15", bd=1)
entry3.place(x=150, y=150)




Buton_image_path = "images/icon.png"
buton_img = Image.open(Buton_image_path)
buton_img = buton_img.resize((35, 24), Image.Resampling.LANCZOS)  # Resize
buton_icon = ImageTk.PhotoImage(buton_img)

# Create the button with the image
buton = tk.Button(frame, image=buton_icon, width=35, height=24, bg="#d3cdcd",command=browse)
buton.place(x=500, y=47)


buton.image = buton_icon





button_image_path = "images/icon.png" 
button_img = Image.open(button_image_path)
button_img = button_img.resize((95, 54), Image.Resampling.LANCZOS)  # Resize 
button_icon = ImageTk.PhotoImage(button_img)

# Create the button with the image
protect_button = tk.Button(root, text="Protect PDF File", compound=tk.LEFT, image=button_icon, width=242, height=50, bg="#d7d7d7", font="arial 14 bold", command=Protect)
protect_button.pack(side=tk.BOTTOM, pady=40)


protect_button.image = button_icon

root.mainloop()

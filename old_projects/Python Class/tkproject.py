import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("Daniel Derflinger - Developed in 2023")

label = tk.Label(root, text="Hello World!", font=("Arial", 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=("Arial", 16))
textbox.pack(padx=10)

root.mainloop()

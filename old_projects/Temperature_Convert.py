# Convert Celcius to Fahrenheit using GUI

# Import the tkinter module
import tkinter as tk

# Create the window
window = tk.Tk()

# Create the title for the window
window.title("Temperature Converter")

# Create the size of the window
window.geometry("400x400")

# Create the function to convert Celcius to Fahrenheit
def convert():
    celcius = float(entry.get())
    fahrenheit = celcius * 9 / 5 + 32
    label_3.config(text=fahrenheit)

# Create the label for the Celcius entry box
label_1 = tk.Label(text="Celcius")
label_1.grid(column=0, row=0)

# Create the entry box for the Celcius entry box
entry = tk.Entry()
entry.grid(column=1, row=0)

# Create the button to convert Celcius to Fahrenheit
button = tk.Button(text="Convert", command=convert)
button.grid(column=0, row=1)

# Create the label for the Fahrenheit entry box
label_2 = tk.Label(text="Fahrenheit")
label_2.grid(column=0, row=2)

# Create the label to close the window
label_3 = tk.Label(text="0")
label_3.grid(column=1, row=2)

# Create the main loop for the window
window.mainloop()

# End of program
"""
 Name: cylinder_calc_gui.py
 Author: Abbigail Rath
 Created: 10/29/24
 Purpose: Python program to calculate
 the surface area and volume of a cylinder while practicing with GUI
"""
# TODO: Import math module
import math
# TODO: Import tkinter for GUI
import tkinter as tk

# Write math.pi as pi so it's easier to write and remember
pi = math.pi


class CylinderCalculator:
    def __init__(self, master):
        # Create title for our program
        self.master = master
        master.title("Cylinder Calculator")

        # Set the size of the GUI window
        root.geometry("350x250") # Width of 400 pixels, Height of 400 pixels

        # Labels for our radius and creation for entry
        self.radius_label = tk.Label(master, text="Radius:", font=("Arial",20))
        self.radius_label.grid(row=0, column=0)
        self.radius_entry = tk.Entry(master)
        self.radius_entry.grid(row=0, column=1)

        # Labels for our height and entry creation
        self.height_label = tk.Label(master, text="Height:",font=("Arial",20))
        self.height_label.grid(row=1, column=0)
        self.height_entry = tk.Entry(master)
        self.height_entry.grid(row=1, column=1)

        # Creation for the button needed to calculate values for cylinder
        self.button = tk.Button(master, text="Calculate", command=self.calculate_values, font=("Arial",20))
        self.button.grid(row=2, column=1, columnspan=2)

        # Creation for volume label
        self.volume = tk.Label(master, text="")
        self.volume.grid(row=3, column=1, columnspan=2)

        # Creation for surface area label
        self.surface_area = tk.Label(master, text="")
        self.surface_area.grid(row=4, column=1, columnspan=2)
    
        # Creation of a clear button
        self.clear_info = tk.Button(master, text="Clear", command=self.clear, font=("Arial",20))
        self.clear_info.grid(row=5,column=1,columnspan=2)

    def calculate_values(self):
        # Use try and except to try the initial formulas for the program, printing out an error if 
        # a value entered is invalid
        try:
            radius = float(self.radius_entry.get())
            height = float(self.height_entry.get())

            # Formula for volume is pi * r^2 * h
            volume = pi * (radius * radius) * height
            # Formula for surface area is (2 * pi * r * h) + (2 * pi * r^2)
            surface_area = (2 * pi * radius * height) + (2 * pi * (radius * radius))

            # Set the text for our GUI to the successfully performed calculations
            self.volume.config(text=f"Volume: {volume:.2f}")
            self.surface_area.config(text=f"Surface Area: {surface_area:.2f}")

        except ValueError:
            self.volume.config(text="Error. Please enter a valid number.")
            self.surface_area.config(text="Error. Please enter a vlid number.")

    # Create a function for the clear button
    def clear(self):
        self.radius_entry.delete(0,tk.END)
        self.height_entry.delete(0,tk.END)
        self.volume.config(text="")
        self.surface_area.config(text="")

# Call the main function
if __name__ == "__main__":
    root = tk.Tk()
    cylinder_calc = CylinderCalculator(root)
    root.mainloop()



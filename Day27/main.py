import tkinter as tk

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.60934
    km_result_label.config(text=f"{km}")

# Creating the main window
window = tk.Tk()
window.title("Mile to Km Converter")

# Creating and placing the widgets
miles_input = tk.Entry(window, width=7)
miles_input.grid(column=1, row=0)

miles_label = tk.Label(window, text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = tk.Label(window, text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = tk.Label(window, text="0")
km_result_label.grid(column=1, row=1)

km_label = tk.Label(window, text="Km")
km_label.grid(column=2, row=1)

calculate_button = tk.Button(window, text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

# Running the main loop
window.mainloop()

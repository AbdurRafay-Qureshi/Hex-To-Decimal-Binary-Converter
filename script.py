import time
import sys
from tkinter import Tk, Label, Entry, Button, messagebox

def animate_intro(text):
    for i in range(len(text)):
        sys.stdout.write(text[i])
        sys.stdout.flush()
        time.sleep(0.01)
    print("\n")

def hex_to_binary():
    input_val = hex_input.get().upper()
    binary_dict = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }
    bin_val = ""
    for digit in input_val:
        if digit in binary_dict:
            bin_val += binary_dict[digit]
        else:
            messagebox.showerror("Error", "Invalid value: " + digit)
            return
    messagebox.showinfo("Result", "Binary value: " + bin_val)

def hex_to_decimal():
    input_val = hex_input.get().upper()
    decimal_dict = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    decimal = 0
    power = len(input_val) - 1
    for digit in input_val:
        if digit in decimal_dict:
            decimal += decimal_dict[digit] * (16 ** power)
            power -= 1
        else:
            messagebox.showerror("Error", "Invalid value: " + digit)
            return
    messagebox.showinfo("Result", "The decimal value of the given hexadecimal number is: " + str(decimal))

def hex_to_binary_and_decimal():
    input_val = hex_input.get().upper()
    binary_dict = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }
    decimal_dict = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    bin_val = ""
    decimal = 0
    power = len(input_val) - 1
    for digit in input_val:
        if digit in binary_dict:
            bin_val += binary_dict[digit]
        else:
            messagebox.showerror("Error", "Invalid value: " + digit)
            return
        if digit in decimal_dict:
            decimal += decimal_dict[digit] * (16 ** power)
            power -= 1
    messagebox.showinfo("Result", "Binary value: " + bin_val + "\nThe decimal value of the given hexadecimal number is: " + str(decimal))

# Create the GUI window
window = Tk()
window.title("Hexadecimal Converter")

# Add a label for the title
title_label = Label(window, text="Hexadecimal Converter", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Add an entry field for hexadecimal input
hex_input = Entry(window, font=("Arial", 12))
hex_input.pack(pady=10)

# Add buttons for conversion options
binary_button = Button(window, text="Hex to Binary", command=hex_to_binary)
binary_button.pack(pady=5)

decimal_button = Button(window, text="Hex to Decimal", command=hex_to_decimal)
decimal_button.pack(pady=5)

both_button = Button(window, text="Both", command=hex_to_binary_and_decimal)
both_button.pack(pady=5)

# Run the GUI window
window.mainloop()
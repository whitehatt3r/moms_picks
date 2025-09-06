import random
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import messagebox
import time


def load_previous_winning_numbers_from_csv(csv_file):
    df = pd.read_csv(csv_file)
    previous_winning_numbers = []
    for _, row in df.iterrows():
        numbers = [int(num) for num in row['Winning Numbers'].split()]
        previous_winning_numbers.append(set(numbers))
    return previous_winning_numbers


def generate_strategic_lottery_numbers(previous_winning_numbers, num_numbers=5, max_number=70):
    number_frequency = {}
    for winning_set in previous_winning_numbers:
        for number in winning_set:
            if number in number_frequency:
                number_frequency[number] += 1
            else:
                number_frequency[number] = 1

    all_numbers = list(range(1, max_number + 1))
    probabilities = [number_frequency.get(num, 1) for num in all_numbers]
    total = sum(probabilities)
    probabilities = [p / total for p in probabilities]

    new_numbers = set()
    while len(new_numbers) < num_numbers:
        new_number = int(np.random.choice(all_numbers, p=probabilities))
        new_numbers.add(new_number)

    power_ball = random.randint(1, 25)
    return sorted(new_numbers), power_ball


def main():
    csv_file = "../.venv/Scripts/Lottery_Mega_Millions_Winning_Numbers__Beginning_2002.csv"
    previous_winning_numbers = load_previous_winning_numbers_from_csv(csv_file)
    new_numbers, power_ball = generate_strategic_lottery_numbers(previous_winning_numbers)
    return new_numbers, power_ball


def flash_label(label, text, flashes=6, delay=200):
    def toggle_flash(count):
        if count > 0:
            current_color = label.cget("bg")
            next_color = "yellow" if current_color == "lightblue" else "lightblue"
            label.config(bg=next_color)
            label.after(delay, toggle_flash, count - 1)
        else:
            label.config(bg="lightblue", text=text)

    toggle_flash(flashes)


def flash_title(label, flashes=6, delay=200):
    def toggle_flash(count):
        if count > 0:
            current_color = label.cget("fg")
            next_color = "red" if current_color == "black" else "black"
            label.config(fg=next_color)
            label.after(delay, toggle_flash, count - 1)

    toggle_flash(flashes)


def generate_numbers():
    try:
        numbers, power_ball = main()
        flash_label(result_label,
                    f"Your new set of lottery numbers: {', '.join(map(str, numbers))} | Power Ball: {power_ball}")
    except FileNotFoundError:
        messagebox.showerror("File Not Found", "The CSV file containing lottery data was not found.")


def create_gui():
    root = tk.Tk()
    root.title("Lottery Number Picker")
    root.geometry("800x500")
    root.configure(bg="lightblue")

    global title_label
    title_label = tk.Label(root, text="Lottery Number Picker", font=("Helvetica", 18, "bold"), bg="lightblue",
                           fg="black")
    title_label.pack(pady=20)
    flash_title(title_label)
    root.after(2000, lambda: flash_title(title_label))

    generate_button = tk.Button(root, text="Generate Lottery Numbers", font=("Helvetica", 14), command=generate_numbers)
    generate_button.pack(pady=20)

    global result_label
    result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="lightblue")
    result_label.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    create_gui()

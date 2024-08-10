import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")

        self.users_data = []

        # Input fields
        self.weight_label = tk.Label(root, text="Weight (kg):")
        self.weight_label.pack()
        self.weight_entry = tk.Entry(root)
        self.weight_entry.pack()

        self.height_label = tk.Label(root, text="Height (m):")
        self.height_label.pack()
        self.height_entry = tk.Entry(root)
        self.height_entry.pack()

        # Calculate button
        self.calculate_button = tk.Button(root, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.pack()

        # Show history button
        self.history_button = tk.Button(root, text="Show BMI History", command=self.show_history)
        self.history_button.pack()

        # Show trends button
        self.trends_button = tk.Button(root, text="Show BMI Trends", command=self.show_trends)
        self.trends_button.pack()

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())

            if weight <= 0 or height <= 0:
                raise ValueError("Weight and height must be positive values.")

            bmi = weight / (height ** 2)
            category = self.classify_bmi(bmi)

            self.users_data.append((weight, height, bmi, category))

            messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}\nCategory: {category}")

        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def classify_bmi(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"

    def show_history(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("BMI History")

        for idx, (weight, height, bmi, category) in enumerate(self.users_data):
            tk.Label(history_window, text=f"Entry {idx + 1}: Weight: {weight} kg, Height: {height} m, "
                                          f"BMI: {bmi:.2f}, Category: {category}").pack()

    def show_trends(self):
        if not self.users_data:
            messagebox.showinfo("No Data", "No BMI data available to display trends.")
            return

        bm_values = [entry[2] for entry in self.users_data]
        plt.plot(bm_values, marker='o')
        plt.title("BMI Trends")
        plt.xlabel("Entry Number")
        plt.ylabel("BMI Value")
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()

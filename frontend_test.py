import tkinter as tk

class GridApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic Grid of Text Entries")
        self.root.geometry("600x400")  # Adjust the window size as needed

        self.column_count = 3
        self.row_count = 2

        # Create header
        self.header = tk.Label(root, text="Dynamic Grid of Text Entries", font=("Arial", 16))
        self.header.grid(row=0, column=0, columnspan=6, pady=2, sticky='w')

        # Create grid frame
        self.grid_frame = tk.Frame(root)
        self.grid_frame.grid(row=1, column=0, columnspan=2 * self.column_count + 2, pady=10)

        # Create initial grid of labels and entries
        self.create_grid()

        # Create control buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.grid(row=self.row_count + 1, column=0, columnspan=2 * self.column_count + 2, pady=10)

        self.add_column_button = tk.Button(self.button_frame, text="+ Column", command=self.add_column)
        self.add_column_button.grid(row=0, column=0, padx=5, pady=5)

        self.remove_column_button = tk.Button(self.button_frame, text="- Column", command=self.remove_column)
        self.remove_column_button.grid(row=0, column=1, padx=5, pady=5)

        self.add_row_button = tk.Button(self.button_frame, text="+ Row", command=self.add_row)
        self.add_row_button.grid(row=0, column=2, padx=5, pady=5)

        self.remove_row_button = tk.Button(self.button_frame, text="- Row", command=self.remove_row)
        self.remove_row_button.grid(row=0, column=3, padx=5, pady=5)

        # Create additional column of controls to the right
        self.create_right_column()

    def create_grid(self):
        for i in range(self.row_count):
            for j in range(self.column_count):
                label = tk.Label(self.grid_frame, text=chr(65 + i) + str(j + 1) + ":")
                label.grid(row=i, column=2 * j, padx=5, pady=5, sticky='e')
                entry = tk.Entry(self.grid_frame, width=10)
                entry.grid(row=i, column=2 * j + 1, padx=5, pady=5)

    def create_right_column(self):
        self.right_column_frame = tk.Frame(self.root)
        self.right_column_frame.grid(row=1, column=2 * self.column_count + 2, rowspan=self.row_count + 2, pady=10, padx=10, sticky='n')

        self.additional_label = tk.Label(self.right_column_frame, text="Additional Controls", font=("Arial", 12))
        self.additional_label.grid(row=0, column=0, padx=5, pady=5)

        # Add other controls here
        self.additional_button = tk.Button(self.right_column_frame, text="New Button")
        self.additional_button.grid(row=1, column=0, padx=5, pady=5)

    def add_column(self):
        self.column_count += 1
        self.create_grid()
        self.update_buttons()

    def remove_column(self):
        if self.column_count > 1:
            for i in range(self.row_count):
                widget = self.grid_frame.grid_slaves(row=i, column=2 * (self.column_count - 1))
                if widget:
                    widget[0].destroy()
                widget = self.grid_frame.grid_slaves(row=i, column=2 * (self.column_count - 1) + 1)
                if widget:
                    widget[0].destroy()
            self.column_count -= 1
            self.create_grid()
            self.update_buttons()

    def add_row(self):
        self.row_count += 1
        self.create_grid()
        self.update_buttons()

    def remove_row(self):
        if self.row_count > 1:
            for i in range(self.column_count):
                widget = self.grid_frame.grid_slaves(row=self.row_count - 1, column=2 * i)
                if widget:
                    widget[0].destroy()
                widget = self.grid_frame.grid_slaves(row=self.row_count - 1, column=2 * i + 1)
                if widget:
                    widget[0].destroy()
            self.row_count -= 1
            self.create_grid()
            self.update_buttons()

    def update_buttons(self):
        self.button_frame.grid(row=self.row_count + 1, column=0, columnspan=2 * self.column_count + 2, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = GridApp(root)
    root.mainloop()

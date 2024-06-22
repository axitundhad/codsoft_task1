import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.config(bg="#E6F7FF")  # Light pastel blue background

        self.tasks = []

        # Create a frame for the listbox and scrollbar
        frame = tk.Frame(self.root, bg="#E6F7FF")
        frame.pack(pady=10)

        # Create a listbox
        self.listbox = tk.Listbox(
            frame,
            width=50,
            height=10,
            selectmode=tk.SINGLE,
            bg="#FFFFFF",  # Background color
            fg="#333333",  # Text color
            selectbackground="#B0E0E6",  # Selected item background color
            selectforeground="#FFFFFF",  # Selected item text color
            bd=2,  # Border width
            relief="solid"  # Border style
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        # Create a scrollbar
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        # Configure the scrollbar
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        # Entry box for adding tasks
        self.entry = tk.Entry(self.root, width=50, bg="#FFFFFF", fg="#333333", bd=2, relief="solid")
        self.entry.pack(pady=10)

        # Button frame to align buttons
        button_frame = tk.Frame(self.root, bg="#E6F7FF")
        button_frame.pack(pady=10)

        # Button style
        button_style = {
            "bg": "#87CEFA",  # Button background color
            "fg": "#333333",  # Button text color
            "activebackground": "#76D7C4",  # Active button background color
            "activeforeground": "#FFFFFF",  # Active button text color
            "bd": 2,  # Border width
            "relief": "solid",  # Border style
            "width": 20  # Button width
        }

        # Add task button
        self.add_button = tk.Button(
            button_frame,
            text="Add Task",
            command=self.add_task,
            **button_style
        )
        self.add_button.grid(row=0, column=0, padx=5, pady=5)

        # Update task button
        self.update_button = tk.Button(
            button_frame,
            text="Update Task",
            command=self.update_task,
            **button_style
        )
        self.update_button.grid(row=0, column=1, padx=5, pady=5)

        # Delete task button
        self.delete_button = tk.Button(
            button_frame,
            text="Delete Task",
            command=self.delete_task,
            **button_style
        )
        self.delete_button.grid(row=1, column=0, padx=5, pady=5)

        # Mark as completed button
        self.complete_button = tk.Button(
            button_frame,
            text="Mark as Completed",
            command=self.mark_completed,
            **button_style
        )
        self.complete_button.grid(row=1, column=1, padx=5, pady=5)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            new_task = simpledialog.askstring("Update Task", "Enter the new task:")
            if new_task:
                self.tasks[selected_task_index] = new_task
                self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def delete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def mark_completed(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.tasks[selected_task_index] = self.tasks[selected_task_index] + " [Completed]"
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to mark as completed.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

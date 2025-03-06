import tkinter as tk
from tkinter import messagebox

class NoteTakingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note Taking App")

        self.notes = []

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.label = tk.Label(self.frame, text="Enter your note:")
        self.label.pack(pady=5)

        self.text_entry = tk.Entry(self.frame, width=50)
        self.text_entry.pack(pady=5)

        self.add_button = tk.Button(self.frame, text="Add Note", command=self.add_note)
        self.add_button.pack(pady=5)

        self.notes_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.notes_listbox.pack(pady=5)

        self.delete_button = tk.Button(self.frame, text="Delete Selected Note", command=self.delete_note)
        self.delete_button.pack(pady=5)

    def add_note(self):
        note = self.text_entry.get()
        if note:
            self.notes.append(note)
            self.update_notes_listbox()
            self.text_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Note cannot be empty!")

    def delete_note(self):
        selected_note_index = self.notes_listbox.curselection()
        if selected_note_index:
            self.notes.pop(selected_note_index[0])
            self.update_notes_listbox()
        else:
            messagebox.showwarning("Warning", "No note selected!")

    def update_notes_listbox(self):
        self.notes_listbox.delete(0, tk.END)
        for note in self.notes:
            self.notes_listbox.insert(tk.END, note)

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteTakingApp(root)
    root.mainloop()

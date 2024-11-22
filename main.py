import tkinter as tk  # GUI library
from tkinter import messagebox, simpledialog  # GUI dialogs for messages and inputs


class TextFileSearchApp:
    def __init__(self, root):
        # Initialize the main app
        self.root = root
        self.root.title("Text File Search Tool")  # Set window title
        self.current_file = "tekstfil1.txt"  # Default selected file

        # GUI components
        self.file_label = tk.Label(root, text=f"Current selected file: {self.current_file}")  # Label for current file
        self.file_label.pack(pady=10)

        self.search_line_button = tk.Button(root, text="Search Line", command=self.search_line)  # Button for line search
        self.search_line_button.pack(pady=5)

        self.search_word_button = tk.Button(root, text="Search Word", command=self.search_word)  # Button for word search
        self.search_word_button.pack(pady=5)

        self.change_file_button = tk.Button(root, text="Change File", command=self.change_file)  # Button to change file
        self.change_file_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Exit", command=self.root.quit)  # Button to exit the app
        self.exit_button.pack(pady=10)

    def update_file_label(self):
        # Update the file label to reflect the current file
        self.file_label.config(text=f"Current selected file: {self.current_file}")

    def change_file(self):
        # Allow the user to select a different file
        options = ["tekstfil1.txt", "tekstfil2.txt", "tekstfil3.txt"]
        choice = simpledialog.askstring("Change File", f"Choose file:\n1. {options[0]}\n2. {options[1]}\n3. {options[2]}")

        if choice in ["1", "2", "3"]:
            self.current_file = options[int(choice) - 1]  # Update file based on user's choice
            self.update_file_label()
        else:
            messagebox.showerror("Error", "Invalid choice. Please try again.")  # Error if input is invalid

    def search_line(self):
        # Search for a text string in the lines of the current file
        try:
            search = simpledialog.askstring("Search Line", "Enter text to search for in the lines:")
            if not search:
                return  # Exit if no input provided

            with open(self.current_file, "r") as f:
                lines = [line.strip() for line in f if search in line]  # Collect matching lines

            if lines:
                messagebox.showinfo("Results", "\n".join(lines))  # Show matching lines
            else:
                messagebox.showinfo("Results", "No matching lines found.")  # Show no match message
        except FileNotFoundError:
            messagebox.showerror("Error", f"The file '{self.current_file}' does not exist.")  # Error for missing file
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")  # Generic error handling

    def search_word(self):
        # Search for occurrences of a specific word in the file
        try:
            search = simpledialog.askstring("Search Word", "Enter a word to search for:")
            if not search:
                return  # Exit if no input provided

            word_count = 0
            with open(self.current_file, "r") as f:
                for line in f:
                    words = line.split()  # Split line into words
                    word_count += words.count(search)  # Count occurrences

            # Show word count and presence
            found_message = f"The word '{search}' was found {word_count} time(s).\nWord found = {'True' if word_count > 0 else 'False'}"
            messagebox.showinfo("Results", found_message)
        except FileNotFoundError:
            messagebox.showerror("Error", f"The file '{self.current_file}' does not exist.")  # Error for missing file
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")  # Generic error handling


if __name__ == "__main__":
    root = tk.Tk()  # Create the main application window
    app = TextFileSearchApp(root)  # Instantiate the app
    root.mainloop()  # Run the app

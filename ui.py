import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk, ImageSequence

class MainPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Page")

        # Set black background
        self.root.configure(bg="black")

        # Load the GIF image
        self.gif_path = r"E:\OneDrive\Desktop\ai5.gif"  # Replace with the actual path to your GIF
        self.frames = []

        # Get the frames from the GIF
        gif = Image.open(self.gif_path)
        for frame in ImageSequence.Iterator(gif):
            img = ImageTk.PhotoImage(frame)
            self.frames.append(img)

        # Create and display the Label with the GIF
        self.gif_label = tk.Label(self.root)
        self.gif_label.pack()

        # Start playing the GIF
        self.play_gif(0)

        # Add a frame for the buttons
        self.controls_frame = tk.Frame(self.root, bg="black")
        self.controls_frame.place(relx=0.5, rely=0.8, anchor="center")

        # Resize the microphone icon
        icon_path = r"E:\OneDrive\Desktop\microphone-button-red-icon.webp"  # Replace with the actual path to your icon
        icon_image = Image.open(icon_path).resize((30, 30))
        self.button_icon = ImageTk.PhotoImage(icon_image)

        # Add a button with the resized microphone icon
        self.button = tk.Button(self.controls_frame, image=self.button_icon, bd=0, command=self.button_click)
        self.button.grid(row=0, column=0, padx=10)

        # Add a button for Chat
        self.chat_button = tk.Button(self.controls_frame, text="Chat", command=self.open_chat_screen)
        self.chat_button.grid(row=0, column=1, padx=10)

    def play_gif(self, frame_index):
        # Display the current frame
        self.gif_label.config(image=self.frames[frame_index])

        # Move to the next frame after a delay (adjust the delay in milliseconds)
        self.root.after(50, lambda: self.play_gif((frame_index + 1) % len(self.frames)))

    def button_click(self):
        # Do something when the button is clicked
        print("Button Clicked!")

    def open_chat_screen(self):
        # Create a new window for the chat screen
        chat_window = tk.Toplevel(self.root)
        chat_window.title("Chat Screen")
        chat_window.geometry(self.root.geometry())  # Set the geometry to match the main window

        # Load another GIF image for the new window (vertical gif)
        new_gif_path = r"E:\OneDrive\Desktop\ai6.gif"  # Replace with the actual path to your vertical GIF
        new_frames = []

        new_gif = Image.open(new_gif_path)
        for frame in ImageSequence.Iterator(new_gif):
            img = ImageTk.PhotoImage(frame)
            new_frames.append(img)

        # Create and display the Label with the new GIF
        new_gif_label = tk.Label(chat_window)
        new_gif_label.place(relx=0.33, rely=0, anchor="n")  # Position at the top (1/3 of the screen width)
        new_gif_label.pack()

        # Start playing the new GIF
        self.play_new_gif(new_gif_label, new_frames, 0)

        # Add text for user interaction
        user_text = "Interact with AI Assistant"
        text_label = tk.Label(chat_window, text=user_text, fg="white", bg="black", font=("Helvetica", 16))
        text_label.place(relx=1/3, rely=2/3, anchor="nw")  # Position in the corner (1/3 of the screen width)

        # Add a larger text box to the new window
        chat_text = scrolledtext.ScrolledText(chat_window, wrap=tk.WORD, width=40, height=20, bg="gray", fg="white")
        chat_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=20)

    def play_new_gif(self, label, frames, frame_index):
        # Display the current frame
        label.config(image=frames[frame_index])

        # Move to the next frame after a delay (adjust the delay in milliseconds)
        label.after(50, lambda: self.play_new_gif(label, frames, (frame_index + 1) % len(frames)))

if __name__ == "__main__":
    root = tk.Tk()
    main_page = MainPage(root)
    root.mainloop()


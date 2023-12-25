import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk, ImageSequence
import action
from speech_to_text import speech_to_text

class MainPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Page")

        # Set black background
        self.root.configure(bg="black")

        # Load the GIF image
        self.gif_path = r"E:\OneDrive\Desktop\os projecr\OS\ai5.gif"  # Replace with the actual path to your GIF
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
        self.button = tk.Button(self.controls_frame, image=self.button_icon, bd=0, command=self.ask)
        self.button.grid(row=0, column=0, padx=10)

        # Add a button for Chat
        self.chat_button = tk.Button(self.controls_frame, text="Chat", command=self.open_chat_screen)
        self.chat_button.grid(row=0, column=1, padx=10)

    def play_gif(self, frame_index):
        # Display the current frame
        self.gif_label.config(image=self.frames[frame_index])

        # Move to the next frame after a delay (adjust the delay in milliseconds)
        self.root.after(50, lambda: self.play_gif((frame_index + 1) % len(self.frames)))

    def ask(self):
        user_val = speech_to_text()  # Get user input using speech recognition
        bot_val = action.Action(user_val)
        self.response_text.insert(tk.END, 'User ---> ' + user_val + "\n")
        if bot_val is not None:
            self.response_text.insert(tk.END, "Bot ---> " + str(bot_val) + '\n')
        if bot_val == "Okay, shutting down":
            self.root.destroy()

    def open_chat_screen(self):
        # Create a new window for the chat screen
        chat_window = tk.Toplevel(self.root)
        chat_window.title("Chat Screen")
        chat_window.geometry(self.root.geometry())  # Set the geometry to match the main window

        # Load another GIF image for the new window (vertical gif)
        new_gif_path = r"E:\OneDrive\Desktop\os projecr\OS\ai6.gif"  # Replace with the actual path to your vertical GIF
        new_frames = []

        new_gif = Image.open(new_gif_path)
        for frame in ImageSequence.Iterator(new_gif):
            img = ImageTk.PhotoImage(frame)
            new_frames.append(img)

        # Create and display the Label with the new GIF
        new_gif_label = tk.Label(chat_window)
        new_gif_label.place(relx=1/3, rely=0, anchor="n")  # Position at the top (1/3 of the screen width)
        new_gif_label.pack()

        # Start playing the new GIF
        self.play_new_gif(new_gif_label, new_frames, 0)

        # Add text for user interaction
        user_text = "Interact with AI Assistant"
        text_label = tk.Label(chat_window, text=user_text, fg="white", bg="black", font=("Helvetica", 16))
        text_label.place(relx=1/3, rely=2/3, anchor="nw")  # Position in the corner (1/3 of the screen width)

        # Add a text box for sending requests
        self.request_entry = tk.Entry(chat_window, bg="gray", fg="white", font=("Helvetica", 12))
        self.request_entry.place(relx=1/3, rely=1/3, anchor="nw", width=300, height=30)

        # Add a text box for displaying responses
        self.response_text = scrolledtext.ScrolledText(chat_window, wrap=tk.WORD, width=40, height=10, bg="gray", fg="white")
        self.response_text.place(relx=1/3, rely=1/2, anchor="nw", width=400, height=200)

        # Load the send icon
        send_icon_path = r"E:\OneDrive\Desktop\os projecr\OS\send_icon.png"  # Replace with the actual path to your send icon
        send_icon = Image.open(send_icon_path).resize((20, 20))
        self.send_icon = ImageTk.PhotoImage(send_icon)

        # Add a button for Send with the icon
        send_button = tk.Button(chat_window, text="Send", image=self.send_icon, compound=tk.LEFT,
                                command=lambda: self.send_request(), bd=0)
        send_button.place(relx=1/3, rely=1/3, anchor="ne")

        # Load the delete icon
        delete_icon_path = r"E:\OneDrive\Desktop\os projecr\OS\delete_icon.png"  # Replace with the actual path to your delete icon
        delete_icon = Image.open(delete_icon_path).resize((20, 20))
        self.delete_icon = ImageTk.PhotoImage(delete_icon)

        # Add a button for Delete with the icon
        delete_button = tk.Button(chat_window, text="Delete", image=self.delete_icon, compound=tk.LEFT,
                                  command=lambda: self.delete_text(), bd=0)
        delete_button.place(relx=1/3, rely=1/2, anchor="ne")

    def play_new_gif(self, label, frames, frame_index):
        # Display the current frame
        label.config(image=frames[frame_index])

        # Move to the next frame after a delay (adjust the delay in milliseconds)
        label.after(50, lambda: self.play_new_gif(label, frames, (frame_index + 1) % len(frames)))

    def send_request(self):
        user_val = self.request_entry.get()
        bot_val = action.Action(user_val)
        self.response_text.insert(tk.END, 'User ---> ' + user_val + "\n")
        if bot_val is not None:
            self.response_text.insert(tk.END, "Bot ---> " + str(bot_val) + '\n')
        if bot_val == "Okay, shutting down":
            self.root.destroy()

    def delete_text(self):
        self.response_text.delete('1.0', tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    main_page = MainPage(root)
    root.mainloop()

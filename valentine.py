import tkinter as tk
import random
from PIL import Image, ImageTk


def display_gif(root, gif_path):
    """Displays an animated GIF in a Tkinter window."""
    
    def update_gif(frame=0):
        """Updates the label to show the next frame of the GIF."""
        frame = (frame + 1) % len(frames)
        gif_label.config(image=frames[frame])
        root.after(100, update_gif, frame)  # Adjust timing as needed

    # Load GIF using PIL
    gif_image = Image.open(gif_path)
    frames = [ImageTk.PhotoImage(gif_image.copy().resize((100, 100))) for _ in range(gif_image.n_frames)]

    # Create label to display the GIF
    gif_label = tk.Label(root)
    gif_label.pack(pady=20)

    # Start animation
    update_gif()

    return gif_label  # Return the label in case further modification is needed

def move_no_button(event):
    """Move the 'No' button to a random location within the window."""
    new_x = random.randint(0, root.winfo_width() - no_button.winfo_width())
    new_y = random.randint(0, root.winfo_height() - no_button.winfo_height())
    no_button.place(x=new_x, y=new_y)

def open_new_window():
    """Opens a new window with a message when 'Yes' is clicked."""
    for widget in root.winfo_children():
        widget.destroy()  # Remove all widgets from root
    
    message_label = tk.Label(root, text="Thank you!!\nSee me at [[Location]] at [[Time]] on Valentine's Day!\nA copy of your response has been saved for legality,\nwith a fine for not showing up set at 100,000 USD =)", font=("Arial", 12))
    message_label.pack(pady=50)
    display_gif(root, "heart.gif")

# Create the main window
root = tk.Tk()
root.title("Important Question")
root.geometry("400x300")

# Create a label for the question
question_label = tk.Label(root, text="Will you be my Valentine?", font=("Arial", 14))
question_label.pack(pady=20)

# Create 'Yes' button
yes_button = tk.Button(root, text="Yes", font=("Arial", 12), command=open_new_window)
yes_button.place(x=130, y=110)

# Create 'No' button
no_button = tk.Button(root, text="No", font=("Arial", 12))
no_button.place(x=230, y=110)
no_button.bind("<Enter>", move_no_button)

root.mainloop()

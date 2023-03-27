import tkinter as tk
from PIL import Image, ImageTk

# Create the GUI window
window = tk.Tk()
window.title("Star Rating System")

# Define a function to display the star rating
def display_rating(text_input):
    # Check the input text and assign a rating value
    if text_input.lower() == "excellent":
        rating = 5
    elif text_input.lower() == "good":
        rating = 4
    elif text_input.lower() == "fair":
        rating = 3
    elif text_input.lower() == "poor":
        rating = 2
    else:
        rating = 1
    
    # Load the star rating image based on the rating value
    image_file = "star_rating_" + str(rating) + ".png"
    image = Image.open(image_file)
    image = image.resize((100, 20), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)

    # Display the star rating image
    label.configure(image=photo)
    label.image = photo

# Create a text input field and a submit button
text_input = tk.Entry(window)
submit_button = tk.Button(window, text="Submit", command=lambda: display_rating(text_input.get()))

# Create a label to display the star rating image
label = tk.Label(window)

# Add the widgets to the window
text_input.pack()
submit_button.pack()
label.pack()

# Run the GUI window
window.mainloop()

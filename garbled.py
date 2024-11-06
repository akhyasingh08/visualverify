# import tkinter
# from tkinter import *
# import custom_button
# import main_menu

# import utils
# from PIL import ImageTk, Image
# from tkinter import Entry
# import random


# def load_menu(window, frame):
#     frame.pack_forget()
#     main_menu.start(window)


# def start(window):
#     filepath = "garbledImages/original_garbled.txt"  # File Path
#     garbledImages = utils.getGarbledImages()
#     num = random.randint(0, len(garbledImages) - 1)
#     filename = garbledImages[num]

#     f = open(filepath, "r")

#     while True:
#         string = f.readline()  # Reading file line by line
#         s1 = string.split(' ')[0]  # Getting first word (filename) of line
#         if s1 == filename[0:len(filename) - 4]:  # Don't need the file extension, only name
#             break
#     # print("Original = ", string)
#     string = string[9:]  # Cropping string
#     string = string.replace(' ', '-')  # Replacing spaces with dashes
#     original_text = string
#     original_text = original_text.rstrip()  # Removing \n
#     f.close()

#     print(original_text)
#     print(filename)

#     window.title("Graphical Authentication System")
#     window.geometry("1280x600")

#     garbled_frame = Frame(window, height=600, width=1280)
#     garbled_frame.pack(fill='both', expand=1)

#     label = Label(garbled_frame, text="Type the words in the image", font=('Calibri', 20))
#     label.pack(padx=40, pady=10)

#     canvas = Canvas(garbled_frame, width=450, height=300)
#     img = (Image.open("garbledImages/" + filename))
#     img = img.resize((450, 300))
#     img = ImageTk.PhotoImage(img)
#     canvas.create_image(10, 10, anchor=NW, image=img)
#     canvas.place(relx=0.45, rely=0.5, anchor=E)

#     def check():
#         entered_text = input.get()
#         if entered_text == original_text:
#             print("Authenticated")
#             utils.create_popup(msg="Authenticated :)", font="Gabriola 28 bold")
#         else:
#             print("Authentication Failed")
#             utils.create_popup(msg="Go Away Robot >_<", font="Gabriola 28 bold")

#     input = StringVar()
#     Label(garbled_frame, text="Enter word", font="ariel 16 bold").place(relx=0.7, rely=0.40, anchor=CENTER)
#     Entry(garbled_frame, textvariable=input, font="ariel 12 bold", relief="groove", width=30, justify=CENTER).place(
#         relx=0.7,
#         rely=0.5,
#         anchor=CENTER)

#     custom_button.TkinterCustomButton(master=garbled_frame, text="Check", height=40, corner_radius=10,
#                                       command=check).place(relx=0.7, rely=0.6, anchor=CENTER)

#     custom_button.TkinterCustomButton(master=garbled_frame, text="Go Back", height=40, corner_radius=10,
#                                       command=lambda: load_menu(window, garbled_frame)).place(relx=0.08, rely=0.08, anchor=CENTER)

#     while True:
#         window.update_idletasks()
#         window.update()



# import tkinter
# from tkinter import *
# import custom_button
# import main_menu
# import utils
# from PIL import ImageTk, Image
# import random

# def load_menu(window, frame):
#     frame.pack_forget()  # Hide the current frame
#     main_menu.start(window)  # Load the main menu

# def start(window):
#     filepath = "garbledImages/original_garbled.txt"  # File path for original text
#     garbledImages = utils.getGarbledImages()  # Fetch garbled images
#     num = random.randint(0, len(garbledImages) - 1)  # Randomly select an image
#     filename = garbledImages[num]  # Get the selected filename

#     # Read the corresponding original text from the file
#     with open(filepath, "r") as f:
#         while True:
#             string = f.readline()  # Reading file line by line
#             s1 = string.split(' ')[0]  # Getting first word (filename) of line
#             if s1 == filename[:-4]:  # Compare without file extension
#                 break
#         original_text = string[9:].replace(' ', '-').rstrip()  # Process the original text

#     print("Original Text:", original_text)  # Debugging output
#     print("Filename:", filename)  # Debugging output

#     window.title("Graphical Authentication System")
#     window.geometry("1280x600")

#     garbled_frame = Frame(window, height=600, width=1280)
#     garbled_frame.pack(fill='both', expand=1)

#     label = Label(garbled_frame, text="Type the words in the image", font=('Calibri', 20))
#     label.pack(padx=40, pady=10)

#     # Load and display the garbled image
#     canvas = Canvas(garbled_frame, width=450, height=300)
#     img = Image.open("garbledImages/" + filename)
#     img = img.resize((450, 300))
#     img = ImageTk.PhotoImage(img)
#     canvas.create_image(10, 10, anchor=NW, image=img)
#     canvas.image = img  # Keep a reference to avoid garbage collection
#     canvas.place(relx=0.45, rely=0.5, anchor=E)

#     def check():
#         entered_text = input_var.get()
#         if entered_text == original_text:
#             print("Authenticated")
#             utils.create_popup(msg="Authenticated :)", font="Gabriola 28 bold")
#         else:
#             print("Authentication Failed")
#             utils.create_popup(msg="Go Away Robot >_<", font="Gabriola 28 bold")

#     input_var = StringVar()
#     Label(garbled_frame, text="Enter word", font="Arial 16 bold").place(relx=0.7, rely=0.40, anchor=CENTER)
#     Entry(garbled_frame, textvariable=input_var, font="Arial 12 bold", relief="groove", width=30, justify=CENTER).place(
#         relx=0.7, rely=0.5, anchor=CENTER)

#     # Check button to verify the input
#     custom_button.TkinterCustomButton(master=garbled_frame, text="Check", height=40, corner_radius=10,
#                                       command=check).place(relx=0.7, rely=0.6, anchor=CENTER)

#     # Button to go back to the main menu
#     custom_button.TkinterCustomButton(master=garbled_frame, text="Go Back", height=40, corner_radius=10,
#                                       command=lambda: load_menu(window, garbled_frame)).place(relx=0.08, rely=0.08, anchor=CENTER)

#     # Main event loop
#     window.mainloop()

# if __name__ == "__main__":
#     root = Tk()
#     start(root)

# import tkinter as tk
# from tkinter import *
# import custom_button
# import main_menu
# import utils
# from PIL import ImageTk, Image
# import random

# def load_menu(window, frame):
#     frame.pack_forget()  # Hide the garbled frame
#     main_menu.start(window)  # Show the main menu

# def create_popup(message, title="Notification"):
#     popup = Toplevel()
#     popup.title(title)
#     popup.geometry("400x200")
#     popup.configure(bg="black")
    
#     label = Label(popup, text=message, font=("Gabriola", 14), bg="black", fg="white")
#     label.pack(pady=20)

#     button = custom_button.TkinterCustomButton(
#         master=popup,
#         text="OK",
#         height=40,
#         corner_radius=10,
#         command=popup.destroy,
#         bg="#444444",
#         text_color="white"
#     )
#     button.pack(pady=10)

# def start(window):
#     filepath = "garbledImages/original_garbled.txt"  # File Path
#     garbledImages = utils.getGarbledImages()
#     num = random.randint(0, len(garbledImages) - 1)
#     filename = garbledImages[num]

#     f = open(filepath, "r")

#     while True:
#         string = f.readline()  # Reading file line by line
#         s1 = string.split(' ')[0]  # Getting first word (filename) of line
#         if s1 == filename[0:len(filename) - 4]:  # Don't need the file extension, only name
#             break

#     string = string[9:]  # Cropping string
#     original_text = string.replace(' ', '-').rstrip()  # Replacing spaces with dashes
#     f.close()

#     window.title("Graphical Authentication System")
#     window.geometry("1280x600")
#     window.configure(bg="black")  # Set the background color to black

#     # Create and pack the garbled frame
#     garbled_frame = Frame(window, bg="black")
#     garbled_frame.pack(fill='both', expand=True)

#     label = Label(garbled_frame, text="Type the words in the image", font=('Calibri', 20), bg="black", fg="white")
#     label.pack(padx=40, pady=(20, 10))

#     canvas_img = Canvas(garbled_frame, width=450, height=300, bg="black", highlightthickness=0)
#     img = Image.open("garbledImages/" + filename)
#     img = img.resize((450, 300))
#     img = ImageTk.PhotoImage(img)
#     canvas_img.create_image(0, 0, anchor=NW, image=img)
#     canvas_img.place(relx=0.5, rely=0.3, anchor=CENTER)

#     def check():
#         entered_text = input.get().strip()  # Get input and remove whitespace
#         if not entered_text:
#             create_popup("Please enter a word before checking.")
#             return

#         if entered_text == original_text:
#             create_popup("Authenticated :)", title="Success")
#         else:
#             input.set("")  # Clear the input field
#             load_menu(window, garbled_frame)  # Remove user and go back to main menu

#     input = StringVar()
#     Label(garbled_frame, text="Enter word", font="ariel 16 bold", bg="black", fg="white").place(relx=0.5, rely=0.75, anchor=CENTER)
#     Entry(garbled_frame, textvariable=input, font="ariel 12 bold", relief="groove", width=30, justify=CENTER).place(
#         relx=0.5,
#         rely=0.8,
#         anchor=CENTER)

#     custom_button.TkinterCustomButton(master=garbled_frame, text="Check", height=40, corner_radius=10,
#                                       command=check, bg="#444444", text_color="white").place(relx=0.5, rely=0.85, anchor=CENTER)

#     custom_button.TkinterCustomButton(master=garbled_frame, text="Go Back", height=40, corner_radius=10,
#                                       command=lambda: load_menu(window, garbled_frame), bg="#444444", text_color="white").place(relx=0.08, rely=0.08, anchor=CENTER)

#     window.mainloop()  # Start the main loop for the window



import tkinter as tk
from tkinter import *
import custom_button
import main_menu
import utils
from PIL import ImageTk, Image
import random

def load_menu(window, frame):
    frame.pack_forget()  # Hide the garbled frame
    main_menu.start(window)  # Show the main menu

def create_popup(window, message, title="Notification", authenticated=True):
    popup = Toplevel(window)
    popup.title(title)
    popup.geometry("400x200")
    popup.configure(bg="black")
    
    label = Label(popup, text=message, font=("Gabriola", 14), bg="black", fg="white")
    label.pack(pady=20)

    button = custom_button.TkinterCustomButton(
        master=popup,
        text="OK",
        height=40,
        corner_radius=10,
        command=lambda: [popup.destroy(), handle_user_removal(window) if not authenticated else None],
        bg="#444444",
        text_color="white"
    )
    button.pack(pady=10)

def handle_user_removal(window):
    print("User removed from the site.")
    blank_screen(window)

def blank_screen(window):
    # Clear the window and display a blank message
    for widget in window.winfo_children():
        widget.destroy()

    blank_frame = Frame(window, bg="black")
    blank_frame.pack(fill='both', expand=True)

    label = Label(blank_frame, text="You have been unauthenticated.", font=("Arial", 24), bg="black", fg="white")
    label.pack(expand=True)

    custom_button.TkinterCustomButton(
        master=blank_frame,
        text="Return to Main Menu",
        height=40,
        corner_radius=10,
        command=lambda: load_menu(window, blank_frame),
        bg="#444444",
        text_color="white"
    ).pack(pady=20)

def start(window):
    filepath = "garbledImages/original_garbled.txt"  # File Path
    garbledImages = utils.getGarbledImages()
    num = random.randint(0, len(garbledImages) - 1)
    filename = garbledImages[num]

    f = open(filepath, "r")

    while True:
        string = f.readline()  # Reading file line by line
        s1 = string.split(' ')[0]  # Getting first word (filename) of line
        if s1 == filename[0:len(filename) - 4]:  # Don't need the file extension, only name
            break

    string = string[9:]  # Cropping string
    original_text = string.replace(' ', '-').rstrip()  # Replacing spaces with dashes
    f.close()

    window.title("Graphical Authentication System")
    window.geometry("1280x600")
    window.configure(bg="black")  # Set the background color to black

    # Create and pack the garbled frame
    garbled_frame = Frame(window, bg="black")
    garbled_frame.pack(fill='both', expand=True)

    label = Label(garbled_frame, text="Type the words in the image", font=('Calibri', 20), bg="black", fg="white")
    label.pack(padx=40, pady=(20, 10))

    canvas_img = Canvas(garbled_frame, width=450, height=300, bg="black", highlightthickness=0)
    img = Image.open("garbledImages/" + filename)
    img = img.resize((450, 300))
    img = ImageTk.PhotoImage(img)
    canvas_img.create_image(0, 0, anchor=NW, image=img)
    canvas_img.place(relx=0.5, rely=0.3, anchor=CENTER)

    def check():
        entered_text = input.get().strip()  # Get input and remove whitespace
        if not entered_text:
            create_popup(window, "Please enter a word before checking.")
            return

        if entered_text == original_text:
            create_popup(window, "Authenticated :)", title="Success", authenticated=True)
        else:
            input.set("")  # Clear the input field
            create_popup(window, "Go Away Robot >_<", title="Failure", authenticated=False)

    input = StringVar()
    Label(garbled_frame, text="Enter word", font="ariel 16 bold", bg="black", fg="white").place(relx=0.5, rely=0.75, anchor=CENTER)
    Entry(garbled_frame, textvariable=input, font="ariel 12 bold", relief="groove", width=30, justify=CENTER).place(
        relx=0.5,
        rely=0.8,
        anchor=CENTER)

    custom_button.TkinterCustomButton(master=garbled_frame, text="Check", height=40, corner_radius=10,
                                      command=check, bg="#444444", text_color="white").place(relx=0.5, rely=0.85, anchor=CENTER)

    custom_button.TkinterCustomButton(master=garbled_frame, text="Go Back", height=40, corner_radius=10,
                                      command=lambda: load_menu(window, garbled_frame), bg="#444444", text_color="white").place(relx=0.08, rely=0.08, anchor=CENTER)

    window.mainloop()  # Start the main loop for the window

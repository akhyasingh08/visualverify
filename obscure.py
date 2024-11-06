# import tkinter
# from tkinter import *
# import custom_button
# import main_menu
# import speech_recognition as sr

# import utils
# from PIL import ImageTk, Image
# import random


# def load_menu(window, frame):
#     frame.pack_forget()
#     main_menu.start(window)


# original_text = []


# def toggle(event):
#     input_text = None

#     while True:
#         e = sr.Recognizer()  # Recognizes all input devices
#         with sr.Microphone() as source:  # setting microphone as default input device
#             try:
#                 print("Say Something. Say 'stop' inorder to stop")
#                 audio = e.listen(source)  # Listens audio
#                 input_text = e.recognize_google(audio)  # Recognizes text using speech recognition
#                 if input_text == "stop":  # Break condition
#                     break
#             except:
#                 print("Exception occured when trying to record")
#         break
#     input_text = input_text[:-5]  # Removing stop from the end of line
#     input_text = input_text.rstrip()  # Removing \n
#     input_text = input_text.lower()  # Converting everything to lowercase
#     input_text = input_text.replace(' ', '-')  # Replacing spaces with dashes

#     print("Original Text = ", original_text[0])
#     print("Input Text = ", input_text)

#     if original_text[0] == input_text:
#         print("Authenticated")
#         utils.create_popup(msg="Authenticated :)", font="Gabriola 28 bold")
#     else:
#         print("Authentication Failed")
#         utils.create_popup(msg="Go Away Robot >_<", font="Gabriola 28 bold")


# def start(window):
#     obscuredImages = utils.getObscuredImages()
#     num = random.randint(1, len(obscuredImages) - 1)
#     filename = obscuredImages[num]  # Filename that will be displayed
#     filepath = "obscuredImages/original_obscure.txt"  # File Path

#     f = open(filepath, "r")

#     while True:
#         string = f.readline()  # Reading file line by line
#         s1 = string.split(' ')[0]  # Getting first word (filename) of line
#         if s1 == filename[0:len(filename) - 4]:  # Don't need the file extension, only name
#             break
#     # print("Original = ", string)
#     string = string[9:]  # Cropping string
#     string = string.replace(' ', '-')  # Replacing spaces with dashes
#     string = string
#     original_text.append(string.rstrip())  # Removing \n
#     f.close()

#     obscure_frame = Frame(window, height=600, width=1280)
#     obscure_frame.pack(fill='both', expand=1)

#     window.title("Graphical Authentication System")
#     window.geometry("1280x600")

#     label = Label(obscure_frame, text="Click on the microphone and speak the words in the following image",
#                   font=('Calibri', 20))
#     label.pack(padx=40, pady=10)

#     canvas = Canvas(obscure_frame, width=450, height=300)
#     img = (Image.open("obscuredImages/" + filename))
#     img = img.resize((450, 300))
#     img = ImageTk.PhotoImage(img)
#     canvas.create_image(10, 10, anchor=NW, image=img)
#     canvas.pack(padx=10, pady=10)

#     canvas2 = Canvas(obscure_frame, width=200, height=170)
#     canvas2.bind("<Button-1>", toggle)
#     img2 = (Image.open("assets/mic.jpg"))
#     img2 = img2.resize((200, 170))
#     img2 = ImageTk.PhotoImage(img2)
#     canvas2.create_image(10, 10, anchor=NW, image=img2)
#     canvas2.pack(padx=20, pady=20)

#     custom_button.TkinterCustomButton(master=obscure_frame, text="Go Back", height=40, corner_radius=10,
#                                       command=lambda: load_menu(window, obscure_frame)).place(relx=0.08, rely=0.08,
#                                                                                               anchor=CENTER)

#     while True:
#         window.update_idletasks()
#         window.update()



# import tkinter as tk
# from tkinter import *
# import custom_button
# import main_menu
# import speech_recognition as sr
# import utils
# from PIL import ImageTk, Image
# import random

# def load_menu(window, frame):
#     frame.pack_forget()  # Hide the obscured frame
#     main_menu.start(window)  # Show the main menu

# original_text = []
# recognizer = sr.Recognizer()  # Create recognizer globally
# mic_active = False  # To keep track of microphone state

# def create_popup(window, message, title="Notification", authenticated=True):
#     popup = Toplevel(window)
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
#         command=lambda: [popup.destroy(), handle_user_removal(window) if not authenticated else None],
#         bg="#444444",
#         text_color="white"
#     )
#     button.pack(pady=10)

# def handle_user_removal(window):
#     print("User removed from the site.")
#     blank_screen(window)

# def blank_screen(window):
#     # Clear the window and display a blank message
#     for widget in window.winfo_children():
#         widget.destroy()

#     blank_frame = Frame(window, bg="black")
#     blank_frame.pack(fill='both', expand=True)

#     label = Label(blank_frame, text="You have been unauthenticated.", font=("Arial", 24), bg="black", fg="white")
#     label.pack(expand=True)

#     custom_button.TkinterCustomButton(
#         master=blank_frame,
#         text="Return to Main Menu",
#         height=40,
#         corner_radius=10,
#         command=lambda: load_menu(window, blank_frame),
#         bg="#444444",
#         text_color="white"
#     ).pack(pady=20)

# def start_recognition():
#     global mic_active
#     mic_active = True
#     print("Say Something. Say 'stop' to end recording.")

#     with sr.Microphone() as source:
#         try:
#             audio = recognizer.listen(source)  # Listens for audio
#             input_text = recognizer.recognize_google(audio)  # Recognizes text using speech recognition
#             process_input(input_text)
#         except Exception as ex:
#             print(f"Error: {ex}")
#             create_popup(window, "Error in speech recognition", title="Error")
#         finally:
#             mic_active = False

# def process_input(input_text):
#     input_text = input_text.lower().replace(' ', '-')  # Process the input

#     print("Original Text = ", original_text[0])
#     print("Input Text = ", input_text)

#     if original_text[0] == input_text:
#         print("Authenticated")
#         create_popup(window, "Authenticated :)", title="Success", authenticated=True)
#     else:
#         print("Authentication Failed")
#         create_popup(window, "Go Away Robot >_<", title="Failure", authenticated=False)

# def start(window):
#     obscuredImages = utils.getObscuredImages()
#     num = random.randint(0, len(obscuredImages) - 1)
#     filename = obscuredImages[num]  # Filename that will be displayed
#     filepath = "obscuredImages/original_obscure.txt"  # File Path

#     f = open(filepath, "r")
#     while True:
#         string = f.readline()  # Reading file line by line
#         s1 = string.split(' ')[0]  # Getting first word (filename) of line
#         if s1 == filename[0:len(filename) - 4]:  # Don't need the file extension, only name
#             break

#     string = string[9:]  # Cropping string
#     original_text.append(string.replace(' ', '-').rstrip())  # Removing \n
#     f.close()

#     window.title("Graphical Authentication System")
#     window.geometry("1280x600")
#     window.configure(bg="black")  # Set the background color to black

#     # Create and pack the obscured frame
#     obscure_frame = Frame(window, bg="black")
#     obscure_frame.pack(fill='both', expand=True)

#     label = Label(obscure_frame, text="Speak the words in the following image",
#                   font=('Calibri', 20), bg="black", fg="white")
#     label.pack(padx=40, pady=(20, 10))

#     canvas = Canvas(obscure_frame, width=450, height=300, bg="black", highlightthickness=0)
#     img = Image.open("obscuredImages/" + filename)
#     img = img.resize((450, 300))
#     img = ImageTk.PhotoImage(img)
#     canvas.create_image(0, 0, anchor=NW, image=img)
#     canvas.pack(padx=10, pady=(10, 20))

#     start_button = custom_button.TkinterCustomButton(
#         master=obscure_frame,
#         text="Start",
#         height=40,
#         corner_radius=10,
#         command=start_recognition,
#         bg="#444444",
#         text_color="white"
#     )
#     start_button.pack(pady=(0, 10))

#     stop_button = custom_button.TkinterCustomButton(
#         master=obscure_frame,
#         text="Stop",
#         height=40,
#         corner_radius=10,
#         command=lambda: print("Recording stopped"),  # Placeholder for stopping
#         bg="#444444",
#         text_color="white"
#     )
#     stop_button.pack(pady=(0, 10))

#     custom_button.TkinterCustomButton(
#         master=obscure_frame,
#         text="Go Back",
#         height=40,
#         corner_radius=10,
#         command=lambda: load_menu(window, obscure_frame),
#         bg="#444444",
#         text_color="white"
#     ).place(relx=0.08, rely=0.08, anchor=CENTER)

#     window.mainloop()  # Start the main loop for the window



# import tkinter as tk
# from tkinter import Toplevel, Frame, Label, Canvas
# import custom_button
# import main_menu
# import speech_recognition as sr
# import utils
# from PIL import ImageTk, Image
# import random

# original_text = []
# recognizer = sr.Recognizer()  # Create recognizer globally
# mic_active = False  # To keep track of microphone state

# def load_menu(window, frame):
#     frame.pack_forget()  # Hide the obscured frame
#     main_menu.start(window)  # Show the main menu

# def create_popup(window, message, title="Notification", authenticated=True):
#     popup = Toplevel(window)
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
#         command=lambda: [popup.destroy(), handle_user_removal(window) if not authenticated else None],
#         bg="#444444",
#         text_color="white"
#     )
#     button.pack(pady=10)

# def handle_user_removal(window):
#     # Use after() to delay the removal
#     window.after(100, lambda: blank_screen(window))

# def blank_screen(window):
#     for widget in window.winfo_children():
#         widget.destroy()

#     blank_frame = Frame(window, bg="black")
#     blank_frame.pack(fill='both', expand=True)

#     label = Label(blank_frame, text="You have been unauthenticated.", font=("Arial", 24), bg="black", fg="white")
#     label.pack(expand=True)

#     custom_button.TkinterCustomButton(
#         master=blank_frame,
#         text="Return to Main Menu",
#         height=40,
#         corner_radius=10,
#         command=lambda: load_menu(window, blank_frame),
#         bg="#444444",
#         text_color="white"
#     ).pack(pady=20)

# def start_recognition(window):
#     global mic_active
#     mic_active = True
#     print("Say Something. Say 'stop' to end recording.")

#     with sr.Microphone() as source:
#         try:
#             audio = recognizer.listen(source)  # Listens for audio
#             input_text = recognizer.recognize_google(audio)  # Recognizes text using speech recognition
#             process_input(input_text, window)
#         except sr.UnknownValueError:
#             print("Could not understand audio")
#             create_popup(window, "Could not understand audio", title="Error")
#         except Exception as ex:
#             print(f"Error: {ex}")
#             create_popup(window, "Error in speech recognition", title="Error")
#         finally:
#             mic_active = False

# def process_input(input_text, window):
#     input_text = input_text.lower().replace(' ', '-')  # Process the input

#     print("Original Text = ", original_text[0])
#     print("Input Text = ", input_text)

#     if original_text[0] == input_text:
#         print("Authenticated")
#         create_popup(window, "Authenticated :)", title="Success", authenticated=True)
#     else:
#         print("Authentication Failed")
#         create_popup(window, "Go Away Robot >_<", title="Failure", authenticated=False)

# def start(window):
#     obscuredImages = utils.getObscuredImages()
#     num = random.randint(0, len(obscuredImages) - 1)
#     filename = obscuredImages[num]  # Filename that will be displayed
#     filepath = "obscuredImages/original_obscure.txt"  # File Path

#     with open(filepath, "r") as f:
#         while True:
#             string = f.readline()  # Reading file line by line
#             s1 = string.split(' ')[0]  # Getting first word (filename) of line
#             if s1 == filename[0:len(filename) - 4]:  # Don't need the file extension, only name
#                 break

#         string = string[9:]  # Cropping string
#         original_text.append(string.replace(' ', '-').rstrip())  # Removing \n

#     window.title("Graphical Authentication System")
#     window.geometry("1280x600")
#     window.configure(bg="black")  # Set the background color to black

#     # Create and pack the obscured frame
#     obscure_frame = Frame(window, bg="black")
#     obscure_frame.pack(fill='both', expand=True)

#     label = Label(obscure_frame, text="Speak the words in the following image",
#                   font=('Calibri', 20), bg="black", fg="white")
#     label.pack(padx=40, pady=(20, 10))

#     canvas = Canvas(obscure_frame, width=450, height=300, bg="black", highlightthickness=0)
#     img = Image.open("obscuredImages/" + filename)
#     img = img.resize((450, 300))
#     img = ImageTk.PhotoImage(img)
#     canvas.create_image(0, 0, anchor=tk.NW, image=img)
#     canvas.pack(padx=10, pady=(10, 20))

#     start_button = custom_button.TkinterCustomButton(
#         master=obscure_frame,
#         text="Start",
#         height=40,
#         corner_radius=10,
#         command=lambda: start_recognition(window),
#         bg="#444444",
#         text_color="white"
#     )
#     start_button.pack(pady=(0, 10))

#     stop_button = custom_button.TkinterCustomButton(
#         master=obscure_frame,
#         text="Stop",
#         height=40,
#         corner_radius=10,
#         command=lambda: print("Recording stopped"),  # Placeholder for stopping
#         bg="#444444",
#         text_color="white"
#     )
#     stop_button.pack(pady=(0, 10))

#     custom_button.TkinterCustomButton(
#         master=obscure_frame,
#         text="Go Back",
#         height=40,
#         corner_radius=10,
#         command=lambda: load_menu(window, obscure_frame),
#         bg="#444444",
#         text_color="white"
#     ).place(relx=0.08, rely=0.08, anchor=tk.CENTER)

#     window.mainloop()  # Start the main loop for the window

import tkinter as tk
from tkinter import Toplevel, Frame, Label, Canvas
import custom_button
import main_menu
import speech_recognition as sr
import utils
from PIL import ImageTk, Image
import random

original_text = []
recognizer = sr.Recognizer()  # Create recognizer globally
mic_active = False  # To keep track of microphone state

def load_menu(window, frame):
    frame.pack_forget()  # Hide the obscured frame
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
    # Use after() to delay the removal
    window.after(100, lambda: blank_screen(window))

def blank_screen(window):
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

def start_recognition(window):
    global mic_active
    mic_active = True
    print("Say Something. Say 'stop' to end recording.")

    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source)  # Listens for audio
            input_text = recognizer.recognize_google(audio)  # Recognizes text using speech recognition
            process_input(input_text, window)
        except sr.UnknownValueError:
            print("Could not understand audio")
            create_popup(window, "Could not understand audio", title="Error")
        except Exception as ex:
            print(f"Error: {ex}")
            create_popup(window, "Error in speech recognition", title="Error")
        finally:
            mic_active = False

def process_input(input_text, window):
    input_text = input_text.lower().replace(' ', '-')  # Process the input

    print("Original Text = ", original_text[0])
    print("Input Text = ", input_text)

    if original_text[0] == input_text:
        print("Authenticated")
        create_popup(window, "Authenticated :)", title="Success", authenticated=True)
    else:
        print("Authentication Failed")
        create_popup(window, "Go Away Robot >_<", title="Failure", authenticated=False)

def start(window):
    obscuredImages = utils.getObscuredImages()
    num = random.randint(0, len(obscuredImages) - 1)
    filename = obscuredImages[num]  # Filename that will be displayed

    filepath = "obscuredImages/original_obscure.txt"  # File Path
    try:
        with open(filepath, "r") as f:
            for line in f:  # Using a for loop to read lines
                s1 = line.split(' ')[0]  # Getting first word (filename) of line
                if s1 == filename[:-4]:  # Don't need the file extension, only name
                    original_text.append(line[9:].replace(' ', '-').rstrip())  # Removing \n
                    break

        # Validate that the filename corresponds to an image
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            raise ValueError("Selected file is not a valid image.")

        img_path = "obscuredImages/" + filename
        img = Image.open(img_path)  # Attempt to open the image
        img = img.resize((450, 300))
        img = ImageTk.PhotoImage(img)

    except FileNotFoundError:
        print(f"File not found: {img_path}")
        create_popup(window, "Image file not found", title="Error")
        return
    except ValueError as ve:
        print(ve)
        create_popup(window, str(ve), title="Error")
        return
    except Exception as ex:
        print(f"Error loading image: {ex}")
        create_popup(window, "Error loading image", title="Error")
        return

    window.title("Graphical Authentication System")
    window.geometry("1280x600")
    window.configure(bg="black")  # Set the background color to black

    # Create and pack the obscured frame
    obscure_frame = Frame(window, bg="black")
    obscure_frame.pack(fill='both', expand=True)

    label = Label(obscure_frame, text="Speak the words in the following image",
                  font=('Calibri', 20), bg="black", fg="white")
    label.pack(padx=40, pady=(20, 10))

    canvas = Canvas(obscure_frame, width=450, height=300, bg="black", highlightthickness=0)
    canvas.create_image(0, 0, anchor=tk.NW, image=img)
    canvas.image = img  # Keep a reference to avoid garbage collection
    canvas.pack(padx=10, pady=(10, 20))

    start_button = custom_button.TkinterCustomButton(
        master=obscure_frame,
        text="Start",
        height=40,
        corner_radius=10,
        command=lambda: start_recognition(window),
        bg="#444444",
        text_color="white"
    )
    start_button.pack(pady=(0, 10))

    stop_button = custom_button.TkinterCustomButton(
        master=obscure_frame,
        text="Stop",
        height=40,
        corner_radius=10,
        command=lambda: print("Recording stopped"),  # Placeholder for stopping
        bg="#444444",
        text_color="white"
    )
    stop_button.pack(pady=(0, 10))

    custom_button.TkinterCustomButton(
        master=obscure_frame,
        text="Go Back",
        height=40,
        corner_radius=10,
        command=lambda: load_menu(window, obscure_frame),
        bg="#444444",
        text_color="white"
    ).place(relx=0.08, rely=0.08, anchor=tk.CENTER)

    window.mainloop()  # Start the main loop for the window

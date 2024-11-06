# from tkinter import messagebox
# import copy
# import hashlib
# from random import randint

# import tkinter
# from tkinter import *
# import custom_button
# import main_menu

# import utils
# from PIL import ImageTk, Image
# from tkinter import Entry

# s_image = []
# s_image.append("")

# def load_menu(window, frame):
#     frame.pack_forget()
#     main_menu.start(window)


# # saves image selected by user
# def clicked(canvas, img_name, event):
#     canvas.config(highlightthickness=1, highlightbackground="black")
#     s_image[0] = img_name;
#     # print(s_image[0])


# # authenticate credentials provided by users
# def authenticate(selected_image, selected_password, selected_name):
#     # checks if there is no empty entry
#     if selected_name == "":
#         messagebox.showinfo("Login System", "Please enter the Username")
#     elif selected_password == "":
#         messagebox.showinfo("Login System", "Please enter the Password")
#     elif selected_name == "" and selected_password == "":
#         messagebox.showinfo("Login System", "Please enter the Username and Password")
#     # print("hiii",selected_image)

#     # taking hash of password entered as its hash stored in backend
#     h = hashlib.new('sha512_256')
#     h.update(selected_password.encode())
#     selected_password = h.hexdigest()
#     filepath = "credentialImages/orig_credentials.txt"  # File Path
#     f = open(filepath, "r")
#     name = ""
#     password = ""
#     image = ""
#     str = ""
#     isUser = 0
#     # file reading to get original credentials
#     while True:
#         string = f.readline()  # Reading file line by line
#         if string == "":
#             if (isUser == 0):
#                 print("username not exist")
#                 messagebox.showinfo("Login System", "password is not correct")
#             break
#         info = string.split(" ")
#         name = copy.deepcopy(info[0])
#         password = copy.deepcopy(info[1])
#         image = copy.deepcopy(info[2])
#         name = name.rstrip()
#         password = password.rstrip()
#         image = image.rstrip()

#         # checks the credentials by somparing with original one
#         if name == selected_name:
#             isUser = 1
#             if password == selected_password:
#                 if image == selected_image:
#                     print("authenticated!!")
#                     messagebox.showinfo("Login System", "authenticated!!")
#                     break
#                 else:
#                     print("image is not correct")
#                     messagebox.showinfo("Login System", "image is not correct")

#                     break
#             else:
#                 print("password is not correct")
#                 messagebox.showinfo("Login System", "password is not correct")
#                 break


# # login page canvas
# def create_canvas(window):
#     window.title("Login Page")
#     window.geometry("1280x600")

#     root = Frame(window, height=600, width=1280)
#     root.pack(fill='both', expand=1)

#     #root.title("Login Page")
#     #root.resizable(0, 0)
#     width = 700
#     height = 700
#     # image class names
#     img_name1 = "cat"
#     img_name2 = "flower"
#     img_name3 = "mouse"

#     # Generates random number to display images
#     num = randint(0, 2)
#     print("Random number = ", num)
#     selected_image = ""

#     # getting image paths from utils
#     imgList = utils.getCredentialImages()

#     # canvas for title
#     canvas = Canvas(root, width=width, height=height, bd=0, highlightthickness=0)
#     canvas.pack(fill=BOTH, expand=True)
#     canvas.create_image(0, 0, anchor='nw')
#     label = Label(root, text="Login Page", font=("Ariel 15 bold"))
#     canvas.create_window(550, 40, anchor="nw", window=label)

#     # canvas for username title
#     user_label = Label(root, text="User name:", font=("Ariel 12 bold"))
#     canvas.create_window(480, 130, anchor="nw", window=user_label)

#     # canvas for password title
#     password_label = Label(root, text="Password:", font=("Ariel 12 bold"))
#     canvas.create_window(480, 210, anchor="nw", window=password_label)

#     # usernmae input feild display
#     user_entry = Entry(root, font=("Ariel 12"))
#     user_entry.focus()
#     selected_name = user_entry.get()
#     canvas.create_window(580, 130, anchor="nw", window=user_entry)

#     # password input feild display
#     pas = StringVar()
#     password_entry = Entry(root, textvar=pas, font=("Ariel 12"), show="*")
#     selected_password = password_entry.get()
#     canvas.create_window(580, 210, anchor="nw", window=password_entry)

#     # Random image display from first class
#     canvas2 = Canvas(root, width=110, height=70)
#     canvas2.bind("<Button-1>",
#                  lambda event: clicked(canvas2, img_name1, event))  # binding button to check if image is clicked
#     canvas2.place(x=450, y=290)
#     img2 = (Image.open("credentialImages/" + imgList[num]))
#     img2 = img2.resize((90, 60))
#     img2 = ImageTk.PhotoImage(img2)
#     canvas2.create_image(10, 10, anchor="nw", image=img2)

#     # Random image display from second class
#     canvas3 = Canvas(root, width=110, height=70)
#     canvas3.bind("<Button-1>",
#                  lambda event: clicked(canvas3, img_name2, event))  # binding button to check if image is clicked
#     canvas3.place(x=600, y=290)
#     img3 = (Image.open("credentialImages/" + imgList[num + 3]))
#     img3 = img3.resize((90, 60))
#     img3 = ImageTk.PhotoImage(img3)
#     canvas3.create_image(10, 10, anchor="nw", image=img3)

#     # Random image display from third class
#     canvas4 = Canvas(root, width=110, height=70)
#     canvas4.bind("<Button-1>",
#                  lambda event: clicked(canvas4, img_name3, event))  # binding button to check if image is clicked
#     canvas4.place(x=750, y=290)
#     img4 = (Image.open("credentialImages/" + imgList[num + 6]))
#     img4 = img4.resize((90, 60))
#     img4 = ImageTk.PhotoImage(img4)
#     canvas4.create_image(10, 10, anchor="nw", image=img4)

#     # login button display
#     # calls authenticate on click with credentials as arguments
#     login = custom_button.TkinterCustomButton(master=root, text="Log In", height=40, corner_radius=10,
#                    command=lambda: authenticate(s_image[0], password_entry.get(), user_entry.get())).place(relx=0.5, rely=0.7, anchor=CENTER)

#     custom_button.TkinterCustomButton(master=root, text="Go Back", height=40, corner_radius=10,
#                                       command=lambda: load_menu(window, root)).place(relx=0.08, rely=0.08,
#                                                                                               anchor=CENTER)

#     window.mainloop()


# def start(window):
#     create_canvas(window)

# from tkinter import messagebox
# import hashlib
# from random import randint
# import tkinter as tk
# from tkinter import Frame, Label, Entry, StringVar
# import custom_button
# import main_menu
# import utils
# from PIL import ImageTk, Image

# s_image = [None]  # Use None for better clarity on uninitialized state

# def load_menu(window, frame):
#     frame.pack_forget()
#     main_menu.start(window)

# def clicked(canvas, img_name, event):
#     canvas.config(highlightthickness=1, highlightbackground="black")
#     s_image[0] = img_name

# def authenticate(selected_image, selected_password, selected_name):
#     if not selected_name:
#         messagebox.showinfo("Login System", "Please enter the Username")
#         return
#     elif not selected_password:
#         messagebox.showinfo("Login System", "Please enter the Password")
#         return

#     # Hash the password
#     h = hashlib.new('sha512_256')
#     h.update(selected_password.encode())
#     selected_password = h.hexdigest()
    
#     filepath = "credentialImages/orig_credentials.txt"
#     try:
#         with open(filepath, "r") as f:
#             users = f.readlines()

#         for line in users:
#             info = line.strip().split(" ")
#             name, password, image = info[0], info[1], info[2]

#             if name == selected_name:
#                 if password == selected_password and image == selected_image:
#                     messagebox.showinfo("Login System", "Authenticated!")
#                     return
#                 else:
#                     messagebox.showinfo("Login System", "Invalid password or image.")
#                     return

#         messagebox.showinfo("Login System", "Username does not exist.")
#     except FileNotFoundError:
#         messagebox.showerror("Error", "Credentials file not found.")
#     except Exception as e:
#         messagebox.showerror("Error", str(e))

# def create_canvas(window):
#     window.title("Login Page")
#     window.geometry("1280x600")

#     root = Frame(window, height=600, width=1280, bg="black")
#     root.pack(fill='both', expand=1)

#     Label(root, text="Login Page", font=("Ariel 15 bold"), bg='black', fg='white').pack(pady=10)

#     # Username input field
#     Label(root, text="User name:", font=("Ariel 12"), bg='black', fg='white').pack(pady=(20, 0))
#     user_entry = Entry(root, font=("Ariel 12"))
#     user_entry.focus()
#     user_entry.pack(pady=(0, 20))

#     # Password input field
#     Label(root, text="Password:", font=("Ariel 12"), bg='black', fg='white').pack(pady=(20, 0))
#     pas = StringVar()
#     password_entry = Entry(root, textvariable=pas, font=("Ariel 12"), show="*")
#     password_entry.pack(pady=(0, 20))

#     # Random image display from utils
#     imgList = utils.getCredentialImages()
#     num = randint(0, len(imgList) - 3)

#     image_frame = Frame(root, bg='black')
#     image_frame.pack(pady=10)

#     for i in range(3):
#         img_canvas = tk.Canvas(image_frame, width=110, height=70, bg='black', highlightthickness=0)
#         img_canvas.bind("<Button-1>", lambda event, img_name=imgList[num + i]: clicked(img_canvas, img_name, event))
#         img_canvas.pack(side=tk.LEFT, padx=10)
        
#         img = Image.open("credentialImages/" + imgList[num + i])
#         img = img.resize((90, 60))
#         img_photo = ImageTk.PhotoImage(img)
#         img_canvas.create_image(10, 10, anchor='nw', image=img_photo)
#         img_canvas.image = img_photo  # Keep a reference to avoid garbage collection

#     # Login button
#     custom_button.TkinterCustomButton(
#         master=root,
#         text="Log In",
#         height=40,
#         corner_radius=10,
#         command=lambda: authenticate(s_image[0], password_entry.get(), user_entry.get())
#     ).pack(pady=20)

#     # Go Back button
#     custom_button.TkinterCustomButton(
#         master=root,
#         text="Go Back",
#         height=40,
#         corner_radius=10,
#         command=lambda: load_menu(window, root)
#     ).pack(pady=5)

#     window.mainloop()

# def start(window):
#     create_canvas(window)


from tkinter import messagebox, StringVar, Entry, Frame, Label, Tk, Canvas
from PIL import ImageTk, Image
import hashlib
from random import randint
import custom_button  # Ensure this module is available
import utils  # Ensure this module is also available
import main_menu  # Importing main_menu

s_image = [None]
current_frame = None
login_attempts = 0  # Counter for login attempts

def load_menu(window):
    main_menu.start(window)

def show_frame(frame):
    global current_frame
    if current_frame is not None:
        current_frame.pack_forget()  # Hide the current frame
    frame.pack(fill='both', expand=True)  # Show the new frame
    current_frame = frame

def clicked(canvas, img_name, event):
    canvas.config(highlightthickness=1, highlightbackground="black")
    s_image[0] = img_name

def authenticate(selected_image, selected_password, selected_name):
    global login_attempts
    if selected_name == "" or selected_password == "":
        messagebox.showinfo("Login System", "Please enter both Username and Password")
        return

    # Hash the password
    h = hashlib.new('sha512_256')
    h.update(selected_password.encode())
    selected_password = h.hexdigest()

    filepath = "credentialImages/orig_credentials.txt"
    try:
        with open(filepath, "r") as f:
            for line in f:
                info = line.split(" ")
                if len(info) < 3:
                    continue  # Skip malformed lines
                name = info[0].rstrip()
                password = info[1].rstrip()
                image = info[2].rstrip()

                if name == selected_name:
                    if password == selected_password and image == selected_image:
                        messagebox.showinfo("Login System", "Authenticated!")
                        login_attempts = 0  # Reset attempts on successful login
                        load_menu(window)  # Redirect to main menu
                        return
                    else:
                        login_attempts += 1
                        messagebox.showinfo("Login System", "Invalid password or image.")
                        break  # Exit for loop after an invalid attempt

            if login_attempts >= 3:
                clear_login_fields()  # Clear fields after 3 attempts
                messagebox.showinfo("Login System", "Too many failed attempts. Please try again.")
            else:
                messagebox.showinfo("Login System", "Username does not exist.")
    except FileNotFoundError:
        messagebox.showinfo("Error", "Credentials file not found.")

def clear_login_fields():
    user_entry.delete(0, 'end')
    password_entry.delete(0, 'end')
    s_image[0] = None  # Reset the selected image

def register(username, password):
    if username == "" or password == "":
        messagebox.showinfo("Registration", "Username and Password cannot be empty.")
        return

    # Hash the password
    h = hashlib.new('sha512_256')
    h.update(password.encode())
    hashed_password = h.hexdigest()

    filepath = "credentialImages/orig_credentials.txt"
    try:
        with open(filepath, "a") as f:
            f.write(f"{username} {hashed_password} {s_image[0]}\n")  # Save the new user
        messagebox.showinfo("Registration", "User registered successfully!")
    except Exception as e:
        messagebox.showinfo("Registration", f"Error saving user: {e}")

def create_login_frame(window):
    frame = Frame(window, height=600, width=1280, bg="black")
    
    Label(frame, text="Login Page", font=("Ariel 15 bold"), bg='black', fg='white').pack(pady=10)

    Label(frame, text="Username:", font=("Ariel 12"), bg='black', fg='white').pack(pady=(20, 0))
    global user_entry
    user_entry = Entry(frame, font=("Ariel 12"))
    user_entry.focus()
    user_entry.pack(pady=(0, 20))

    Label(frame, text="Password:", font=("Ariel 12"), bg='black', fg='white').pack(pady=(20, 0))
    pas = StringVar()
    global password_entry
    password_entry = Entry(frame, textvariable=pas, font=("Ariel 12"), show="*")
    password_entry.pack(pady=(0, 20))

    imgList = utils.getCredentialImages()
    num = randint(0, len(imgList) - 3)

    image_frame = Frame(frame, bg='black')
    image_frame.pack(pady=10)

    for i in range(3):
        img_canvas = Canvas(image_frame, width=110, height=70, bg='black', highlightthickness=0)
        img_canvas.bind("<Button-1>", lambda event, img_name=imgList[num + i]: clicked(img_canvas, img_name, event))
        img_canvas.pack(side='left', padx=10)

        img = Image.open("credentialImages/" + imgList[num + i])
        img = img.resize((90, 60))
        img_photo = ImageTk.PhotoImage(img)
        img_canvas.create_image(10, 10, anchor='nw', image=img_photo)
        img_canvas.image = img_photo  # Keep a reference to avoid garbage collection

    login_button = custom_button.TkinterCustomButton(
        master=frame,
        text="Log In",
        height=40,
        corner_radius=10,
        command=lambda: authenticate(s_image[0], password_entry.get(), user_entry.get())
    )
    login_button.pack(pady=(20, 5))

    register_button = custom_button.TkinterCustomButton(
        master=frame,
        text="Register",
        height=40,
        corner_radius=10,
        command=lambda: show_frame(create_registration_frame(window))
    )
    register_button.pack(pady=(5, 20))

    return frame

def create_registration_frame(window):
    frame = Frame(window, height=600, width=1280, bg="black")
    
    Label(frame, text="Registration Page", font=("Ariel 15 bold"), bg='black', fg='white').pack(pady=10)

    Label(frame, text="Username:", font=("Ariel 12"), bg='black', fg='white').pack(pady=(20, 0))
    user_entry = Entry(frame, font=("Ariel 12"))
    user_entry.focus()
    user_entry.pack(pady=(0, 20))

    Label(frame, text="Password:", font=("Ariel 12"), bg='black', fg='white').pack(pady=(20, 0))
    pas = StringVar()
    password_entry = Entry(frame, textvariable=pas, font=("Ariel 12"), show="*")
    password_entry.pack(pady=(0, 20))

    imgList = utils.getCredentialImages()
    num = randint(0, len(imgList) - 3)

    image_frame = Frame(frame, bg='black')
    image_frame.pack(pady=10)

    for i in range(3):
        img_canvas = Canvas(image_frame, width=110, height=70, bg='black', highlightthickness=0)
        img_canvas.bind("<Button-1>", lambda event, img_name=imgList[num + i]: clicked(img_canvas, img_name, event))
        img_canvas.pack(side='left', padx=10)

        img = Image.open("credentialImages/" + imgList[num + i])
        img = img.resize((90, 60))
        img_photo = ImageTk.PhotoImage(img)
        img_canvas.create_image(10, 10, anchor='nw', image=img_photo)
        img_canvas.image = img_photo  # Keep a reference to avoid garbage collection

    register_button = custom_button.TkinterCustomButton(
        master=frame,
        text="Register",
        height=40,
        corner_radius=10,
        command=lambda: register(user_entry.get(), password_entry.get())
    )
    register_button.pack(pady=(20, 5))

    back_button = custom_button.TkinterCustomButton(
        master=frame,
        text="Back to Login",
        height=40,
        corner_radius=10,
        command=lambda: show_frame(create_login_frame(window))
    )
    back_button.pack(pady=(5, 20))

    return frame

def start(window):
    show_frame(create_login_frame(window))

if __name__ == "__main__":
    window = Tk()
    start(window)
    window.mainloop()

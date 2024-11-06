# from tkinter import messagebox, StringVar, Entry, Frame, Label, Tk, Canvas
# from PIL import ImageTk, Image
# import hashlib
# from random import randint
# import custom_button  # Ensure this module is available
# import utils  # Ensure this module is also available
# import main_menu  # Importing main_menu

# s_image = [None]
# current_frame = None

# def load_menu(window):
#     main_menu.start(window)

# def show_frame(frame):
#     global current_frame
#     if current_frame is not None:
#         current_frame.pack_forget()
#     frame.pack(fill='both', expand=True)
#     current_frame = frame

# def clicked(canvas, img_name, event):
#     canvas.config(highlightthickness=1, highlightbackground="black")
#     s_image[0] = img_name

# def authenticate(selected_image, selected_password, selected_name):
#     if selected_name == "" or selected_password == "":
#         messagebox.showinfo("Login System", "Please enter both Username and Password")
#         return

#     # Hash the password
#     h = hashlib.new('sha512_256')
#     h.update(selected_password.encode())
#     selected_password = h.hexdigest()

#     filepath = "credentialImages/orig_credentials.txt"
#     try:
#         with open(filepath, "r") as f:
#             for line in f:
#                 info = line.split(" ")
#                 if len(info) < 3:
#                     continue  # Skip malformed lines
#                 name = info[0].rstrip()
#                 password = info[1].rstrip()
#                 image = info[2].rstrip()

#                 if name == selected_name:
#                     if password == selected_password and image == selected_image:
#                         messagebox.showinfo("Login System", "Authenticated!")
#                         load_menu(window)  # Redirect to main menu
#                         return
#                     else:
#                         messagebox.showinfo("Login System", "Invalid password or image.")
#                         return

#             messagebox.showinfo("Login System", "Username does not exist.")
#     except FileNotFoundError:
#         messagebox.showinfo("Error", "Credentials file not found.")

# def register(username, password):
#     if username == "" or password == "":
#         messagebox.showinfo("Registration", "Username and Password cannot be empty.")
#         return

#     # Hash the password
#     h = hashlib.new('sha512_256')
#     h.update(password.encode())
#     hashed_password = h.hexdigest()

#     filepath = "credentialImages/orig_credentials.txt"
#     try:
#         with open(filepath, "a") as f:
#             f.write(f"{username} {hashed_password} {s_image[0]}\n")  # Save the new user
#         messagebox.showinfo("Registration", "User registered successfully!")
#     except Exception as e:
#         messagebox.showinfo("Registration", f"Error saving user: {e}")

# def create_login_frame(window):
#     frame = Frame(window, height=600, width=1280, bg="black")
#     frame.pack(fill='both', expand=True)

#     Label(frame, text="Login Page", font=("Ariel 15 bold"), bg='black', fg='white').pack(pady=10)

#     Label(frame, text="Username:", font=("Ariel 12"), bg='black', fg='white').pack(pady=(20, 0))
#     user_entry = Entry(frame, font=("Ariel 12"))
#     user_entry.focus()
#     user_entry.pack(pady=(0, 20))

#     Label(frame, text="Password:", font=("Ariel 12"), bg='black', fg='white').pack(pady=(20, 0))
#     pas = StringVar()
#     password_entry = Entry(frame, textvariable=pas, font=("Ariel 12"), show="*")
#     password_entry.pack(pady=(0, 20))

#     imgList = utils.getCredentialImages()
#     num = randint(0, len(imgList) - 3)

#     image_frame = Frame(frame, bg='black')
#     image_frame.pack(pady=10)

#     for i in range(3):
#         img_canvas = Canvas(image_frame, width=110, height=70, bg='black', highlightthickness=0)
#         img_canvas.bind("<Button-1>", lambda event, img_name=imgList[num + i]: clicked(img_canvas, img_name, event))
#         img_canvas.pack(side='left', padx=10)

#         img = Image.open("credentialImages/" + imgList[num + i])
#         img = img.resize((90, 60))
#         img_photo = ImageTk.PhotoImage(img)
#         img_canvas.create_image(10, 10, anchor='nw', image=img_photo)
#         img_canvas.image = img_photo  # Keep a reference to avoid garbage collection

#     login_button = custom_button.TkinterCustomButton(
#         master=frame,
#         text="Log In",
#         height=40,
#         corner_radius=10,
#         command=lambda: authenticate(s_image[0], password_entry.get(), user_entry.get())
#     )
#     login_button.pack(pady=(20, 5))

#     register_button = custom_button.TkinterCustomButton(
#         master=frame,
#         text="Register",
#         height=40,
#         corner_radius=10,
#         command=lambda: show_frame(create_registration_frame(window))
#     )
#     register_button.pack(pady=(5, 20))

#     return frame

# def create_registration_frame(window):
#     frame = Frame(window, height=600, width=1280, bg="black")
    
#     Label(frame, text="Registration Page", font=("Ariel 15 bold"), bg='black', fg='white').pack(pady=10)

#     Label(frame, text="Username:", font=("Ariel 12"), bg='black', fg='white').pack(pady=(20, 0))
#     user_entry = Entry(frame, font=("Ariel 12"))
#     user_entry.focus()
#     user_entry.pack(pady=(0, 20))

#     Label(frame, text="Password:", font=("Ariel 12"), bg='black', fg='white').pack(pady=(20, 0))
#     pas = StringVar()
#     password_entry = Entry(frame, textvariable=pas, font=("Ariel 12"), show="*")
#     password_entry.pack(pady=(0, 20))

#     imgList = utils.getCredentialImages()
#     num = randint(0, len(imgList) - 3)

#     image_frame = Frame(frame, bg='black')
#     image_frame.pack(pady=10)

#     for i in range(3):
#         img_canvas = Canvas(image_frame, width=110, height=70, bg='black', highlightthickness=0)
#         img_canvas.bind("<Button-1>", lambda event, img_name=imgList[num + i]: clicked(img_canvas, img_name, event))
#         img_canvas.pack(side='left', padx=10)

#         img = Image.open("credentialImages/" + imgList[num + i])
#         img = img.resize((90, 60))
#         img_photo = ImageTk.PhotoImage(img)
#         img_canvas.create_image(10, 10, anchor='nw', image=img_photo)
#         img_canvas.image = img_photo  # Keep a reference to avoid garbage collection

#     register_button = custom_button.TkinterCustomButton(
#         master=frame,
#         text="Register",
#         height=40,
#         corner_radius=10,
#         command=lambda: register(user_entry.get(), password_entry.get())
#     )
#     register_button.pack(pady=(20, 5))

#     back_button = custom_button.TkinterCustomButton(
#         master=frame,
#         text="Back to Login",
#         height=40,
#         corner_radius=10,
#         command=lambda: show_frame(create_login_frame(window))
#     )
#     back_button.pack(pady=(5, 20))

#     return frame

# def start(window):
#     show_frame(create_login_frame(window))

# if __name__ == "__main__":
#     window = Tk()
#     start(window)
#     window.mainloop()



# from tkinter import messagebox, StringVar, Entry, Frame, Label, Tk, Canvas
# from PIL import ImageTk, Image
# import hashlib
# from random import randint
# import custom_button  # Ensure this module is available
# import utils  # Ensure this module is also available
# import main_menu  # Importing main_menu

# s_image = [None]
# current_frame = None

# def show_frame(frame):
#     global current_frame
#     if current_frame is not None:
#         current_frame.pack_forget()  # Hide the current frame
#     frame.pack(fill='both', expand=True)  # Show the new frame
#     current_frame = frame

# def clicked(canvas, img_name, event):
#     canvas.config(highlightthickness=1, highlightbackground="black")
#     s_image[0] = img_name

# def authenticate(selected_image, selected_password, selected_name):
#     if selected_name == "" or selected_password == "":
#         messagebox.showinfo("Login System", "Please enter both Username and Password")
#         return

#     h = hashlib.new('sha512_256')
#     h.update(selected_password.encode())
#     selected_password = h.hexdigest()

#     filepath = "credentialImages/orig_credentials.txt"
#     try:
#         with open(filepath, "r") as f:
#             for line in f:
#                 info = line.split(" ")
#                 if len(info) < 3:
#                     continue
#                 name = info[0].rstrip()
#                 password = info[1].rstrip()
#                 image = info[2].rstrip()

#                 if name == selected_name:
#                     if password == selected_password and image == selected_image:
#                         messagebox.showinfo("Login System", "Authenticated!")
#                         load_menu()  # Redirect to main menu
#                         return
#                     else:
#                         messagebox.showinfo("Login System", "Invalid password or image.")
#                         return

#             messagebox.showinfo("Login System", "Username does not exist.")
#     except FileNotFoundError:
#         messagebox.showinfo("Error", "Credentials file not found.")

# def register(username, password):
#     if username == "" or password == "":
#         messagebox.showinfo("Registration", "Username and Password cannot be empty.")
#         return

#     h = hashlib.new('sha512_256')
#     h.update(password.encode())
#     hashed_password = h.hexdigest()

#     filepath = "credentialImages/orig_credentials.txt"
#     try:
#         with open(filepath, "a") as f:
#             f.write(f"{username} {hashed_password} {s_image[0]}\n")
#         messagebox.showinfo("Registration", "User registered successfully!")
#     except Exception as e:
#         messagebox.showinfo("Registration", f"Error saving user: {e}")

# def create_login_frame():
#     frame = Frame(window, height=600, width=1280, bg="black")
    
#     Label(frame, text="Login Page", font=("Ariel 15 bold"), bg='black', fg='white').pack(pady=10)

#     Label(frame, text="Username:", font=("Ariel 12"), bg='black', fg='white').pack(pady=(20, 0))
#     user_entry = Entry(frame, font=("Ariel 12"))
#     user_entry.focus()
#     user_entry.pack(pady=(0, 20))

#     Label(frame, text="Password:", font=("Ariel 12"), bg='black', fg='white').pack(pady=(20, 0))
#     pas = StringVar()
#     password_entry = Entry(frame, textvariable=pas, font=("Ariel 12"), show="*")
#     password_entry.pack(pady=(0, 20))

#     imgList = utils.getCredentialImages()
#     num = randint(0, len(imgList) - 3)

#     image_frame = Frame(frame, bg='black')
#     image_frame.pack(pady=10)

#     for i in range(3):
#         img_canvas = Canvas(image_frame, width=110, height=70, bg='black', highlightthickness=0)
#         img_canvas.bind("<Button-1>", lambda event, img_name=imgList[num + i]: clicked(img_canvas, img_name, event))
#         img_canvas.pack(side='left', padx=10)

#         img = Image.open("credentialImages/" + imgList[num + i])
#         img = img.resize((90, 60))
#         img_photo = ImageTk.PhotoImage(img)
#         img_canvas.create_image(10, 10, anchor='nw', image=img_photo)
#         img_canvas.image = img_photo

#     login_button = custom_button.TkinterCustomButton(
#         master=frame,
#         text="Log In",
#         height=40,
#         corner_radius=10,
#         command=lambda: authenticate(s_image[0], password_entry.get(), user_entry.get())
#     )
#     login_button.pack(pady=(20, 5))

#     register_button = custom_button.TkinterCustomButton(
#         master=frame,
#         text="Register",
#         height=40,
#         corner_radius=10,
#         command=lambda: show_frame(create_registration_frame())
#     )
#     register_button.pack(pady=(5, 20))

#     return frame

# def create_registration_frame():
#     frame = Frame(window, height=600, width=1280, bg="black")
    
#     Label(frame, text="Registration Page", font=("Ariel 15 bold"), bg='black', fg='white').pack(pady=10)

#     Label(frame, text="Username:", font=("Ariel 12"), bg='black', fg='white').pack(pady=(20, 0))
#     user_entry = Entry(frame, font=("Ariel 12"))
#     user_entry.focus()
#     user_entry.pack(pady=(0, 20))

#     Label(frame, text="Password:", font=("Ariel 12"), bg='black', fg='white').pack(pady=(20, 0))
#     pas = StringVar()
#     password_entry = Entry(frame, textvariable=pas, font=("Ariel 12"), show="*")
#     password_entry.pack(pady=(0, 20))

#     imgList = utils.getCredentialImages()
#     num = randint(0, len(imgList) - 3)

#     image_frame = Frame(frame, bg='black')
#     image_frame.pack(pady=10)

#     for i in range(3):
#         img_canvas = Canvas(image_frame, width=110, height=70, bg='black', highlightthickness=0)
#         img_canvas.bind("<Button-1>", lambda event, img_name=imgList[num + i]: clicked(img_canvas, img_name, event))
#         img_canvas.pack(side='left', padx=10)

#         img = Image.open("credentialImages/" + imgList[num + i])
#         img = img.resize((90, 60))
#         img_photo = ImageTk.PhotoImage(img)
#         img_canvas.create_image(10, 10, anchor='nw', image=img_photo)
#         img_canvas.image = img_photo

#     register_button = custom_button.TkinterCustomButton(
#         master=frame,
#         text="Register",
#         height=40,
#         corner_radius=10,
#         command=lambda: register(user_entry.get(), password_entry.get())
#     )
#     register_button.pack(pady=(20, 5))

#     back_button = custom_button.TkinterCustomButton(
#         master=frame,
#         text="Back to Login",
#         height=40,
#         corner_radius=10,
#         command=lambda: show_frame(create_login_frame())
#     )
#     back_button.pack(pady=(5, 20))

#     return frame

# def load_menu():
#     show_frame(main_menu.start(window))  # Assuming main_menu has a start function

# def start():
#     show_frame(create_login_frame())

# if __name__ == "__main__":
#     window = Tk()
#     start()
#     window.mainloop()
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

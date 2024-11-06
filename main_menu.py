# # Import the required libraries
# from tkinter import *
# from tkinter import font
# import custom_button
# import garbled
# import obscure
# import password
# import segments


# def load_garbled(window, menu_frame):
#     menu_frame.pack_forget()
#     garbled.start(window)


# def load_obscured(window, menu_frame):
#     menu_frame.pack_forget()
#     obscure.start(window)


# def load_segmented(window, menu_frame):
#     menu_frame.pack_forget()
#     segments.start(window)


# def load_password(window, menu_frame):
#     menu_frame.pack_forget()
#     password.start(window)


# def start(win):
#     win.geometry("1280x600")
#     win.title("Graphical Authentication System")

#     menu_frame = Frame(win, height=600, width=1280)
#     menu_frame.pack(fill='both', expand=1)

#     label = Label(menu_frame, text="Graphical Authentication System", font=('Freestyle Script', 54))
#     label.pack(padx=40, pady=30)

#     btn_height = 90
#     btn_width = 450
#     btn_font = ('Trebuchet MS', 14)

#     btn1 = custom_button.TkinterCustomButton(master=menu_frame, text="Test Garbled Images", text_font=btn_font,
#                                              height=btn_height, width=btn_width, corner_radius=10,
#                                              command=lambda: load_garbled(win, menu_frame)).place(relx=0.3, rely=0.4,
#                                                                                                   anchor=CENTER)
#     btn2 = custom_button.TkinterCustomButton(master=menu_frame, text="Test Segmented Images", text_font=btn_font,
#                                              height=btn_height, width=btn_width, corner_radius=10,
#                                              command=lambda: load_segmented(win, menu_frame)).place(relx=0.3,
#                                                                                                     rely=0.7,
#                                                                                                     anchor=CENTER)
#     btn3 = custom_button.TkinterCustomButton(master=menu_frame, text="Test Obscured Images", text_font=btn_font,
#                                              height=btn_height, width=btn_width, corner_radius=10,
#                                              command=lambda: load_obscured(win, menu_frame)).place(relx=0.7,
#                                                                                                    rely=0.4,
#                                                                                                    anchor=CENTER)
#     btn4 = custom_button.TkinterCustomButton(master=menu_frame, text="Test Password/Image Authentication",
#                                              text_font=btn_font,
#                                              height=btn_height, width=btn_width, corner_radius=10,
#                                              command=lambda: load_password(win, menu_frame)).place(relx=0.7,
#                                                                                                    rely=0.7,
#                                                                                                    anchor=CENTER)

#     win.mainloop()


# if __name__ == "__main__":
#     win = Tk()
#     start(win)



# from tkinter import *
# import custom_button
# import garbled
# import obscure
# import password
# import segments

# def load_garbled(window, menu_frame):
#     menu_frame.pack_forget()
#     garbled.start(window)

# def load_obscured(window, menu_frame):
#     menu_frame.pack_forget()
#     obscure.start(window)

# def load_segmented(window, menu_frame):
#     menu_frame.pack_forget()
#     segments.start(window)

# def load_password(window, menu_frame):
#     menu_frame.pack_forget()
#     password.start(window)

# def start(win):
#     win.geometry("1280x600")
#     win.title("Visual Verify")
#     win.configure(bg="black")  # Set the background color to black

#     menu_frame = Frame(win, bg="#2e2e2e", bd=5, relief=RAISED)  # Dark gray frame
#     menu_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

#     label = Label(menu_frame, text="Visual Verify", font=('Freestyle Script', 54), bg="#2e2e2e", fg="white")
#     label.pack(padx=40, pady=(30, 10))

#     btn_font = ('Trebuchet MS', 14)

#     def create_button(text, command):
#         btn = custom_button.TkinterCustomButton(
#             master=menu_frame,
#             text=text,
#             text_font=btn_font,
#             height=90,
#             width=450,
#             corner_radius=10,
#             command=command,
#             bg="#444444",  # Darker button color
#             border_color="#777777",
#             text_color="white"  # Button text color
#         )
#         btn.pack(pady=(10, 0))  # Vertical spacing between buttons

#     # Create buttons for navigation
#     create_button("Test Garbled Images", lambda: load_garbled(win, menu_frame))
#     create_button("Test Segmented Images", lambda: load_segmented(win, menu_frame))
#     create_button("Test Obscured Images", lambda: load_obscured(win, menu_frame))
#     create_button("Test Password/Image Authentication", lambda: load_password(win, menu_frame))

#     win.mainloop()

# if __name__ == "__main__":
#     win = Tk()
#     start(win)


# from tkinter import *
# import custom_button
# import garbled
# import obscure
# import password
# import segments

# def load_garbled(menu_frame):
#     menu_frame.pack_forget()  # Hide the menu frame
#     garbled.start()  # Call garbled's start function

# def load_obscured(menu_frame):
#     menu_frame.pack_forget()  # Hide the menu frame
#     obscure.start()  # Call obscured's start function

# def load_segmented(menu_frame):
#     menu_frame.pack_forget()  # Hide the menu frame
#     segments.start()  # Call segmented's start function

# def load_password(menu_frame):
#     menu_frame.pack_forget()  # Hide the menu frame
#     password.start()  # Call password's start function

# def create_menu_frame(win):
#     menu_frame = Frame(win, bg="#2e2e2e", bd=5, relief=RAISED)
#     menu_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

#     label = Label(menu_frame, text="Visual Verify", font=('Freestyle Script', 54), bg="#2e2e2e", fg="white")
#     label.pack(padx=40, pady=(30, 10))

#     btn_font = ('Trebuchet MS', 14)

#     def create_button(text, command):
#         btn = custom_button.TkinterCustomButton(
#             master=menu_frame,
#             text=text,
#             text_font=btn_font,
#             height=90,
#             width=450,
#             corner_radius=10,
#             command=command,
#             bg="#444444",
#             border_color="#777777",
#             text_color="white"
#         )
#         btn.pack(pady=(10, 0))

#     # Create buttons for navigation
#     create_button("Test Garbled Images", lambda: load_garbled(menu_frame))
#     create_button("Test Segmented Images", lambda: load_segmented(menu_frame))
#     create_button("Test Obscured Images", lambda: load_obscured(menu_frame))
#     create_button("Test Password/Image Authentication", lambda: load_password(menu_frame))

#     return menu_frame

# def start(win):
#     win.geometry("1280x600")
#     win.title("Visual Verify")
#     win.configure(bg="black")
#     create_menu_frame(win)

# if __name__ == "__main__":
#     win = Tk()
#     start(win)
#     win.mainloop()
from tkinter import *
import custom_button
import garbled
import obscure
import password
import segments

def load_garbled(win, menu_frame):
    menu_frame.pack_forget()  # Hide the menu frame
    garbled.start(win)  # Pass the window to garbled's start function

def load_obscured(win, menu_frame):
    menu_frame.pack_forget()  # Hide the menu frame
    obscure.start(win)  # Pass the window to obscured's start function

def load_segmented(win, menu_frame):
    menu_frame.pack_forget()  # Hide the menu frame
    segments.start(win)  # Pass the window to segmented's start function

def load_password(win, menu_frame):
    menu_frame.pack_forget()  # Hide the menu frame
    password.start(win)  # Call the start function in the password module

def create_menu_frame(win):
    menu_frame = Frame(win, bg="#2e2e2e", bd=5, relief=RAISED)
    menu_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    label = Label(menu_frame, text="Visual Verify", font=('Freestyle Script', 54), bg="#2e2e2e", fg="white")
    label.pack(padx=40, pady=(30, 10))

    btn_font = ('Trebuchet MS', 14)

    def create_button(text, command):
        btn = custom_button.TkinterCustomButton(
            master=menu_frame,
            text=text,
            text_font=btn_font,
            height=90,
            width=450,
            corner_radius=10,
            command=command,
            bg="#444444",
            border_color="#777777",
            text_color="white"
        )
        btn.pack(pady=(10, 0))

    # Create buttons for navigation
    create_button("Test Garbled Images", lambda: load_garbled(win, menu_frame))
    create_button("Test Segmented Images", lambda: load_segmented(win, menu_frame))
    create_button("Test Obscured Images", lambda: load_obscured(win, menu_frame))
    create_button("Test Password/Image Authentication", lambda: load_password(win, menu_frame))

    return menu_frame

def start(win):
    win.geometry("1280x600")
    win.title("Visual Verify")
    win.configure(bg="black")
    create_menu_frame(win)

if __name__ == "__main__":
    win = Tk()
    start(win)
    win.mainloop()

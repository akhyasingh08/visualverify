# import tkinter
# from tkinter import *
# import custom_button
# import main_menu

# import utils
# from PIL import ImageTk, Image
# import random


# def load_menu(window, frame):
#     frame.pack_forget()
#     main_menu.start(window)


# def start(window):
#     window.title("Graphical Authentication System")
#     window.geometry("1280x600")

#     segments_frame = Frame(window, height=600, width=1280)
#     segments_frame.pack(fill='both', expand=1)

#     label = Label(segments_frame, text="Please select the pictures in correct order", font=('Calibri', 20))
#     label.pack(padx=400, pady=10)

#     ## Draw order image

#     canvas = Canvas(segments_frame, width=300, height=250)
#     canvas.bind("<Button-1>", utils.callback)
#     img = (Image.open("segmentedImages/order.jpg"))
#     img = img.resize((300, 250))
#     img = ImageTk.PhotoImage(img)
#     canvas.create_image(10, 10, anchor=NW, image=img)
#     canvas.pack(padx=10, pady=10)

#     imgList = utils.getSegmentedImages("circle")
#     random.shuffle(imgList)
#     imgClickData = []

#     for imgPath in imgList:
#         var = utils.imageClick(imgPath)
#         imgClickData.append(var)

#     # Draw shuffled segments

#     canvas2 = Canvas(segments_frame, width=200, height=150)
#     canvas2.bind("<Button-1>", imgClickData[0].clicked)
#     canvas2.place(x=100, y=400)
#     img2 = (Image.open(imgList[0]))
#     img2 = img2.resize((200, 150))
#     img2 = ImageTk.PhotoImage(img2)
#     canvas2.create_image(10, 10, anchor=NW, image=img2)

#     canvas3 = Canvas(segments_frame, width=200, height=150)
#     canvas3.bind("<Button-1>", imgClickData[1].clicked)
#     canvas3.place(x=400, y=400)
#     img3 = (Image.open(imgList[1]))
#     img3 = img3.resize((200, 150))
#     img3 = ImageTk.PhotoImage(img3)
#     canvas3.create_image(10, 10, anchor=NW, image=img3)

#     canvas4 = Canvas(segments_frame, width=200, height=150)
#     canvas4.bind("<Button-1>", imgClickData[2].clicked)
#     canvas4.place(x=700, y=400)
#     img4 = (Image.open(imgList[2]))
#     img4 = img4.resize((200, 150))
#     img4 = ImageTk.PhotoImage(img4)
#     canvas4.create_image(10, 10, anchor=NW, image=img4)

#     canvas5 = Canvas(segments_frame, width=200, height=150)
#     canvas5.bind("<Button-1>", imgClickData[3].clicked)
#     canvas5.place(x=1000, y=400)
#     img5 = (Image.open(imgList[3]))
#     img5 = img5.resize((200, 150))
#     img5 = ImageTk.PhotoImage(img5)
#     canvas5.create_image(10, 10, anchor=NW, image=img5)

#     custom_button.TkinterCustomButton(master=segments_frame, text="Go Back", height=40, corner_radius=10,
#                                       command=lambda: load_menu(window, segments_frame)).place(relx=0.08, rely=0.08,
#                                                                                               anchor=CENTER)

#     while True:
#         window.update_idletasks()
#         window.update()

#         if utils.checkAllClicked(imgClickData):
#             sortedClickList = sorted(imgClickData)

#             if (sortedClickList[0].id == 1) and (sortedClickList[1].id == 2) and (sortedClickList[2].id == 3) and (
#                     sortedClickList[3].id == 4):
#                 utils.create_popup(msg="Authenticated :)", font="Gabriola 28 bold")
#             else:
#                 utils.create_popup(msg="Go Away Robot >_<", font="Gabriola 28 bold")

#             utils.setAllUnclicked(imgClickData)

# import tkinter as tk
# from tkinter import *
# import custom_button
# import main_menu
# import utils
# from PIL import ImageTk, Image
# import random

# def load_menu(window, frame):
#     frame.pack_forget()
#     main_menu.start(window)

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
#         command=lambda: [popup.destroy(), handle_user_removal()],
#         bg="#444444",
#         text_color="white"
#     )
#     button.pack(pady=10)

# def handle_user_removal():
#     print("User removed from the site.")
#     load_menu(window, segments_frame)  # Redirect to the main menu

# def start(window):
#     global segments_frame
#     segments_frame = Frame(window, bg="black")
#     segments_frame.pack(fill='both', expand=1)

#     window.title("Graphical Authentication System")
#     window.geometry("1280x600")
#     window.configure(bg="black")  # Set background color to black

#     label = Label(segments_frame, text="Please select the pictures in correct order", font=('Calibri', 20), bg="black", fg="white")
#     label.pack(pady=10)

#     # Draw order image
#     canvas_order = Canvas(segments_frame, width=300, height=250, bg="black", highlightthickness=0)
#     img_order = Image.open("segmentedImages/order.jpg")
#     img_order = img_order.resize((300, 250))
#     img_order = ImageTk.PhotoImage(img_order)
#     canvas_order.create_image(0, 0, anchor=NW, image=img_order)
#     canvas_order.pack(pady=10)

#     imgList = utils.getSegmentedImages("circle")
#     random.shuffle(imgList)
#     imgClickData = []

#     for imgPath in imgList:
#         var = utils.imageClick(imgPath)
#         imgClickData.append(var)

#     # Draw shuffled segments
#     for i in range(4):
#         canvas_segment = Canvas(segments_frame, width=200, height=150, bg="black", highlightthickness=0)
#         canvas_segment.bind("<Button-1>", imgClickData[i].clicked)
#         canvas_segment.place(x=100 + i * 300, y=400)
        
#         img_segment = Image.open(imgList[i])
#         img_segment = img_segment.resize((200, 150))
#         img_segment = ImageTk.PhotoImage(img_segment)
#         canvas_segment.create_image(0, 0, anchor=NW, image=img_segment)
#         canvas_segment.image = img_segment  # Keep a reference to avoid garbage collection

#     custom_button.TkinterCustomButton(
#         master=segments_frame,
#         text="Go Back",
#         height=40,
#         corner_radius=10,
#         command=lambda: load_menu(window, segments_frame),
#         bg="#444444",
#         text_color="white"
#     ).place(relx=0.08, rely=0.08, anchor=CENTER)

#     authenticated = False  # Flag to check if user is authenticated

#     # Main loop for checking clicks
#     while True:
#         window.update_idletasks()
#         window.update()

#         if utils.checkAllClicked(imgClickData):
#             sortedClickList = sorted(imgClickData)

#             if all(sortedClickList[i].id == i + 1 for i in range(4)):
#                 if not authenticated:  # Only create the popup if not already authenticated
#                     create_popup("Authenticated :)", title="Success")
#                     authenticated = True  # Set the flag to true
#             else:
#                 if not authenticated:  # Only create the popup if not already authenticated
#                     create_popup("Go Away Robot >_<", title="Failure")
#                     authenticated = True  # Set the flag to true

#             utils.setAllUnclicked(imgClickData)  # Reset the clicked state

import tkinter as tk
from tkinter import *
import custom_button
import main_menu
import utils
from PIL import ImageTk, Image
import random

def load_menu(window, frame):
    frame.pack_forget()
    main_menu.start(window)

def create_popup(window, message, title="Notification", authenticated=False):
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
    global segments_frame
    segments_frame = Frame(window, bg="black")
    segments_frame.pack(fill='both', expand=1)

    window.title("Graphical Authentication System")
    window.geometry("1280x600")
    window.configure(bg="black")

    label = Label(segments_frame, text="Please select the pictures in correct order", font=('Calibri', 20), bg="black", fg="white")
    label.pack(pady=10)

    # Draw order image
    canvas_order = Canvas(segments_frame, width=300, height=250, bg="black", highlightthickness=0)
    img_order = Image.open("segmentedImages/order.jpg")
    img_order = img_order.resize((300, 250))
    img_order = ImageTk.PhotoImage(img_order)
    canvas_order.create_image(0, 0, anchor=NW, image=img_order)
    canvas_order.pack(pady=10)

    imgList = utils.getSegmentedImages("circle")
    random.shuffle(imgList)
    imgClickData = []

    for imgPath in imgList:
        var = utils.imageClick(imgPath)
        imgClickData.append(var)

    # Draw shuffled segments
    for i in range(4):
        canvas_segment = Canvas(segments_frame, width=200, height=150, bg="black", highlightthickness=0)
        canvas_segment.bind("<Button-1>", imgClickData[i].clicked)
        canvas_segment.place(x=100 + i * 300, y=400)
        
        img_segment = Image.open(imgList[i])
        img_segment = img_segment.resize((200, 150))
        img_segment = ImageTk.PhotoImage(img_segment)
        canvas_segment.create_image(0, 0, anchor=NW, image=img_segment)
        canvas_segment.image = img_segment  # Keep a reference to avoid garbage collection

    custom_button.TkinterCustomButton(
        master=segments_frame,
        text="Go Back",
        height=40,
        corner_radius=10,
        command=lambda: load_menu(window, segments_frame),
        bg="#444444",
        text_color="white"
    ).place(relx=0.08, rely=0.08, anchor=CENTER)

    authenticated = False  # Flag to check if user is authenticated

    while True:
        window.update_idletasks()
        window.update()

        if utils.checkAllClicked(imgClickData):
            sortedClickList = sorted(imgClickData)

            if all(sortedClickList[i].id == i + 1 for i in range(4)):
                if not authenticated:
                    create_popup(window, "Authenticated :)", title="Success", authenticated=True)
                    authenticated = True
            else:
                if not authenticated:
                    create_popup(window, "Go Away Robot >_<", title="Failure", authenticated=False)
                    authenticated = True

            utils.setAllUnclicked(imgClickData)

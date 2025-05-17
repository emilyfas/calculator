import csv
import customtkinter as ctk


from calculator.constants import (STANDARD_START_NUMBER, WINDOW_WIDTH, WINDOW_HEIGHT, BUTTON_HEIGHT, BUTTON_WIDTH, \
                                  BUTTON_FONT_SIZE, COLOR_BG, COLOR_BUTTON_NUM, COLOR_BUTTON_NUM_HOVER, COLOR_BUTTON_EQUALS,
                                  COLOR_BUTTON_EQUALS_HOVER, COLOR_BUTTON_OPS_HOVER, \
                                  COLOR_BUTTON_OPS, HISTORY_FILE_PATH, COLOR_BUTTON_HISTORY, COLOR_BUTTON_HISTORY_HOVER,
                                  COLOR_BUTTON_CLEAR_HISTORY, COLOR_BUTTON_CLEAR_HISTORY_HOVER, IMG_CLEAR_FILE_PATH,
                                  IMG_DEL_FILE_PATH, IMG_CALCULATOR_FILE_PATH)
from calculator.history import clear_history_csv, display_history_line, clear_history
from calculator.logic import handle_input
from PIL import Image


def start_app():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    app = ctk.CTk()
    app.title('calculator')
    app.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
    app.configure(fg_color=COLOR_BG)
    app.resizable(0,0)
    app.iconbitmap(IMG_CALCULATOR_FILE_PATH)

    display_container = ctk.CTkFrame(app, fg_color='transparent')
    display_container.pack(pady=12, padx=10)

    def block_keybord(event):
        return "break"

    display = ctk.CTkEntry(display_container,
                           width=WINDOW_WIDTH,
                           justify='right',
                           font=("Segoe UI Variable", 22),
                           fg_color=COLOR_BG,
                           border_width=1,
                           border_color='#2b2b2b'
                           )
    display.insert(0, STANDARD_START_NUMBER)
    display.configure(insertontime=0)
    display.bind("<Key>", block_keybord)
    display.pack(ipady=25)

    buttons_container = ctk.CTkFrame(app, fg_color=COLOR_BG)
    buttons_container.pack()

    def open_popup():
        popup = ctk.CTkToplevel(app)
        popup.title("History")
        popup.geometry(f"300x400+{app.winfo_x()}+{app.winfo_y()}")
        popup.resizable(False, False)
        popup.bind("<Escape>", lambda event: popup.destroy())

        with open(HISTORY_FILE_PATH, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            rows = list(reader)

            # Checks if list its empty
            if not rows.copy():
                label_history_empty = ctk.CTkLabel(popup, text='No history yet.\nTry making some operations!')
                label_history_empty.pack(expand=True)
            else:
                container_history = create_container_history(master=popup, width=380, height=250)
                for i, row in enumerate(rows):
                    text, result = row

                    display_history_line(container_history=container_history, index=i, text=text,
                                         result=result, display=display, popup=popup)
                    popup.after(100, lambda: container_history._parent_canvas.yview_moveto(1.0))

                img_path_clear = Image.open(IMG_CLEAR_FILE_PATH)
                img_clear = ctk.CTkImage(img_path_clear, size=(17,17))
                button_clear_history = ctk.CTkButton(popup, text='', height=35, width= 100,
                                                            font=("Segoe UI Variable", BUTTON_FONT_SIZE),
                                                            fg_color= COLOR_BUTTON_CLEAR_HISTORY,
                                                            hover_color= COLOR_BUTTON_CLEAR_HISTORY_HOVER,
                                                            image = img_clear)

                button_clear_history.bind('<Button-1>', lambda event: clear_history(popup))
                button_clear_history.pack(pady=(0,10))

        popup.transient(app)
        popup.focus()
        popup.grab_set()
        popup.wait_window()


    button_history = ctk.CTkButton(buttons_container, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text="History",
                                       font=("Segoe UI Variable", BUTTON_FONT_SIZE),
                                        fg_color= COLOR_BUTTON_HISTORY,
                                        hover_color= COLOR_BUTTON_HISTORY_HOVER,
                                        command=open_popup)
    button_history.grid(row=1, column=0, ipadx=0, ipady=0, padx=2, pady=2, sticky="ew", columnspan=2)

    create_button(master=buttons_container, display=display, row=1, col=2,
                  text='C', color=COLOR_BUTTON_OPS, color_hover=COLOR_BUTTON_OPS_HOVER)

    img_path_del = Image.open(IMG_DEL_FILE_PATH)
    img_del = ctk.CTkImage(img_path_del)
    button_del = ctk.CTkButton(buttons_container, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text="",
                               font=("Segoe UI Variable", BUTTON_FONT_SIZE),
                               fg_color=COLOR_BUTTON_OPS,
                               hover_color=COLOR_BUTTON_OPS_HOVER,
                               border_width=0,
                               image=img_del
                               )
    button_del.bind('<Button-1>', lambda event: handle_input("del", display))
    button_del.grid(row=1, column=3, padx=1, pady=1)

    create_button(master=buttons_container, display=display, row=2, col=0,
                  text='7', color=COLOR_BUTTON_NUM, color_hover=COLOR_BUTTON_NUM_HOVER)

    create_button(master=buttons_container, display=display, row=2, col=1,
                  text='8', color=COLOR_BUTTON_NUM, color_hover=COLOR_BUTTON_NUM_HOVER)

    create_button(master=buttons_container, display=display, row=2, col=2,
                  text='9', color=COLOR_BUTTON_NUM, color_hover=COLOR_BUTTON_NUM_HOVER)

    create_button(master=buttons_container, display=display, row=2, col=3,
                  text='*', color=COLOR_BUTTON_OPS, color_hover=COLOR_BUTTON_OPS_HOVER)

    create_button(master=buttons_container, display=display, row=3, col=0,
                  text='4', color=COLOR_BUTTON_NUM, color_hover=COLOR_BUTTON_NUM_HOVER)

    create_button(master=buttons_container, display=display, row=3, col=1,
                  text='5', color=COLOR_BUTTON_NUM, color_hover=COLOR_BUTTON_NUM_HOVER)

    create_button(master=buttons_container, display=display, row=3, col=2,
                  text='6', color=COLOR_BUTTON_NUM, color_hover=COLOR_BUTTON_NUM_HOVER)

    create_button(master=buttons_container, display=display, row=3, col=3,
                  text='-', color=COLOR_BUTTON_OPS, color_hover=COLOR_BUTTON_OPS_HOVER)

    create_button(master=buttons_container, display=display, row=4, col=0,
                  text='1', color=COLOR_BUTTON_NUM, color_hover=COLOR_BUTTON_NUM_HOVER)

    create_button(master=buttons_container, display=display, row=4, col=1,
                  text='2', color=COLOR_BUTTON_NUM, color_hover=COLOR_BUTTON_NUM_HOVER)

    create_button(master=buttons_container, display=display, row=4, col=2,
                  text='3', color=COLOR_BUTTON_NUM, color_hover=COLOR_BUTTON_NUM_HOVER)

    create_button(master=buttons_container, display=display, row=4, col=3,
                  text='+', color=COLOR_BUTTON_OPS, color_hover=COLOR_BUTTON_OPS_HOVER)

    create_button(master=buttons_container, display=display, row=5, col=0,
                  text='%', color=COLOR_BUTTON_OPS, color_hover=COLOR_BUTTON_OPS_HOVER)

    create_button(master=buttons_container, display=display, row=5, col=1,
                  text='0', color=COLOR_BUTTON_NUM, color_hover=COLOR_BUTTON_NUM_HOVER)

    create_button(master=buttons_container, display=display, row=5, col=2,
                  text='/', color=COLOR_BUTTON_OPS, color_hover=COLOR_BUTTON_OPS_HOVER)

    create_button(master=buttons_container, display=display, row=5, col=3,
                  text='=', color=COLOR_BUTTON_EQUALS, color_hover=COLOR_BUTTON_EQUALS_HOVER)


    def on_close():
        app.destroy()

    app.protocol("WM_DELETE_WINDOW", on_close)
    app.mainloop()


def create_button(master, display, text, color, color_hover, row, col):
    button = ctk.CTkButton(master, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text=text,
                                  font=("Segoe UI Variable", BUTTON_FONT_SIZE),
                                  fg_color=color,
                                  hover_color=color_hover,
                                  border_width=0
                                  )
    button.bind('<Button-1>', lambda event: handle_input(text, display))
    button.grid(row=row, column=col, padx=1, pady=1)

def create_container_history(master, width, height) -> ctk.CTkScrollableFrame:
    frame = ctk.CTkScrollableFrame(master, width=width, height=height)
    frame.pack(padx=10, pady=10, fill="both", expand=True)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=0)
    frame.grid_columnconfigure(2, weight=1)
    frame.grid_rowconfigure((0, 1), weight=1)

    return frame

import csv
import customtkinter as ctk

from calculator.constants import HISTORY_FILE_PATH, BUTTON_FONT_SIZE, COLOR_BUTTON_HISTORY_ITEM, \
    COLOR_BUTTON_HISTORY_ITEM_HOVER, BUTTON_HISTORY_HEIGHT
from calculator.logic import restore_history


def save_operation_csv(operation, result):

    with open(HISTORY_FILE_PATH, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([operation, result])


def clear_history_csv():
    with open(HISTORY_FILE_PATH, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Operação", "Resultado"])


def clear_history(popup):
    clear_history_csv()
    popup.destroy()


def cut_text(text, max_chars=8):
    return text if len(text) <= max_chars else text[:max_chars] + "..."


def display_history_line(container_history, index, text, result, display, popup):
    button = create_button_history(container_history, text)
    button.bind('<Button-1>', lambda event, t=text: restore_history(t, display, popup))
    button.grid(row=index, column=0)

    ctk.CTkLabel(container_history, text='=', width=30, justify='center', height=BUTTON_HISTORY_HEIGHT).grid(row=index, column=1)

    result_button = create_button_history(container_history, result)
    result_button.bind('<Button-1>', lambda event, r=result: restore_history(r, display, popup))
    result_button.grid(row=index, column=2)


def create_button_history(container_history, text) -> ctk.CTkButton:
    button = ctk.CTkButton(container_history,
                           width=100,
                           height=BUTTON_HISTORY_HEIGHT,
                           anchor="w",
                           text=cut_text(text),
                           font=("Segoe UI Variable", BUTTON_FONT_SIZE),
                           fg_color=COLOR_BUTTON_HISTORY_ITEM,
                           hover_color=COLOR_BUTTON_HISTORY_ITEM_HOVER,
                           border_width=0)

    return button
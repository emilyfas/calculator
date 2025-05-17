import tkinter as tk

from sympy import simplify, sympify
from decimal import Decimal
from calculator.constants import STANDARD_START_NUMBER, OPERATORS


# Expression to be calculated will be stored here
expression = ''

def handle_input(input_txt, display):
    if input_txt.isdigit():
        delete_standard_number(display)
        update_display(input_txt, display)
        update_expression(display.get())
    elif is_an_operator(input_txt) and len(expression) >= 1:
        if is_an_operator(expression[-1]):
            return
        else:
            update_display(input_txt, display)
            update_expression(display.get())
    elif input_txt.lower() == 'c':
        clear_everything(display)
        display_standard_number(display)
    elif input_txt.lower() == 'del':
        delete_last_char(display)
        if display.get() == '':
            display_standard_number(display)
    elif input_txt == '=':
        if is_an_operator(expression[-1]):
            return

        result = process_operation(expression)
        if result == "Erro":
            clear_display(display)
            update_display("Erro", display)
            return
        finalize_operation(expression, result, display)


def clear_everything(display):
    clear_display(display)
    update_expression(display.get())
    return


def delete_last_char(display):
    new_expression = expression[:-1]
    clear_display(display)
    update_display(new_expression, display)
    update_expression(new_expression)
    return


def update_display(txt, display):
    display.insert(tk.END, txt)
    display.xview_moveto(1)


def clear_display(display):
    display.delete(0, tk.END)


def delete_standard_number(display):
    if display.get() == f'{STANDARD_START_NUMBER}':
        clear_everything(display)
        pass


def update_expression(txt):
    global expression
    expression = txt


def is_an_operator(txt):
    return txt in OPERATORS


def display_standard_number(display):
    display.insert(0, STANDARD_START_NUMBER)


def restore_history(text, display, popup):
    popup.destroy()
    clear_everything(display)
    update_display(text, display)
    update_expression(text)


def process_operation(operation_str):
    try:
        operation = sympify(operation_str)
        result = simplify(operation).evalf()

        float_result = float(result)

        if float_result.is_integer():
            num = Decimal(int(float_result))
        else:
            num = Decimal(str(float_result)).quantize(Decimal('1.0000000000')).normalize()

        return num
    except Exception as e:
        return "Error"


def finalize_operation(op, result, display):
    from calculator.history import save_operation_csv
    save_operation_csv(op, result)
    clear_everything(display)
    update_display(f'{result}', display)
    update_expression(f'{result}')

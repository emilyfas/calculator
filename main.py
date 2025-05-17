from calculator.gui import start_app
from calculator.history import clear_history_csv


def main():
    start_app()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_history_csv()

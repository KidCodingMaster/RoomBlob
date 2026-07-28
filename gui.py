import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.validation import Validation
from create_rooms import create_rooms


def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()


def home_page(*args):
    clear_screen()

    container = tb.Frame(root)
    container.grid(row=0, column=0)

    container.rowconfigure((0, 1, 2), weight=1)
    container.columnconfigure((0, 1, 2), weight=1)

    title_txt = tb.Label(container, text="RoomBlob", font=("Helvetica", 28, "bold"))
    title_txt.grid(row=0, column=1, pady=50)

    create_rooms_btn = tb.Button(
        container, text="Create Rooms", width=10, command=create_rooms_page
    )
    create_rooms_btn.grid(row=1, column=1, pady=20)


def create_rooms_sumbit(
    create_rooms_spinbox,
    create_rooms_text_success,
    create_rooms_text_failed,
):
    try:
        rooms = int(create_rooms_spinbox.get())
    except:
        rooms = None

    if rooms and rooms is not None:
        create_rooms(int(rooms))

        create_rooms_text_failed.grid_remove()

        create_rooms_text_success.grid(row=3, column=1)
    else:

        create_rooms_text_success.grid_remove()

        create_rooms_text_failed.grid(row=3, column=1)


def create_rooms_page():
    clear_screen()

    container = tb.Frame(root)
    container.grid(row=0, column=0)

    container.rowconfigure((0, 1, 2), weight=1)
    container.columnconfigure((0, 1, 2), weight=1)

    title_txt = tb.Label(container, text="RoomBlob", font=("Helvetica", 28, "bold"))
    title_txt.grid(row=0, column=1, pady=50)
    title_txt.bind("<Button-1>", home_page)

    create_rooms_spinbox = tb.Spinbox(container, from_=0, to=float("inf"))
    create_rooms_spinbox.grid(row=1, column=1)
    Validation.numeric(create_rooms_spinbox)

    create_rooms_text_success = tb.Label(
        container, text="Rooms Created Successfully", bootstyle="success"
    )
    create_rooms_text_failed = tb.Label(
        container, text="Rooms Created Failed", bootstyle="danger"
    )

    create_rooms_sumbit_btn = tb.Button(
        container,
        text="Create Rooms",
        command=lambda: create_rooms_sumbit(
            create_rooms_spinbox,
            create_rooms_text_success,
            create_rooms_text_failed,
        ),
    )
    create_rooms_sumbit_btn.grid(row=2, column=1, pady=10)


root = tb.Window(themename="superhero")
root.geometry("400x300")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

home_page()

root.mainloop()

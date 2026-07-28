import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.validation import Validation
from create_rooms import create_rooms
from give_review import give_review


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

    give_review_btn = tb.Button(
        container, text="Give Review", width=10, command=give_review_page
    )
    give_review_btn.grid(row=2, column=1, pady=20)


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


def give_review_page_submit(
    give_review_page_room,
    give_review_page_review,
    give_review_page_success_text,
    give_review_page_failed_text,
):

    try:
        room = int(give_review_page_room.get())
    except:
        room = None

    review = give_review_page_review.get()

    give_review_page_room.delete(0, "end")
    give_review_page_review.delete(0, "end")

    if room and room is not None:
        give_review(str(room), review)

        give_review_page_failed_text.grid_remove()

        give_review_page_success_text.grid(row=4, column=1)
    else:

        give_review_page_success_text.grid_remove()

        give_review_page_failed_text.grid(row=4, column=1)


def give_review_page():
    clear_screen()

    container = tb.Frame(root)
    container.grid(row=0, column=0)

    container.rowconfigure((0, 1, 2), weight=1)
    container.columnconfigure((0, 1, 2), weight=1)

    title_txt = tb.Label(container, text="RoomBlob", font=("Helvetica", 28, "bold"))
    title_txt.grid(row=0, column=1, pady=50)
    title_txt.bind("<Button-1>", home_page)

    give_review_rooms_text = tb.Label(container, text="Room: ")
    give_review_rooms_text.grid(row=1, column=0)

    give_review_rooms_entry = tb.Entry(container)
    give_review_rooms_entry.grid(row=1, column=1)

    give_review_review_text = tb.Label(container, text="Review: ")
    give_review_review_text.grid(row=2, column=0)

    give_review_review_entry = tb.Entry(container)
    give_review_review_entry.grid(row=2, column=1, pady=5)

    give_review_page_success_text = tb.Label(
        container, text="Review Created Successfully", bootstyle="success"
    )
    give_review_page_failed_text = tb.Label(
        container, text="Review Created Failed", bootstyle="danger"
    )

    give_review_entry_btn = tb.Button(
        container,
        text="Submit",
        command=lambda: give_review_page_submit(
            give_review_rooms_entry,
            give_review_review_entry,
            give_review_page_success_text,
            give_review_page_failed_text,
        ),
    )
    give_review_entry_btn.grid(row=3, column=1)


root = tb.Window(themename="superhero")
root.geometry("400x300")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

home_page()

root.mainloop()

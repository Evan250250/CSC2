from tkinter import * 
from tkinter import ttk

main_window = Tk()

label_full_name = Label(main_window, font='bold',text="Full Name").grid(column=0,row=1)
entry_full_name = Entry(main_window)
entry_full_name.grid(column=1,row=1)

label_receipt_number = Label(main_window, font='bold',text="Receipt Number").grid(column=0,row=2)
entry_receipt_number = Entry(main_window)
entry_receipt_number.grid(column=1,row=2)

label_items_that_hired = Label(main_window, font='bold',text="Items that hired").grid(column=0,row=3)
entry_items_hired = Entry(main_window)
entry_items_hired.grid(column=1,row=3)

label_number_of_items = Label(main_window, font='bold',text="Number of items").grid(column=0,row=4)
entry_number_of_items = Entry(main_window)
entry_number_of_items.grid(column=1,row=4)


def check_inputs():
    # these are the global variables that are used
    global shop_details, entry_full_name, entry_receipt_number, entry_items_hired, entry_number_of_items, total_entries
    input_check = 0
    if len(entry_full_name.get()) == 0:
        Label(main_window, fg="red", font='bold', text="Required") .grid(column=2, row=0)
        input_check = 1

    if (entry_receipt_number.get().isdigit()):
        Label(main_window, fg="red", font='bold', text="Required") .grid(column=2, row=1)
        input_check = 1

    if len(entry_items_hired.get()) == 0:
        Label(main_window, fg="red", font='bold', text="Required") .grid(column=2, row=2)
        input_check = 1

    if (entry_number_of_items.get().isdigit()):
        if int(entry_number_of_items.get()) < 1 or int(entry_campers.get()) > 500:
            Label(main_window, fg="red", font='bold', text="1-500 only") .grid(column=2, row=3)
            input_check = 1
    else:
        Label(main_window, fg="red", font='bold', text="5-10 only") .grid(column=2, row=4)
        input_check = 1
    if input_check == 0:
        append_name()

def delete_row ():
    global camp_details, delete_item, total_entries, name_count
    try:
        del camp_details[int(delete_item.get())]
        total_entries -= 1
        delete_item.delete(0,'end')
        for widget in frame.winfo_children():
            widget.destroy()
        frame.pack_forget()
        print_camp_details()
    except IndexError:
        messagebox.showerror('error', 'That row does not exist')
    except ValueError:
        messagebox.showerror('error', 'Is that even a number?')


def main():
    global shop, entry_full_name, entry_receipt_number, entry_items_hired, entry_number_of_items, total_entries
    shop = []
    total_entries = 0
    main_window.mainloop()

main()
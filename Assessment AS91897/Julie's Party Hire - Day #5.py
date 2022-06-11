from tkinter import * 
from tkinter import ttk

main_window = Tk()


def quit():
    main_window.destroy()

def entry_labels():
     label_full_name = Label(frame, font='bold',text="Full Name")
     label_full_name.grid(column=0, row=0)
     label_receipt_number = Label(frame, font='bold',text="Receipt Number")
     label_receipt_number.grid(column=0, row=1)
     label_items_that_hired = Label(frame, font='bold',text="Items that hired")
     label_items_that_hired.grid(column=0, row=2)
     label_number_of_items = Label(frame, font='bold',text="Number of items")
     label_number_of_items.grid(column=0, row=3)

def entry_button():
    print_button = Button(frame, text = "Enter", command = append_entry)
    print_button.grid(column=3, row=1)

    delete_row_button = Button(frame, text = 'Delete Row', command = delete_row)
    delete_row_button.grid(column=4, row=3)

    quit_button = Button(frame, text= "Quit", command=quit)
    quit_button.grid(column=4, row=0)



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
        check_inputs()

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

def setup_buttons():
    global camp_details, entry_leader,entry_location,entry_campers,entry_weather, total_entries, delete_item
    Button(main_window, text="Update",command=check_inputs) .grid(column=1,row=1)
    Label(main_window,text="Full Name").grid(column=0,row=1)
    entry_full_name = Entry(main_window)
    entry_full_name.grid(column=1,row=1)
    Label(main_window, font='bold',text="Receipt Number").grid(column=0,row=2)
    entry_receipt_number = Entry(main_window)
    entry_receipt_number.grid(column=1,row=2)
    label(main_window, font='bold',text="Items hired").grid(column=0,row=3)
    entry_items_hired = Entry(main_window)
    entry_items_hired.grid(column=1,row=3)
    Label(main_window, font='bold',text="Number of items").grid(column=0,row=4)
    entry_number_of_items = Entry(main_window)
    entry_number_of_items.grid(column=1,row=4)


def main():
    global main_frame
    main_frame = Frame(main_window)
    main_frame.grid(row=0,column=0)

    main_window = Tk()
    setup_buttons()
    main_window.mainloop()
main()
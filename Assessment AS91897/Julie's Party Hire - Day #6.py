from tkinter import * 
from tkinter import ttk

main_window = Tk()

def entry_labels():
     Label(main_window, font='bold',text="Full Name").grid(column=0,row=1)
     entry_full_name = Entry(main_window)
     entry_full_name.grid(column=1,row=1)

     Label(main_window, font='bold',text="Receipt Number").grid(column=0,row=2)
     entry_receipt_number = Entry(main_window)
     entry_receipt_number.grid(column=1,row=2)

     Label(main_window, font='bold',text="Items that hired").grid(column=0,row=3)
     entry_items_that_hired = Entry(main_window)
     entry_items_that_hired.grid(column=1,row=3)

     Label(main_window, font='bold',text="Number of items").grid(column=0,row=4)
     entry_number_of_items = Entry(main_window)
     entry_number_of_items.grid(column=1,row=4)

def entry_button():
     Button(main_window, text="Quit",command=quit) .grid(column=0, row=5)
     Button(main_window, text="Update",command=check_inputs) .grid(column=1,row=6) 

#For button "quit"
def quit():
    main_window.destroy()

#For button #update
def check_inputs():
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

def main():
    global main_window
    entry_labels()
    entry_button()

main()
main_window.mainloop()
from logging import root
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk

main_window = Tk()

def table_headers():
    row_header = Label(main_window, text='Row', font = '10')
    row_header.grid(column=0, row=6)
    
    customer_header = Label(main_window, text='Customer name', font = '10')
    customer_header.grid(column=1, row=6)

    receipt_header = Label(main_window, text='Receipt number', font = '10')
    receipt_header.grid(column=2, row=6)

    item_header = Label(main_window, text='Item hired', font = '10')
    item_header.grid(column=3, row=6)

    num_header = Label(main_window, text='Number of items', font = '10')
    num_header.grid(column=4, row=6)

#For button "quit"
def quit():
    main_window.destroy()

#For button #update
def append_details():
    global customer_details, entry_customer_name, entry_receipt_number, entry_number_of_items, entry_items_hired, total_entries
    if len([entry_customer_name.get()]) != 0:
        customer_details.append([entry_customer_name.get(), entry_receipt_number.get(), entry_items_hired.get(), entry_number_of_items.get()])
        entry_customer_name.delete(0,'end')
        entry_receipt_number.delete(0,'end')
        entry_items_hired.delete(0,'end')
        entry_number_of_items.delete(0,'end')
        total_entries == 4
        print_camp_details()

def print_camp_details (): 
    global j_names, total_entries, name_count
    name_count = 0 
    Label(main_window, font='bold',text="Customer name").grid(column=0,row=1)
    Label(main_window, font='bold',text="Receipt number").grid(column=0,row=2)
    Label(main_window, font='bold',text="Number of items").grid(column=0,row=3) 
    Label(main_window, font='bold',text="Items hired").grid(column=0,row=4)

    while name_count < total_entries :
       a = Label(main_window, text=name_count).grid(column=0,row=name_count+8) 
       b = Label(main_window, text=(customer_details[name_count][0])).grid(column=7,row=name_count+8)
       c = Label(main_window, text=(customer_details[name_count][1])).grid(column=7,row=name_count+8)
       d = Label(main_window, text=(customer_details[name_count][2])).grid(column=7,row=name_count+8)
       e = Label(main_window, text=(customer_details[name_count][3])).grid(column=7,row=name_count+8)
       name_count +=  1

def main():
    global main_window
    global customer_details, total_entries
    customer_details = []
    total_entries = 0
    entry_labels()
    entry_button()
    table_headers()

main()
main_window.mainloop()
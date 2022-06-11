from tkinter import * 
from tkinter import messagebox
from tkinter import ttk

main_window = Tk()

def entry_labels():
     global shop_details, entry_customer_name, entry_receipt_number, entry_number_of_items, entry_items_hired, total_entries
     Label(main_window, font='bold',text="Customer name").grid(column=0,row=1)
     entry_customer_name = Entry(main_window)
     entry_customer_name.grid(column=1,row=1)

     Label(main_window, font='bold',text="Receipt number").grid(column=0,row=2)
     entry_receipt_number = Entry(main_window)
     entry_receipt_number.grid(column=1,row=2)

     Label(main_window, font='bold',text="Number of items").grid(column=0,row=3)
     entry_number_of_items = Entry(main_window)
     entry_number_of_items.grid(column=1,row=3)

     Label(main_window, font='bold',text="Items hired").grid(column=0,row=4)
     entry_items_hired = Entry(main_window)
     items_hired = StringVar()
     entry_items_hired = ttk.Combobox(main_window, textvariable=items_hired, values=('Books Candy Canned Food Car Parts Chips Clothing Electronics Food Fruit Hats Instruments Jewelry Pets Shoes Furniture Smartphones Soda Tablet Toys Video Games'), state='readonly')
     entry_items_hired.grid(column=1,row=4)

def entry_button():
     Button(main_window, font='bold', text="Quit",command=quit) .grid(column=3,row=1)
     Button(main_window, font='bold', text="Append details", command=append_details) .grid(column=3,row=2)
     Button(main_window, font='bold', text="Delete row").grid(column=3,row=3) 

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
    if len(customer_details.get()) == 0:
        shop_details.append([entry_customer_name.get(), entry_receipt_number.get(), entry_items_hired.get(), entry_number_of_items.get()])
        entry_customer_name.delete(0,'end')
        entry_receipt_number.delete(0,'end')
        entry_items_hired.set(0,'end')
        entry_number_of_items.delete(0,'end')
        total_entries == 1


def main():
    global main_window
    global shop_details, customer_details, total_entries
    customer_details = []
    total_entries = 0
    entry_labels()
    entry_button()
    table_headers()

main()
main_window.mainloop()
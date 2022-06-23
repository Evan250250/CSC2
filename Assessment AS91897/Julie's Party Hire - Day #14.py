from tkinter import * 
from tkinter import messagebox
from tkinter import ttk

def print_shop_details(): 
    global j_names, total_entries, name_count, frame
    name_count = 0 
    Label(frame, font='bold',text="Row").grid(column=0,row=6)
    Label(frame, font='bold',text="Customer name").grid(column=1,row=6)
    Label(frame, font='bold',text="Receipt number").grid(column=2,row=6)
    Label(frame, font='bold',text="Items quantity").grid(column=3,row=6) 
    Label(frame, font='bold',text="Items hired").grid(column=4,row=6)
    frame.grid(column =0, row =6)

    while name_count < total_entries :
       Label(frame, text=name_count).grid(column=0,row=name_count+8) 
       Label(frame, text=(shop_details[name_count][0])).grid(column=1,row=name_count+8)
       Label(frame, text=(shop_details[name_count][1])).grid(column=2,row=name_count+8)
       Label(frame, text=(shop_details[name_count][2])).grid(column=3,row=name_count+8)
       Label(frame, text=(shop_details[name_count][3])).grid(column=4,row=name_count+8)
       name_count +=  1

def entry_labels():
#labels   
    global shop_details, entry_customer_name, entry_receipt_number, entry_items_quantity, entry_items_hired, total_entries, delete_item
    Label(main_window, font='bold',text="Customer name").grid(column=0,row=1) 
    entry_customer_name = Entry(main_window)
    entry_customer_name.insert(0, "Customer name")
    entry_customer_name.grid(column=1,row=1)

    Label(main_window, font='bold',text="Receipt number").grid(column=0,row=2)
    entry_receipt_number = Entry(main_window)
    entry_receipt_number.insert(0, "Receipt number")
    entry_receipt_number.grid(column=1,row=2)


    Label(main_window, font='bold',text="Items quantity").grid(column=0,row=3) 
    entry_items_quantity = Entry(main_window)
    entry_items_quantity.insert(0, "Items quantity")
    entry_items_quantity.grid(column=1,row=3)

 
    Label(main_window, font='bold',text="Items hired").grid(column=0,row=4)
    entry_items_hired = Entry(main_window)
    items_hired = StringVar()
    entry_items_hired = ttk.Combobox(main_window, textvariable=items_hired, values=('Anti-bacterial spray', 'Books', 'Candy', 'Canned Food', 'Food', 'Car Parts', 'Chips', 'Clothing', 'Electronics', 'Food', 'Fruit', 'Hats', 'Instruments', 'Jewelry', 'Pets', 'Shoes', 'Furniture', 'Smartphones', 'Soda', 'Tablet', 'Toys', 'Video Games'), state='readonly')
    entry_items_hired.grid(column=1,row=4)

#button
    Button(main_window, font='bold', text="Quit",command=quit).grid(column=3,row=1)
    Button(main_window, font='bold', text="Append details", command=append_details).grid(column=3,row=2)
    Button(main_window, font='bold', text="Delete row", command=delete_row).grid(column=3,row=3) 
    delete_item = Entry(main_window)

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
    global shop_details, entry_customer_name, entry_receipt_number, entry_items_quantity, entry_items_hired, total_entries
    shop_details.append([entry_customer_name.get(), entry_receipt_number.get(), entry_items_quantity.get(), entry_items_hired.get()])
    entry_customer_name.delete(0,'end')
    entry_receipt_number.delete(0,'end')
    entry_items_hired.delete(0,'end')
    entry_items_quantity.delete(0,'end')
    total_entries += 1
    print_shop_details()

def delete_row():
    global shop_details, delete_item, total_entries, name_count
    del shop_details[int(delete_item.get())]
    total_entries - 1
    delete_item.delete(0, 'end')
    # clear the last item displayed on the GUI
    Label(main_window, text="                                       ").grid(column=0,row=name_count+7) 
    Label(main_window, text="                                       ").grid(column=1,row=name_count+7)
    Label(main_window, text="                                       ").grid(column=2,row=name_count+7)
    Label(main_window, text="                                       ").grid(column=3,row=name_count+7)
    Label(main_window, text="                                       ").grid(column=4,row=name_count+7)
    frame.pack_forget()
    print_shop_details()

def main():
    global main_window
    global shop_details, total_entries, frame
    shop_details = []
    total_entries = 0
    main_window = Tk()
    entry_labels()
    frame = Frame(main_window)
    frame.grid(row=0,column=0)
    main_window.mainloop()

main()
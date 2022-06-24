from tkinter import *
from tkinter import ttk

global main_window

def quit():
    main_window.destroy()

def entry_labels():
    customer_name = Label(frame,text="Customer name")
    customer_name.grid(column=0,row=0)

    receipt_number = Label(frame,text="Receipt number")
    receipt_number.grid(column=0,row=1)

    items_quantiny = Label(frame,text="Items quantity")
    items_quantiny.grid(column=0,row=2) 

    items_hired = Label(frame,text="Items hired")
    items_hired.grid(column=0,row=3)


def entry():
    def entry_customer_name_focus(e):
        entry_customer_name.delete(0,"end")
    global entry_customer_name
    entry_customer_name = Entry(frame)
    entry_customer_name.insert(0, "Full name*")
    entry_customer_name.bind("<FocusIn>", entry_customer_name_focus)
    entry_customer_name.grid(column=1, row=0, pady=5)

    def entry_receipt_number_focus(e):
        entry_receipt_number.delete(0,"end")
    global entry_receipt_number
    entry_receipt_number = Entry(frame)
    entry_receipt_number.insert(0, "Number only*")
    entry_receipt_number.bind("<FocusIn>", entry_receipt_number_focus)
    entry_receipt_number.grid(column=1, row=1, pady=5)

    def entry_items_quantity_focus(e):
        entry_items_quantity.delete(0,"end")
    global entry_items_quantity
    entry_items_quantity = Entry(frame)
    entry_items_quantity.insert(0, "Between 1 and 500*")
    entry_items_quantity.bind("<FocusIn>", entry_items_quantity_focus)
    entry_items_quantity.grid(column=1, row=2, pady=5)
    
    global entry_items_hired
    entry_items_hired = Entry(frame)
    items_hired = StringVar()
    entry_items_hired = ttk.Combobox(frame, textvariable=items_hired, values=('Books', 'Candy', 
    'Canned Food', 'Food', 'Car Parts', 'Chips', 'Clothing', 'Electronics', 'Food', 
    'Fruit', 'Hats', 'Instruments', 'Jewelry', 'Pets', 'Shoes', 'Furniture', 
    'Smartphones', 'Soda', 'Tablet', 'Toys', 'Video Games'), state='readonly')
    entry_items_hired.grid(column=1, row=3, pady=5)

    def delete_row_entry_focus(e):
        delete_row_entry.delete(0,"end")
    global delete_row_entry
    delete_row_entry = Entry(frame)
    delete_row_entry.insert(0, "Row #")
    delete_row_entry.bind("<FocusIn>", delete_row_entry_focus)
    delete_row_entry.grid(column=3, row=3, pady=5)


def button():
    quit_button = Button(frame, text= "Quit", width = 12, command=quit)
    quit_button.grid(column=3, row=0)

    print_button = Button(frame, text = "Append Details", width = 12, command = append_details)
    print_button.grid(column=3, row=1)

    delete_row_button = Button(frame, text = 'Delete Row', width = 12,  command = delete_row)
    delete_row_button.grid(column=3, row=2)

def table_header():
    row_header = Label(frame, text = 'Row', font = 'Arial 10 bold')
    row_header.grid(column=0, row=6)

    customer_header = Label(frame, text= 'Customer name', font = 'Arial 10 bold')
    customer_header.grid(column=1, row=6)

    receipt_header = Label(frame, text= 'Receipt number', font = 'Arial 10 bold')
    receipt_header.grid(column=2, row=6)

    num_header = Label(frame, text= 'Items quantity', font = 'Arial 10 bold')
    num_header.grid(column=3, row=6)

    item_header = Label(frame, text= 'Item hired', font = 'Arial 10 bold')
    item_header.grid(column=4, row=6)

def append_details():

    global second_frame
    second_frame = Frame(main_window)
    second_frame.grid(column=0, row=6)

    customer_name_error_var.set("")
    receipt_number_error_var.set("")
    items_quantity_error_var.set("")
    items_hired_error_var.set("")


    global name_count
    name_count = 0
    global ROWS_ABOVE
    ROWS_ABOVE = 6


    try:
        entry_customer_name_str = str(entry_customer_name.get())
        entry_receipt_number_str = str(entry_receipt_number.get())
        entry_items_quantity_int = str(entry_items_quantity.get())
        entry_items_hired_int = str(entry_items_hired.get())

        if len(entry_customer_name.get()) != 0:
            input_data_col1.append([entry_customer_name_str])
            input_data_col2.append([entry_receipt_number_str])
            input_data_col3.append([entry_items_quantity_int])
            input_data_col4.append([entry_items_hired_int])
            counters['total_entries'] += 1
      
        print(input_data_col1)
        print(input_data_col2)
        print(input_data_col3)
        print(input_data_col4)

        while name_count < counters ['total_entries']:
            global name

            row = Label(second_frame, text=name_count)
            row.grid(column=0, row=name_count + ROWS_ABOVE, padx=30)

            name = Label(second_frame, text=(input_data_col1[name_count][-1])) 
            name.grid(column=1, row=name_count + ROWS_ABOVE, padx=30)
            
            item = Label(second_frame, text=(input_data_col2[name_count][-1]))
            item.grid(column=2, row=name_count + ROWS_ABOVE, padx=30)
            
            receipt = Label(second_frame, text=(input_data_col3[name_count][-1]))
            receipt.grid(column=3, row=name_count + ROWS_ABOVE, padx=30)
            
            num = Label(second_frame, text=(input_data_col4[name_count][-1]))
            num.grid(column=4, row= name_count + ROWS_ABOVE, padx=30)
            
            name_count += 1

        entry_customer_name.delete(0,END)
        entry_receipt_number.delete(0,END)
        entry_items_quantity.delete(0,END)
        entry_items_hired.delete(0,END)

    except:

        entry_customer_name.delete(0,END)
        entry_receipt_number.delete(0,END)
        entry_items_quantity.delete(0,END)
        entry_items_hired.delete(0,END)

def delete_row():

    user_del =int(delete_row_entry.get())
     
    counters['total_entries'] -= 1
    input_data_col1.pop(user_del)
    input_data_col2.pop(user_del)
    input_data_col3.pop(user_del)
    input_data_col4.pop(user_del)
    

    for widget in second_frame.winfo_children():
        widget.destroy()

    append_details()

    
    print(input_data_col1)
    print(input_data_col2)
    print(input_data_col3)
    print(input_data_col4)


def main():
    global main_window
    main_window = Tk()

    global input_data_col1
    input_data_col1 = []
    
    global input_data_col2
    input_data_col2 = []
    
    global input_data_col3
    input_data_col3 = []
    
    global input_data_col4
    input_data_col4 = []

    global shop_details
    shop_details = []

    global input_data
    input_data = []
    
    global frame
    frame = Frame(main_window)
    frame.grid(row=0,column=0)

    global counters
    counters = {'total_entries':0, 'name_count':0}
    global number
    number = {'total_entries':0}

    def stringvars():
        global customer_name_error_var
        customer_name_error_var = StringVar()
        customer_name_error_var.set("")

        global receipt_number_error_var
        receipt_number_error_var = StringVar()
        receipt_number_error_var.set("")

        global items_quantity_error_var
        items_quantity_error_var = StringVar()
        items_quantity_error_var.set("")

        global items_hired_error_var
        items_hired_error_var = StringVar()
        items_hired_error_var.set("")

    stringvars()
    
    entry_labels()
    entry()
    button()
    table_header()


main()
main_window.mainloop()

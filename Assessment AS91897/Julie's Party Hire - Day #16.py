from tkinter import * 
from tkinter import ttk

main_window = Tk()

def entry_labels():

    Label(main_window, font='bold',text="Customer name").grid(column=0,row=1)
    Label(main_window, font='bold',text="Receipt number").grid(column=0,row=2)
    Label(main_window, font='bold',text="Items quantity").grid(column=0,row=3) 
    Label(main_window, font='bold',text="Items hired").grid(column=0,row=4)

def entries():
    global entry_customer_name, entry_receipt_number, entry_items_quantity, entry_items_hired, delete_row_entry

    def entry_customer_name_focus(e):
        entry_customer_name.delete(0,"end")

    entry_customer_name = Entry(main_window)

    entry_customer_name.insert(0, "Customer name")
    entry_customer_name.grid(column=1,row=1)
    entry_customer_name.bind("<FocusIn>", entry_customer_name_focus)

    def entry_receipt_number_focus(e):
        entry_receipt_number.delete(0,"end")

    entry_receipt_number = Entry(main_window)
    entry_receipt_number.insert(0, "Receipt number")
    entry_receipt_number.grid(column=1,row=2)
    entry_receipt_number.bind("<FocusIn>", entry_receipt_number_focus)

    def entry_items_quantity_focus(e):
        entry_items_quantity.delete(0,"end")

    entry_items_quantity = Entry(main_window)
    entry_items_quantity.insert(0, "Items quantity")
    entry_items_quantity.grid(column=1,row=3)
    entry_items_quantity.bind("<FocusIn>", entry_items_quantity_focus)

    entry_items_hired = Entry(main_window)

    items_hired = StringVar()
    entry_items_hired = ttk.Combobox(main_window, textvariable=items_hired, values=('Anti-bacterial spray', 'Books', 'Candy', 'Canned Food', 'Food', 'Car Parts', 'Chips', 'Clothing', 'Electronics', 'Food', 'Fruit', 'Hats', 'Instruments', 'Jewelry', 'Pets', 'Shoes', 'Furniture', 'Smartphones', 'Soda', 'Tablet', 'Toys', 'Video Games'), state='readonly')
    entry_items_hired.grid(column=1,row=4)

    delete_row_entry = Entry(main_window)
    delete_row_entry.grid(column=4, row=2)

def button():
    quit_button = Button(main_window, font='bold', text= "Quit", command=quit)
    quit_button.grid(column=4, row=0)

    print_button = Button(main_window, font='bold', text = "Append Details", command = append_details)
    print_button.grid(column=3, row=1)

    delete_row_button = Button(main_window, font='bold', text = 'Delete Row', command = delete_row)
    delete_row_button.grid(column=4, row=3)

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

def quit():
    main_window.destroy()

def append_details():
    
    global second_frame
    second_frame = Frame(main_window)
    second_frame.grid(row=0,column=0)

    customer_name_error_var.set("")
    receipt_number_error_var.set("")
    items_quantity_error_var.set("")
    items_hired_error_var.set("")

    global name_count
    name_count = 0

    try:
        entry_customer_name_str = str(entry_customer_name.get())
        entry_receipt_number_str = str(entry_receipt_number.get())
        entry_items_quantity_int = str(entry_items_quantity.get())
        entry_items_hired_int = str(entry_items_hired.get())



        if len(name_entry.get()) != 0:
            input_data_col1.append([entry_customer_name_str])
            input_data_col2.append([entry_receipt_number_str])
            input_data_col3.append([entry_items_quantity_int])
            input_data_col4.append([entry_items_hired_int])
            total_entries += 1
      

        
        print(input_data_col1)
        print(input_data_col2)
        print(input_data_col3)
        print(input_data_col4)
        
       
        while name_count < total_entries :
            global name

            Label(second_frame, font='bold',text="Row").grid(column=0,row=6)
            Label(second_frame, font='bold',text="Customer name").grid(column=1,row=6)
            Label(second_frame, font='bold',text="Receipt number").grid(column=2,row=6)
            Label(second_frame, font='bold',text="Items quantity").grid(column=3,row=6) 
            Label(second_frame, font='bold',text="Items hired").grid(column=4,row=6)

            Label(second_frame, text=name_count).grid(column=0,row=name_count+8) 
            Label(second_frame, text=(shop_details[name_count][0])).grid(column=1,row=name_count+8)
            Label(second_frame, text=(shop_details[name_count][1])).grid(column=2,row=name_count+8)
            Label(second_frame, text=(shop_details[name_count][2])).grid(column=3,row=name_count+8)
            Label(second_frame, text=(shop_details[name_count][3])).grid(column=4,row=name_count+8)
            name_count +=  1

        entry_customer_name.delete(0,END)
        entry_receipt_number.delete(0,END)
        entry_items_quantity.delete(0,END)
        entry_items_hired.delete(0,END)

    except:
        entry_customer_name.set("Check inputs")
        entry_items_hired.set("")

        entry_customer_name.delete(0,END)
        entry_receipt_number.delete(0,END)
        entry_items_quantity.delete(0,END)
        entry_items_hired.delete(0,END)

def delete_row():

    user_del =int(delete_row_entry.get())
     
    total_entries -= 1
    input_data_col1.pop(user_del)
    input_data_col2.pop(user_del)
    input_data_col3.pop(user_del)
    input_data_col4.pop(user_del)


    data = [input_data_col1,input_data_col2,input_data_col3,input_data_col4]

    

    for widget in second_frame.winfo_children():
        widget.destroy()

    append_details()

    
    print(input_data_col1)
    print(input_data_col2)
    print(input_data_col3)
    print(input_data_col4)


def error_prevention():

    customer_name_error = Label(main_window, textvariable = customer_name_error_var, fg = 'red')
    customer_name_error.grid(column=2, row=0)

    receipt_number_error = Label(main_window, textvariable = receipt_number_error_var, fg = 'red')
    receipt_number_error.grid(column=2, row=1)

    items_quantity_error = Label(main_window, textvariable = items_quantity_error_var, fg = 'red', width = 13)
    items_quantity_error.grid(column=2, row=2)
    
    items_hired_error = Label(main_window, textvariable = items_hired_error_var, fg = 'red')
    items_hired_error.grid(column=2, row=3)

def main():

    global input_data_col1
    input_data_col1 = []

    global input_data_col2
    input_data_col2 = []
    
    global input_data_col3
    input_data_col3 = []
    
    global input_data_col4
    input_data_col4 = []

    global input_data

    input_data = []

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
    entries()
    button()
    table_headers()
    error_prevention()

main()
main_window.mainloop()
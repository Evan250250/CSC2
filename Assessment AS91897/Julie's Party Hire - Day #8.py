from functools import total_ordering
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

     Label(main_window, font='bold',text="Items hired").grid(column=0,row=3)
     entry_items_hired = Entry(main_window)
     entry_items_hired.grid(column=1,row=3)
     entry_items_hired = StringVar()
     entry_items_hired = ttk.Combobox(main_window, textvariable=items_hired, values=('Sunny', 'Cloudy', 'Rain', 'Snow'), state='readonly')
     entry_items_hired.grid(column=1,row=5)

     Label(main_window, font='bold',text="Number of items").grid(column=0,row=4)
     entry_number_of_items = Entry(main_window)
     entry_number_of_items.grid(column=1,row=4)

def entry_button():
     Button(main_window, font='bold', text="Quit",command=quit) .grid(row=13,column=5)
     Button(main_window, font='bold', text="Enter") .grid(column=3,row=2)
     Button(main_window, font='bold', text="Delete row").grid(column=3,row=3) 
 

def table_headers():
    row_header = Label(main_window, text='Row', font = '10')
    row_header.grid(column=0, row=6)
    
    customer_header = Label(main_window, text='Customer Name', font = '10')
    customer_header.grid(column=1, row=6)

    receipt_header = Label(main_window, text='Receipt Number', font = '10')
    receipt_header.grid(column=3, row=6)

    item_header = Label(main_window, text='Item Hired', font = '10')
    item_header.grid(column=2, row=6)

    num_header = Label(main_window, text='Number Hired', font = '10')
    num_header.grid(column=4, row=6)

#For button "quit"
def quit():
    main_window.destroy()

#For button #update
def append_details():
    global shop_details, entry_full_name, entry_receipt_number, entry_items_hired, entry_number_of_item, total_entries
    if len(shop_details.get()) != 0:
        shop_details.append([entry_full_name.get(), entry_receipt_number.get(), entry_items_hired.get(), entry_number_of_item.get(), total_entries.get()])
        entry_full_name.delete(0,'end')
        entry_receipt_number.delete(0,'end')
        entry_items_hired,(0,'end')
        entry_number_of_item,(0,'end')
        total_entries += 1
   
#delete a row from the list

def delete_row ():
    global camp_details, delete_item, total_entries, name_count
    try:
        del camp_details[int(delete_item.get())]
        total_entries -= 1
        delete_item.delete(0,'end')
        for widget in frame.winfo_children():
            widget.destroy()
        frame.pack_forget()
    except IndexError:
        messagebox.showerror('error', 'That row does not exist')
    except ValueError:
        messagebox.showerror('error', 'Is that even a number?')

append_details()

def main():
    global main_window
    entry_labels()
    entry_button()
    table_headers()

main()
main_window.mainloop()
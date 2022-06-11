from tkinter import * 
from tkinter import ttk

root = Tk()
global shop, entry_full_name, entry_receipt_number, entry_items_that_hired, entry_number_of_items, total_entries

def append_details():
     if len(entry_full_name.get()) != 0:
        shop.append([entry_full_name.get(), entry_receipt_number.get(), entry_items_that_hired.get(), entry_number_of_items.get(), total_entries.get()])
     camp_details.append([entry_leader.get(),entry_location.get(),entry_campers.get(),entry_weather.get()])
        ntry_leader.delete(0,'end')
         entry_location.delete(0,'end')
                            entry_campers.delete(0,'end')
                            entry_weather.delete(0,'end')
        total_entries +=  1
    print_camp_details()
                            
                        else:
                            messagebox.showerror('error', 'What is your weather?')
                    else:
                        messagebox.showerror('error', 'Number of campers must be between 10 to 15')
        else:
            messagebox.showerror('error', 'Needs to be a whole number')
    else:
        messagebox.showerror('error', 'What is your leader name?')
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
        print_camp_details()
    except IndexError:
        messagebox.showerror('error', 'That row does not exist')
    except ValueError:
        messagebox.showerror('error', 'Is that even a number?')

label_full_name = Label(root, font='bold',text="Full Name").grid(column=0,row=1)
entry_full_name = Entry(main_window)
entry_full_name.grid(column=1,row=2)


label_receipt_number = Label(root, font='bold',text="Receipt Number").grid(column=0,row=2)
entry_receipt_number = Entry(main_window)
entry_receipt_number.grid(column=1,row=3)

label_items_that_hired = Label(root, font='bold',text="Items that hired").grid(column=0,row=3)
entry_items_that_hired = Entry(main_window)
entry_items_that_hired.grid(column=1,row=4)

label_number_of_items = Label(root, font='bold',text="Number of items").grid(column=0,row=4)
entry_number_of_items = Entry(main_window)
entry_number_of_items.grid(column=1,row=5)

button_quit = Button(root, text = 'Quit') 
button_quit.configure(command=root.destroy)

labels = [label_full_name, receipt_number, items_that_hired, number_of_items]
entries = [label_full_name, receipt_number, items_that_hired, number_of_items]
buttons = [button_quit]

def main():
    global root
    global camp_details, entry_name,entry_age,entry_gender, total_entries, frame
    camp_details = []
    total_entries = 0
    root = Tk()
    setup_buttons()
    frame = Frame(root)
    root.mainloop()

main()
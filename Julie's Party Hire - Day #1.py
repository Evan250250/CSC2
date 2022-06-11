from tkinter import * 
from tkinter import ttk

root = Tk()

def print_shop_details():
    # these are the global variables that are used
    global j_names, total_entries, name_count
    name_count = 0

Label(root, font='bold',text="Full Name").grid(column=0,row=7)
Label(root, font='bold',text="Receipt Number").grid(column=1,row=7)
Label(root, font='bold',text="Items that hired").grid(column=2,row=7)
Label(root, font='bold',text="Number of items").grid(column=3,row=7)

    while name_count < total_entries :
        Label(root, text=name_count).grid(column=0,row=name_count+8) 
        Label(root, text=(shop_details[name_count][0])).grid(column=1,row=name_count+8)
        Label(root, text=(shop_details[name_count][1])).grid(column=2,row=name_count+8)
        Label(root, text=(shop_details[name_count][2])).grid(column=3,row=name_count+8)
        Label(root, text=(shop_details[name_count][3])).grid(column=4,row=name_count+8)
        name_count += 1

#start the program running
def main():
    global main_window
    global shop_details, entry_name,entry_age,entry_gender, total_entries
    shop_details = []
    total_entries = 0
    main_window =Tk()
    setup_buttons()
  
    
main()
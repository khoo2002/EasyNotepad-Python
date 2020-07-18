##author = KHOOZHAOWEI
##time = 19/7/2020
import tkinter as tk
import re

main = tk.Tk()
main.title('NOTEPAD-Python')
main.geometry('800x600')

b_menu = tk.Menu(main)
file_menu = tk.Menu(b_menu,tearoff=0)
file = open('notepadpy.txt','a+')
def fc_new():
    text.delete('1.0',tk.END)   

def fc_open():
    fcopenfile = tk.Toplevel()
    fcopenfile.geometry('400x200')
    fcopenfile.title('Open NOTEPAD-Python')
    file_path_entry = tk.Entry(fcopenfile,text='path')
    def comfirm():
        file_path_text = file_path_entry.get()
        fc_open_file = open(file_path_text,'rb')
        fc_open_content = fc_open_file.read()
        text.delete('1.0',tk.END)
        text.insert(tk.END,fc_open_content)
        fcopenfile.withdraw()
    file_path_button = tk.Button(fcopenfile,text='Comfirm',command=comfirm)
    file_path_entry.pack(fill='x')
    file_path_button.pack(fill='x')
    
def fc_save():
    fcsavefile = tk.Toplevel()
    fcsavefile.geometry('400x200')
    fcsavefile.title('Save NOTEPAD-Python')
    file_path_entry = tk.Entry(fcsavefile,text='path')
    def comfirm():
        file_path_text = file_path_entry.get()
        fc_save_file = open(file_path_text,'w')
        fc_save_file.write(text.get('1.0',tk.END))
        fc_save_file.close()
        fcsavefile.withdraw()
    file_path_button = tk.Button(fcsavefile,text='Comfirm',command=comfirm)
    file_path_entry.pack(fill='x')
    file_path_button.pack(fill='x')


b_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label="New",command=fc_new)
file_menu.add_command(label="Open",command=fc_open)
file_menu.add_command(label="Save",command=fc_save)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=main.quit)

text = tk.Text(main)
text.pack(fill='both')
file.close()
main.config(menu=b_menu)
main.mainloop()
import pathlib
import pygubu
import tkinter as tk
import tkinter.ttk as ttk

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "newproject"


class NewprojectApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel_1 = tk.Tk() if master is None else tk.Toplevel(master)

        self.frame_1 = ttk.Frame(self.toplevel_1)

        self.label_1 = ttk.Label(self.frame_1)
        self.label_1_text = tk.StringVar(value='ここに入力')
        self.label_1.configure(foreground='#000000', justify='center', relief='sunken', text='ここに入力')
        self.label_1.configure(textvariable=self.label_1_text)
        self.label_1.grid(column='0', padx='5', pady='5', row='0')

        self.entry_1 = ttk.Entry(self.frame_1)
        self.entry_var = tk.StringVar(value='')
        self.entry_1.configure(justify='center', textvariable=self.entry_var, validate='key')
        self.entry_1.grid(column='0', padx='5', pady='5', row='1', sticky='ew')

        self.button_1 = ttk.Button(self.frame_1)
        self.button_string = tk.StringVar(value='button_1')
        self.button_1.configure(text='button_1', textvariable=self.button_string)
        self.button_1.grid(column='0', padx='5', pady='5', row='2')
        self.button_1.configure(command=self.button_click)

        self.label_2 = ttk.Label(self.frame_1)
        self.label_2_str = tk.StringVar(value='label_2')
        self.label_2.configure(text='label_2', textvariable=self.label_2_str)
        self.label_2.grid(column='0', padx='5', pady='5', row='3')

        self.frame_1.configure(height='200', relief='groove', width='200')
        self.frame_1.grid(column='0', row='0', sticky='nsew')

        self.toplevel_1.configure(height='200', width='200')

        # Main widget
        self.mainwindow = self.toplevel_1

        self.number = 0

    def run(self):
        self.mainwindow.mainloop()

    def button_click(self):
        self.number += 1
        print(f"button clicked :{self.number}")
        self.label_2_str.set(f"Input is :{self.entry_var.get()}\nbutton clicked :{self.number}")
        pass


if __name__ == '__main__':
    app = NewprojectApp()
    app.run()

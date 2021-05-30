import tkinter as tk
import tkinter.ttk as ttk
import sword

class SwordSelector(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master)

        self.__create_widgets()
        self.__display_widgets()
    
    def __create_widgets(self):
        self.__label = tk.Label(self, text='Select a sword type')

        self.__option = tk.StringVar(self)
        self.__selector = ttk.Combobox(self, values=sword.Sword.make_spinner(), textvariable=self.__option)

        self.__button = tk.Button(self, text='Generate recipe!', command=self.__button_command)
    
    def __display_widgets(self):
        self.__label.pack(expand=True, fill='both', anchor='w')
        self.__selector.pack(expand=True, fill='both')
        self.__button.pack(expand=True, fill='both')
    
    def __button_command(self):
        self.__choice = sword.Sword(_type=self.__option.get())
        self.__recipe.update_recipe(self.__choice.make_recipe())
    
    def set_recipe(self, recipe):
        self.__recipe = recipe


class Recipe(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master)

        self.__create_widgets()
        self.__display_widgets()
    
    def __create_widgets(self):
        self.__charcoal = tk.Label(self, text='Charcoal')
        self.__charcoal_value = tk.Label(self, text='000')

        self.__steel = tk.Label(self, text='Steel')
        self.__steel_value = tk.Label(self, text='000')

        self.__coolant = tk.Label(self, text='Coolant')
        self.__coolant_value = tk.Label(self, text='000')

        self.__whetstone = tk.Label(self, text='Whetstone')
        self.__whetstone_value = tk.Label(self, text='000')
    
    def __display_widgets(self):
        self.__charcoal.grid(row=0, column=0, sticky='nsew')
        self.__charcoal_value.grid(row=0, column=1, sticky='nsew')
        self.__steel.grid(row=0, column=2, sticky='nsew')
        self.__steel_value.grid(row=0, column=3, sticky='nsew')
        self.__coolant.grid(row=1, column=0, sticky='nsew')
        self.__coolant_value.grid(row=1, column=1, sticky='nsew')
        self.__whetstone.grid(row=1, column=2, sticky='nsew')
        self.__whetstone_value.grid(row=1, column=3, sticky='nsew')

    def update_recipe(self, values):
        for widget, value in zip(
                [self.__charcoal_value, self.__steel_value,
                 self.__coolant_value, self.__whetstone_value], values):
            widget['text'] = value
import tkinter as tk
from gui import SwordSelector, Recipe

def getscreensize(root):
    return root.winfo_screenheight(), root.winfo_screenwidth()

def getwindowsize(window):
    return window.winfo_height(), window.winfo_width()

def center_window(window, root):
    H, W = getscreensize(root)
    h, w = getwindowsize(root)
    print(H, W, h, w)

root = tk.Tk()
root.title(string='TKRB toolkit v0.0.0')
root.geometry('+700+300')

main = tk.Frame(root)
main.pack()

selector = SwordSelector(main)
recipe = Recipe(main)

selector.set_recipe(recipe)

selector.pack(expand=True, fill='both', side='left')
recipe.pack(expand=True, fill='both', side='left')

center_window(root, main)
root.mainloop()
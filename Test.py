from tkinter import * 
from tkinter import messagebox

window = Tk()
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
window.withdraw()

messagebox.showinfo('HT_Smile','Task has been done !')

window.deiconify()
window.destroy()
window.quit()
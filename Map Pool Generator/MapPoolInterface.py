#Victor Stolle MapPoolInterface.py
import sys
from Tkinter import *
from MapPoolGenerator import MapPoolGenerator
from PIL import ImageTk, Image
class MapPoolInterface:


    '''
    Usage: m = MapPoolInterface()

    '''

    def __init__(self):

        self.counter = 0


        self.root = Tk()
        self.root.title("osu!UCI Summer League 2015")
        self.root.config(width = 800, height = 800)       

        self.path = "OSL_background.jpg"
        self.img = ImageTk.PhotoImage(Image.open(self.path))

        self.panel = Label(self.root, image = self.img)
        self.text = Text(self.root, bg = "#888888")
        self.scroll = Scrollbar(self.root)
        self.scroll.pack(side="right", fill = "y")
        self.text.pack(side = "left", fill = "both", expand = 1)
        self.run_button = Button(self.root, text = "Run", command = self.run_func)

        self.exit_button = Button(self.root, text = "Exit", command = self.byebye)


        self.run_button.grid(row = 0, column = 1)
        self.exit_button.grid(row = 1, column = 2)
        self.run_button.pack(side = "top")
        self.exit_button.pack(side = "bottom")
        self.panel.pack(side = "top", fill = "both", expand = 1)
        self.mpg = MapPoolGenerator()


        sys.stdout = TextRedirector(self.text, "stdout")


        
    def run_func(self):
        self.mpg.run()
        self.run_button.destroy()


    def byebye(self):
        self.destroy()
    
    def run(self):
        self.root.mainloop()



class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")



if __name__ == "__main__":

    m = MapPoolInterface()

    m.run()



'''



text = tk.Text(container, ...)
scrollbar = tk.Scrollbar(container, ...)
scrollbar.pack(side="right", fill="y")
text.pack(side="left", fill="both", expand=True)


'''
